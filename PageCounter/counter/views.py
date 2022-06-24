from django.shortcuts import render

def home(request):
    counter = request.session.get('count', 0)
    newCounter = counter + 1
    request.session['count'] = newCounter
    return render(request, 'counter/Home.html', {'count' : newCounter})
