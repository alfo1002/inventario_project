from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class EmailAPIView(APIView):
    def post(self, request):
        try:
            to_email = "xxxxx@hotmail.com"
            subject = "Mensaje de Prueba"
            message = request.data.get('message')
            send_mail(subject, message, None, [to_email])
            return Response({'message': 'Correo Enviado con Exito'}, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({'message': error_message}, status=status.HTTP_400_BAD_REQUEST)