from django.shortcuts import render
from django.contrib import messages
from .models import Register
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.crypto import get_random_string
from .forms import RegisterForm
import datetime


def register(request):
    form = RegisterForm
    context = {"form": form}
    if request.method == "POST":
        form = form(request.POST)
        print(request.POST)
        if form.is_valid():
            print('valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            birthday = request.POST['birthday']
            print(birthday)
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            event = form.cleaned_data['event']
            event_id = get_random_string(length=10)
            try:
                birthday = datetime.datetime.strptime(str(birthday),"%d/%m/%Y")
                print(birthday)
            except ValueError:
                return render(request, "index.html", {"form":form, "error_message":"Wrong date format, use d/d/Y"})
            else:
                ins = Register(first_name=first_name, last_name=last_name, birthday=birthday, gender=gender, email=email, phone=phone, event=event, event_id =event_id)
                print(first_name,last_name,birthday,gender,email,phone,event,event_id)
                ins.save()
                messages.success(request, 'Registration successful')
                template = render_to_string('email_template.html', {'first_name':first_name, 'event':event, 'event_id':event_id})
                email = EmailMessage(
                    'Successful Registration',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                email.fail_silently=False
                email.send()
                return render(request, "index.html", {"form": form})
        else:
            print("form invalid")
            return render(request, "index.html", {"form":form})
    else:
        return render(request, "index.html",context)


