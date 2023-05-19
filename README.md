README

# Course Review App

This repository contains a Course Review application where users can share and review courses they have learned.

![image](https://github.com/risakatelynt/studybuddy/assets/124533180/bae82320-3106-49fa-84f2-cdcd6434995f)

![image](https://github.com/risakatelynt/studybuddy/assets/124533180/2fef6947-ae16-4706-8097-ae2d4eebc421)

![image](https://github.com/risakatelynt/studybuddy/assets/124533180/7c2854bf-a45f-40a7-b476-baee5af3aeda)

## Features

- Add descriptions, notes, and images for courses.
- Rate and review courses.
- View and discover courses reviewed by other users.
- Search and filter courses based on different criteria.

## Technologies Used

- Django: Python web framework for building backend applications.
- jQuery: JavaScript library for simplifying HTML document traversal and manipulation.
- Bootstrap: CSS framework for responsive web design.
- HTML: Markup language for structuring web pages.
- CSS: Style sheet language for specifying the visual presentation of a document.

## Installation

1. Clone the repository:

```
git clone <repository-url>
```

2. Setup and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate   # For Unix/Linux
env\Scripts\activate   # For Windows
```

3. Install the Python dependencies:

```
pip install -r requirements.txt
```

4. Set up the database:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

6. Access the application in your browser:

```
http://127.0.0.1:8000/
```

## Configuration

To configure the application, modify the following files:

- `server/config.js`: Configure the MongoDB connection settings.

## Usage

1. Sign up for a new account or log in with existing credentials.
2. Explore the courses available in the application.
3. Add a new course by providing a description, notes, and images.
4. Rate and review courses that you have learned.
5. View detailed information about a specific course, including its ratings and reviews.
6. Search for courses based on keywords.
7. Edit or delete your own courses, ratings, and reviews.
8. Log out from the application when done.
