from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, "logreg/index.html")

def process(request):
    if request.method == "POST":
        result = User.objects.basic_validator(request.POST)
        if len(result['errors'])>0:
            for g in result['errors']:
                messages.error(request, g) 
            return redirect("/logreg")       
        else:
            for h in result['success']:
                messages.error(request, h)
            ps = request.POST['password']
            hash1 = bcrypt.hashpw(ps.encode(), bcrypt.gensalt())
            y = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1)
            request.session['user_id'] = y.id
            return redirect("/logreg/success")
  
        

def success(request):
    if 'user_id' in request.session:
            muk = User.objects.get(id = request.session['user_id'])
            p = {
                'name': muk.first_name
            }
            return render(request, "logreg/index2.html", p)
    return redirect("/logreg")   


def login(request):
    if request.method == "POST":
        result = User.objects.validation2(request.POST)
        if result['status']:
            m = User.objects.filter(email = request.POST['email'])
            request.session["user_id"] = m[0].id 
            for g in result['errors']:
                messages.error(request, g)          
            return redirect("/logreg/success")
        else:
            for g in result['errors']:
                messages.error(request, g)
                return redirect("/logreg") 
        
          
    

def reset(request):
    del request.session['user_id']
    return redirect("/logreg")
    
