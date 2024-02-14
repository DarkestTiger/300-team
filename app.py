from flask import Flask, render_template, request,url_for, Response
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
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

@app.route('/members/1')
def members1():
     return render_template('profle.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)