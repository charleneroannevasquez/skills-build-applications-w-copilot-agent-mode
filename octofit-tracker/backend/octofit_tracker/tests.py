from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test Hero", email="test@hero.com", team="Test Team")
        self.assertEqual(user.name, "Test Hero")
        self.assertEqual(user.email, "test@hero.com")
        self.assertEqual(user.team, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", members=["Test Hero"])
        self.assertEqual(team.name, "Test Team")
        self.assertIn("Test Hero", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test Hero", activity="Running", duration=30)
        self.assertEqual(activity.user, "Test Hero")
        self.assertEqual(activity.activity, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team="Test Team", points=100)
        self.assertEqual(lb.team, "Test Team")
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="Test Hero", workout="Pushups", reps=20)
        self.assertEqual(workout.user, "Test Hero")
        self.assertEqual(workout.workout, "Pushups")
        self.assertEqual(workout.reps, 20)
