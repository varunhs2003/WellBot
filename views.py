from django.shortcuts import render
from django.http import JsonResponse
from .models import Symptom  # Import your models as needed

def chatbot(request):
    if request.method == 'POST':
        response = request.POST.get('response')
        if response:
            if response in ['good', 'ok', 'lonely', 'school', 'relationship', 'family', 'personal']:
                return handle_response(response)
            else:
                return JsonResponse({'error': 'Invalid response.'})

    symptoms = Symptom.objects.all()  # Adjust as per your model structure
    return render(request, 'chat_app/chatbot.html', {'symptoms': symptoms})

def handle_response(response):
    # Define the mapping of responses to redirect URLs
    response_map = {
        'good': 'good_results',
        'ok': 'ok_results',
        'lonely': 'lonely_results',
        'school': 'school_results',
        'relationship': 'relationship_results',
        'family': 'family_results',
        'personal': 'personal_results',
        'mental' : 'mental_test',
    }

    if response in response_map:
        redirect_url = response_map[response]
        return JsonResponse({'redirect_url': redirect_url})
    else:
        return JsonResponse({'error': 'Invalid response.'})

def good_results(request):
    issues = ['Issue 1', 'Issue 2', 'Issue 3']  # Replace with your data logic
    return render(request, 'chat_app/good.html', {'issues': issues})

def ok_results(request):
    return render(request, 'chat_app/ok.html')

def lonely_results(request):
    return render(request, 'chat_app/lonely.html')

def school_results(request):
    return render(request, 'chat_app/school_results.html')

def relationship_results(request):
    return render(request, 'chat_app/relationship.html')

def family_results(request):
    return render(request, 'chat_app/family.html')

def personal_results(request):
    return render(request, 'chat_app/personal.html')


from django.shortcuts import render, redirect

def mental_test(request):
    return render(request, 'chat_app/mental_q1.html')

def mental_test_submit(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')


        # Example logic to determine mental health issues
        mental_issues = []

        if q1 == 'often':
            mental_issues.append('Stress')
            if q2 == 'yes':
                mental_issues.append('Anxiety')
            elif q3 == 'yes':
                mental_issues.append('Panic Disorder')
            if q4 == 'yes':
                mental_issues.append('Insomnia')
            if q5 == 'yes':
                mental_issues.append(' Psychosis, Schizophrenia')
            if q6 == 'yes':
                mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
            if q7 == 'yes':
                mental_issues.append(' Suicidal ideation, Potentially Depression')

        elif q1 == 'always':
            mental_issues.append('Stress')
            if q2 == 'yes':
                mental_issues.append('Anxiety')
            elif q3 == 'yes':
                mental_issues.append('Panic Disorder')
            if q4 == 'yes':
                mental_issues.append('Insomnia')
            elif q5 == 'yes':
                mental_issues.append(' Psychosis, Schizophrenia')
            elif q6 == 'yes':
                mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
            elif q7 == 'yes':
                mental_issues.append(' Suicidal ideation, Potentially Depression')

        elif q2 == 'yes':
                mental_issues.append('Anxiety')
                if q3 == 'yes':
                    mental_issues.append('Panic Disorder')
                if q4 == 'yes':
                    mental_issues.append('Insomnia')
                if q5 == 'yes':
                    mental_issues.append(' Psychosis, Schizophrenia')
                if q6 == 'yes':
                    mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
                elif q7 == 'yes':
                    mental_issues.append(' Suicidal ideation, Potentially Depression')
        elif q3 == 'yes':
                mental_issues.append('Panic Disorder')
                if q4 == 'yes':
                    mental_issues.append('Insomnia')
                elif q5 == 'yes':
                    mental_issues.append(' Psychosis, Schizophrenia')
                if q6 == 'yes':
                    mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
                elif q7 == 'yes':
                    mental_issues.append(' Suicidal ideation, Potentially Depression')
        elif q4 == 'yes':
                mental_issues.append('Insomnia')
                if q5 == 'yes':
                    mental_issues.append(' Psychosis, Schizophrenia')
                if q6 == 'yes':
                    mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
                elif q7 == 'yes':
                    mental_issues.append(' Suicidal ideation, Potentially Depression')
        elif q5 == 'yes':
                mental_issues.append(' Psychosis, Schizophrenia')
                if q6 == 'yes':
                    mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
                elif q7 == 'yes':
                    mental_issues.append(' Suicidal ideation, Potentially Depression')
        elif q6 == 'yes':
                mental_issues.append(' PTSD (Post-Traumatic Stress Disorder)')
                if q7 == 'yes':
                    mental_issues.append(' Suicidal ideation, Potentially Depression')
        elif q7 == 'yes':
                mental_issues.append(' Suicidal ideation, Potentially Depression')



        # Render results.html with identified issues
        return render(request, 'chat_app/results.html', {'mental_issues': mental_issues})

    # Handle GET request or other cases by redirecting back to mental_test
    return redirect('mental_test')  

def results(request):
    # Dummy data for testing
    mental_issues = ['Stress', 'Trouble sleeping']

    return render(request, 'chat_app/results.html', {'mental_issues': mental_issues})

