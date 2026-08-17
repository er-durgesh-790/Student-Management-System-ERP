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


## Professional Mobile Dashboard Update

This package includes:
- Responsive admin dashboard with mobile hamburger menu and slide-out sidebar.
- Responsive student dashboard with mobile sidebar navigation.
- Admin name/profile display and improved header spacing.
- Student notices/messages managed from **Portal Content**.
- Chairman profile and message managed from **Portal Content**.
- Academic calendar events managed from **Portal Content**.
- Social-media links can be added by the admin and open in a new tab.
- Existing admin/student password-change pages are retained.

### After copying to the Git repository

```powershell
cd C:\StudentERP_Git
git status
git add .
git commit -m "Professional mobile ERP dashboard and portal content"
git push
```

Render should then deploy the new commit automatically.
