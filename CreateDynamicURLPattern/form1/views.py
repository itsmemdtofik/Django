from django.shortcuts import render



def home(request, check):
    print(check)
    return render(request, 'form1/Index.html' , {'ch' : check})

#def clickResponse(request, my_id):
#    student = {'id': my_id}
#    return render(request, 'form1/clickResponse.html', student)
# StudentForm(auto_id = True,False,chaini_%s etc)

def clickResponse(request, my_id = 1):
    if my_id == 1:
        student = {'id': my_id, 'name':'Mohammad Tofik'}

    if my_id == 2:
        student = {'id': my_id, 'name':'Mohammad Zaheer'}

    if my_id == 3:
        student = {'id': my_id, 'name':'Rahul Kumar'}

    if my_id == 4:
        student = {'id': my_id, 'name':'Kumar Sonu'}
    return render(request, 'form1/clickResponse.html', student)


def AnotherClickResponse(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id': my_id, 'name':'Mohammad Tofik', 'info':'Mohammad Pathan'}

    if my_id == 2 and my_subid == 6:
        student = {'id': my_id, 'name':'Mohammad Zaheer', 'info':'Mohammad Noor'}

    if my_id == 3 and my_subid == 7:
        student = {'id': my_id, 'name':'Rahul Kumar', 'info':'Mohammad Faiz'}

    if my_id == 4 and my_subid == 8:
        student = {'id': my_id, 'name':'Kumar Sonu',  'info':'Sandeep Maheshwari'}
    return render(request, 'form1/clickResponse.html', student)
