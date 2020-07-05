import click
from flask.cli import with_appcontext
from application import db

from .models import User

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
    test_user = User(first_name='Princess',
                     last_name='Diana',
                     email='diana@gmail.com')
    test_user.set_password("222222")
    
    test_user2 = User(first_name='George',
                     last_name='Floyd',
                     email='floyd@gmail.com')
    test_user2.set_password("222222")
    
    db.session.add(test_user)
    db.session.add(test_user2)
    db.session.commit()
    
    print('Database Seeded')
    