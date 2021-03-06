import os

from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Course, Category
from .filters import CourseFilter


EMAIL = os.environ.get('EMAIL')

def home(request):
    courses = Course.objects.all()

    filter = CourseFilter(request.GET, queryset=courses)
    courses = filter.qs
    
    context = {"courses": courses, 'filter': filter}
    return render(request, 'home.min.html', context)

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
    return render(request, 'course-detail.min.html', data)

def search_courses(request):
    if(request.method == 'POST'):
        searched = request.POST['searched']
        courses = Course.objects.filter(name__icontains=searched)
        return render(request, 'search-courses.min.html', {"searched":searched, "courses": courses})
    else:
        return render(request, 'search-courses.min.html', {})

def about(request):
    total_courses = Course.objects.all().count()  
    total_categories = Category.objects.all().count()
    context = {'courses':total_courses, 'categories':total_categories}
    return render(request, 'about.min.html', context)

def terms(request):
    return render(request, 'terms.min.html', {})

def glossary(request):
    return render(request, 'glossary.min.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(
            message_name,
            message,
            message_email,
            [EMAIL],
        )
        return render(request, 'contact.min.html', {'message_name':message_name})
    else:
        return render(request, 'contact.min.html', {})
        