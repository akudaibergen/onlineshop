from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Product, Order


class ProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'color', 'size', 'category')


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        company = Category.objects.create(name=validated_data.get('name'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'owner', 'date', 'status', 'products')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']