from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .utils import *
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from askme.forms import LoginForm, RegisterForm, SettingsForm, AskForm, AnswerForm


def askme(request):
    QUESTIONS = Question.objects.get_new()
    page = paginate(QUESTIONS, request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,
                      'title': 'New Questions'
                  })

def hot(request):
    QUESTIONS = Question.objects.get_hot()
    page = paginate(list(reversed(QUESTIONS)), request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,                      
                      'title': 'Hot Questions'
                  })

@login_required
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(user=request.user)
            return redirect(reverse('askme:question', args=[question.id]))
    else:
        form = AskForm()
    
    return render(request, 'ask.html', {'form': form})

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    ANSWERS = Answer.objects.filter(question__id=question_id)
    page = paginate(ANSWERS, request)
    return render(request, 'question.html', 
                  context={
                      'question': question,
                      'page_obj': page,                      
                      'answers': page.object_list
                  })

@login_required
def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(author=request.user, question=question)
            answers = Answer.objects.filter(question=question)
            page = paginate(answers, request)
            redirect_url = f"{question.get_absolute_url()}?page={page.paginator.num_pages}#answer-{answer.id}"
            return redirect(redirect_url)
    else:
        form = AnswerForm()

    return render(request, 'question.html', {'question': question, 'form': form})

def tag(request, tag_name):
    QUESTIONS = Question.objects.get_new().filter(tags__name=tag_name)
    page = paginate(QUESTIONS, request)
    return render(request, 'index.html', 
                  context={
                      'questions': page.object_list,
                      'page_obj': page,                      
                      'title': 'Tag: ' + tag_name,
                  })

@login_required
def settings(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            
            print("User data saved:", user.username, user.email)

            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                print("User re-authenticated successfully")
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                print("Reauthentication failed")
        else:
            print("Form errors:", form.errors)
    else:
        form = SettingsForm(instance=user)
    return render(request, 'settings.html', {'form': form})

def login(request):
    continue_url = request.GET.get('next', reverse('askme:main_page'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(continue_url)
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'continue_url': continue_url})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('index'))
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    
def logout(request):
    auth.logout(request)
    current_url = request.META.get('HTTP_REFERER', '/')
    return redirect(current_url)


