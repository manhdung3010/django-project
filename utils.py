# utils.py
from rest_framework.response import Response

def standard_response(data, message, code):
    return Response({
        "data": data,
        "message": message,
        "code": code
    }, status=code)
