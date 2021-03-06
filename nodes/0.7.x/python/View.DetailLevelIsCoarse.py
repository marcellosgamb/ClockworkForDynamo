import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

views = UnwrapElement(IN[0])
booleans = list()
for view in views:
	try:
		if str(view.DetailLevel) == 'Coarse':
			booleans.append(True)
		else:
			booleans.append(False)
	except:
		booleans.append(False)
OUT = booleans