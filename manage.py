import os 
from app import app,db 
from flask_script import Manager, Server 
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
server = Server(host="0.0.0.0", port=5060)
manager.add_command("runserver", server)
manager.add_command('db', MigrateCommand)

@manager.command  
def drop():
    print "dropping all tables..."
    return db.drop_all()

@manager.command 
def create():
    print "creating all tables"
    return db.create_all()

if __name__ == "__main__":
    manager.run()
