from flask import json, Flask
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)

@app.errorhandler(InternalServerError)
def handle_500(e):
    original = getattr(e, "original_exception", None)

    if original is None:
        # direct 500 error, such as abort(500)
        return render_template("500.html"), 500

    # wrapped unhandled error
    return render_template("500_unhandled.html", e=original), 500

if __name__ == "__main__":
    app.run(debug=True)

