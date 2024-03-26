from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from .serializers import GroupSerializer, UserSerializer, AdminSerializer, ChatAppSerializer, CricketAppSerializer, EarningAppSerializer, SlotAppSerializer, BaccaratAppSerializer
from .models import Admin, ChatApp, CricketApp, EarningApp, SlotApp, BaccaratApp

class HealthCheckViews(viewsets.ModelViewSet):
    def get(self, request, format=None):
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    max_page_size = 10


    # Backend Views API's



class AdminViews(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('id')
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Admin Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Admin Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Admin not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Admin Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Admin Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Admin Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class ChatAppViews(viewsets.ModelViewSet):
    queryset = ChatApp.objects.all().order_by('id')
    serializer_class = ChatAppSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = ChatAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Chat Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Chat Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Chat user not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Chat Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Chat Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Chat Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class CricketAppViews(viewsets.ModelViewSet):
    queryset = CricketApp.objects.all().order_by('id')
    serializer_class = CricketAppSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def create(self, request, *args, **kwargs):
        serializer = CricketAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Cricket Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Cricket Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Cricket user not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Cricket Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Cricket Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Cricket Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class EarningAppViews(viewsets.ModelViewSet):
    queryset = EarningApp.objects.all().order_by('id')
    serializer_class = EarningAppSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = EarningAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Earning Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Earning Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Earning user not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Earning Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Earning Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Earning Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class SlotAppViews(viewsets.ModelViewSet):
    queryset = SlotApp.objects.all().order_by('id')
    serializer_class = SlotAppSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = SlotAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Slot Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Slot Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Slot user not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Slot Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Slot Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Slot Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class BaccaratAppViews(viewsets.ModelViewSet):
    queryset = BaccaratApp.objects.all().order_by('id')
    serializer_class = BaccaratAppSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = BaccaratAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Baccarat Account created successfully',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.get_serializer(instance)
            response_data = {
                'message': 'Result Baccarat Data',
                'data': serializer.data
            }
            return Response(response_data)
        except Admin.DoesNotExist:
            return Response({'message': 'Baccarat user not found'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        id_filter = request.query_params.get('id')
        username_filter = request.query_params.get('username')

        if id_filter:
            queryset = queryset.filter(id=id_filter)
        if username_filter:
            queryset = queryset.filter(username__icontains=username_filter)

        queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'message': 'Result Baccarat Data List',
            'data': serializer.data
        }
        return self.get_paginated_response(response_data)


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Baccarat Account updated successfully',
                'data': serializer.data
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'Message': 'Baccarat Account Deleted Duccessfully'}, status=status.HTTP_204_NO_CONTENT)


class AdminUserListView(viewsets.ModelViewSet):
    def list(self, request):
        chat_apps = ChatApp.objects.all()
        cricket_apps = CricketApp.objects.all()
        earning_apps = EarningApp.objects.all()
        slot_apps = SlotApp.objects.all()
        baccarat_apps = BaccaratApp.objects.all()

        chat_data = ChatAppSerializer(chat_apps, many=True).data
        cricket_data = CricketAppSerializer(cricket_apps, many=True).data
        earning_data = EarningAppSerializer(earning_apps, many=True).data
        slot_data = SlotAppSerializer(slot_apps, many=True).data
        baccarat_data = BaccaratAppSerializer(baccarat_apps, many=True).data

        response_data = {
            "message": "Result Admin User List",
            "data": {
                "chat_app": chat_data,
                "cricket_app": cricket_data,
                "earning_app": earning_data,
                "slot_app": slot_data,
                "baccarat_app": baccarat_data
            }
        }
        return Response(response_data)