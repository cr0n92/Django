from rest_framework import serializers
from givmed.models import *
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('userName', 'userPhone', 'email', 'birthDate', 'userAddres', 'sex')


class MedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Med
        fields = ('barcode', 'medName', 'expirationDate', 'medPhone', 'boxes', 'postedDate')


class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacy
        fields = ('pharmacyPhone', 'pharmacyName', 'region', 'pharmacyAddress', 
                'description', 'website', 'supervisor', 'supervisorMail', 'userName', 'passWord')


class NeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Need
        fields = ('needDate', 'needPhone', 'needMedName', 'substance', 'quantity', 'needNotes')


class ReturnNeedsSerializer(serializers.ModelSerializer):
    needAddress = serializers.ReadOnlyField(source='needPhone.pharmacyAddress')
    needPhone = serializers.ReadOnlyField(source='needPhone.pharmacyPhone')

    class Meta:
        model = Need
        fields = ('id','needMedName', 'needPhone', 'needAddress')


class RegisterSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password',)


class RegisterSerializer2(serializers.ModelSerializer):
    #user_id = serializers.SerializerMethodField('is_named_bar')

    class Meta:
        model = UserProfile
        fields = ('userPhone','user')

# class RegisterSerializer2(serializers.Serializer):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     userPhone = models.CharField(primary_key=True, max_length=10)
#     birthDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
#     userAddress = models.CharField(max_length=100, default='')
    

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
    


class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = ('donationDate', 'donatorPhone', 'donatedPhone', 'donationId', 
                'donationBarcode', 'deliveryType', 'deliveryDate')