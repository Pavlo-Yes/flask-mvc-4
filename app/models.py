from app import db

users_and_pets = db.Table(
    'users_and_pets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('pet_id', db.Integer, db.ForeignKey('pet.id'), primary_key=True),
)


class PetModel(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def __str__(self):
        return f'{self.id} {self.name}'

    def __repr__(self):
        return f'{self.id} {self.name}'


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False, default=4)
    pets = db.relationship('PetModel', backref='users', lazy=True, secondary=users_and_pets)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.id} {self.name}'

    def __repr__(self):
        return f'{self.id} {self.name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_age(cls, age):
        return cls.query.filter(cls.age == age).all()
