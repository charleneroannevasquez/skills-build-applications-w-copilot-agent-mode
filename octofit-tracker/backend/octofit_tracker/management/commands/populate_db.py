from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

HELP = 'Populate the octofit_db database with test data'

# Sample superhero data
USERS = [
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
]
TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Spider-Man"]},
    {"name": "DC", "members": ["Batman", "Superman", "Wonder Woman"]},
]
ACTIVITIES = [
    {"user": "Iron Man", "activity": "Running", "duration": 30},
    {"user": "Batman", "activity": "Cycling", "duration": 45},
]
LEADERBOARD = [
    {"team": "Marvel", "points": 120},
    {"team": "DC", "points": 110},
]
WORKOUTS = [
    {"user": "Superman", "workout": "Strength", "reps": 50},
    {"user": "Wonder Woman", "workout": "Yoga", "reps": 20},
]

class Command(BaseCommand):
    help = HELP

    def handle(self, *args, **options):
        client = MongoClient(host=settings.DATABASES['default']['CLIENT']['host'], port=settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        # Ensure unique index on email
        db.users.create_index("email", unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
