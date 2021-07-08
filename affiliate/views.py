from django.shortcuts import get_object_or_404, render
from .models import Course, Category
from .filters import CourseFilter

def home(request):
    courses = Course.objects.all()

    #orders = courses.order_set.all()
    #order_count = orders.count()

    filter = CourseFilter(request.GET, queryset=courses)
    courses = filter.qs

    context = {"courses": courses, 'filter': filter}
    return render(request, 'home.html', context)

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

def about(request):
    total_courses = Course.objects.all().count()  
    total_categories = Category.objects.all().count()
    context = {'courses':total_courses, 'categories':total_categories}
    return render(request, 'about.html', context)

def terms(request):
    return render(request, 'terms.html', {})

def glossary(request):
    return render(request, 'glossary.html', {})

def contact(request):
    return render(request, 'contact.html', {})