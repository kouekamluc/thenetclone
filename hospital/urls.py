from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static  
from django.conf import  settings

urlpatterns = [
    path('' , views.HomePageView.as_view() , name='home'),
    path('services/' , views.ServiceListView.as_view() , name='services'),
    path('services/<int:pk>/' , views.ServiceDetailView.as_view() , name='service_details'),
    path('mentors/' , views.MentorListView.as_view() , name='mentors'),
    path('mentor/<int:pk>/' , views.MentorDetailView.as_view(), name='mentor_details'),
    path('faqs/', views.FaqListView.as_view() , name='faqs'),
    path('gallery/' , views.GalleryListView.as_view() , name='gallery'),
    path('contact/' , views.ContactView.as_view(), name='contact'),
]
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)