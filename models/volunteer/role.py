# coding=utf-8
from main import db


class Role(db.Model):
    __tablename__ = 'volunteer_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True, index=True)
    description = db.Column(db.String)
    # Things to know for the shift
    role_notes = db.Column(db.String)


class RolePermission(db.Model):
    __versioned__ = {}
    __tablename__ = 'volunteer_role_permission'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)


class UserRole(db.Model):
    __tablename__ = 'volunteer_user_role'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('volunteer_role.id'), primary_key=True)


"""
Qualifications include:
 - Over 18
 - Bar training
 - Bar supervisor training
 - DBS check (reduces min required for a shift)
 - Checked into site
 - Phone validated

class Qual(db.Model):
    __tablename__ = 'volunteer_qual'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)

class RoleQuals(db.Model):
    __tablename__ = 'volunteer_role_qual'
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
    qual_id = db.Column(db.Integer, db.ForeignKey('qual.id'), primary_key=True)
    required = db.Column(db.Boolean, nullable=False, default=False)
    self_certified = db.Column(db.Boolean, nullable=False, default=False)

class UserQuals(db.Model):
    __tablename__ = 'user_role_qual'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    qual_id = db.Column(db.Integer, db.ForeignKey('qual.id'), primary_key=True)
"""

