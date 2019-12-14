import os
import uuid
import base64
import random

from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView, View
from django.template.context_processors import csrf
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Desire
from utils import common


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
            if desire.desire and os.path.exists(desire.desire.path):
                os.remove(desire.desire.path)
            desire.desire = ContentFile(base64.b64decode(svg_data))
            desire.desire.name = str(uuid.uuid4()) + '.png'
            desire.save(update_fields=('desire',))
            # バックグラウンドを設定
            data = common.set_background_image(desire.desire.path)
            if data:
                if desire.desire_bg and os.path.exists(desire.desire_bg.path):
                    os.remove(desire.desire_bg.path)
                desire.desire_bg = data
                desire.desire_bg.name = str(uuid.uuid4()) + '.png'
                desire.save(update_fields=('desire_bg',))
            return JsonResponse({'message': '送信しました、ありがとうございました。'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '送信失敗しました。該当するメールアドレスが登録されていません。'}, status=400)
        except Exception as ex:
            return JsonResponse({'message': str(ex)}, status=400)


class WallView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': Desire.objects.filter(desire_bg__isnull=False),
        }
        return render(request, '{}.html'.format(kwargs.get('type')), context)


class DesireImageView(View):

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email')
        try:
            desire = Desire.objects.get(email=email)
            image_file = desire.desire.path
            return HttpResponse(File(open(image_file, 'rb')), content_type="image/png")
        except ObjectDoesNotExist:
            return JsonResponse({}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class RandomImageView(View):

    def get(self, request, *args, **kwargs):
        is_random = False
        object_list = list(Desire.objects.filter(
            showed=False, desire__isnull=False, priority__isnull=False
        ).order_by('priority'))
        if len(object_list) == 0:
            object_list = list(Desire.objects.filter(showed=False, desire__isnull=False))
            is_random = True
        try:
            if is_random:
                desire = random.choice(object_list)
            else:
                desire = object_list[0]
            desire.showed = True
            desire.save(update_fields=('showed',))
            return JsonResponse({'url': desire.desire.url, 'name': desire.full_name})
        except IndexError:
            return JsonResponse({'url': ''})

    def post(self, *args, **kwargs):
        Desire.objects.all().update(showed=False)
        return JsonResponse({})
