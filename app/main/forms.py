from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators=[Required()])
    submit = SubmitField('Share')


class PitchForm(FlaskForm):
    pitch_title = StringField('Enter Title Of The Pitch Here...', validators=[Required()])
    content = TextAreaField('Enter Your Pitch Here...', validators=[Required()])
    category = SelectField('Category', choices=[('Interview-Pitch','Interview Pitch'),('Product-Pitch','Product Pitch'),('Promotion-Pitch','Promotion Pitch'),('Business-Pitch','Business Pitch')], validators=[Required()])
    submit = SubmitField('Submit Pitch It!')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit Comment')
