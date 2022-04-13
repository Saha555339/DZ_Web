from django.shortcuts import render

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",
        "number": i
    } for i in range(5)
]

def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})

def question(request, i:int):
    return render(request, "question_page.html", {"question": QUESTIONS[i]})

def ask(request):
    return render(request, "ask_question.html")

def log_in(request):
    return render(request, "log_in.html")

def registration(request):
    return render(request, "registration.html")

def settings(request):
    return render(request, "settings.html")
