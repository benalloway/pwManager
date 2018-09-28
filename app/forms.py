from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email
from app.models import User, Group


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class CreateGroupForm(FlaskForm):
    group_name = StringField('Group Name', validators=[DataRequired()])
    group_email = StringField('Group Email', validators=[DataRequired(), Email()])
    group_password = StringField('Group Password', validators=[DataRequired()])
    group_is_admin = BooleanField('Is Group Admin')
    submit = SubmitField('Add Group')

    def validate_group_name(self, group_name):
        group = Group.query.filter_by(group_name=group_name.data).first()
        if group is not None:
            raise ValidationError('Please use a different Group Name.')
