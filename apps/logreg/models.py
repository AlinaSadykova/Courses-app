from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
strongRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
        y = User.objects.filter(email = postData['email'])
        response =  {
            'status': False,
            'errors': [],
            'success':[]
        }
        
        if len(postData['first_name']) < 2:
            response['errors'].append("User first_name should be at least 2 characters") 
        if len(postData['last_name']) < 2:
            response['errors'].append("User last_name should be at least 2 characters") 
        if len(postData['password'])<6:
            response['errors'].append("Password is too short") 
        if  not strongRegex.match(postData['password']):
            response['errors'].append("Password must contain at least 1 uppercase character and number")
        if (postData['password'])!=(postData['confps']):
            response['errors'].append("Passwords don not match") 
        if  not EMAIL_REGEX.match(postData['email']):
            response['errors'].append("Invalid email") 
        if len(y)>0:
            response['errors'].append("email already exists") 
        if len(response['errors'])==0:
            response['status']=True
            response['success'].append("You are successfully registered!")
        return response

    def validation2(self, postData):
        response =  {
            'status': False,
            'errors': []
        }
        y = User.objects.filter(email = postData['email'])
        if len(y)>0:
            if bcrypt.checkpw(postData['password'].encode(), y[0].password.encode()):
                response['errors'].append("you are successfully logged in")
                response['status'] = True
        else:
            response['errors'].append("you can not be logged in") 
        return response



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


