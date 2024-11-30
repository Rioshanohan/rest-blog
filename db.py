import sqlite3, random, datetime
from models import Post

def getNewId():
    return random.getrandbits(28)

posts = [
    {
        'title': 'My first post',
        'content': 'Hello world!',
        'timestamp': datetime.datetime.now()
    },
    {
        'title': 'My second post',
        'content': 'Sphinx of black quartz, judge my vow.',
        'timestamp': datetime.datetime.now()
    }
]

def connect():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS blog (id INTEGER PRIMARY KEY, title TEXT, content TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
    for i in posts:
        p = Post(getNewId(), i['title'], i['content'], i['timestamp'])
        insert(p)

def insert(post):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO blog VALUES (?,?,?,?)", (
        post.id, post.title, post.content, post.timestamp
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM blog")
    rows = cur.fetchall()
    posts = []
    for i in rows:
        post = Post(*i)
        post.append(post)
    conn.close()
    return posts

def update(post):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("UPDATE blog SET title=?, content=? WHERE id=?" (post.title, post.content, post.id))
    conn.commit()
    conn.close()


def delete(to_delete):
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM blog WHERE id=?", (to_delete,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('blog.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books")
    conn.commit()
    conn.close()
