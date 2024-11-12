from django.shortcuts import render
from .utils import *


QUESTIONS = [
   {
    'id': i,
    'title': f'How do you ask questions? This is a question #{i}',
    'text': f'Some text about question #{i}, explaining the question more thoroughly. More text, More text, More text, More text, More text,'
   } for i in range(1, 70)
]
ANSWERS = [
   {
    'id': i,
    'text': f'First of all, the number of my answer is {i}. So, as I was saying, my answer is very long and nice, my answer is very long and nice, my answer is very long and nice '
   } for i in range(1, 10)
]


def askme(request):
    page = paginate(QUESTIONS, request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,
                      'title': 'New Questions'
                  })

def hot(request):
    page = paginate(list(reversed(QUESTIONS)), request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,                      
                      'title': 'Hot Questions'
                  })

def ask(request):
    return render(request, 'ask.html')

def question(request, question_id):
    page = paginate(ANSWERS, request)
    return render(request, 'question.html', 
                  context={
                      'question': QUESTIONS[question_id-1],
                      'page_obj': page,                      
                      'answers': page.object_list
                  })

def tag(request, tag_name):
    page = paginate(QUESTIONS, request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,                      
                      'title': 'Tag: ' + tag_name,
                  })

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
