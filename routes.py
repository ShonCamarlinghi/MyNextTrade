from flask import Blueprint, render_template, jsonify, request, redirect
from models import db, User
user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user')

@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    all_users = User.query.all()
    result = [user.serialize() for user in all_users]
    response = {
       'message': 'Returning all users',
       'result': result
    }

    return jsonify(response)

    #### return render_template('index.html')

@user_blueprint.route('/create', methods=['POST'])
def create_user():
    data = request.get_json ()
    username = data.get ( 'username' )
    email = data.get ( 'email' )
    password = data.get ( 'password' )
    if User.query.filter_by ( username=username ).first ():
        return jsonify ( {'message': 'Username already exists'} ), 400

    new_user = User ( username=username, email=email, password=password )
    db.session.add ( new_user )
    db.session.commit ()

    response = {
        'message': 'User created successfully',
        'user': new_user.serialize ()
    }

    return jsonify ( response )

