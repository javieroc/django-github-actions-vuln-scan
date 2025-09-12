from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

class HelloWorldView(APIView):
    def get(self, request):
        cursor = connection.cursor()
        user_id = request.query_params.get("id", '1')
        cursor.execute("SELECT * FROM auth_user WHERE id = " + user_id)
        user = cursor.fetchone()
        return Response({"user": user})