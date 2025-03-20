Flask Form Handling Project with SQLite

Overview:
This project is a Flask-based web application that allows users to submit a form, validate the data, store it in an SQLite database, and view the stored records. The project also includes features like flash messages and record deletion.

Features:
- Form Submission: Users can enter their details and submit the form.
- Validation: Client-side (HTML5 & JavaScript) and server-side (Flask) validation.
- Database Storage: Uses SQLite with SQLAlchemy ORM.
- Flash Messages: Displays success or error messages.
- Record Viewing: A separate page to display stored records.
- Delete Records: Users can remove records from the database.
- Bootstrap UI: Responsive and user-friendly interface.

Tech Stack:
- Frontend: HTML, CSS, JavaScript (Bootstrap)
- Backend: Flask (Python)
- Database: SQLite (SQLAlchemy ORM)
- Version Control: Git & GitHub

Project Structure:

/flask_form_project
│── /templates
│   ├── form.html          # Form submission page
│   ├── records.html       # Display stored records
│── /static
│   ├── styles.css         # CSS file for styling
│── app.py                 # Main Flask application
│── database.db            # SQLite database file (auto-generated)
│── requirements.txt       # List of dependencies
│── README.md              # Project description


Installation & Setup:

Step 1: Clone the Repository
    sh
git clone https://github.com/suraj1821/flask-form-project
cd flask_form_project


Step 2: Create a Virtual Environment
    sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


 Step 3: Install Dependencies
    sh
pip install -r requirements.txt


 Step 4: Run the Application
    sh
python app.py

The app will run on http://127.0.0.1:5000/.

Usage:
1. Navigate to http://127.0.0.1:5000/ to access the form.
2. Fill out the form and submit it.
3. If the submission is successful, a success message will be displayed.
4. Click on the "View Records" button to see all stored submissions.
5. Optionally, delete a record if needed.

Enhancements & Future Improvements:
-  AJAX-based form submission for a better user experience.
-  Pagination for the records page.
-  Search & filter functionality.
-  Deploy the project on Render/Vercel/Heroku.

License
This project is licensed under the MIT License.


Contributions are welcome! Feel free to fork the repository and submit pull requests.

https://github.com/user-attachments/assets/cac1dea0-e711-4d93-95e7-4bfb79f5bdf3
