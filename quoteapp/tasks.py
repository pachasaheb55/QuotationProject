""" Tasks file for quoteapp """
from __future__ import absolute_import, unicode_literals
from io import BytesIO
import os

from celery import shared_task
from xhtml2pdf import pisa
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from quoteapp.models import Quotation

# celery shared task lets you create tasks that can be used by any app(s)
@shared_task
def pdf_generator_task(quotation):
    """ Convert HTML to PDF function """
    # get the quote details
    quote = get_quote_object(quotation)
    template = get_template('summary.html')
    # setting the quote context params
    context = {'quote': quote, 'coverages': list(quote.coverage.all())}
    # Render the template
    html = template.render(context)
    # open a PDF file
    with open('static/pdf/report.pdf', 'wb') as file:
        # write the content into PDF file
        pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), file)
    send_email(quote)


def send_email(quote):
    """ Send Email method """
    subject, from_email = 'Quote Summary for Vehicle', os.environ.get("EMAIL_HOST_USER", None)
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>Quote Summary</strong> from ' \
                   'Quotation Application For Motor Insurance @ Powered By TIGER LABS</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email,
                                 [quote.customer.email])
    msg.attach_alternative(html_content, "text/html")
    with open('static/pdf/report.pdf', 'rb') as file:
        msg.attach('attachment.pdf', file.read(), 'application/pdf')
        msg.send()


def get_quote_object(quote_id):
    """ required to get the quotation details """
    return Quotation.objects.get(id=quote_id)
