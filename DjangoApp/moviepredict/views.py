from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'moviepredict/index.html', {})

def result(request, budget):
    return render(request, 'moviepredict/result.html', {'budget' : budget})

def makeRatingPrediction(request):
    try:
        actor1 = request.POST['actor1']
        actor2 = request.POST['actor2']
        actor3 = request.POST['actor3']
        actor4 = request.POST['actor4']
        actor5 = request.POST['actor5']
        budget = request.POST['budget']
        runtime = request.POST['runtime']

        print(budget)
    except (KeyError):
        return render(request, 'moviepredict/index.html', 
            {
                'error_message': "You didn't select a choice",
            }
        )
    else:
        #return HttpResponseRedirect(reverse('moviepredict:result', args=(budget,)))
        return render(request, 'moviepredict/result.html', 
            {
                'budget' : budget,
                'actor1' : actor1,
                'actor2' : actor2,
                'actor3' : actor3,
                'actor4' : actor4,
                'actor5' : actor5,
                'runtime' : runtime,
            })