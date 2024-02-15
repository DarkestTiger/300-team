import os
import sys
import flask
import copy
from flask import Flask, render_template, request, url_for, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)


class BookMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.name} {self.message} 작성자 by {self.name}'


with app.app_context():
    db.create_all()

@app.route('/', methods=['Get'])
def home():
    books = BookMsg.query.order_by('id').all()
    # print(books)
    print(f'home called')
    return render_template('index.html', data=books)


@app.route('/get_books')
def get_books():
    books = BookMsg.query.all()
    return jsonify([{'id': book.id, 'name': book.name, 'message': book.message} for book in books])

@app.route('/Books/create/', methods=['POST'])
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

    # books = BookMsg.query.order_by('id').all()
    return jsonify({'id': book.id, 'name': book.name, 'message': book.message})

    # return render_template('index.html', data=books)


member_datas = {
    1: {
        'img_url': '../static/image/이준승.jpg',
        'blog_url': 'https://itsallmyworld.tistory.com/',
        'name': '이준승',
        'introduce': '안녕하세요, 저는 이 준승 이에요\n저는 AI 웹 개발자가 되는것이 꿈이에요.',
        'programming_languages': ['html', 'CSS', 'JS', 'Python'],
        'strength': 'Ctrl + C , Ctrl + V',
        'mbti': 'INTP',
        'tmi': '스파르타 AI 6기 화이팅!'
    },
    2: {
        'img_url': '../static/image/이현기.jpg',
        'blog_url': 'https://blog.naver.com/dldl5040',
        'name': '이현기',
        'introduce': '안녕하세요 이현기 입니다. 데이터분석직무를 희망하고 있습니다. 앞으로 잘 부탁 드리겠습니다.',
        'programming_languages': ['html','c','css','Python'],
        'strength': '깊게는 아니지만 얕게 여러분야를 배워 상대적으로 분야에 관계없이 적응을 잘 합니다.',
        'mbti': 'ISTP',
        'tmi': '헬스케어 잘알 계시면 연락바랍니다. 1조 화이팅!'
    },
    # 3: {
    #     'img_url': '../static/image/이규민.jpg',
    #     'blog_url': 'https://blog.naver.com/verty9045',
    #     'name': '이규민',
    #     'introduce': '안녕하세요? 반갑습니다 ~~',
    #     'programming_languages': ['html','CSS'],
    #     'strength': '부족한점 을 노력으로 채울려고 한다',
    #     'mbti': '모름',
    #     'tmi': '다 같이 열공 해봐요!'
    # },
    4: {
        'img_url': '../static/image/이상일.jpg',
        'blog_url': 'https://silee-sw.tistory.com/',
        'name': '이상일',
        'introduce': '안녕하세요 이상일이라고 해요\n 대규모 트래픽이 발생하는 시스템의 \n백엔드 개발자를 목표하고 있어요',
        'programming_languages': ['java', 'python'],
        'strength': '코드 다듬기',
        'mbti': 'ISFP',
        'tmi': '머리털은 취업하고 자를 예정입니다...'
    },
    5: {
        'img_url': '../static/image/권진우.png',
        'blog_url': 'https://blog.naver.com/rkdvo10',
        'name': '권진우',
        'introduce': '안녕하세요 저는 권진우입니다. 나의 꿈은 팀원들이 저를 믿을 수 있는 개발자가 되고 싶습니다.',
        'programming_languages': ['HTML', 'CSS', 'Python', 'JS'],
        'strength': '사람들을 재밌게 해줍니다.',
        'mbti': 'ISFJ',
        'tmi': '다들 화이팅!'
    },
}


@app.route('/members/<memberid>')
def members(memberid):
    # member
    memberid = int(memberid)
    print(f'memberid={memberid}')
    context = copy.deepcopy(member_datas[memberid])

    # replace \n -> <br>
    languages = ', '.join(context['programming_languages'])

    context['programming_languages'] = languages
    context['introduce'] = context['introduce'].replace('\n', '<br>')

    return render_template('profile_member.html', data=context)
    # return render_template('profle.html', data=context)


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
    if len(sys.argv) >= 2:
        print(f'port = {sys.argv[1]}')
        app.run(debug=True, port=sys.argv[1])
    else:
        app.run(debug=True, port=5000)
