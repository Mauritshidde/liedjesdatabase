from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, email_validator, EqualTo

class ToevoegenForm(FlaskForm):
    naam_liedje_toevoegen = StringField('naam van het liedje', validators=[DataRequired()])
    confirm = SelectField('weet je zekere dat je dit contact wilt torvoegen', choices=["confirm", "cancel"], validators[DataRequired()])
    submit = SubmitField('Submit')
