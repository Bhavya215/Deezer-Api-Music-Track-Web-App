from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, DecimalField, validators, SubmitField

class TrackSearchForm(FlaskForm):
    q = StringField('Track Name', [validators.Length(min=1, max=50)])
    #submit = SubmitField("Find")
class TrackForm(FlaskForm):
    track_id = IntegerField('Track ID', [validators.NumberRange(min=20)])
    readable = BooleanField('Readable', [validators.NumberRange(min=0)])
    title = StringField('Title', [validators.Length(min=1, max=100)])
    title_short = StringField('Short Title Name', [validators.Length(min=0, max=50)])
    track_link = StringField('Track Link', [validators.Length(min=0)])
    duration = IntegerField('Duration', [validators.NumberRange(min=1)])
    track_rank = IntegerField('Rank', [validators.NumberRange(min=0)])
    artist_name = StringField('Artist Name', [validators.Length(min=0, max=80)])
    album_name = StringField('Album Name', [validators.Length(min=0, max=50)])
    #submit = SubmitField("Save")

class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', [validators.Length(min=1, max=100)])