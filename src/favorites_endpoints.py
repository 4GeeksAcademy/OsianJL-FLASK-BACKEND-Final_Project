from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "super-secret"  
jwt = JWTManager(app)

# @app.route('/favorites/<int:item_id>', methods=['POST'])
# @jwt_required()
# def add_new_favorite(item_id):
#     data = request.json()
#     email = get_jwt_identity()
#     item_type = data.item_type

#     user_exists = User.query.filter_by(email=email).first()

#     if user_exists is None: 
#            return jsonify({"msg": "This user does not exist"}), 401

#     user_id = user_exists.id

   
#     if item_type is "planet":

#         planet = Planets.query.filter_by(id=item_id).first()
#         if planet is None: 
#            return jsonify({"msg": "This planet does not exist"}), 401
#         new_favorite = Favorites(planets_id=item_id, user_id=user_id)
#         db.session.add(new_favorite)
#         db.session.commit()
#         response_body = {
#                  "msg": "ok", 
#                  "results": planet.serialize()
#             }
#         return jsonify(response_body), 200 

#     if item_type is "character":
#         character = Characters.query.filter_by(id=item_id).first()
#         if character is None: 
#            return jsonify({"msg": "This character does not exist"}), 401
#         new_favorite = Favorites(characters_id=item_id, user_id=user_id)
#         db.session.add(new_favorite)
#         db.session.commit()
#         response_body = {
#                  "msg": "ok", 
#                  "results": character.serialize()
#             }
#         return jsonify(response_body), 200 

#     if item_type is "starship":
#         starship = Starships.query.filter_by(id=item_id).first()
#         if starship is None: 
#            return jsonify({"msg": "This starship does not exist"}), 401
#         new_favorite = Favorites(starships_id=item_id, user_id=user_id)
#         db.session.add(new_favorite)
#         db.session.commit()
#         response_body = {
#                  "msg": "ok", 
#                  "results": starship.serialize()
#             }
#         return jsonify(response_body), 200 


#     # else:
#     #         return ({"msg": "this user already has this planet as a favorite"}), 200


####### OBTENER TODOS LOS FAVORITOS DE UN USUARIO ######
@app.route('/user/favorites', methods=['GET'])
@jwt_required()
def get_all_favorites_of_user():
    email = get_jwt_identity()

    user_exists = User.query.filter_by(email=email).first()

    if user_exists is None: 
           return jsonify({"msg": "This user does not exist"}), 401

    user_id = user_exists.id

    query_results = Favorites.query.filter_by(user_id=user_id).all()

    # planet_exists = Planets.query.filter_by(id=planet_id).first()
    

    if query_results:
        results = list(map(lambda item: item.serialize(), query_results))
        print(results)
        return jsonify({"msg": "ok", "results": results}), 200
    
    else: 
        return jsonify({"msg": "this user has no favorites yet"}), 404
    

# AÑADIR PLANETA FAVORITO
@app.route('/favorites/planet/<int:planet_id>', methods=['POST'])
@jwt_required()
def add_new_favorite_planet(planet_id):

    email = get_jwt_identity()
  

    user_exists = User.query.filter_by(email=email).first()

    if user_exists is None: 
           return jsonify({"msg": "This user does not exist"}), 401

    user_id = user_exists.id

    planet_exists = Planets.query.filter_by(id=planet_id).first()
    
    if planet_exists is None: 
           return jsonify({"msg": "This planet does not exist"}), 401
    
    
    query_results = Favorites.query.filter_by(planets_id=planet_id, user_id=user_id).first()
    print(query_results)
    if query_results is None: 

            new_favorite = Favorites(planets_id=planet_id, user_id=user_id)
            new_planet = Planets.query.filter_by(id=planet_id).first()
            db.session.add(new_favorite)
            db.session.commit()

            response_body = {
                 "msg": "ok", 
                 "results": new_planet.serialize()
            }
            return jsonify(response_body), 200 

    else:
            return ({"msg": "this user already has this planet as a favorite"}), 200
    

# AÑADIR NAVE ESPACIAL FAVORITA 
@app.route('/favorites/starship/<int:starship_id>', methods=['POST'])
@jwt_required()
def add_new_favorite_starship(starship_id):

    email = get_jwt_identity()

    user_exists = User.query.filter_by(email=email).first()

    if user_exists is None: 
           return jsonify({"msg": "This user does not exist"}), 401

    user_id = user_exists.id

    starships_exists = Starships.query.filter_by(id=starship_id).first()

    if starships_exists is None: 
           return jsonify({"msg": "This starship does not exist"}), 401
    

    query_results = Favorites.query.filter_by(starships_id=starship_id, user_id=user_id).first()

    if query_results is None: 

            new_favorite = Favorites(starships_id=starship_id, user_id=user_id)
            new_starship = Starships.query.filter_by(id=starship_id).first()
            db.session.add(new_favorite)
            db.session.commit()

            response_body = {
                 "msg": "ok", 
                 "results": new_starship.serialize()
            }
            return jsonify(response_body), 200 

    else:
            return ({"msg": "this user already has this starship as a favorite"}), 200
    
#AÑADIR PERSONAJE FAVORITO 
@app.route('/favorites/character/<int:character_id>', methods=['POST'])
@jwt_required()
def add_new_favorite_character(character_id):
    email = get_jwt_identity()
    
    user_exists = User.query.filter_by(email=email).first()

    if user_exists is None:
         return jsonify({"msg": "this user does not exist"}), 401
    
    user_id = user_exists.id

    characters_exists = Characters.query.filter_by(id=character_id).first()
    
    if characters_exists is None:
         return jsonify({"msg": "this character does not exist"}), 401
   
    query_results = Favorites.query.filter_by(characters_id=character_id, user_id=user_id).first()

    if query_results is None: 

            new_favorite = Favorites(characters_id=character_id, user_id=user_id)
            new_character = Characters.query.filter_by(id=character_id).first()
            db.session.add(new_favorite)
            db.session.commit()
            return ({"msg": "ok", "results": new_character.serialize()}), 200

    else:
            return ({"msg": "this user already has this character as a favorite"}), 200
        

########## BORRAR UN PLANETA FAVORITO DE UNA CUENTA DE UN USUARIO#############################
    
# # 1 #PRIMER MÉTODO, USANDO EL REQUEST.JSON PARA SABER IDS DE USUARIO Y PLANETA
# @app.route('/favorites/planet/<int:planets_id>', methods=['DELETE'])
# def delete_favorite_planet(planets_id):
#     data = request.json

#     user_exists = User.query.filter_by(id=data["user_id"]).first()
#     planets_exists = Planets.query.filter_by(id=data["planets_id"]).first()
    
#     if user_exists and planets_exists: 

#         query_results = Favorites.query.filter_by(planets_id=data["planets_id"], user_id=data["user_id"]).first()

#         if query_results: 
         
#             db.session.delete(query_results)
#             db.session.commit()
#             return ({"msg": "ok, its deleted"}), 200

        

#         else: 

#            return ({"msg": "there is nothing to delete"}), 200

       

# # 2 # SEGUNDO MÉTODO, USANDO LA URL DINÁMICA PARA SABER IDS DE USUARIO Y PLANETA (METODO OPTIMO)        
# @app.route('/favorites/character/<int:user_id>/<int:characters_id>', methods=['DELETE'])
# def delete_favorite_character(user_id,characters_id):
   

#     user_exists = User.query.filter_by(id=user_id).first()
#     character_exists = Characters.query.filter_by(id=characters_id).first()
    
#     if user_exists and character_exists: 

#         query_results = Favorites.query.filter_by(characters_id=characters_id, user_id=user_id).first()

#         if query_results: 
         
#             db.session.delete(query_results)
#             db.session.commit()
#             return ({"msg": "ok, its deleted"}), 200

        

#         else: 

#            return ({"msg": "there is nothing to delete"}), 200

       
#BORRAR UN FAVORITO USANDO EL ID DEL FAVORITO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
@app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
@jwt_required()
def delete_favorite(favorite_id):
    email = get_jwt_identity()

    user_exists = User.query.filter_by(email=email).first()
    if user_exists is None: 
            return jsonify({"msg": "this user does not exist"})
    
    user_id = user_exists.id

    favorite_exists = Favorites.query.filter_by(id=favorite_id).first()
    if favorite_exists is None: 
            return jsonify({"msg": "this favorite does not exist"})
    

    query_results = Favorites.query.filter_by(id=favorite_id, user_id=user_id).first()

    if query_results: 
         
            db.session.delete(query_results)
            db.session.commit()
            return ({"msg": "ok, its deleted"}), 200

    else: 

           return ({"msg": "there is nothing to delete"}), 200


