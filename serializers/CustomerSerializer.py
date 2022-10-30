from rest_framework import serializers

from dashboard.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("customer_username", "customer_password")
        model = Customers

    @staticmethod
    def authenticate(data):
        username = data["customer_username"]
        password = data["customer_password"]
        user = Customers.objects.filter(customer_username=username, customer_password=password)
        if user:
            return True
        return False

    @staticmethod
    def create(validated_data):
        username = validated_data["customer_username"]
        password = validated_data["customer_password"]
        customer_exist = Customers.objects.filter(customer_username=username, customer_password=password).exists()
        if customer_exist:
            return True
        else:
            customer = Customers.objects.create(customer_username=username, customer_password=password)
            customer.save()
            customer_payload = {"customer_name": customer.customer_username}
            return customer_payload


class ReadAllCustomers(serializers.ModelSerializer):
    class Meta:
        fields = ("customer_username", "customer_password")
        model = Customers

    @staticmethod
    def get_all_customers():
        customers = Customers.objects.all().defer("customer_password")
        if customers:
            return customers
        return None
