from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #otan diagrafei enas Auth User
    				#diagrafetai to UserProfile alla oxi to antistrofo
    userPhone = models.CharField(primary_key=True, max_length=10)
    birthDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    userAddress = models.CharField(max_length=100, default='')
    SEX_CHOICES = (
    	('M', 'Male'),
    	('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES , default='M') #na valoume choices
    OS_CHOICES = (
    	('A', 'Android'),
    	('I', 'IOS'),
    )
    os = models.CharField(max_length=1, choices=OS_CHOICES , default='A') 
    uuid = models.CharField(max_length=100, default='')


    class Meta:
    	verbose_name_plural = 'UserProfiles'
        ordering = ('userPhone', )#ordering me vash to username

    def __unicode__(self):
        return self.userPhone


class UserReg(models.Model):
    useras = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=4)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
   

    class Meta:
    	verbose_name_plural = 'UserRegs'
        ordering = ('otp', )
        
    def __unicode__(self):
        return self.otp


class MedInfo(models.Model):
	medEof = models.CharField(primary_key=True, max_length=13, default='')
	medName = models.TextField(max_length=600)
	medSubs = models.CharField(max_length=200, default='')
	medPrice = models.FloatField(default=0)
	medCateg = models.CharField(max_length=200, default='')


	class Meta:
		verbose_name_plural = 'MedsInfo'
		ordering = ('medName', )

	def __unicode__(self):
		return self.medEof


class Med(models.Model):
    barcode = models.CharField(primary_key=True, max_length=12)
    eofcode = models.ForeignKey(MedInfo, related_name='info', default='')
    medPhone = models.ForeignKey(UserProfile, related_name='meds', default='')
    postedDate = models.DateField(auto_now=False, auto_now_add=True, null=True)
    expirationDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    notes = models.TextField(max_length=140, blank=True, default='')
    STATE_CHOICES = (
    	('O', 'Open'),
    	('C', 'Closed'),
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES , default='C')
    forDonation = models.BooleanField(default=True)


    class Meta:
        ordering = ('postedDate', )
        unique_together = ('medPhone', 'barcode')

    def __unicode__(self):
        return self.barcode


class Pharmacy(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pharmacyPhone = models.CharField(primary_key=True, max_length=10, default='')
	pharmacyName = models.CharField(max_length=100)
	pharmacyNameGen = models.CharField(max_length=100, default='')
	gps_x = models.FloatField(default=0)
	gps_y = models.FloatField(default=0)
	region = models.CharField(max_length=100)
	pharmacyAddress = models.CharField(max_length=100)
	description = models.TextField(max_length=500, blank=True, default='')
	website = models.URLField(max_length=250, blank=True, default='')
	supervisor = models.CharField(max_length=50)
	supervisorMail = models.EmailField(max_length=254, blank=True, default='')
	# openTime
	# howToGoThere


	class Meta:
		verbose_name_plural = 'Pharmacies'
		ordering = ('pharmacyPhone', )

	def __unicode__(self):
		return self.pharmacyPhone


class Need(models.Model):
	needDate = models.DateField(auto_now=False, auto_now_add=True)
	needPhone = models.ForeignKey(Pharmacy, related_name='nPhone')
	needMedName = models.CharField(max_length=200, blank=True, default='') #merikes fores onoma merikes drastikh ousia
	substance = models.CharField(max_length=200, blank=True, default='')
	quantity = models.IntegerField(blank=True, default=0) #proeraitiko
	needNotes = models.TextField(max_length=500, blank=True, default='')


	class Meta:
		verbose_name_plural = 'Needs'
		ordering = ('needDate', )

	def __unicode__(self):
		return str(self.id)


class Donation(models.Model):
	donationDate = models.DateField(auto_now=False, auto_now_add=True)
	donatorPhone = models.ForeignKey(UserProfile, related_name='uPhone')
	donatedPhone = models.ForeignKey(Pharmacy, related_name='dPhone')
	donationId = models.ForeignKey(Need, related_name='dId')
	donationBarcode = models.ForeignKey(Med, related_name='nBarcode')
	DELIVERAS = (
		('U', 'user'),
		('V', 'volunteer')
	)
	deliveryType = models.BooleanField(max_length=1, choices=DELIVERAS, default='U') #dwrhths h ethelodhs
	deliveryDate = models.DateField(auto_now=False, auto_now_add=False)


	class Meta:
		verbose_name_plural = 'Donations'
		ordering = ('deliveryDate', )
		unique_together = ('donatorPhone', 'donatedPhone', 'donationBarcode', 'donationId' )

	def __unicode__(self):
		return u'%s %s %s %s' % (self.donatorPhone, self.donatedPhone, self.donationBarcode, self.donationId)