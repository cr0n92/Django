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

    class Meta:
        model = UserProfile
        fields = ('user', 'userPhone', 'birthDate', 'userAddress', 'sex')


class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = ('donationDate', 'donatorPhone', 'donatedPhone', 'donationId', 
                'donationBarcode', 'deliveryType', 'deliveryDate')


class MedInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedInfo
        fields = ('med_name', 'med_subs', 'med_price')