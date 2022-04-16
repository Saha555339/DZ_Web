from django.shortcuts import render

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",
        "number": i
    } for i in range(5)
]

TAGS = [
    {
        "name": f"Tag {i}",
        "number": i
    } for i in range(3)
]

TOP_MEMBERS = [
    {
        "name": f"Member {1}"
    } for i in range(2)
]

ANSWERS = [
    {
        "text": f"Answer {i}",
        "author": f"Author {i}"
    } for i in range(3)
]


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS, "tags": TAGS, "top_members": TOP_MEMBERS})


def question(request, i: int):
    return render(request, "question_page.html",
                  {"question": QUESTIONS[i], "tags": TAGS, "top_members": TOP_MEMBERS, "answers": ANSWERS})


def ask(request):
    return render(request, "ask_question.html", {"tags": TAGS, "top_members": TOP_MEMBERS})


def log_in(request):
    return render(request, "log_in.html", {"tags": TAGS, "top_members": TOP_MEMBERS})


def registration(request):
    return render(request, "registration.html", {"tags": TAGS, "top_members": TOP_MEMBERS})


def settings(request):
    return render(request, "settings.html", {"tags": TAGS, "top_members": TOP_MEMBERS})


def hot_questions(request):
    return render(request, "hot_questions.html", {"questions": QUESTIONS, "tags": TAGS, "top_members": TOP_MEMBERS})


def tags_question(request, number: int):
    return render(request, "tag_questions.html",
                  {"questions": QUESTIONS, "tags": TAGS, "tag": TAGS[number], "top_members": TOP_MEMBERS})
