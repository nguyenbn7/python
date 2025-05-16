from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def get_categories(request: HttpRequest):
    return Response({"categories": []})
