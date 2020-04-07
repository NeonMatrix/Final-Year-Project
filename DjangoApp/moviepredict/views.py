from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .make_prediction import *

# View for the form page of the web app.
def index(request):
    return render(request, 'moviepredict/index.html', {})


# code to process the movie detail submitted through the form 
# and redirect the web app to the reult page
def makeRatingPrediction(request):

    #get values from the ubmitted form
    try:
        movieTitle = request.POST['movieTitle']
        directorList = request.POST.getlist('director[]')
        actorsList = request.POST.getlist('actor[]')
        budget = request.POST['budget']
        runtime = request.POST['runtime']
        genre = request.POST.getlist('genre')

    # incase there is an error with the submission form, 
    # it will relaod the page with an error message displaued
    except (KeyError):
        return render(request, 'moviepredict/index.html', 
            {
                'error_message': "Fill in all details",
            }
        )
    else:

        # initislaing varibles to be used when processing the movie data to make a prediction 
        totalActorOscars = 0
        totalActorNomOscars = 0
        totActorOtherWins = 0
        totActorOtherNoms = 0
        totalDirectorOscars = 0
        totalDirectorNomOscars = 0
        totDirectorOtherWins = 0
        totDirectorOtherNoms = 0

        animation = 0
        action = 0
        adventure = 0
        comedy = 0
        crime = 0
        documentary = 0
        drama = 0
        family = 0
        fantasy = 0
        history = 0
        horror = 0
        music = 0
        mystery = 0
        science_fiction = 0
        romance = 0
        thriller = 0
        western = 0
        war = 0
        
        if 'Animation' in genre:
            animation = 1
        if 'Action' in genre:
            action = 1
        if 'Adventure' in genre:
            adventure = 1
        if 'Comedy' in genre:
            comedy = 1
        if 'Crime' in genre:
            crime = 1
        if 'Documentary' in genre:
            documentary = 1
        if 'Drama' in genre:
            drama = 1
        if 'Family' in genre:
            family = 1
        if 'Fantasy' in genre:
            fantasy = 1
        if 'History' in genre:
            history = 1
        if 'Horror' in genre:
            horror = 1
        if 'Music' in genre:
            music = 1
        if 'Mystery' in genre:
            mystery = 1
        if 'Science Fiction' in genre:
            science_fiction = 1
        if 'Romance' in genre:
            romance = 1
        if 'Thriller' in genre:
            thriller = 1
        if 'Western' in genre:
            western = 1
        if 'War' in genre:
            war = 1

        # get total amount of oscars and awards won/nomtiated by the actors submitted in the form
        for actor in actorsList:
            awards = getActorAwards(actor)
            totalActorOscars = totalActorOscars + awards[0]
            totalActorNomOscars = totalActorNomOscars + awards[1]
            totActorOtherWins = totActorOtherWins + awards[2]
            totActorOtherNoms = totActorOtherNoms + awards[3]
        
        # get total amount of oscars and awards won/nomtiated by the directors submitted in the form
        for director in directorList:
            awards = getDirectorAwards(director)
            totalDirectorOscars = totalDirectorOscars + awards[0]
            totalDirectorNomOscars = totalDirectorNomOscars + awards[1]
            totDirectorOtherWins = totDirectorOtherWins + awards[2]
            totDirectorOtherNoms = totDirectorOtherNoms + awards[3]

        # predict movie rating with the movie details
        rating = preditRating([runtime, budget, animation, action, adventure, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, science_fiction, romance, thriller, western, war, totalActorOscars, totalActorNomOscars, totActorOtherWins, totActorOtherNoms, totalDirectorOscars, totalDirectorNomOscars, totDirectorOtherWins, totDirectorOtherNoms])

        # redirect the web app to the results to page to display the predicted rating 
        return render(request, 'moviepredict/result.html', 
            {
                # the context for the results page
                'movieTitle' : movieTitle,
                'budget' : budget,
                'runtime' : runtime,
                'actors' : actorsList,
                'directors' : directorList,
                'genre' : genre,
                'rating' : rating,
                'num_stars' : range(rating),
                'num_black_stars' : range(10 - rating)
            })