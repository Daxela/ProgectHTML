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
from .WebProcessor import WebProcessor
from django.template.response import TemplateResponse
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

class Main(APIView):

    def post(self, request):
        url = request.POST.get("fname")
        name_site = request.POST.get("lname")

        header_site = name_site
        header_url = url

        k = 0
        num = 0
        num_n = 0
        flag = True
        for char in url:
            num = num + 1
            if char == '/':
                k = k + 1
            if (k == 2) & flag:
                num_n = num
                flag = False
            if k == 3:
                host = url[num_n:num - 1]
                break

        header_host = host

        if not Site.objects.filter(site_name=name_site, site_host=host).exists():
            datakey = ["site_id", "site_host", "site_name"]
            data = dict.fromkeys(datakey)

            data['site_host'] = host
            data['site_name'] = name_site
            site_serializer = SiteSerializer(data=data)
            if site_serializer.is_valid():
                site_serializer.save()

        site = Site.objects.get(site_name=name_site, site_host=host)
        site_id=site.site_id

        if not Page.objects.filter(page_url=url, page_site_id=site_id).exists():
            datakey = ["page_id", "page_site_id", "page_url"]
            data = dict.fromkeys(datakey)

            data['page_site_id'] = site_id
            data['page_url'] = url
            page_serializer = PageSerializer(data=data)
            if page_serializer.is_valid():
                page_serializer.save()

        page = Page.objects.get(page_site_id=site_id, page_url=url)
        page_id = page.page_id

        processor = WebProcessor()
        general_data, deleted_data = processor.process(url)
        general_data = processor.post_process(general_data)

        if not Request.objects.filter(request_page_id=page_id).exists():
            datakey = ["request_id", "request_page_id", "request_datetime", "request_html_content"]
            data = dict.fromkeys(datakey)
            data['request_html_content'] = " ".join(general_data)
            data['request_page_id'] = page_id
            request_serializer = RequestSerializer(data=data)
            if request_serializer.is_valid():
                request_serializer.save()

            request_t = Request.objects.get(request_page_id=page_id)
            request_id = request_t.request_id
            header_number = request_id
            text = request_t.request_html_content


            for types in deleted_data:
                datakey = ["content_id", "content_request_id", "content_type", "content_content"]
                data = dict.fromkeys(datakey)
                data['content_type'] = types
                data['content_content'] = " ".join(deleted_data[types])
                data['content_request_id'] = request_id
                content_serializer = ContentSerializer(data=data)
                if content_serializer.is_valid():
                    content_serializer.save()
        else:
            request_t = Request.objects.get(request_page_id=page_id)
            header_number = request_t.request_id
            text = request_t.request_html_content

        key = ["header_number", "header_site", "header_url", "header_host", "text"]
        data = dict.fromkeys(key)
        data['header_number'] = header_number
        data['header_site'] = header_site
        data['header_url'] = header_url
        data['header_host'] = header_host
        data['text'] = text

        return TemplateResponse(request, "Result.html", data)


class Main1(APIView):

    def get(self, request, request_id):
        header_number = request_id
        requests = Request.objects.get(request_id=request_id)
        text = requests.request_html_content
        header_url = requests.request_page_id.page_url
        header_site = requests.request_page_id.page_site_id.site_name
        header_host = requests.request_page_id.page_site_id.site_host

        key = ["header_number", "header_site", "header_url", "header_host", "text"]
        data = dict.fromkeys(key)
        data['header_number'] = header_number
        data['header_site'] = header_site
        data['header_url'] = header_url
        data['header_host'] = header_host
        data['text'] = text

        return TemplateResponse(request, "Result.html", data)

class Del(APIView):

    def get(self, request, request_id):
        req = request_id
        content = Content.objects.get(content_request_id=request_id)
        val = []
        key = []
        j = 0
        for i in content:
            j += 1
            n = []
            n.append(i.content_type)
            n.append(i.content_content)
            val.append(n)
            strj = 'a' + str(j)
            key.append(strj)
        data = dict(zip(key, val))
        return TemplateResponse(request, "Del.html", data)