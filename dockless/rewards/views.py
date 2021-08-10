from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def valReward(request):
    return render(request, 'rewards/valReward.html') 


@login_required
def invalReward(request):
    return render(request, 'rewards/invalReward.html') 