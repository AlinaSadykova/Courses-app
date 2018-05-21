from django.shortcuts import render, HttpResponse, redirect
from .models import Course
import datetime

def index(request):
    print(Course.objects.all().values())
    context = {
        'everything': Course.objects.all()
    }
    
    print(context)

    return render(request, 'courses_app/index.html', context)

# def create(request):
    
def create(request):
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        print(Course.objects.all().values())

        return redirect("/")
    else:
        return redirect("/")

def remove(request):
    print(request.POST['course_id'])
    me = Course.objects.get(id = request.POST['course_id'])
    dic = {
        'name': me.name,
        'desc': me.desc   
    }
    print(dic['name'])
    if request.method == "POST":
        me = Course.objects.get(id = request.POST['course_id'])
        me.delete()
        return render(request, 'courses_app/index2.html', dic)
  

    return render(request, 'courses_app/index2.html', dic)

    # def create(request):
    # if request.method == "POST":
    #     Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    #     print(Course.objects.all().values())

    #     return redirect("/")
    # else:
    #     return redirect("/")







# def create(request):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Course.objects.basic_validator(request.POST)
#         # check if the errors object has anything in it
#     if len(errors):
#             # if the errors object contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#             # redirect the user back to the form to fix the errors
#         return redirect("/")
#     else:
        
#     return redirect('/')





# Create your views here.
