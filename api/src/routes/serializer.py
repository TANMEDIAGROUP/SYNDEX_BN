from rest_framework import serializers
from api.models import UserModel

class UserSerialize (serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields="__all__"
