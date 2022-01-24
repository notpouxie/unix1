from rest_framework.views import APIView
from django.shortcuts import render


class Handler(APIView):

    def get(self, request):
        return render(request, 'views/index.html')
