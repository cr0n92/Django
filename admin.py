from django.contrib import admin
from givmed.models import *

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	#list_display = Users._meta.get_all_field_names()
	list_display = ['userPhone', 'sex', 'birthDate']

class MedAdmin(admin.ModelAdmin):
	list_display = ['barcode', 'eofcode', 'medPhone', 'postedDate', 'notes', 'state', 'forDonation']
	
class PharmacyAdmin(admin.ModelAdmin):
	list_display = ['pharmacyPhone', 'pharmacyName', 'region', 'pharmacyAddress', 
                	'description', 'website', 'supervisor', 'supervisorMail']

class NeedAdmin(admin.ModelAdmin):
	list_display = ['needDate', 'needPhone', 'needMedName', 'substance', 'quantity', 'needNotes']

class UserRegAdmin(admin.ModelAdmin):
	list_display = ['useras','otp','active']

class DonationAdmin(admin.ModelAdmin):
	list_display = ['donationDate', 'donatorPhone', 'donatedPhone', 'donationId', 
                	'donationBarcode', 'deliveryType', 'deliveryDate']

class MedInfoAdmin(admin.ModelAdmin):
	list_display = ['medEof', 'medName', 'medSubs', 'medCateg', 'medPrice']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Med, MedAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(MedInfo, MedInfoAdmin)
admin.site.register(UserReg, UserRegAdmin)