# Train Booking Fullstack App

Django REST backend + React frontend.

## Quickstart (development)

### Backend
```
cd backend
python -m venv venv
source venv/bin/activate   # windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver 8000
```

### Frontend
```
cd frontend
npm install
npm start
```

API endpoints:
- GET  http://127.0.0.1:8000/api/trains/
- POST http://127.0.0.1:8000/api/trains/<id>/book/   JSON body: { "seats": 2 }



## Docker (development)

You can run the whole stack with Docker Compose (uses Postgres):

```
docker-compose build
docker-compose up
```

- Backend will be on http://localhost:8000
- Frontend (served by nginx) will be on http://localhost:3000

Ensure you copy `.env` and adjust secrets before running in production.

## GitHub Actions (CI)

A workflow is included at `.github/workflows/ci.yml` that:
- Checks out code
- Sets up Node and Python
- Installs backend and frontend dependencies
- Builds the React app
- Runs Django migrations and collects static (for CI preview)

You may need to add secrets (if deploying).
