import django_filters

from .models import *


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        # por enquanto deixa só categoria, depois inclui mais
        fields = ['category']
        # exclude = ['name', 'image', 'description', 'summary', 'link']
