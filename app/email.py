from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_ticket_email(receiver, data):
    subject = 'YOUR EVENT TICKET'
    sender = 'coremoringa@gmail.com'

    html_content = render_to_string('email/ticketemail.html', {"data": data})
    text_content = render_to_string('email/ticketemail.txt', {"data": data})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
