from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class FormSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    age = request.form['age']
    gender = request.form['gender']
    address = request.form['address']

    
    if not name or not email or not phone or not age or not gender or not address:
        flash("All fields are required!", "danger")
        return redirect(url_for('index'))

    if len(phone) != 10 or not phone.isdigit():
        flash("Phone number must be exactly 10 digits.", "danger")
        return redirect(url_for('index'))

    try:
        age = int(age)  
    except ValueError:
        flash("Age must be a valid number.", "danger")
        return redirect(url_for('index'))

    
    if FormSubmission.query.filter_by(email=email).first():
        flash("Email already exists! Use a different email.", "danger")
        return redirect(url_for('index'))

    
    new_entry = FormSubmission(name=name, email=email, phone=phone, age=age, gender=gender, address=address)
    db.session.add(new_entry)
    db.session.commit()

    flash("Form submitted successfully!", "success")
    return redirect(url_for('index'))


@app.route('/records')
def records():
    records = FormSubmission.query.all()
    return render_template('records.html', records=records)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    record = FormSubmission.query.get(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Record deleted successfully!", "success")
    else:
        flash("Record not found!", "danger")

    return redirect(url_for('records'))

if __name__ == '__main__':
    app.run(debug=True)
