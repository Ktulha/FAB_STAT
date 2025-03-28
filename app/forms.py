from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, DateField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_uploads import UploadSet, IMAGES


images = UploadSet('images', IMAGES)


class FabricFormABC(FlaskForm):
    """Base form for fabric related data."""
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    width = FloatField('Width')
    picture = FileField('Pictures', validators=[
                        FileRequired(), FileAllowed(images, 'Images only!')])

    submit = SubmitField('Submit')
