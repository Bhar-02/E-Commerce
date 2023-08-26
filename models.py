from app import db,login_manager
from app import app 
from flask_login import UserMixin


@login_manager.user_loader

def load_user(user_id ):
    with app.app_context():
        return User.query.get(int(user_id))
    
class User(db.Model,UserMixin):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(10),nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}','{self.is_admin}')"


class Store(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    Category=db.Column(db.String(40),nullable=False)
    product=db.Column(db.String(40),nullable=False)
    amt=db.Column(db.Integer,nullable=False)
    

    def __repr__(self):
        return f"Store('{self.category}','{self.product}','{self.amt}')"