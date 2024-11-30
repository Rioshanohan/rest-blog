from flask import Flask, request, jsonify
import os, re, datetime
import db
from models import Post


app = Flask(__name__)

if not os.path.isfile('blog.db'):
    db.connect()


@app.route('/')
def index():
    return 'Blog!'

@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    title = req_data['title']
    content = req_data['content']
    posts = [p.serialize() for p in db.view()]
    
    p = Post(db.getNewId(), title, content, datetime.datetime.now())
    print('new post: ', p.serialize())
    db.insert(p)
    new_posts = [p.serialize() for p in db.view()]
    print('posts in blog: ', new_posts)

    return jsonify({
        'res': p.serialize(),
        'status': '200',
        'msg': 'success creating new post!'
        })

@app.route('/request', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    posts = [p.serialize() for p in db.view()]
    if(content_type == 'application/json'):
        json = request.json
        for p in posts:
            if p['id'] == int(json['id']):
                return jsonify({
                    'res': p,
                    'status': '200',
                    'msg': 'GET success!'
                })
        return jsonify({
            'error': f"Error! Post with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
            'res': posts,
            'status': '200',
            'msg': 'GET success!',
            'no_of_posts': len(posts)
        })

if __name__ == '__main__':
    app.run()

