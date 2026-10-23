@echo off
cd /d "%~dp0"
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
echo Installing dependencies...
python -m pip install -r requirements.txt
echo Starting EWB Student Database CRUD Application...
echo Open http://127.0.0.1:8000/docs
python -m uvicorn app.main:app --reload
