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
import urllib2
import random

#edw mporw na kanw ena query mesa se ena while gia to an uparxei mh active xrhsths me idio otp
#opote sunexizw na paragw otp
def otp_maker():
	#return "%04d" % random.randrange(0, 10000, 1)
	return '1234'

def send_sms(phone,otp):
	urllib2.urlopen("https://rest.nexmo.com/sms/json?api_key=fea55ff0&api_secret=aabaffcc&to=30"+phone+"&from=GivMed&text=Hello+from+GivMed.Your+code+is+%3A"+otp).read()

	
#http://stackoverflow.com/questions/630453/put-vs-post-in-rest/2590281#2590281


@api_view(['POST','GET'])
def user_register(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        n1 = request.data.copy()
        n1['password'] = 123
        serializer = UserSerializer(data=n1)
        if serializer.is_valid():
            a = serializer.save()

            n1['user'] = a.id
            serializer = UserProfileSerializer(data=n1)
            if serializer.is_valid():
                b=serializer.save()
                #otp = otp_maker() 
                #send_sms(b.userPhone,otp)
                #n1['otp'] = otp
                #n1['useras'] = a.id
                #serializer = UserRegSerializer(data=n1)
                #if serializer.is_valid(raise_exception=True):
                	#c=serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                a.delete()
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request):
    """
    Update a user.
    """
    if request.method == 'PUT':
        try:
            user = UserProfile.objects.get(userPhone=userPhone)
        except UserProfile.DoesNotExist:
            raise Http404    	
        n1 = request.data.copy()
        n1['password'] = '123'
        serializer = UserSerializer(data=n1)
        if serializer.is_valid():
            a = serializer.save()

            n1['user'] = a.id
            serializer = UserProfileSerializer(data=n1)
            if serializer.is_valid():
                b=serializer.save()
                #otp = otp_maker() 
                #send_sms(b.userPhone,otp)
                #n1['otp'] = otp
                #n1['useras'] = a.id
                #serializer = UserRegSerializer(data=n1)
                #if serializer.is_valid(raise_exception=True):
                	#c=serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                a.delete()
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, userPhone):
        try:
            return UserProfile.objects.get(userPhone=userPhone)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, userPhone, format=None):
        user = self.get_object(userPhone)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, userPhone, format=None):
        '''req_copy = request.data.copy()
        medi = Med.objects.get(barcode=request.data['barcode'])
        med_d = MedSerializer(medi).data
        med_d['medPhone'] = UserProfile.objects.get(userPhone=phone)

        for key, value in req_copy.items():
            med_d[key] = value

        serializer = MedSerializer(medi, data=med_d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    	------------------------------------------------------------'''

        n1 = request.data.copy()
        userP = UserProfile.objects.get(userPhone=userPhone)
        user = userP.user
        user_d = UserSerializer(user).data
        for key, value in n1.items():
            user_d[key] = value
        serializer = UserSerializer(user, data=user_d)
        if serializer.is_valid():
            serializer.save()
            userP_d = UserProfileSerializer(userP).data
            for key, value in n1.items():
                userP_d[key] = value

            
            serializer = UserProfileSerializer(userP, data=userP_d)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        '''a = self.get_object(userPhone)
        b = a.user
        n1 = request.data.copy()
        #n1['user'] = b.id
        #request.data['password'] = '123'
        serializer = UserProfileSerializer(a, data=n1,partial=True)
        if serializer.is_valid():
            print 'lolita'
            c= serializer.save()
            n1['user'] = c.id
          #   for field in a._meta.fields:
    		    # print field
            serializer = UserProfileSerializer(a, data=n1)
            if serializer.is_valid():
            	print 'karioka'
                serializer.save()
                print a.userAddress
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

    '''def delete(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        medi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''



@api_view(['POST',])
def otp_verify(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        if request.data['otp'] == '1234':
        	# a=UserReg.objects.get(otp=request.data['otp'])
        	# a.active = True
            return Response(status=status.HTTP_202_ACCEPTED)
        else:	    	
            return Response(status=status.HTTP_200_OK)



@receiver(post_save, sender=settings.AUTH_USER_MODEL) #ftianei token gia kathe xrhsth pou ginetai save
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



@api_view(['DELETE',])
def med_del(request, barcode):
    """
    Delete a med.
    """
    #authentication_classes = ( TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    if request.method == 'DELETE':
        medi = Med.objects.get(barcode=barcode)
        medi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST', 'PUT', 'GET',])
def med_detail(request, phone):
    """
    Insert, update or fetch a med instance.
    """

    if request.method == 'GET':
        medis = Med.objects.filter(medPhone=phone)
        serializer = MedSerializer(medis, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        req_copy = request.data.copy()
        req_copy['medPhone'] = UserProfile.objects.get(userPhone=phone)
        req_copy['eofcode'] = MedInfo.objects.get(medEof=request.data['eofcode'])
        serializer = MedSerializer(data=req_copy)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        req_copy = request.data.copy()
        medi = Med.objects.get(barcode=request.data['barcode'])
        med_d = MedSerializer(medi).data
        med_d['medPhone'] = UserProfile.objects.get(userPhone=phone)

        for key, value in req_copy.items():
            med_d[key] = value

        serializer = MedSerializer(medi, data=med_d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class PharmacyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pharmacyPhone):
        try:
            return Pharmacy.objects.get(pharmacyPhone=pharmacyPhone)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pharmacyPhone, format=None):
        pharmacy = self.get_object(pharmacyPhone)
        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)

    '''def put(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        serializer = MedSerializer(medi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, barcode, format=None):
        medi = self.get_object(barcode)
        medi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     '''   

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

class NeedsListIOS(APIView):
    """
    Dinei lista me ola ta Needs opws ta theloun oi IOS
    """
    def get(self, request, format=None):
        need = Need.objects.all()
        serializer = NeedIOSerializer(need, many=True)
        return Response(serializer.data)

    