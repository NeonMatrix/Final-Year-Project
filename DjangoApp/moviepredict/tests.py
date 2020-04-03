from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import *
from .make_prediction import *
#import DjangoApp.moviepredict.make_prediction

class TestMakePrediction(TestCase):

    def setUp(self):
        Actor.objects.create(name="Brad Pitt", imdb_id="nm0000093")
        Director.objects.create(name="Steven Spielberg", imdb_id="nm0000229")

    def test_get_actorId_that_exists(self):
        actorId = getActorID("Brad Pitt")
        self.assertEqual(actorId, "nm0000093")

    def test_get_actorId_that_does_not__exists(self):
        actorId = getActorID("Actor1")
        self.assertEqual(actorId, 0)

    def test_get_directorId_that_exists(self):
        directorId = getDirectorID("Steven Spielberg")
        self.assertEqual(directorId, "nm0000229")

    def test_get_directorId_that_does_not__exists(self):
        actorId = getActorID("Director1")
        self.assertEqual(actorId, 0)

    def test_get_actor_awards_for_existing_actor(self):
        awards = getActorAwards("Brad Pitt")
        self.assertEqual(awards, [2,0,112,199])

    def test_get_actor_awards_for_non_existing_actor(self):
        awards = getActorAwards("actor_test_case")
        self.assertEqual(awards, [0,0,0,0])

    def test_get_director_awards_for_existing_director(self):
        awards = getDirectorAwards("Steven Spielberg")
        self.assertEqual(awards, [3,0,189,204])

    def test_get_director_awards_for_non_existing_director(self):
        awards = getDirectorAwards("director_test_case")
        self.assertEqual(awards, [0,0,0,0])

    def test_predict_rating_for_4_star_movie(self):
        #movie is tt0326820
        movieDetails = [94,2500000,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,23,11,0,0,3,0,3]
        rating = preditRating(movieDetails)
        self.assertEqual(rating, 4)

    def test_predict_rating_for_8_star_movie(self):
        #movie is tt0266543
        movieDetails = [100,94000000,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,8,357,546,4,0,61,94,8]
        rating = preditRating(movieDetails)
        self.assertEqual(rating, 8)