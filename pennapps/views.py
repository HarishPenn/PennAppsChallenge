from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import ApplicationForm
from .models import Application
# Create your views here.
@login_required(login_url='/login')
def index(request):
    status = ''
    application = Application.objects.filter(applicant=request.user)
    if not application:
        status = 'No application submitted'
    else:
        app = application[0]
        if app.status == 'PROC':
            status = "Processing"
        elif app.status == 'ACPT':
            status = "Accepted"
        elif app.status == 'RJCT':
            status = "Rejected"
        else:
            status = "Waitlisted"
    return render(request, 'pennapps/index.html',{'application_status': status})
@login_required(login_url='/login')
def application(request):
    try:
        application = Application.objects.get(applicant=request.user)
        editing = True
    except Application.DoesNotExist:
        application = None  # Set to None instead of False
        editing = False
    if request.method == 'POST':
        if editing:
            form = ApplicationForm(request.POST, instance=application)
        else:
            form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)  # Get instance from form
            application.applicant = request.user  # Assign the current user
            application.save()  # Save the instance
            return redirect('index')
    else:
        if editing:
            form = ApplicationForm(instance=application)
        else:
            form = ApplicationForm()
    return render(request, 'pennapps/application.html', {'is_penn_student': request.user.is_penn_student, 'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            error_message = "Invalid username or password"
            return render(request, 'pennapps/login.html', {'error_message': error_message})
    else:
        return render(request, 'pennapps/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username, password)
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'pennapps/signup.html', {'form': form})
