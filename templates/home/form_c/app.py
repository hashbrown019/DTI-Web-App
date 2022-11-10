from flask import Flask, render_template, url_for
import bp_app as bp
app = Flask(__name__)
app.register_blueprint(bp.app)

if __name__ == "__main__":
    app.run(debug=True)