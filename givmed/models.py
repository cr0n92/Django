from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userPhone = models.CharField(primary_key=True, max_length=10)
    birthDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    userAddress = models.CharField(max_length=100, default='')
    SEX_CHOISES = (
    	('M', 'Male'),
    	('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOISES , default='M') #na valoume choices

    class Meta:
    	verbose_name_plural = 'UserProfiles'
        ordering = ('userPhone', )#ordering me vash to username

    def __unicode__(self):
        return self.userPhone


class Med(models.Model):
    barcode = models.CharField(primary_key=True, max_length=12)
    medPhone = models.ForeignKey(UserProfile, related_name='meds', default='')
    medName = models.CharField(max_length=90)
    postedDate = models.DateField(auto_now=False, auto_now_add=True, null=True)
    expirationDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    boxes = models.IntegerField(default=1)
    #notes = models.TextField(max_length=140, blank=True, default='')

    class Meta:
        ordering = ('medName', )
        unique_together = ('medPhone', 'barcode')

    def __unicode__(self):
        return self.barcode


class Pharmacy(models.Model):
	pharmacyPhone = models.CharField(primary_key=True, max_length=10, default='')
	pharmacyName = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	pharmacyAddress = models.CharField(max_length=100)
	description = models.TextField(max_length=500, blank=True, default='')
	website = models.URLField(max_length=250, blank=True, default='')
	supervisor = models.CharField(max_length=50)
	supervisorMail = models.EmailField(max_length=254, blank=True, default='')
	userName = models.CharField(max_length=100)
	passWord = models.CharField(max_length=100)
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
	needMedName = models.CharField(max_length=100, blank=True, default='') #merikes fores onoma merikes drastikh ousia
	substance = models.CharField(max_length=100, blank=True, default='')
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