from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database

db = SQLAlchemy(app)
Migrate(app, db)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_categories = db.Column(db.JSON)
    action_categories = db.Column(db.JSON)
    subscription_status = db.Column(db.Enum('ACTIVE', 'EXPIRED'))

    def __repr__(self):
        return f'<User {self.id}>'

@app.route('/api/update-categories', methods=['POST'])
def update_categories():
    data = request.get_json()
    user_id = data.get('userId')
    question_categories = data.get('questionCategories')
    action_categories = data.get('actionCategories')

    if not user_id or not isinstance(question_categories, list) or not isinstance(action_categories, list):
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.get(user_id)
    if user:
        user.question_categories = question_categories
        user.action_categories = action_categories
        db.session.commit()
        return jsonify({'userId': user_id, 'questionCategories': user.question_categories, 'actionCategories': user.action_categories}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/get-categories', methods=['GET'])
def get_categories():
    user_id = request.args.get('userId')
    user = User.query.get(user_id)
    if user:
        return jsonify({'userId': user_id, 'questionCategories': user.question_categories, 'actionCategories': user.action_categories}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
