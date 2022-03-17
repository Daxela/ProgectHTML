from django.shortcuts import render

# Create your views here.
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
import json


class Site_l(APIView):
    def get(self, request):
        site = Site.objects.all()
        site_serializer = SiteSerializer(instance=site, many=True)
        return Response(site_serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        site_serializer = SiteSerializer(data=data)
        if site_serializer.is_valid():
            site_serializer.save()
        return Response(site_serializer.data)


class Site_d(APIView):
    def get(self, request, site_id):
        try:
            site = Site.objects.get(site_id=site_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        site_serializer = SiteSerializer(instance=site)
        return Response(site_serializer.data)

    def put(self, request, site_id):
        try:
            site = Site.objects.get(site_id=site_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        site_serializer = SiteSerializer(instance=site, data=request.data, partial=True)
        if site_serializer.is_valid():
            site_serializer.save()
        return Response(site_serializer.data)

    def delete(self, request, site_id):
        try:
            site = Site.objects.get(site_id=site_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        site_serializer = SiteSerializer(instance=site)
        site.delete()
        return Response(site_serializer.data)


class Page_l(APIView):
    def get(self, request):
        expand = request.GET.get("expand")
        page_site_id = request.GET.get("site_id")
        page = Page.objects.all()
        if page_site_id is not None:
            page = page.filter(page_site_id=page_site_id)
        if expand is not None:
            page_serializer = PageExpandSerializer(instance=page, many=True)
        else:
            page_serializer = PageSerializer(instance=page, many=True)
        return Response(page_serializer.data)

    def post(self, request):
        page_serializer = PagePostSerializer(data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
        return Response(page_serializer.data)


class Page_d(APIView):
    def get(self, request, page_id):
        try:
            page = Page.objects.get(page_id=page_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        page_serializer = PageSerializer(instance=page)
        return Response(page_serializer.data)

    def put(self, request, page_id):
        try:
            page = Page.objects.get(page_id=page_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        page_serializer = PageSerializer(instance=page, data=request.data, partial=True)
        if page_serializer.is_valid():
            page_serializer.save()
        return Response(page_serializer.data)

    def delete(self, request, page_id):
        try:
            page = Page.objects.get(page_id=page_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        page_serializer = PageSerializer(instance=page)
        page.delete()
        return Response(page_serializer.data)

class Request_l(APIView):
    def get(self, request):
        requests = Request.objects.all()
        request_serializer = RequestSerializer(instance=requests, many=True)
        return Response(request_serializer.data)

    def post(self, request):
        request_serializer = RequestSerializer(data=request.data)
        if request_serializer.is_valid():
            request_serializer.save()
        return Response(request_serializer.data)


class Request_d(APIView):
    def get(self, request, request_id):
        try:
            requests = Request.objects.get(request_id=request_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request_serializer = RequestSerializer(instance=requests)
        return Response(request_serializer.data)

    def put(self, request, request_id):
        try:
            requests = Request.objects.get(request_id=request_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request_serializer = RequestSerializer(instance=requests, data=request.data, partial=True)
        if request_serializer.is_valid():
            request_serializer.save()
        return Response(request_serializer.data)

    def delete(self, request, request_id):
        try:
            requests = Request.objects.get(request_id=request_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request_serializer = RequestSerializer(instance=requests)
        requests.delete()
        return Response(request_serializer.data)

class Content_l(APIView):
    def get(self, request):
        content_request_id = request.GET.get("request_id")
        content_content = request.GET.get("content")
        content = Content.objects.all()
        if content_request_id is not None:
            content = content.filter(content_request_id=content_request_id)
        if content_content is not None:
            content = content.filter(content_content__icontains=content_content)
        content_serializer = ContentSerializer(instance=content, many=True)
        return Response(content_serializer.data)

    def post(self, request):
        content_serializer = ContentSerializer(data=request.data)
        if content_serializer.is_valid():
            content_serializer.save()
        return Response(content_serializer.data)


class Content_d(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        content_serializer = ContentSerializer(instance=content)
        return Response(content_serializer.data)

    def put(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        content_serializer = ContentSerializer(instance=content, data=request.data, partial=True)
        if content_serializer.is_valid():
            content_serializer.save()
        return Response(content_serializer.data)

    def delete(self, request, content_id):
        try:
            content = Content.objects.get(content_id=content_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        content_serializer = ContentSerializer(instance=content)
        content.delete()
        return Response(content_serializer.data)

class osno(APIView):

    def post(self, request):
        page_serializer = PagePostSerializer(data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()

        ps = request.data

        from bs4 import BeautifulSoup
        import requests as req

        url = ps.get('page_url')
        resp = req.get(url)

        soup = BeautifulSoup(resp.text, 'lxml')

        file = open("test.txt", "w")
        file.write(str(soup.text))
        file.close()

        osnov = ""
        with open("test.txt", "r") as file1:
            for line in file1:
                if line != "\n":
                    osnov = osnov + line


        datakey=["request_id", "request_html_content", "request_page_id"]
        data=dict.fromkeys(datakey)
        data['request_html_content']=osnov
        data['request_page_id'] = ps.get('page_id')
        request_serializer = RequestSerializer(data=data)
        if request_serializer.is_valid():
            request_serializer.save()

        return HttpResponse(osnov)