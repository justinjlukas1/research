import edgar
import xlrd
import xlwt

#https://www.datacamp.com/community/tutorials/python-excel-tutorial

company = edgar.Company("Oracle Corp", "0001341439")
tree = company.getAllFilings(filingType = "10-K")
docs = edgar.getDocuments(tree, noOfDocuments=2)

# https://github.com/joeyism/py-edgar

f = open("demofile.txt", "w")
f.write("%s" % docs)

workbook = xlrd.open_workbook('listofITfirms.xls')
# worksheet = workbook.sheet_by_name('Sheet1')
# workbook = xlwt.open_workbook('listofITfirms.xls')
# sheet = workbook.add_sheet('Sheet_1')
# sheet.write(0, 0,'Inserting data in 1st Row and 1st Column')



# # Import pandas
# import pandas as pd
#
# # Assign spreadsheet filename to `file`
# file = 'listofITfirms.xls'
#
# # Load spreadsheet
# xl = pd.ExcelFile(file)
#
# # Print the sheet names
# print(xl.sheet_names)
#
# # Load a sheet into a DataFrame by name: df1
# df1 = xl.parse('Sheet4')

sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0)

# Extracting number of rows
print(sheet.nrows)
sheet.cell_value(0, 4)

for i in range(sheet.nrows):
    print(sheet.cell_value(i, 4))
