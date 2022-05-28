from django.http import HttpResponse, JsonResponse
from .models import Site
from .serializers import SiteSerializer
from .models import Page
from .serializers import PageSerializer, PagePostSerializer
from .models import Request
from .serializers import RequestSerializer
from .models import Content
from .serializers import ContentSerializer
from .serializers import PageExpandSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .WebProcessor import WebProcessor

from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, "Main.html")

def req(request):
    return TemplateResponse(request, "Request.html")

def history(request):
    requests = Request.objects.all()
    val = []
    key = []
    j = 0
    for i in requests:
        j += 1
        n = []
        n.append(i.request_id)
        n.append(i.request_page_id.page_url)
        n.append(i.request_page_id.page_site_id.site_name)
        n.append(i.request_datetime)
        val.append(n)
        strj = 'a'+str(j)
        key.append(strj)
    data = dict(zip(key, val))
    return TemplateResponse(request, "History.html", data)