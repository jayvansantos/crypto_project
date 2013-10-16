from main.models import Student
from django.http import HttpResponse
from django.template import Context, Template

from gnupg import GPG

gpg = GPG()
key_id = '5F3F7F75D210724D'


def students_view(request):
    students = Student.objects.all()
    t = Template("<ul>{% for s in students %}<li>{{ s }}</li>{% endfor %}</ul>")
    c = Context({'students': students})
    
    return HttpResponse(t.render(c))
    

def students_view_crypto(request):
    t = Template("<ul>{% for student in students %}<li>{{ student }}</li>{% endfor %}</ul>")

    c = Context({"students": Student.objects.all()})

    data = t.render(c)

    return HttpResponse(str(gpg.encrypt(data, key_id, always_trust=True)))
