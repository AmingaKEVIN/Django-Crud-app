from django.shortcuts import render,redirect
from.models import Student
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
     data= Student.objects.all()
     context={"data":data}
     return render(request,"index.html",context)
 
def insert(request):
   
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")
   
def about(request):
    return render(request,"about.html")
@login_required  
def update(request, id):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit= Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")
   
    d= Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)
@login_required
def delete(request, id):
     d= Student.objects.get(id=id)
     d.delete()
     return redirect("/")
     
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to a home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to a home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')