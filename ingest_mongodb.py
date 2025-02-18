from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['sparkify']  
collection = db['logData']  

@app.route('/')
def top_songs_artists():
    # Aggregation query to get top 10 songs
    top_songs = list(collection.aggregate([
        {"$group": {"_id": "$song", "totalPlays": {"$sum": "$play_count"}}},
        {"$sort": {"totalPlays": -1}},
        {"$limit": 10}
    ]))

    # Aggregation query to get top 10 artists
    top_artists = list(collection.aggregate([
        {"$group": {"_id": "$artist", "totalPlays": {"$sum": "$play_count"}}},
        {"$sort": {"totalPlays": -1}},
        {"$limit": 10}
    ]))

    return render_template('index.html', top_songs=top_songs, top_artists=top_artists)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
