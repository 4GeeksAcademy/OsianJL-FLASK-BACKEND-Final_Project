from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites

#ACTUALIZAR USUARIO (USANDO SU EMAIL Y SU PASSWORD COMO COINCIDENCIA DENTRO DEL BODY)    
@app.route('/user', methods=['PUT'])
def update_user():
    data = request.json

    user = User.query.filter_by(email=data["email"]).first()
    
    
    if user:
    
            user.first_name=data["first_name"], 
            user.last_name=data["last_name"], 
            user.email=data["email"],
            user.password=data["password"]
                
            
            db.session.commit()
            return ({"msg": "ok, the user has been updated in the database"}), 200

       

    else:
            return ({"msg": "this user does not exist, you can't update it"}), 404


# ACTUALIZAR DATOS DE UN PLANETA USANDO URL DINAMICA E ID DEL PLANETA
@app.route('/planet/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    data = request.json

    planet = Planets.query.filter_by(id=planet_id).first()
    
    if planet: 
    
            planet.name=data["name"], 
            planet.climate=data["climate"], 
            # planet.population=data["population"], 
            # planet.orbital_period=data["orbital_period"], 
            # planet.rotation_period=data["rotation_period"], 
            # planet.diameter=data["diameter"]
                
            
            db.session.commit()
            return ({"msg": "ok, the planet has been updated in the database"}), 200

       

    else:
            return ({"msg": "this planet does not exist, you can't update it"}), 200