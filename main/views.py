from main.models import Student
from django.http import HttpResponse
from django.template import Context, Template


def students_view(request):
    students = Student.objects.all()
    t = Template("<ul>{% for s in students %}<li>{{ s }}</li>{% endfor %}</ul>")
    c = Context({'students': students})
    
    return HttpResponse(t.render(c))
    
