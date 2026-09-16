HireHub – Online Job Portal & Recruitment Management System
HireHub is a Django-based Online Job Portal and Recruitment Management System.
The system connects Job Seekers and Recruiters on a single platform. Job Seekers can create profiles, upload resumes, search for jobs and apply for suitable jobs. Recruiters can create companies, post jobs, view applications and update application statuses.
---
1. Project Overview
HireHub is developed using Python and Django. It provides role-based access for Job Seekers and Recruiters and includes authentication, profile management, company management, job management, job search and filtering, applications, dashboards, Django Admin and REST API support.
---
2. Objectives
The main objectives of HireHub are:
Provide an online platform for job searching and recruitment.
Allow Job Seekers to create and manage profiles.
Allow Job Seekers to upload resumes and profile pictures.
Allow Recruiters to create and manage companies.
Allow Recruiters to create and manage job postings.
Provide job search and filtering functionality.
Allow Job Seekers to apply for jobs.
Allow Recruiters to manage job applications.
Provide application status tracking.
Provide separate dashboards for Job Seekers and Recruiters.
Provide Django Admin management.
Provide REST API functionality.
---
3. User Roles
Job Seeker
A Job Seeker can:
Register an account.
Login and logout.
Create and edit profile.
Add phone number and location.
Add skills and experience.
Upload resume.
Upload profile picture.
Search jobs.
Filter jobs.
View job details.
Apply for jobs.
View submitted applications.
Track application status.
Recruiter
A Recruiter can:
Register an account.
Login and logout.
Create recruiter profile.
Create company.
Edit company.
Delete company.
Upload company logo.
Create jobs.
Edit jobs.
Delete jobs.
View applications.
Update application status.
Manage recruitment activities.
Admin
The Admin can:
Manage users.
Manage profiles.
Manage companies.
Manage jobs.
Manage applications.
Access Django Admin panel.
---
4. Technologies Used
Python
Django
Django ORM
HTML
CSS
Bootstrap
JavaScript
SQLite
Django REST Framework
Pillow
Git
GitHub
Postman / Browser API testing
---
5. Main Modules
The project contains the following Django applications:
```text
accounts
users
companies
jobs
applications
dashboard
api
```
Accounts
Handles:
Registration
Login
Logout
Authentication
Users
Handles:
User profiles
User roles
Resume upload
Profile picture upload
Companies
Handles:
Company creation
Company listing
Company editing
Company deletion
Company logo upload
Jobs
Handles:
Job creation
Job listing
Job details
Job editing
Job deletion
Search
Filtering
Pagination
Applications
Handles:
Job applications
Cover letters
Application listing
Application status
Recruiter application management
Dashboard
Provides separate dashboard functionality for:
Job Seekers
Recruiters
API
Provides REST API endpoints for project data.
---
6. Project Structure
```text
HireHub/
│
├── manage.py
├── db.sqlite3
├── README.md
│
├── hirehub/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
├── users/
├── companies/
├── jobs/
├── applications/
├── dashboard/
├── api/
│
├── templates/
├── static/
│
└── media/
    ├── resumes/
    ├── profile_pictures/
    └── company_logos/
```
---
7. Database Models
The project uses Django ORM with SQLite database.
User
Django's built-in User model is used for authentication.
Profile
Stores additional user information such as:
Phone
Location
Skills
Experience
Resume
Profile picture
User type
Created date
Company
Stores:
Recruiter
Company name
Description
Website
Location
Logo
Created date
Job
Stores:
Recruiter
Company
Job title
Description
Requirements
Location
Salary
Job type
Experience required
Deadline
Created date
Application
Stores:
Job Seeker
Job
Cover letter
Application status
Applied date
Application statuses are:
```text
Pending
Shortlisted
Rejected
Selected
```
---
8. Authentication and Authorization
HireHub uses Django's built-in authentication system.
The system provides:
User registration
Login
Logout
Password hashing
Password confirmation
Role selection
Login protection
Role-based authorization
CSRF protection
Job Seeker and Recruiter features are protected according to their user roles.
---
9. Job Search and Filtering
Users can search and filter available jobs using:
Keyword
Location
Job Type
Company
Supported job types:
```text
Full Time
Part Time
Internship
Contract
```
Pagination is also implemented for job listings.
---
10. Job Application Workflow
The main recruitment workflow is:
```text
Job Seeker Registration
        ↓
Login
        ↓
Create / Update Profile
        ↓
Upload Resume
        ↓
Browse Jobs
        ↓
Search / Filter Jobs
        ↓
View Job Details
        ↓
Apply for Job
        ↓
Recruiter Views Application
        ↓
Recruiter Updates Status
        ↓
Job Seeker Checks Application Status
```
---
11. Application Status
Recruiters can update application status.
Available statuses:
```text
Pending
Shortlisted
Rejected
Selected
```
Job Seekers can view their current application status from the My Applications page.
---
12. Dashboards
Job Seeker Dashboard
The Job Seeker dashboard provides application-related information including:
Total Applications
Pending Applications
Shortlisted Applications
Selected Applications
Rejected Applications
Recruiter Dashboard
The Recruiter dashboard provides recruitment-related information including:
Total Companies
Total Jobs
Total Applications
Pending Applications
Shortlisted Applications
Selected Applications
Rejected Applications
---
13. REST API
HireHub provides REST API functionality using Django REST Framework.
Example Endpoint
```text
GET /api/jobs/
```
Local URL
```text
http://127.0.0.1:8000/api/jobs/
```
The API returns job information in JSON format.
Single Job Example
```text
http://127.0.0.1:8000/api/jobs/2/
```
---
14. Django Admin
The Django Admin panel is available at:
```text
http://127.0.0.1:8000/admin/
```
Admin can manage:
Users
Profiles
Companies
Jobs
Applications
---
15. Installation and Setup
Step 1: Clone the Project
```bash
git clone <your-github-repository-url>
```
Step 2: Open Project Folder
```bash
cd HireHub
```
Step 3: Create Virtual Environment
```bash
python -m venv venv
```
Step 4: Activate Virtual Environment
For Windows:
```bash
venv\Scripts\activate
```
Step 5: Install Dependencies
```bash
pip install django pillow djangorestframework
```
Step 6: Run Migrations
```bash
python manage.py migrate
```
Step 7: Create Superuser
```bash
python manage.py createsuperuser
```
Step 8: Start Development Server
```bash
python manage.py runserver
```
Open the following URL in your browser:
```text
http://127.0.0.1:8000/
```
---
16. Important URLs
Feature	URL
Home	`/`
Register	`/register/`
Login	`/login/`
Role Dashboard	`/users/role-home/`
Profile	`/users/profile/`
Companies	`/company/`
Create Company	`/company/create/`
Jobs	`/jobs/`
Create Job	`/jobs/create/`
My Applications	`/applications/my-applications/`
Recruiter Applications	`/applications/recruiter-applications/`
Admin	`/admin/`
Jobs API	`/api/jobs/`
---
17. Testing Completed
The following features have been tested:
Registration
Login
Logout
Role-based access
Profile management
Resume upload
Profile picture upload
Company creation
Company editing
Company deletion
Job creation
Job editing
Job deletion
Job search
Location filtering
Job type filtering
Company filtering
Pagination
Job details
Job application
Application listing
Application status update
Job Seeker dashboard
Recruiter dashboard
Django Admin
REST API GET request
---
18. Security Features
The project uses Django security features including:
Password hashing
CSRF protection
Authentication
Login-required protected pages
Role-based authorization
Form validation
---
19. Future Scope
Possible future improvements include:
Email notifications
Advanced job recommendations
Resume parsing
Recruiter analytics
Online interviews
Advanced REST API
Cloud deployment
Mobile application
Advanced search
Job alerts
---
20. Conclusion
HireHub provides an end-to-end online recruitment platform using Django.
It connects Job Seekers and Recruiters and provides features such as authentication, profile management, company management, job posting, job searching, job applications, application tracking, dashboards, admin management and REST API support.
The project demonstrates the practical use of Django, Django ORM, authentication, forms, file uploads, role-based authorization, CRUD operations, search, filtering, pagination and REST API development.