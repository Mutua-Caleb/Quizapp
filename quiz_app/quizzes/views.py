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
    category = get_object_or_404(Category, id=category_id)
    questions = Question.objects.filter(category=category) 

    if request.method == 'POST': 
        selected_choices = {}  # Use a dictionary to map question IDs to selected choices
        correct_answers_count = 0 
        total_questions = questions.count()

        for question in questions:
            # Get the submitted choices for the current question
            submitted_choices = request.POST.getlist(f'choice{question.id}')
            selected_choices[question.id] = submitted_choices
            
            # Ensure correct_answers is a list
            correct_answers = question.correct_answers
            if isinstance(correct_answers, int):
                correct_answers = [correct_answers]  # Convert to list if it's a single integer

            # Check if the submitted choices match the correct answers
            if set(submitted_choices) == set(map(str, correct_answers)): 
                correct_answers_count += 1

        # Calculate the score as a percentage
        score = (correct_answers_count / total_questions) * 100

        # Prepare zipped_data for the template
        zipped_data = [
            {
                'question': question,
                'selected': selected_choices[question.id]
            } for question in questions
        ]

        # Render the results page
        return render(request, 'quizzes/results.html', {
            'category': category, 
            'questions': questions,
            'selected_choices': selected_choices,
            'score': score,
            'zipped_data': zipped_data,
        })

    # Render the category page with questions
    return render(request, 'quizzes/category.html', {
        'category': category, 
        'questions': questions,
    })


def admin_panel(request):
    return render(request, 'quizzes/admin_panel.html')
