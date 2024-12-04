from flask import url_for
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
from app import db


class Notes(db.Model):

  __tablename__ = 'notes'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(256), nullable=False)
  note = db.Column(db.Text)
  is_active = db.Column(db.Boolean, default=True)

  def __repr__(self):
    return f'<Notes {self.email}>'

  def save(self):
    if not self.id:
      db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_by_id(id):
    return Notes.query.get(id)

  @staticmethod
  def get_by_email(email):
    return Notes.query.filter_by(email=email).first()

  @staticmethod
  def get_all_notes():
    return Notes.query.filter_by(is_active=True).all()
