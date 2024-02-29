

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


from flask import jsonify
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






if __name__ == "__main__":
    # app.run(debug=True)

    with app.app_context():
        db.create_all() 

    app.run(debug=True)



