from flask import Flask,jsonify,request
import csv

allArticle = []
with open("article.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticle = data[1:]

likeArticle = []
notlikeArticle = []
app = Flask(__name__)

@app.route("/get-article")
def getarticle():
    return jsonify({
        "data": allArticle[0],
        "status":"success"
    })

@app.route("/like-article",methods=["POST"])
def like_article():
    article = allArticle[0]
    allArticle = allArticle[1:]
    likeArticle.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/notlike-article",methods=["POST"])
def notlike_article():
    article = allArticle[0]
    allArticle = allArticle[1:]
    notlikeArticle.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()
    