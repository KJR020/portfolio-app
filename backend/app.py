from flask import Flask, jsonify, request

app = Flask(__name__)

# 仮の画像データリスト
images = []


@app.route("/api/images", methods=["GET"])
def get_images():
    return jsonify(images)


@app.route("/api/images", methods=["POST"])
def add_image():
    new_image = request.get_json()
    images.append(new_image)
    return jsonify(new_image), 201


if __name__ == "__main__":
    app.run(debug=True)
