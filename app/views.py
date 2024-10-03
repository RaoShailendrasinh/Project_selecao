from django.shortcuts import render,HttpResponse
from app.models import *

# Create your views here.
def index(request):
    ServiceContent = Service.objects.all()
    TestimonialContent = Testimonial.objects.all()
    context ={
   
    'ServiceContent':ServiceContent,
    'TestimonialContent':TestimonialContent,
  }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        # Save data to the database
        contact_message = Contact(name=name, email=email, message=message,subject=subject)
        contact_message.save()

        return HttpResponse('Message submitted successfully!') 
    return render(request, 'index.html',context)
    