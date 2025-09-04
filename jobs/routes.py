from flask import Blueprint, render_template, request, redirect, url_for

jobs_bp = Blueprint('jobs', __name__, template_folder='templates')

# Temporary job list (later can be replaced with database)
job_listings = []

@jobs_bp.route('/', methods=['GET', 'POST'])
def jobs_home():
    if request.method == 'POST':
        title = request.form.get('title')
        company = request.form.get('company')
        location = request.form.get('location')
        description = request.form.get('description')
        phone = request.form.get('phone')
        job = {
            'title': title,
            'company': company,
            'location': location,
            'description': description,
            'phone': phone
        }
        job_listings.append(job)
        return redirect(url_for('jobs.jobs_home'))
    return render_template('jobs.html', jobs=job_listings)