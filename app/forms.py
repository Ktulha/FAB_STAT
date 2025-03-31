from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, DateField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired, FileAllowed, FileField


class FabricFormABC(FlaskForm):
    """Base form for fabric related data."""
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    width = FloatField('Width')
    submit = SubmitField('Submit')
