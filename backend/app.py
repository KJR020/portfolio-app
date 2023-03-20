import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "url": self.url}


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/api/images", methods=["GET"])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])


@app.route("/api/images", methods=["POST"])
def add_image():
    data = request.get_json()
    new_image = Image(title=data["title"], url=data["url"])
    db.session.add(new_image)
    db.session.commit()
    return jsonify(new_image.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)
