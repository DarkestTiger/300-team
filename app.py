import os
import flask
from flask import Flask, render_template, request, url_for, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)


@app.route('/', methods=['Get'])
def home():

    books = BookMsg.query.order_by('id').all()
    print(books)
    return render_template('index.html', books=books)


class BookMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.name} {self.message} 작성자 by {self.name}'


with app.app_context():
    db.create_all()


@app.route('/Books/create/', methods=['Post'])
def createbooks():
    # form에서 가져온 데이터 받아오기
    username_recieve = request.form.get('username')
    print(username_recieve)
    msg_recieve = request.form.get('msg')
    print(msg_recieve)
    # 데이터 db에 저장하기
    book = BookMsg(name=username_recieve, message=msg_recieve)
    print(book)
    db.session.add(book)
    db.session.commit()

    books = BookMsg.query.order_by('id').all()

    return render_template('index.html', books=books)


member_datas = {
    1: {
        'img_url': 'image/rtan00.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '이준승',
        'introduce': '안녕하세요~\n르탄이에요',
        'programming_languages': ['java', 'python', 'html'],
        'strength': '멍떄리기',
        'mbti': 'ISFP',
        'tmi': '자전거 여행 좋아합니다~ 같이 하실분 DM 주세요~'
    },
    2: {
        'img_url': 'static/image/rtan00.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '이상일',
        'introduce': '안녕하세요~\n르탄이에요',
        'programming_languages': ['java', 'python', 'html'],
        'strength': '멍떄리기',
        'mbti': 'ISFP',
        'tmi': '자전거 여행 좋아합니다~ 같이 하실분 DM 주세요~'
    },
    3: {
        'img_url': 'static/image/rtan00.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '이현기',
        'introduce': '안녕하세요~\n르탄이에요',
        'programming_languages': ['java', 'python', 'html'],
        'strength': '멍떄리기',
        'mbti': 'ISFP',
        'tmi': '자전거 여행 좋아합니다~ 같이 하실분 DM 주세요~'
    },
    4: {
        'img_url': 'static/image/rtan00.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '권진우',
        'introduce': '안녕하세요~\n르탄이에요',
        'programming_languages': ['java', 'python', 'html'],
        'strength': '멍떄리기',
        'mbti': 'ISFP',
        'tmi': '자전거 여행 좋아합니다~ 같이 하실분 DM 주세요~'
    },
    5: {
        'img_url': 'static/image/rtan00.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '이규민',
        'introduce': '안녕하세요~\n르탄이에요',
        'programming_languages': ['java', 'python', 'html'],
        'strength': '멍떄리기',
        'mbti': 'ISFP',
        'tmi': '자전거 여행 좋아합니다~ 같이 하실분 DM 주세요~'
    },
}

@app.route('/members/<memberid>')
def members(memberid):
    # member
    memberid = int(memberid)
    print(f'memberid={memberid}')
    context = member_datas[memberid]

    # replace \n -> <br>
    context['introduce'] = context['introduce'].replace('\n', '<br>')

    return render_template('profle.html', data=context)


@app.route('/members/member1')
def members1():
    return flask.redirect(flask.url_for('members', memberid=1))


@app.route('/members/member2')
def members2():
    return flask.redirect(flask.url_for('members', memberid=2))


@app.route('/members/member3')
def members3():
    return flask.redirect(flask.url_for('members', memberid=3))

@app.route('/members/member4')
def members4():
    return flask.redirect(flask.url_for('members', memberid=4))


@app.route('/members/member5')
def members5():
    return flask.redirect(flask.url_for('members', memberid=5))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
