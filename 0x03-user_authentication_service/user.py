#!/usr/bin/env python3
"""User model"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """Represents a user in the system."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    hashed_password = db.Column(db.String(80), nullable=False)
    session_id = db.Column(db.String(64), nullable=False)
    reset_token = db.Column(db.String(64), nullable=False)
