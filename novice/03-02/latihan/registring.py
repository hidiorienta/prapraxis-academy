from flask import Flask

app = Flask(__name__)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = 'Not enough storage space.'

app.register_error_handler(InsufficientStorage, handle_507)

raise InsufficientStorage()

if __name__ == "__main__":
    app.run(debug=True)
