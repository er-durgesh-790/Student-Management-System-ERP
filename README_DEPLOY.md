# Student Management System ERP - Web Deployment

## Render settings
- Runtime: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn StudentERP_Web.aap:app`
- Health Check Path: `/health`

## Required environment variable
Set `SECRET_KEY` in Render to a long random value.

## Default admin account
- Username: `admin`
- Initial password: `admin123`

Change the password immediately after the first login from **Change Password**.

## Important
The current application uses SQLite. On Render's free web service, local filesystem/database data is not persistent across all restarts/redeploys. For production use, move the database to PostgreSQL or attach persistent storage.
