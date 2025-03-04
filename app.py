from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the UserData model
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    father_name = db.Column(db.String(150), nullable=False)
    caste = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(150), nullable=False)
    religion = db.Column(db.String(150), nullable=False)
    profession = db.Column(db.String(150), nullable=False)
    birth_date = db.Column(db.String(150), nullable=False)
    birth_place = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    nationality = db.Column(db.String(150), nullable=False)
    id_card = db.Column(db.String(150), nullable=False)
    passport_number = db.Column(db.String(150), nullable=True)
    education = db.Column(db.String(150), nullable=False)
    language = db.Column(db.String(150), nullable=False)
    parents_profession = db.Column(db.String(150), nullable=False)
    spouse_children_details = db.Column(db.String(150), nullable=False)
    family_details = db.Column(db.String(150), nullable=False)
    famous_person_relation = db.Column(db.String(150), nullable=True)
    friend_reference = db.Column(db.String(150), nullable=True)
    criminal_record = db.Column(db.String(150), nullable=True)
    general_character = db.Column(db.String(150), nullable=True)
    assets = db.Column(db.String(150), nullable=True)
    political_affiliation = db.Column(db.String(150), nullable=True)
    councilor_report = db.Column(db.String(150), nullable=True)
    remarks = db.Column(db.String(150), nullable=True)

# Initialize the database inside an application context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Collect data from the form
    data = {
        'name': request.form['name'],
        'father_name': request.form['fatherName'],
        'caste': request.form['caste'],
        'contact': request.form['contact'],
        'religion': request.form['religion'],
        'profession': request.form['profession'],
        'birth_date': request.form['birthDate'],
        'birth_place': request.form['birthPlace'],
        'address': request.form['address'],
        'nationality': request.form['nationality'],
        'id_card': request.form['idCard'],
        'passport_number': request.form['passportNumber'],
        'education': request.form['education'],
        'language': request.form['language'],
        'parents_profession': request.form['parentsProfession'],
        'spouse_children_details': request.form['spouseChildrenDetails'],
        'family_details': request.form['familyDetails'],
        'famous_person_relation': request.form['famousPersonRelation'],
        'friend_reference': request.form['friendReference'],
        'criminal_record': request.form['criminalRecord'],
        'general_character': request.form['generalCharacter'],
        'assets': request.form['assets'],
        'political_affiliation': request.form['politicalAffiliation'],
        'councilor_report': request.form['councilorReport'],
        'remarks': request.form['remarks']
    }

    # Create a new record in the database
    new_user = UserData(**data)
    db.session.add(new_user)
    db.session.commit()

    # Save data to a text file using the user's name
    file_name = f"{data['name']}.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"User Data for {data['name']}:\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

    # Return a confirmation page
    return render_template('submit.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
