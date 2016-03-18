import xlrd
from givmed.models import MedInfo

# vazoume ton kwdiko (280...), to onoma, thn drastikh ousia kai thn palia timh, 
# h 8erapautikh kathgoria menei kenh
workbook = xlrd.open_workbook(filename='/home/awe/GIVMED/ono_barc_drast_17-07-2015.xlsx')
worksheet = workbook.sheet_by_name('Meds')

for i in xrange(1, worksheet._dimnrows):
	eof = unicode(worksheet.cell(i, 1).value)
	name = unicode(worksheet.cell(i, 2).value)
	subs = unicode(worksheet.cell(i, 4).value)
	price = unicode(worksheet.cell(i, 11).value)

	MedInfo(medEof = eof, medName = name, medSubs = subs, medPrice = price).save()


print "Added %d new meds." % (worksheet._dimnrows)

# apo to kainourgio excel ananewnoume tis times kai an kapoios kwdikos
# den yparxei ton topo8etoume
workbook = xlrd.open_workbook(filename='/home/awe/GIVMED/ono_barc_timh_31-12-2015.xlsx')
worksheet = workbook.sheet_by_name('Meds')

newMeds = 0
updMeds = 0

for i in xrange(1, worksheet._dimnrows):
	eof = unicode(worksheet.cell(i, 1).value)
	name = unicode(worksheet.cell(i, 2).value)
	price = unicode(worksheet.cell(i, 8).value)

	# uncomment this line if the excel has a cell with substance info and 
	# place the number of the column below (i, #column)
	#subs = unicode(worksheet.cell(i, 4).value)

	med = MedInfo.objects.filter(medEof=eof)

	if not med:
		MedInfo(medEof = eof, medName = name, medPrice = price).save()
		newMeds += 1
	else:
		med[0].medPrice = price
		med[0].save()
		updMeds += 1

print "Added %d new meds and updated %d old meds." % (newMeds, updMeds)