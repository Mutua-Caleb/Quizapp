from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Category, Question

def home(request):
    categories = Category.objects.all()
    return render(request, 'quizzes/home.html', {'categories': categories})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        user = authenticate(request, username=username)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'quizzes/login.html')

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    questions = Question.objects.filter(category=category) 

    if request.method == 'POST': 
        #process the submitted answers 
        selected_choices = [] 
        correct_answers_count = 0 
        total_question = questions.count() 

        for question in questions: 
            submitted_choices = request.POST.getlist(f'choice{question.id}')
            selected_choices.append(submitted_choices)
            #Check if the student's answers match the correct answers 
            if set(submitted_choices) == set(question.correct_answers): 
                correct_answers_count +=1 
            

        # calculate score or feedback here 
        score = correct_answers_count/total_question * 100

        #You could redirect to a results page
        return render(request, 'quizzes/results.html', {
            'category': category, 
            'questions': questions,
            'selected_choices': selected_choices,
            'score': score,
        })
    # return render(request, 'quizzes/category.html', {'category': category, 'questions': questions})

def admin_panel(request):
    return render(request, 'quizzes/admin_panel.html')
