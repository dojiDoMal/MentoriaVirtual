from django.shortcuts import get_object_or_404, render
from .models import Course

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {"courses": courses})

def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    data = dict()
    data["course"] = course
    data["name"] = course.name
    data["image"] = course.image
    data["description"] = course.description
    data["summary"] = course.summary
    data["rating"] = course.rating
    data["price"] = course.price
    data["category"] = course.category
    data["author"] = course.author
    data["link"] = course.link
    return render(request, 'course-detail.html', data)

def search_courses(request):
    if(request.method == 'POST'):
        searched = request.POST['searched']
        courses = Course.objects.filter(name__icontains=searched)
        return render(request, 'search-courses.html', {"searched":searched, "courses": courses})
    else:
        return render(request, 'search-courses.html', {})
