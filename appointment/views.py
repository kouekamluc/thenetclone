from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.views.generic import View
from hospital.models import Mentor 
from .models import Appointment


# Create your views here.

class AppointmentView(View):
    def get(self , request , *args , **kwargs):
        context = {
            'mentors':Mentor.objects.all()
        }
        return render(request , "appointment/home.html" , context)
    def post(self, request , *args , **kwargs):
        name = reqeust.POST.get('name')
        phone = reqeust.POST.get('phone')
        email = reqeust.POST.get('email')
        mentor_id = reqeust.POST.get('mentor')
        date = reqeust.POST.get('date')
        time = reqeust.POST.get('time')
        note = reqeust.POST.get('note')
        
        if mentor_id:
            mentor = get_object_or_404(Mentor , id=mentor_id)
        if (name and phone and email and mentor and date and time):
            Appointment.objects.create(
                name=name , phone=phone , email=email , mentor=mentor , date=date , time=time ,note=note
            )
            messages.success(request , 'Appointment done successfully')
            return redirect('appointment')