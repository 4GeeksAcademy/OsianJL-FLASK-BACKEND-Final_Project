from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites


# BORRAR USUARIO EN BASE A SU NOMBRE        
@app.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json

    user_exists = User.query.filter_by(first_name=data["first_name"]).first()
    
    if user_exists: 
         
            db.session.delete(user_exists)
            db.session.commit()
            return ({"msg": "ok, its deleted"}), 200

        

    else: 

           return ({"msg": "there is nothing to delete"}), 200
    

# BORRAR TODOS LOS USUARIOS       
@app.route('/users', methods=['DELETE'])
def delete_all_users():
    users_deleted = User.query.delete()
    db.session.commit()
    
    if users_deleted > 0: 
            return ({"msg": "ok, all users have been deleted"}), 200

    else: 

           return ({"msg": "there are no users to delete"}), 200
    

# BORRAR PLANETAS EN BASE A SU NOMBRE        
@app.route('/planet', methods=['DELETE'])
def delete_planet():
    data = request.json

    
    planet_exists = Planets.query.filter_by(name=data["name"]).first()
    
    if planet_exists: 
         
            db.session.delete(planet_exists)
            db.session.commit()
            return ({"msg": "ok, its deleted"}), 200

        

    else: 

           return ({"msg": "there is nothing to delete"}), 200

# BORRAR TODOS LOS PLANETAS        
@app.route('/planets', methods=['DELETE'])
def delete_all_planets():
   
    planets_deleted = Planets.query.delete()
    db.session.commit()
    
    if planets_deleted > 0: 
            return ({"msg": "ok, all planets have been deleted"}), 200

    else: 

           return ({"msg": "there are no planets to delete"}), 200