from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

new_title = db.movies.find_one({'title' : '매트릭스'})
new_score = new_title['score']

# movies = list(db.movies.find({'score' : new_score}))
# for movie in movies:
#     print(movie['title'])

db.movies.update_many({'score': new_score}, {'$set' : {'score' : 0}})