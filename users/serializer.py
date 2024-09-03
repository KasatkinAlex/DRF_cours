from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["password"] = "Пароль захеширован"
        return representation


class UserSerializerList(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "tg_chat_id")
