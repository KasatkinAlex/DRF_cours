from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserSerializerList(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_chat_id")
