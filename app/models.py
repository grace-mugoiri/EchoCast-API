from  . import db

class Episodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    audio_url = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, server_default=db.func.now())