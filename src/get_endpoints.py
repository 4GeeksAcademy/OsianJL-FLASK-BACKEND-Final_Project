from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites

#OBTENER TODOS LOS USUARIOS: 
@app.route('/all_users', methods=['GET'])
def get_all_users():
    query_results = User.query.all()
    results = list(map(lambda item: item.serialize(), query_results))

    if results == []:
        return jsonify("no users in the database"), 404
    
    response_body = {
        "msg": "ok",
        "results": results
    }
    
    return jsonify(response_body), 200

#OBTENER TODOS LOS PLANETAS
@app.route('/all_planets', methods=['GET'])
def get_all_planets():
    query_results = Planets.query.all()
    results = list(map(lambda item: item.serialize(), query_results))

    if results == []:
        return jsonify("no planets in the database"), 404
    
    response_body = {
        "msg": "ok",
        "results": results
    }
    
    return jsonify(response_body), 200

#OBTENER TODOS LOS PERSONAJES:
@app.route('/all_characters', methods=['GET'])
def get_all_characters():
    query_results = Characters.query.all()
    results = list(map(lambda item: item.serialize(), query_results))

    if results == []:
        return jsonify("no characters in the database"), 404
    
    response_body = {
        
        "msg": "ok",
        "results": results
    }
    
    return jsonify(response_body), 200

#OBTENER TODAS LAS NAVES ESPACIALES: 
@app.route('/all_starships', methods=['GET'])
def get_all_starships():
    query_results = Starships.query.all()
    results = list(map(lambda item: item.serialize(), query_results))

    if results == []:
        return jsonify("no starships in the database"), 404
    
    response_body = {
        "msg": "ok",
        "results": results
    }
    
    return jsonify(response_body), 200

#OBTENER UN USUARIO CONCRETO USANDO SU ID CON URL DINAMICA
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    query_results = User.query.filter_by(id=user_id).first()
   

    if query_results is None:
        return jsonify({"msg": "there is no user matching the ID provided"}), 404
    
    response_body = {
        "msg": "ok",
        "results": query_results.serialize()
    }
    return jsonify(response_body), 200

#OBTENER UNA NAVE ESPACIAL CONCRETA USANDO SU ID CON URL DINAMICA
@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_one_starship(starship_id):
    query_result = Starships.query.filter_by(id=starship_id).first()

    if query_result is None:
         return jsonify({"msg": "there is no starship matching the ID provided"}), 404
    
    response_body = {
        "msg": "ok",
        "results": query_result.serialize()
    }
    return jsonify(response_body), 200

#OBTENER UN PLANETA CONCRETO USANDO URL DINAMICA 
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    query_result = Planets.query.filter_by(id=planet_id).first()
   

    if query_result is None:
        return jsonify({"msg": "there is no planet matching the ID provided"}), 404
    
    response_body = {
        "msg": "ok",
        "results": query_result.serialize()
    }
    return jsonify(response_body), 200



#OBTENER UN PERSONAJE CONCRETO USANDO URL DINAMICA
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_one_character(character_id):

    query_result = Characters.query.filter_by(id=character_id).first()
    print(query_result)
    if query_result is None:
        return jsonify({"msg": "there is no character matching the ID provided"}), 404
    
    response_body = {
        "msg": "ok",
        "id": query_result.id,
        "results": query_result.serialize()
    }
    return jsonify(response_body), 200

