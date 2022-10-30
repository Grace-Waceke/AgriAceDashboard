# from multiprocessing import context
# from django.shortcuts import render
from django.shortcuts import redirect, render
from rest_framework import views, status
from rest_framework.decorators import parser_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from dashboard.forms import FarmerForm
from dashboard.models import Farmer
from serializers import CustomerSerializer


# # Create your views here.
# def dashboard_with_pivot(request):
#     return render(request, 'dashboard_with_pivot.html', {})
# def index(request):
#     return render (request, "home/home.html")
# def card(request):
#     context={}
#     return render (request, "card.html", context)


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)


def index(request):
    return render(request, 'index.html')


def farmer_Form(request):
    if request.method == "POST":
        form = FarmerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("farmerslist")
        else:
            print(form.errors)
    else:
        form = FarmerForm()
    return render(request, "farmers_Form.html", {"form": form})


def farmers_list(request):
    farmers = Farmer.objects.all()
    return render(request, "farmers_list.html", {"farmers": farmers})


class CustomerLoginView(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer.CustomerSerializer
    parser_classes(JSONParser, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            logged_in = serializer.authenticate(request.data)
            if logged_in:
                return Response({"message": "Successfully logged in"},
                                status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED)


class CustomerRegisterView(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer.CustomerSerializer
    parser_classes(JSONParser, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            customer = serializer.create(request.data)
            if customer is not None and customer is True:
                return Response({"message": "customer already exists", "payload": customer},
                                status=status.HTTP_208_ALREADY_REPORTED)

            return Response({"message": "success", "payload": customer},
                            status=status.HTTP_201_CREATED)

        return Response({"message": "Failed", "payload": serializer.data},
                        status=status.HTTP_417_EXPECTATION_FAILED)


class ViewAllCustomers(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer.ReadAllCustomers
    parser_classes(JSONParser, )
    pagination_class = PageNumberPagination

    def get(self, request):
        serializer = CustomerSerializer.ReadAllCustomers(self.serializer_class.get_all_customers(), many=True)
        return Response({"message": "success", "payload": serializer.data},
                        status=status.HTTP_200_OK)
