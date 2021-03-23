
from django.shortcuts import render
from email_backed.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    if request.method == 'POST':
        form = request.POST
        subject = 'Details'
        message = f'Parent Name : {form["parent"]}\nChild Name : {form["child"]}\nEmail Name : {form["email"]}\nPhone Number : {form["phone"]}\nGrade : {form["grade"]}'
        recepient = request.POST.get('email')
       
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'form.html')
    return render(request, 'form.html')

