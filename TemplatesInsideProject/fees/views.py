from django.shortcuts import render


def fees_one(request):
	course_name = 'Python programming Language'
	course_fees = 4000
	course_duration = '4 month'
	fees_details_one = {'cn':course_name, 'cd':course_duration, 'cf':course_fees}
	return render(request, 'fees/feesone.html', context = fees_details_one)

def fees_two(request):
	course_name = 'Python programming Language'
	course_fees = 4000
	course_duration = '4 month'
	fees_details_two = {'cn':course_name, 'cd':course_duration, 'cf':course_fees}
	return render(request, 'fees/feesone.html', context = fees_details_two)

def information(request):
	return render(request, 'fees/info.html')