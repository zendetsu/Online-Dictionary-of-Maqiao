from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import distinct

# Initialize Flask App
app = Flask(__name__)

# Configure the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://omams:your_password@localhost/maqiao_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Define the Database Model
class DictionaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(300), nullable=False)
    page_number = db.Column(db.Integer, nullable=True)
    definition = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text)
    related = db.Column(db.String(300))

# Routes
@app.route("/")
def home():
    entries = DictionaryEntry.query.with_entities(
        DictionaryEntry.word,
        DictionaryEntry.page_number,
        DictionaryEntry.definition,
        DictionaryEntry.example,
        DictionaryEntry.related
    ).distinct(DictionaryEntry.word).all()

    return render_template("home.html", entries=entries)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip()
    if not query:
        results = []
    else:
        # Fetch unique results for the search query
        results = DictionaryEntry.query.with_entities(
            DictionaryEntry.word,
            DictionaryEntry.page_number,
            DictionaryEntry.definition,
            DictionaryEntry.example,
            DictionaryEntry.related
        ).filter(DictionaryEntry.word.contains(query)).distinct(DictionaryEntry.word).all()

    return render_template("search.html", results=results, query=query)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the table directly without migrations
    app.run(debug=True)

