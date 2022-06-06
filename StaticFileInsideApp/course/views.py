from django.shortcuts import render


def course_one(request):
	course_name = 'Python programming Language'
	course_fees = 4000
	course_duration = '4 month'
	course_details_one = {'cn':course_name, 'cd':course_duration, 'cf':course_fees}
	return render(request, 'course/courseone.html', context = course_details_one)


def course_two(request):
	course_name = 'Python programming Language'
	course_fees = 4000
	course_duration = '4 month'
	course_details_two = {'cn':course_name, 'cd':course_duration, 'cf':course_fees}
	return render(request, 'course/coursetwo.html', context = course_details_two)


def information(request):
	return render(request, 'course/info.html')
