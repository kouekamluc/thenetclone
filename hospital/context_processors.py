from .models import Mentor , Service 


def footer_content(request):
    services = Service.objects.all()
    mentors = Mentor.objects.all()
    
    context = {
        'services':services,
        'mentors':mentors
    }
    return context