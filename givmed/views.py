from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from givmed.models import *
from givmed.serializers import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

@api_view(['POST',])
def user_register(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        n1 = request.data.copy()

        serializer = RegisterSerializer1(data=n1)
        if serializer.is_valid():
            a = serializer.save()

            n1['user'] = a.id
            serializer = RegisterSerializer2(data=n1)
            if serializer.is_valid():
                b=serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                a.delete()
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@receiver(post_save, sender=settings.AUTH_USER_MODEL) #ftianei token gia kathe xrhsth pou ginetai save
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class MedList(APIView):
    """
    List all snippets, or create a new snippet.

    """
    authentication_classes = ( TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
    	print request.user
    	print request.auth
        medis = Med.objects.all()
        serializer = MedSerializer(medis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, barcode):
        try:
            return Med.objects.get(barcode=barcode)
        except Med.DoesNotExist:
            raise Http404

    def get(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        serializer = MedSerializer(medi)
        return Response(serializer.data)

    def put(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        serializer = MedSerializer(medi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        medi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NeedsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        need = Need.objects.all()
        serializer = ReturnNeedsSerializer(need, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)