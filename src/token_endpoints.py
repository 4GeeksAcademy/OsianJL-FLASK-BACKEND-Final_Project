from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "super-secret"  
jwt = JWTManager(app)
# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    print(email)
    print(password)
    query_results = User.query.filter_by(email=email).first()

    if query_results is None:
            return jsonify({"msg": "Bad Request"}), 404
    print(query_results.email)
    print(query_results.password)

    if email == query_results.email and password == query_results.password:
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token)
    
    else: 
            return jsonify({"msg": "Bad email or password. I am sorry"}), 401

    
    


#SIGN IN ############################################################################################
@app.route("/signup", methods=["POST"])
def signup():
    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user_exists = User.query.filter_by(email=email).first()
    
    if user_exists is None: 

            new_user = User(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                password=password
                )
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"msg": "new user successfully created"})
            
    else:
        return jsonify({"error": "User already exists"}), 400
    
    # CONDICIONAL RENDERING #############################################################################

@app.route("/valid-token", methods=["GET"])
@jwt_required()
def valid_token():
     current_user = get_jwt_identity()
     querty_results = User.query.filter_by(email=current_user).first()
     if querty_results is None:
            return jsonify({"msg": "user does not exist",
                           "is_logged": False}), 404
     
     return jsonify({"is_logged": True}), 200