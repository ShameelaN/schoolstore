from django.urls import path
from . import views
app_name='student_form'
urlpatterns = [

    path('student',views.student,name="student"),
]