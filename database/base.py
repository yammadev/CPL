from application import app as main
from flask_sqlalchemy import SQLAlchemy

main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)

# Create
@main.before_first_request
def create_tables():
    db.create_all()
    print('Create tables [Ok]')

# Delete
def delete_tables():
    db.drop_all()
    print('Delete tables [Ok]')
