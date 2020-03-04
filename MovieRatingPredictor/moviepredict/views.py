from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PredictedMovie

def index(request):
    return render(request, 'moviepredict/index.html', {})

def result(request, budget):
    return render(request, 'moviepredict/result.html', {'budget' : budget})

def makeRatingPrediction(request):
    try:
        budget = request.POST['budget']
        print(budget)
    except (KeyError):
        return render(request, 'moviepredict/index.html', 
            {
                'error_message': "You didn't select a choice",
            }
        )
    else:
        #return HttpResponseRedirect(reverse('moviepredict:result', args=(budget,)))
        return render(request, 'moviepredict/result.html', {'budget' : budget})