# pip install openpyxl
from openpyxl import load_workbook
from givmed.models import MedInfo

wb = load_workbook(filename='/home/awe/farmaka.xlsx', read_only=True)
ws = wb['Meds'] # ws is now an IterableWorksheet

meds = iter(ws.rows)
next(meds)

for row in meds:
	MedInfo(med_name = str(row[0].value), med_subs = str(row[1].value), med_price = float(row[4].value)).save()
