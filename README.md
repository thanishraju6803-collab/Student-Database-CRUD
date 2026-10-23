# EWB Student Database CRUD Application

A Python backend project based on the EWB Edu Tech internship assignment.

## Mandatory requirements

- Python
- FastAPI
- SQLite
- Create, Read, Update and Delete student records
- Input validation
- Missing-record handling
- Persistent database

## Student fields

- Student ID
- Name
- Date of Birth
- Email
- Phone
- Course
- Address
- Enrollment Date

## Setup

### 1. Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
uvicorn app.main:app --reload
```

### 4. Open API documentation

Open:

http://127.0.0.1:8000/docs

## API endpoints

- POST `/students/` - Create a student
- GET `/students/` - List students
- GET `/students/{student_id}` - Get one student
- PUT `/students/{student_id}` - Update a student
- DELETE `/students/{student_id}` - Delete a student

Filtering examples:

- `/students/?name=Rahul`
- `/students/?course=B.Tech%20CSE`

## Testing

Run:

```bash
pytest
```

## Database

SQLite database `students.db` is created automatically when the application starts.

Do not commit real student personal information or secrets.
