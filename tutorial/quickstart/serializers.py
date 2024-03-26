from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.db.models import fields
from .models import Admin, ChatApp, CricketApp, EarningApp, SlotApp, BaccaratApp


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'id',
            'username',
            'password'
        ]


class ChatAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatApp
        fields = [
            'id',
            'username',
            'password',
            'phone_number',
            'address',
            'created_at'
        ]


class CricketAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CricketApp
        fields = [
            'id',
            'username',
            'password',
            'phone_number',
            'address',
            'created_at'
        ]


class EarningAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EarningApp
        fields = [
            'id',
            'username',
            'password',
            'phone_number',
            'address',
            'created_at'
        ]


class SlotAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlotApp
        fields = [
            'id',
            'username',
            'password',
            'phone_number',
            'address',
            'created_at'
        ]


class BaccaratAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaccaratApp
        fields = [
            'id',
            'username',
            'password',
            'phone_number',
            'address',
            'created_at'
        ]

