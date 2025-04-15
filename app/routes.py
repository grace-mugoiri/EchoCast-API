from flask import Blueprint, request, jsonify
from app.models import db, Episode

main = Blueprint("main", __name__)

@main.route("/episodes", methods=["POST"])
def create_episode():
    data = request.get_json()
    new_episode = Episode(
        title=data["title"],
        description=data["description"],
        audio_url=data["audio_url"]
    )
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({"message": "Episode added"}), 201

@main.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": ep.id,
        "title": ep.title,
        "description": ep.description,
        "audio_url": ep.audio_url,
        "date_posted": ep.date_posted
    } for ep in episodes]), 200

@main.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "title": episode.title,
        "description": episode.description,
        "audio_url": episode.audio_url,
        "date_posted": episode.date_posted
    }), 200

@main.route("/episodes/<int:id>", methods=["PUT"])
def update_episode(id):
    episode = Episode.query.get_or_404(id)
    data = request.get_json()
    episode.title = data.get("title", episode.title)
    episode.description = data.get("description", episode.description)
    episode.audio_url = data.get("audio_url", episode.audio_url)
    db.session.commit()
    return jsonify({"message": "Episode updated"}), 200

@main.route("/episodes/<int:id>", methods=["DELETE"])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200
