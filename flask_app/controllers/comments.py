from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import user,convo,comment
import requests



@app.route('/get_comments/<int:id>')
def apiComments(id):

    r = requests.get(f"http://localhost:5000/get_api_comments/{id}")
    print(r)
    return jsonify(r.json())


@app.route('/get_api_comments/<int:id>')
def getComments(id):

    convo_data = {'convo_id':id}
    # all_comments = comment.Comment.get_all_from_convo(convo_data)

    return jsonify(comment.Comment.get_all_from_convo(convo_data))



@app.route('/create/comment', methods = ['POST'])
def addComment():
    comment.Comment.save(request.form)
    # one_comment = comment.Comment.get_one(request.form)
    # print(one_comment)

    # data = {
    #     'name': f'{one_comment.creator.first_name} {one_comment.creator.last_name}',
    #     'pic':one_comment.creator.pic_url,
    #     'comment': one_comment.comment,
    #     'created_at': one_comment.created_at
    # }

    return redirect(request.referrer)


