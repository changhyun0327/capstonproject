from django.urls import path

#from mainapp.views import mainpage
from capstonapp.views import mainpage

app_name = 'capstonapp' #만든것과 이름 똑같이

urlpatterns =[
    path('capstonpage/',mainpage,name='mainpage')
]