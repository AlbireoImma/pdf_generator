from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

# Create your views here.
def index(request):
    # email = EmailMessage(
    # 'Hello There!',
    # 'An automated email by Django',
    # 'no-reply@masfondos.cl',
    # ['faam1612@gmail.com'],
    # )
    # email.attach_file('pdfs/test.pdf')
    # email.send(fail_silently=False)
    template = get_template('send/mail.html')
    html_content = template.render()
    subject, from_email, to = 'hello', 'no-reply@masfondos.cl', 'faam1612@gmail.com'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('pdfs/test.pdf')
    msg.send(fail_silently=False)
    return render(request, 'send/index.html')