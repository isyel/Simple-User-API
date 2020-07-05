import click
from flask.cli import with_appcontext
from application import db
import models

@click.command('db_create')
@with_appcontext
def db_create():
    db.create_all()
    print('Database Created')


@click.command('db_drop')
@with_appcontext
def db_drop():
    db.drop_all()
    print('Database Dropped')
    

@click.command('db_seed')
@with_appcontext
def db_seed():
    test_user = User(first_name='Isykal',
                     last_name='Jammy',
                     email='jammy@gmail.com',
                     password='222222')
    
    db.session.add(test_user)
    db.session.commit()
    
    print('Database Seeded')
    