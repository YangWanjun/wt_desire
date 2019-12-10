import uuid
import base64

from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.template.context_processors import csrf

from .models import Desire


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email') + '@wisdom-technology.co.jp'
        str_svg_data = request.POST.get('user_signature')
        ext, svg_data = str_svg_data.split(';base64,')
        context = {}
        context.update(csrf(request))
        try:
            desire = Desire.objects.get(email=email)
            desire.desire = ContentFile(base64.b64decode(svg_data))
            desire.desire.name = str(uuid.uuid4()) + '.svg'
            desire.save()
            messages.add_message(request, messages.INFO, '送信しました、ありがとうございました。')
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR, '送信失敗しました。該当するメールアドレスが登録されていません。')
        return self.render_to_response(context)
