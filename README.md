# HireHub — Online Job Portal & Recruitment Management System

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-5.2%2B-092E20) ![License](https://img.shields.io/badge/License-MIT-green)


HireHub is a Django-based recruitment platform that brings job seekers and recruiters together. Job seekers can build profiles, explore vacancies and track applications. Recruiters can manage company details, publish jobs and review applications.

> **Project status:** Academic / portfolio project. Review security, API permissions and deployment settings before using real personal data or deploying publicly.

## Features

### Job seekers
- Register and sign in using the Job Seeker role.
- Create and update a profile with skills, experience, location and contact details.
- Upload a resume and profile picture.
- Search and filter jobs by keyword, location, job type and company.
- View job details, submit applications and track application status.

### Recruiters
- Register and sign in using the Recruiter role.
- Create and manage company profiles and logos.
- Create, update and delete job postings.
- Review applications submitted to their jobs.
- Update application status: Pending, Shortlisted, Selected or Rejected.

### Platform
- Role-aware login and role-based page access.
- Separate dashboards for job seekers and recruiters.
- Django admin interface.
- Read-only REST API endpoints for jobs, companies and applications.
- Responsive custom CSS styling.

## Technology stack

- Python
- Django
- Django REST Framework
- SQLite (development database)
- HTML, CSS and JavaScript
- Pillow (image uploads)

## Project structure

```text
HIERHUB_DJANGO_FINAL_PROJECT/
├── accounts/                 # Authentication and registration
├── applications/             # Job applications and status workflow
├── api/                      # REST API serializers, views and URLs
├── companies/                 # Recruiter company management
├── dashboard/                 # Role-specific dashboards
├── docs/                      # Architecture and project documentation
├── screenshots/               # Add sanitized UI screenshots before publishing
├── hirehub/                   # Django settings and root URLs
├── jobs/                      # Job posting, search and filters
├── media/                     # Local uploads (ignored by Git)
├── static/css/                # Project stylesheet
├── templates/                 # Django HTML templates
├── users/                     # Profiles and user roles
├── .env.example               # Example environment configuration
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/HireHub.git
cd HireHub
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and set a private `DJANGO_SECRET_KEY`. The settings module reads environment variables directly; if you use a `.env` file locally, make sure your terminal or IDE loads those values, or set them in PowerShell:

```powershell
$env:DJANGO_SECRET_KEY="your-private-development-key"
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
```

Do not commit `.env` or share your secret key.

### 5. Create database tables

```bash
python manage.py migrate
```

### 6. Create an administrator (optional)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. The login page is at `http://127.0.0.1:8000/login/`.

## API endpoints

| Endpoint | Description |
| --- | --- |
| `/api/jobs/` | List jobs |
| `/api/jobs/<id>/` | Retrieve one job |
| `/api/companies/` | List companies |
| `/api/companies/<id>/` | Retrieve one company |
| `/api/applications/` | List applications |
| `/api/applications/<id>/` | Retrieve one application |

**Important:** Review and restrict API permissions before deployment. Application records may contain personal information; they must not be exposed publicly.

## Application statuses

- `Pending` — application received.
- `Shortlisted` — candidate selected for the next stage.
- `Selected` — candidate selected for the role.
- `Rejected` — application not selected.

## Development checks

```bash
python manage.py check
python manage.py test
```

## GitHub publishing checklist

- [ ] Update the repository URL and maintainer details if needed.
- [ ] Add screenshots of the actual running application to a `screenshots/` folder.
- [ ] Confirm `.env`, database files and uploaded media are not staged.
- [ ] Run migrations and verify the project starts from a clean clone.
- [ ] Review API permissions and production security settings.

## Documentation

See [`docs/architecture.md`](docs/architecture.md) for the app responsibilities, data relationships and route overview.

## License

This project is distributed under the MIT License. See [`LICENSE`](LICENSE).
