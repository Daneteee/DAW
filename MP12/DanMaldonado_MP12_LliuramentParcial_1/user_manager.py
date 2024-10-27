from pymongo.collection import Collection
import bcrypt

class UserManager:
    def __init__(self, collection: Collection):
        self.collection = collection

    def register(self, username, password, role):
        # Comprovem si existeix l'usuari
        if self.collection.find_one({"username": username}):
            return False
        
        else:
            # Encriptem la contrasenya
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Creem un nou usuari i l'afegim
            user_data = {
                "username": username,
                "password": hashed_password,
                "role": role
            }

            self.collection.insert_one(user_data)
            return True

    def login(self, username, password):
        # Busquem usuari
        user = self.collection.find_one({"username": username})

        # Verifiquemcontrasenya i si l'usuari existeix
        return user and bcrypt.checkpw(password.encode('utf-8'), user['password'])

    def getRole(self, username):
            # Busquem l'usuari per nom d'usuari
            user = self.collection.find_one({"username": username})
            if user:
                return user['role']  # Retorna el rol si l'usuari existeix
            else:
                print("ERROR: L'usuari no existeix.")
                return None
            
            
    def getUserID(self, username):
        # Busquem l'usuari per nom d'usuari i retornem el seu ObjectID
        user = self.collection.find_one({"username": username})
        if user:
            return user['_id']  # Retorna el ObjectID (sense convertir a string)
        
        else: 
            print("ERROR: L'usuari no existeix.")
            return None