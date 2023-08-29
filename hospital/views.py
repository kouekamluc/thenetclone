from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import  Slider , Service , Mentor , Faq , Gallery

from django.views.generic import ListView , DetailView , TemplateView


# Create your views here.



class HomePageView(ListView):
    template_name = 'hospital/home.html'
    queryset = Service.objects.all()
    context_object_name = 'services'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all() 
        context["experts"] = Mentor.objects.all() 
        return context
    

class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = 'hospital/services.html'
    
    
class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = 'hospital/service_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
    
class MentorListView(ListView):
    template_name = 'hospital/team.html'
    queryset = Mentor.objects.all()
    paginate_by = 8
    
class MentorDetailView(DetailView):
    template_name = 'hospital/team-details.html'
    queryset = Mentor.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mentors"] =Mentor.objects.all() 
        return context
    
class FaqListView(ListView):
    template_name = 'hospital/faqs.html'
    queryset = Faq.objects.all()
    
class GalleryListView(ListView):
    template_name = 'hospital/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9
    
class ContactView(TemplateView):
    template_name = 'hospital/contact.html'
    
    def post(self , request  , *args , **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')                
        
        if subject == '':
            subject = 'MentorShip Contact'
            
        if name and message and email and phone:
            send_mail(
                subject + "-"+phone , 
                message , 
                email ,
                ['luckevinkouekam@gmail.com'],
                fail_silently=False,
            )
            messages.success(request , "Email has been sent successfully...")
        return redirect('contact')