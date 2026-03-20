

# Content Monitoring & Flagging System

## Overview

This project is a backend system built using Django and Django REST Framework. It monitors content based on user-defined keywords, generates flags for matches, and supports a review workflow with suppression logic.

## Features

* Add keywords via API
* Scan content (mock dataset used)
* Match keywords with content using scoring logic
* Generate flags for matches
* Review flags (pending, relevant, irrelevant)
* Suppression logic to avoid re-flagging irrelevant content unless updated

## Matching Logic

* Exact match in title → 100
* Partial match in title → 70
* Match in body → 40

## Suppression Logic

If a flag is marked as **irrelevant**, it will not reappear unless:

* The content item’s `last_updated` field is newer than the time it was reviewed

## Tech Stack

* Django
* Django REST Framework
* SQLite

## Setup Instructions

1. Clone the repository

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Start server:
   python manage.py runserver

## API Endpoints

### Add Keyword

POST /api/keywords/
{
"name": "django"
}

### Run Scan

POST /api/scan/

### Get Flags

GET /api/flags/

### Update Flag Status

PATCH /api/flags/{id}/
{
"status": "irrelevant"
}

## Assumptions

* Matching is case-insensitive
* Mock dataset used instead of external API
* Duplicate flags avoided using unique constraint

## Future Improvements

* Background jobs (Celery)
* Better NLP-based matching
* Pagination & filtering
* UI dashboard
