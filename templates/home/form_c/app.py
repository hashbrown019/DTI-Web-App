from flask import Flask, render_template, url_for
import bp_app as bp
import excel_migration as em
app = Flask(__name__)
app.register_blueprint(bp.app)
app.register_blueprint(em.app)

if __name__ == "__main__":
    app.run(debug=True)