from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateRecord(FlaskForm):
    title = TextField('Customer Name')
    shortdesc = TextField('Email')
    priority = IntegerField('Mobile No:')
    create = SubmitField('Create')

class DeleteRecord(FlaskForm):
    key = TextField('Customer ID')
    title = TextField('Customer Name')
    delete = SubmitField('Delete')

class UpdateRecord(FlaskForm):
    key = TextField('Customer ID')
    shortdesc = TextField('Email')
    update = SubmitField('Update')
