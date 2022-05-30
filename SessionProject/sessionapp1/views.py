from django.shortcuts import render
from sessionapp1.forms import SessionForm
from django.http import HttpResponse


def sessionConnection(request):
    stud = SessionForm(request.POST)
    return render(request, 'sessionapp1/login.html', {'form1': stud})


# Here we validate our form
def sessionLogin(request):
    username = "not logged in"
    contactNumber = "not found"
    if request.method == "POST":
        MyLoginForm = SessionForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            contactNumber = MyLoginForm.cleaned_data['contactNumber']
    else:
        MyLoginForm = SessionForm()
    context = {'username': username, 'contactNumber': contactNumber}
    return render(request, 'sessionapp1/loggedin.html', context)



# Heer the code is for session
def sessionFormView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        context = {'username': username}
        return render(request, 'sessionapp1/formView.html', context)
    else:
        return render(request, 'sessionapp1/formView.html', {})

# To logout from the site


def sessionLogout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("<strong>You are logged out </strong>")

