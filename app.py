from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/shop', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    all_sellist = list(db.sellist.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'sellist': all_sellist})

## API 역할을 하는 부분
@app.route('/sell_list2', methods=['POST'])
def order():
    title_receive = request.form['title_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    content ={
        'title' : title_receive,
        'count' : count_receive,
        'address' : address_receive,
        'number' : number_receive
    }

    db.sellist.insert_one(content)

    return jsonify({'result': 'success', 'msg':'저장이 완료되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)