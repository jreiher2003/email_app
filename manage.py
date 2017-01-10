import os 
from app import app 
from flask_script import Manager, Server 

manager = Manager(app)
server = Server(host="0.0.0.0", port=5060)
manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()
