from django.shortcuts import render

# Create your views here.
def chempionats(request):
    return render(request, '/chempionats/chempionats.html')