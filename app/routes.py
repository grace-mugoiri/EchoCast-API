from flask import BluePrint, request, jsonify
from .models import Episodes
from . import db

main = BluePrint('main', __name__)
@main.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episodes.query.all()
    return jsonify([{
        "id": e.id,
        "title": e.title,
        "description": e.description,
        "audio_url": e.audio_url,
        "date_posted": e.date_posted
    } for e in episodes])