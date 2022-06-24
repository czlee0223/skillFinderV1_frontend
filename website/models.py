from . import db

class ProgLang(db.Model):
    __tablename__ = 'programminglanguages'
    Words = db.Column(db.String,primary_key=True)
    DS_count = db.Column(db.Integer,nullable=False)
    DA_count = db.Column(db.Integer,nullable=False)
    DE_count = db.Column(db.Integer,nullable=False)
    ML_count = db.Column(db.Integer,nullable=False)
    
class Education(db.Model):
    __tablename__ = 'education'
    Words = db.Column(db.String,primary_key=True)
    DS_count = db.Column(db.Integer,nullable=False)
    DA_count = db.Column(db.Integer,nullable=False)
    DE_count = db.Column(db.Integer,nullable=False)
    ML_count = db.Column(db.Integer,nullable=False)

class Library(db.Model):
    __tablename__ = 'library'
    Words = db.Column(db.String,primary_key=True)
    DS_count = db.Column(db.Integer,nullable=False)
    DA_count = db.Column(db.Integer,nullable=False)
    DE_count = db.Column(db.Integer,nullable=False)
    ML_count = db.Column(db.Integer,nullable=False)
    
class Tools(db.Model):
    __tablename__ = 'tools'
    Words = db.Column(db.String,primary_key=True)
    DS_count = db.Column(db.Integer,nullable=False)
    DA_count = db.Column(db.Integer,nullable=False)
    DE_count = db.Column(db.Integer,nullable=False)
    ML_count = db.Column(db.Integer,nullable=False)
    
class Location(db.Model):
    __tablename__ = 'location'
    Words = db.Column(db.String,primary_key=True)
    DS_count = db.Column(db.Integer,nullable=False)
    DA_count = db.Column(db.Integer,nullable=False)
    DE_count = db.Column(db.Integer,nullable=False)
    ML_count = db.Column(db.Integer,nullable=False)



