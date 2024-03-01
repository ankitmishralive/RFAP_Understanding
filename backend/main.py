

# ----------- Create --------
# firstname 
# lastname 
# email


# Request means jobhi vahi hum server ko bhejte, 
# get-> accessing or retrieving 
# post means creating 
# put for updating
# patch-> used for  partial updating 


# json is infromation from our server 
# response is from server


from flask import jsonify, request
from config import app,db 
from models import Contact



@app.route("/",methods=["GET"])
def index():
    return "Hey....API Here"


@app.route("/contacts",methods=["GET"])
def get_contacts():
    print("----HelloW-----Inside API----------")
    contacts = Contact.query.all() 
    print("---Fetching------",contacts)
    # json_contacts = list(map(lambda x: x.to_json(), contacts))
    json_contacts = [contact.to_json() for contact in contacts]
    json_contacts = list(json_contacts)

    return jsonify({"Contacts":json_contacts})
    # return jsonify(json_contacts)


@app.route("/create_contact",methods=["POST"])
def create_contact():
    first_name = request.json.get("firstname")
    last_name = request.json.get("lastname")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message":"You must include first name, last name and email"}),400
    
    new_contact = Contact(first_name=first_name,
                          last_name=last_name,
                          email=email,)
    try: 
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}),400 
    
    return jsonify({"message":"user created!"}),201 


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
 
    contact = Contact.query.get(user_id)

    if not contact: 
        return jsonify({"message":"user not found.!"})
    

    db.session.delete(contact)
    db.session.commit() 
    
    return jsonify({"message":"user deleted!"}),200



@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
 
    contact = Contact.query.get(user_id)

    if not contact: 
        return jsonify({"message":"user not found.!"})
    

    data = request.json
    contact.first_name = data.get("firstname",contact.first_name)
    contact.last_name = data.get("lastname",contact.last_name)
    contact.email = data.get("email",contact.email)

    db.session.commit()
    

    return jsonify({"message":"user Updated !"}),200




if __name__ == "__main__":
    # app.run(debug=True)

    with app.app_context():
        db.create_all() 

    app.run(debug=True)



