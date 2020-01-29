from django.http import HttpResponse

from polls.models import Question


def funkcja_widoku(request):
    html = """
    <!doctype html>
    <html>
    <head></head>
    <body>
    Hello ALX!!!
    </body>
    </html>
    """
    return HttpResponse('Hello ALX!')

def hello_name(request, name):
    html = f"""
    <!doctype html>
    <html>
    <head></head>
    <body>
    Hello {name}!!!
    </body>
    </html>
    """
    return HttpResponse(html)

def index(request):
    return HttpResponse("Hello World! That's polls index")

def questions_list(request):
    qs = Question.objects.all()
    text = ""
    for q in qs:
        text += str(q)
        text += "<br>"
    return HttpResponse(text)

# zad domowe
# widok szczegolow
# questions/1
# questions/2
#
# djangoproject.com
# https://docs.djangoproject.com/en/3.0/intro/tutorial01/ - 02-03
# na środę na egzamin
# https://pythonprinciples.com/challenges/