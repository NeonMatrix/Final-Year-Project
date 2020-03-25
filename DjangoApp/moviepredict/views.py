from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .make_prediction import *

def index(request):
    return render(request, 'moviepredict/index.html', {})

def result(request, budget):
    return render(request, 'moviepredict/result.html', {'budget' : budget})

def makeRatingPrediction(request):
    try:
        actorsList = request.POST.getlist('actor[]')
        budget = request.POST['budget']
        runtime = request.POST['runtime']
        genre = request.POST.getlist('genre')
        director = request.POST['director']

    except (KeyError):
        return render(request, 'moviepredict/index.html', 
            {
                'error_message': "You didn't select a choice",
            }
        )
    else:

        totalActorOscars = 0
        totalActorNomOscars = 0
        totActorOtherWins = 0
        totActorOtherNoms = 0

        animation = '0'
        action = '0'
        adventure = '0'
        comedy = '0'
        crime = '0'
        documentary = '0'
        drama = '0'
        family = '0'
        fantasy = '0'
        history = '0'
        horror = '0'
        music = '0'
        mystery = '0'
        science_fiction = '0'
        romance = '0'
        thriller = '0'
        western = '0'
        war = '0'
        
        if 'Animation' in genre:
            animation = '1'
        if 'Action' in genre:
            action = '1'
        if 'Adventure' in genre:
            adventure = '1'
        if 'Comedy' in genre:
            comedy = '1'
        if 'Crime' in genre:
            crime = '1'
        if 'Documentary' in genre:
            documentary = '1'
        if 'Drama' in genre:
            drama = '1'
        if 'Family' in genre:
            family = '1'
        if 'Fantasy' in genre:
            fantasy = '1'
        if 'History' in genre:
            history = '1'
        if 'Horror' in genre:
            horror = '1'
        if 'Music' in genre:
            music = '1'
        if 'Mystery' in genre:
            mystery = '1'
        if 'Science Fiction' in genre:
            science_fiction = '1'
        if 'Romance' in genre:
            romance = '1'
        if 'Thriller' in genre:
            thriller = '1'
        if 'Western' in genre:
            western = '1'
        if 'War' in genre:
            war = '1'

        for actor in actorsList:
            awards = getActorAwards(actor)
            totalActorOscars = totalActorOscars + awards[0]
            totalActorNomOscars = totalActorNomOscars + awards[1]
            totActorOtherWins = totActorOtherWins + awards[2]
            totActorOtherNoms = totActorOtherNoms + awards[3]

        directorAwards = getDirectorAwards(director)

        rating = preditRating([runtime, budget, animation, action, adventure, comedy, crime, documentary, drama, family, fantasy, history, horror, music, mystery, science_fiction, romance, thriller, western, war, str(totalActorOscars), str(totalActorNomOscars), str(totActorOtherWins), str(totActorOtherNoms), directorAwards[0], directorAwards[1], directorAwards[2], directorAwards[3]])

        #return HttpResponseRedirect(reverse('moviepredict:result', args=(budget,)))
        return render(request, 'moviepredict/result.html', 
            {
                'budget' : budget,
                'runtime' : runtime,
                'actors' : actorsList,
                'genre' : genre,
                'totalActorOscars' :  totalActorOscars,
                'totalActorNomOscars' : totalActorNomOscars,
                'totActorOtherWins' : totActorOtherWins,
                'totActorOtherNoms' : totActorOtherNoms,
                'directorOscars' : directorAwards[0],
                'directorOscarsNom' : directorAwards[1],
                'directorOtherWins' : directorAwards[2],
                'directorOtherNoms' : directorAwards[3],
                'rating' : rating,
                'num_stars' : range(rating),
                'num_black_stars' : range(10 - rating)
            })