from django.conf.urls import url
import re
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^reset$', views.reset)

  

] 