from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Signup
import random
from uuid import uuid4


class Newsletter(APIView):
    def get(self, request, format=None):
        return HttpResponse(str(uuid4()))

    def post(self, request, format=None):
        json_body = request.data
        email = json_body.get('email')
        Signup.objects.create(email=email, confirmationId=random.randint(0, 1000000), confirmed=False)
        return HttpResponse()
