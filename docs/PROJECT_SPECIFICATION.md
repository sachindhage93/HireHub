# HIREHUB – PROJECT SPECIFICATION

**Project Title:** Online Job Portal & Recruitment Management System  
**Project Type:** Django Web Application  
**Backend:** Python and Django  
**Frontend:** HTML5, CSS3, Bootstrap, JavaScript  
**Database:** SQLite (development)  
**API:** Django REST Framework

## 1. Project Overview
HireHub is a web-based job portal and recruitment management system that connects job seekers with recruiters. Job seekers can create profiles, upload resumes, search and filter job openings, apply for jobs, and track application status. Recruiters can create company profiles, publish and manage job posts, review applicants, and update application statuses. Administrators manage users and system data.

## 2. Problem Statement
Traditional recruitment often relies on emails, spreadsheets, and manual resume collection. These disconnected processes make it difficult to organize vacancies, applications, and candidate status. HireHub provides one centralized platform to manage the recruitment workflow digitally.

## 3. Project Objectives
- Develop a multi-app web application using Python and Django.
- Use Django Models and ORM for database operations.
- Implement registration, login, logout, and role-based access.
- Allow job seekers to maintain profiles and upload resumes.
- Allow recruiters to manage company profiles and job postings.
- Provide job search, filtering, and pagination.
- Support job applications and application-status tracking.
- Provide separate dashboards for job seekers and recruiters.
- Provide administrative management through Django Admin.
- Expose job data through Django REST Framework API.
- Maintain source code and documentation using Git and GitHub.

## 4. User Roles
| Role | Responsibilities |
|---|---|
| Job Seeker | Register/login, manage profile, upload resume, search jobs, apply, track applications. |
| Recruiter | Register/login, manage profile, create company, post/manage jobs, view applicants, update statuses. |
| Admin | Manage users, profiles, companies, jobs, and applications. |

## 5. Functional Requirements
1. User registration with role selection.
2. User login and logout.
3. Role-based authorization for seeker and recruiter features.
4. Job seeker/recruiter profile creation and editing.
5. Resume and profile-picture upload.
6. Recruiter company creation, listing, editing, and deletion.
7. Job creation, listing, details, editing, and deletion by authorized recruiters.
8. Search jobs using keywords and filters such as location, job type, and company.
9. Paginate job listings.
10. Allow job seekers to apply for jobs with a cover letter.
11. Allow recruiters to view applications for their jobs.
12. Allow recruiters to update application status (Pending, Shortlisted, Rejected, Selected).
13. Display seeker and recruiter dashboard statistics.
14. Provide REST API access to job records.
15. Provide admin management and validation/error messages.

## 6. Non-Functional Requirements
- Responsive and understandable user interface.
- Secure password handling using Django authentication.
- CSRF protection for POST forms.
- Authenticated access to private pages.
- Server-side validation of user input and uploads.
- Maintainable modular application structure.
- Do not expose secret keys or credentials in source control.

## 7. Technology Stack
| Layer | Technology |
|---|---|
| Programming language | Python |
| Backend framework | Django |
| Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| Database | SQLite for local development |
| REST API | Django REST Framework |
| Image uploads | Pillow |
| IDE | Visual Studio Code |
| Version control | Git and GitHub |
| API testing | Browser/Postman |

## 8. Main Django Apps / Modules
- **accounts:** Registration, login, logout and authentication.
- **users:** User profile and role information.
- **companies:** Recruiter company management.
- **jobs:** Job posting, job details, editing, deletion, search and filtering.
- **applications:** Job applications and status management.
- **dashboard:** Job seeker and recruiter dashboards.
- **api:** REST API serializers, views and URL routes.

## 9. Database Entities
The database design uses Django's built-in `auth_user` table and four project model tables:
- **Profile:** One-to-one extension of a User, including phone, location, skills, experience, resume, profile picture, user type and creation date.
- **Company:** Recruiter-owned company information including name, description, website, location, logo and creation date.
- **Job:** Job vacancy information, linked to a recruiter and a company.
- **Application:** A seeker's application to a job, including cover letter, status and application date.

See [ER_DIAGRAM.md](ER_DIAGRAM.md) for the ER diagram and relationship details.

## 10. Main Workflows
**Job Seeker:** Register → Login → Complete Profile → Search/Filter Jobs → View Job Details → Apply → Track Application Status.

**Recruiter:** Register → Login → Complete Profile → Create Company → Post Job → View Applicants → Update Application Status.

**Admin:** Login to Django Admin → Manage users, profiles, companies, jobs and applications.

## 11. REST API
The project contains a Django REST Framework jobs API. The confirmed list endpoint in the project is:
- `GET /api/jobs/` — retrieve the job list.

Other endpoints and HTTP methods should be documented according to the actual API URL and view configuration.

## 12. Testing Requirements
- Registration, valid login, invalid login and logout.
- Job list and detail pages.
- Authorized job creation, editing and deletion.
- Job seeker cannot access recruiter-only actions.
- Successful application and recruiter applicant management.
- Application status update.
- Form validation and upload validation.
- API response and permissions.

## 13. Expected Deliverables
- Complete Django source code.
- GitHub repository.
- README installation and usage instructions.
- Project specification and ER diagram.
- Project report and implementation screenshots.
- Test cases/results and API evidence.
- Final working demonstration.

## 14. Future Enhancements
- Enforce duplicate-application prevention at database level.
- Email notifications for application-status changes.
- Skill-based job recommendations.
- Recruiter analytics and charts.
- API authentication and expanded API endpoints.
- Cloud media storage and production deployment.
