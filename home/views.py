from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def service(request):
    return render(request,"service.html")



def contact(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            full_name,
            message,
            email,
            ['juniormbuyi4000@gmail.com']
        )

        return render(request,"index.html", context={"full": full_name})
    else:
        return render(request,"contact.html")



def maison(request):
    return render(request,"maison.html")