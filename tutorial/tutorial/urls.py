from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('healthcheck/get', views.HealthCheckViews.as_view({'get': 'get'})),
    path('token/create', views.TokenObtainView.as_view({'post': 'create'})),

    path('admin/list', views.AdminViews.as_view({'get': 'list'})),
    path('admin/user/list', views.AdminUserListView.as_view({'get': 'list'})),
    path('admin/create', views.AdminViews.as_view({'post': 'create'})),
    path('admin/retrieve/<int:pk>', views.AdminViews.as_view({'get': 'retrieve'})),
    path('admin/update/<int:pk>', views.AdminViews.as_view({'patch': 'update'})),
    path('admin/delete/<int:pk>', views.AdminViews.as_view({'delete': 'delete'})),

    path('chat/list', views.ChatAppViews.as_view({'get': 'list'})),
    path('chat/create', views.ChatAppViews.as_view({'post': 'create'})),
    path('chat/retrieve/<int:pk>', views.ChatAppViews.as_view({'get': 'retrieve'})),
    path('chat/update/<int:pk>', views.ChatAppViews.as_view({'patch': 'update'})),
    path('chat/delete/<int:pk>', views.ChatAppViews.as_view({'delete': 'delete'})),

    path('cricket/list', views.CricketAppViews.as_view({'get': 'list'})),
    path('cricket/create', views.CricketAppViews.as_view({'post': 'create'})),
    path('cricket/retrieve/<int:pk>', views.CricketAppViews.as_view({'get': 'retrieve'})),
    path('cricket/update/<int:pk>', views.CricketAppViews.as_view({'patch': 'update'})),
    path('cricket/delete/<int:pk>', views.CricketAppViews.as_view({'delete': 'delete'})),

    path('earning/list', views.EarningAppViews.as_view({'get': 'list'})),
    path('earning/create', views.EarningAppViews.as_view({'post': 'create'})),
    path('earning/retrieve/<int:pk>', views.EarningAppViews.as_view({'get': 'retrieve'})),
    path('earning/update/<int:pk>', views.EarningAppViews.as_view({'patch': 'update'})),
    path('earning/delete/<int:pk>', views.EarningAppViews.as_view({'delete': 'delete'})),

    path('slot/list', views.SlotAppViews.as_view({'get': 'list'})),
    path('slot/create', views.SlotAppViews.as_view({'post': 'create'})),
    path('slot/retrieve/<int:pk>', views.SlotAppViews.as_view({'get': 'retrieve'})),
    path('slot/update/<int:pk>', views.SlotAppViews.as_view({'patch': 'update'})),
    path('slot/delete/<int:pk>', views.SlotAppViews.as_view({'delete': 'delete'})),

    path('baccarat/list', views.BaccaratAppViews.as_view({'get': 'list'})),
    path('baccarat/create', views.BaccaratAppViews.as_view({'post': 'create'})),
    path('baccarat/retrieve/<int:pk>', views.BaccaratAppViews.as_view({'get': 'retrieve'})),
    path('baccarat/update/<int:pk>', views.BaccaratAppViews.as_view({'patch': 'update'})),
    path('baccarat/delete/<int:pk>', views.BaccaratAppViews.as_view({'delete': 'delete'})),
]



