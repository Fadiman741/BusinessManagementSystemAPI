from rest_framework import serializers
from .models import Task, User, Menu, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "contacts",
            "datecreated",
            "dateofbirth",
            "role",
            "status",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class MenuSerialiazer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Menu
        fields = [
            "id",
            # "user",
            "Name",
            "Description",
            "Price",
            "Category",
            "tags",
            "image"
        ]

    def __str__(self):
        return self.menu_name


# class OrderSerializer(serializers.ModelSerializer):
#     # user = UserSerializer()
#     items = MenuSerialiazer(many=True)

#     class Meta:
#         model = Order
#         fields = [
#             "id",
#             # "user",
#             "items",
#             "status",
#             "order_number",
#             "created_at",
#             "updated_at",
#         ]

class OrderSerializer(serializers.ModelSerializer):
    items = MenuSerialiazer(read_only=True, many=True)  # Assuming MenuSerializer is your nested serializer

    class Meta:
        model = Order
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'