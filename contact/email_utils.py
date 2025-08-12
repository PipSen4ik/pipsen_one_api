from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import os
from email.mime.image import MIMEImage

def send_contact_email_notification(context, reply_to_email):
    subject = f"📬 Сообщение с сайта DevPortfolio MG — {context['name']}"
    html_content = render_to_string('contact/email_template.html', context)
    text_content = (
        f"Новое сообщение с сайта DevPortfolio MG\n"
        f"От: {context['name']} <{reply_to_email}>\n"
        f"Сообщение:\n{context['message']}\n"
        f"Сайт: {context['website_url']}"
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.DEFAULT_FROM_EMAIL],
        reply_to=[reply_to_email],
    )
    msg.attach_alternative(html_content, "text/html")

    logo_path = os.path.join(settings.BASE_DIR, 'contact', 'static', 'contact', 'img', 'logo.png')
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data)
        image.add_header('Content-ID', '<logo>')
        msg.attach(image)

    msg.send(fail_silently=False)