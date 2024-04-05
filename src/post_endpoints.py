from flask import jsonify, request
from common import app
from models import db, User, Planets, Characters, Starships, Favorites


#CREAR UN USUARIO

@app.route('/user', methods=['POST'])
def add_new_user():
    data = request.json
    print(data)
    user_exists = User.query.filter_by(first_name=data["first_name"]).first()
    
    if user_exists is None: 

            new_user = User(
                first_name=data["first_name"], 
                last_name=data["last_name"], 
                email=data["email"], 
                password=data["password"]
                )
            db.session.add(new_user)
            db.session.commit()
            return jsonify({
            "msg": "New user has been added successfuly",
        }), 200
    else:
        return jsonify({"error": "User already exists"}), 400    
    

#CREAR UN PLANETA NUEVO
@app.route('/planet', methods=['POST'])
def add_new_planet():
    data = request.json
    print(data)

    planet_exists = Planets.query.filter_by(name=data["name"]).first()
    
    if planet_exists is None: 

            new_planet = Planets(
                name=data["name"], 
                climate=data["climate"], 
                # population=data["population"], 
                # orbital_period=data["orbital_period"], 
                # rotation_period=data["rotation_period"], 
                # diameter=data["diameter"]
                )
            db.session.add(new_planet)
            db.session.commit()
            return ({"msg": "ok, a new planet has been added to the database"}), 200

       

    else:
            return ({"msg": "this planet is already included in the database"}), 200
    

#CREAR UNA NAVE ESPACIAL NUEVA
@app.route('/starship', methods=['POST'])
def add_new_starship():
    data = request.json
    print(data)

    starship_exists = Starships.query.filter_by(name=data["name"]).first()
    
    if starship_exists is None: 

            new_starship = Starships(
                name=data["name"], 
                manufacturer=data["manufacturer"], 
                # crew=data["crew"], 
                # passengers=data["passengers"], 
                # consumables=data["consumables"], 
                # cost_in_credits=data["cost_in_credits"]
                )
            db.session.add(new_starship)
            db.session.commit()
            return ({"msg": "ok, a new starship has been added to the database"}), 200

       

    else:
            return ({"msg": "this starship is already included in the database"}), 200
    

#CREAR UN PERSONAJE NUEVO
@app.route('/character', methods=['POST'])
def add_new_character():
    data = request.json
    print(data)

    character_exists = Characters.query.filter_by(name=data["name"]).first()
    
    if character_exists is None: 

            new_character = Characters(
                name=data["name"], 
                height=data["height"], 
                # mass=data["mass"], 
                # hair_color=data["hair_color"], 
                # eye_color=data["eye_color"], 
                # gender=data["gender"],
                # birth_year=data["birth_year"]
                )
            db.session.add(new_character)
            db.session.commit()
            return ({"msg": "ok, a new character has been added to the database"}), 200

       

    else:
            return ({"msg": "this character is already included in the database"}), 200



