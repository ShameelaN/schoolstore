from django.contrib import messages
from django.shortcuts import render

from student_form.models import Students


# Create your views here.

def student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        number=request.POST.get('number')
        mailid=request.POST.get('mailid')
        address=request.POST.get('address')
        department=request.POST.get('department')
        courses=request.POST.get('courses')
        purpose=request.POST.get('purpose')
        materials=request.POST.get('materials')
        st=Students(name=name,date=date,age=age,gender=gender,number=number,mailid=mailid,address=address,department=department,courses=courses,purpose=purpose,materials=materials)
        st.save()
        messages.success(request, 'Information Submitted Successfully.')





    return render(request,'student.html')