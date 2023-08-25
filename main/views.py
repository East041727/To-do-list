from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm,SignupForm
from django.db.models import Q
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required,permission_required


from .decorators import allowed_users_in_to_do_list,unauthorized_user





def Homepage(request):
    q = request.GET.get('search')
    if q:
        tasks = Task.objects.filter(Q(name__icontains=q) &  Q(status__icontains=q))
    else:
         tasks = Task.objects.all().order_by('-created')

   
    return render(request, 'main/index.html',{'tasks':tasks})


@login_required(login_url='login')
def create_something(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
            
        return render(request, 'main/forms.html',{'form':form})
    return render(request, 'main/forms.html',{'form':form})
        
   

@login_required(login_url='login')
def update_something(request,slug):
    task = get_object_or_404(Task, slug=slug)
    form = TaskForm(instance=task)
    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
          form.save()
        return redirect('home')
    return render(request, 'main/forms.html',{'form':form})


@login_required(login_url='login')
def delete_something(request,slug):
    task = Task.objects.filter(slug=slug).first()
    task.delete()
    return redirect('home')



@unauthorized_user
def SignupView(request):
  
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                return redirect('home')
        return render(request, 'main/signup.html',{'form': form})



@unauthorized_user
def LoginView(request):
        if request.method == 'POST':
            username = request.POST.get('email').lower()
            
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'main/login.html')
            




def LogoutView(request):
    logout(request)
    return redirect('register')