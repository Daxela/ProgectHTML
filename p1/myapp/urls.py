
from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('call', views.Site_v)

urlpatterns = [
    path('site/', views.Site_l.as_view()),
    path('site/<int:site_id>/', views.Site_d.as_view()),
    path('page/', views.Page_l.as_view()),
    path('page/<int:page_id>/', views.Page_d.as_view()),
    path('request/', views.Request_l.as_view()),
    path('request/<int:request_id>/', views.Request_d.as_view()),
    path('content/', views.Content_l.as_view()),
    path('content/<int:content_id>/', views.Content_d.as_view()),
    path('work/page/', views.osno.as_view())
    #path('app/', include(router.urls)),
]

