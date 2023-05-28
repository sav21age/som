from django.conf import settings
from django.utils.html import strip_tags
from django.views.generic import FormView, TemplateView
from django.core.mail import EmailMessage

from common.loggers import logger
from feedback.forms import FeedbackForm


class FeedbackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback/form.html'

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject').strip()
        # name = form.cleaned_data.get('name')
        sender = form.cleaned_data.get('sender')
        message = strip_tags(form.cleaned_data.get('message'))

        try:
            self.success_url = 'success/'

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # from address
                settings.LIST_OF_EMAIL_RECIPIENTS, # recipients
                reply_to=[sender,]  # reply to address set by your user
            )
            email.send()

            # send_mail(subject,
            #     'От: %s (%s)\n%s' % (name, sender, message),
            #     settings.EMAIL_HOST_USER,
            #     settings.LIST_OF_EMAIL_RECIPIENTS)

        except Exception as e:
            logger.error(e)
            self.success_url = 'failure/'

        return super(FeedbackFormView, self).form_valid(form)


class ThanksTemplateView(TemplateView):
    template_name = 'feedback/success.html'


class FailureTemplateView(TemplateView):
    template_name = 'feedback/failure.html'