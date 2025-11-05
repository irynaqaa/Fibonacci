from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)

@app.route('/pets', methods=['GET'])
def get_pets():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    if limit < 1 or limit > 100:
        return jsonify({'message': 'Invalid pagination limit. Must be between 1 and 100.'}), 400

    offset = (page - 1) * limit
    pets_query = Pet.query.limit(limit).offset(offset)
    pets = pets_query.all()

    total_pets = Pet.query.count()
    total_pages = (total_pets + limit - 1) // limit

    return jsonify({
        'current_page': page,
        'total_pages': total_pages,
        'pets': [pet.to_dict() for pet in pets]
    })

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
