from rest_framework import serializers
from givmed.models import *
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user','userPhone', 'birthDate', 'sex', 'os', 'uuid')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password','email')


class MedSerializer(serializers.ModelSerializer):
    medName = serializers.ReadOnlyField(source='eofcode.medName')
    medPrice = serializers.ReadOnlyField(source='eofcode.medPrice')

    class Meta:
        model = Med
        fields = ('barcode', 'eofcode', 'expirationDate', 'medPhone', 'notes', 'state', 'forDonation',
                    'medName', 'medPrice')


class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacy
        fields = ('pharmacyPhone', 'pharmacyName', 'region', 'pharmacyAddress', 
                'description', 'website', 'supervisor', 'supervisorMail')


class NeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Need
        fields = ('needDate', 'needPhone', 'needMedName', 'substance', 'quantity', 'needNotes')


class NeedIOSerializer(serializers.ModelSerializer):
    needPharmacyGPSx = serializers.ReadOnlyField(source='needPhone.gps_x')
    needPharmacyName = serializers.ReadOnlyField(source='needPhone.pharmacyName')
    needPharmacyNameGen = serializers.ReadOnlyField(source='needPhone.pharmacyNameGen')
    needPharmacyGPSy = serializers.ReadOnlyField(source='needPhone.gps_y')
    needPhone = serializers.ReadOnlyField(source='needPhone.pharmacyPhone')


    class Meta:
        model = Need
        fields = ('needMedName','needPharmacyName','needPharmacyNameGen','needPharmacyGPSx', 'needPharmacyGPSy','needPhone')


class ReturnNeedsSerializer(serializers.ModelSerializer):
    needAddress = serializers.ReadOnlyField(source='needPhone.pharmacyAddress')
    needPhone = serializers.ReadOnlyField(source='needPhone.pharmacyPhone')

    class Meta:
        model = Need
        fields = ('id','needMedName', 'needPhone', 'needAddress')


'''class UserProfileSerializer(serializers.ModelSerializer):
    #user_id = serializers.SerializerMethodField('is_named_bar')

    class Meta:
        model = UserProfile
        fields = ('userPhone','user')'''


class UserRegSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserReg
        fields = ('useras', 'otp', )


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


class MedInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedInfo
        fields = ('medEof', 'medName', 'medSubs', 'medCateg', 'medPrice')