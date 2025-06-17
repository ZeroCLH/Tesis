from flask import render_template
from database.MongoDb import MongoDb
from models.User import User
from bson.objectid import ObjectId

db = MongoDb().db()

def index():

    cedula = '0705463420'
    findUser = db.users.find_one({'identification':cedula})

    print(findUser)

    return render_template("/views/index.html") #dirección hacia el front

def login():

    cedula = '0705463420'
    findUser = db.users.find_one({'identification':cedula})

    if findUser:
        findUser["name"] = "DARWIN PILALOA"
        db.users.update_one({"_id": ObjectId(findUser["_id"])}, {"$set": findUser})

    return render_template("/views/login.html")
    

def register():

    #creación del objeto
    newUser = User("0705463420","DARWIN","123","ADMIN",True)
    #asignación de fecha de creación
    newUser.createUser()
    #insertar en la base de datos
    db.users.insert_one(newUser.getUser())    

    return render_template("/views/register.html")