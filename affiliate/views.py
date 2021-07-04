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
    # Adicionar mais dados
    return render(request, 'course-detail.html', data)
