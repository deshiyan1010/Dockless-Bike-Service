from django.shortcuts import render


def valReward(request):
    return render(request, 'rewards/valReward.html') 

def invalReward(request):
    return render(request, 'rewards/invalReward.html') 