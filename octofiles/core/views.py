# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DocumentView(APIView):
    def get(self, request, slug):
        return Response(status=status.HTTP_200_OK)
