import os
import xlsxwriter
import xlrd
import xlwt
import urllib2
import time
import csv
import sys

from collections import OrderedDict

priorto = "20190101"
countFiles = 100


# words = ['reorganization', 'restructuring', 'appointments', 'executive moves', 'mergers and acquisitions', 'demergers', 'spin-offs']
# workbook = xlsxwriter.Workbook('test.xlsx')




words = ['anticipate', 'believe', 'depend', 'fluctuate', 'indefinite', 'likelihood', 'possible', 'predict', 'risk', 'uncertain']
word_vectors = ['anticipate risk', 'indefinite risk', 'fluctuate risk', 'risk likelihood', 'possible risk', 'predict risk', 'uncertain risk']
workbook = xlsxwriter.Workbook("EDGAR_Results.xlsx")


worksheet = workbook.add_worksheet()

row = 0
col = 0

worksheet.write(row, col, 'Company Name')
col = col + 1

worksheet.write(row,col, 'CIK')
col = col + 1

worksheet.write(row,col, 'GVKey')
col = col + 1

worksheet.write(row,col, 'Year')
col = col + 1

worksheet.write(row,col, 'HTML')
col = col + 1

start = col
date_line = False
count = OrderedDict()
temp_count = OrderedDict()
count_vector = OrderedDict()

for elem in words:
    temp_count[elem] = 0
    count[elem] = 0


# only include if using word_vectors
for elem in word_vectors:
    count_vector[elem] = 0

for word in words:
    worksheet.write_string(row, col, word)
    col = col + 1

# only include if using word_vectors
for word in word_vectors:
    worksheet.write_string(row,col,word)
    col = col + 1

row = row + 1

# should be whatever file path contains the data being analyzed
path = r'C:\Users\research\desktop\research-master\edgar-10k-mda-master\sec-edgar-master\SEC-Edgar-Data'
pathOriginal = path
print path

for companyTicker in os.listdir(path):
    print companyTicker
    path = path + '\\' + str(companyTicker)
    for cik in os.listdir(path):
        print ('\t' + cik)
        path = path + '\\' + str(cik)
        for file_type in os.listdir(path):
            path = path + '\\' + str(file_type)
            for file in os.listdir(path):
                col = start
                print ('\t\t' + file)

                worksheet.write_string(row, 0, companyTicker)
                worksheet.write_string(row, 1, cik)
                # worksheet.write_string(row, 4, file)
                worksheet.write_string(row, 4, "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cik)+"&type=10-K&dateb="+str(priorto)+"&owner=exclude&output=xml&count="+str(countFiles))

                response3 = open(os.path.join(path, str(file)), "r")
                for line in response3:





                    # find date of file. Could also use:

                    # <SEC-DOCUMENT>0000905155-97-000075.txt : 19971002
                    # <SEC-HEADER>0000905155-97-000075.hdr.sgml : 19971002
                    # ACCESSION NUMBER:		0000905155-97-000075
                    # CONFORMED SUBMISSION TYPE:	10-K
                    # PUBLIC DOCUMENT COUNT:		8
                    # CONFORMED PERIOD OF REPORT:	19970630
                    # FILED AS OF DATE:		19971001

                    if(line.startswith("CONFORMED PERIOD OF REPORT:")):
                        date_line = True

                    elements = line.split()

                    if(date_line):
                        worksheet.write_string(row, 3, elements[-1])
                        # print elements[-1]
                    date_line = False

                    for word in words:
                        # count[word] = count[word] + elements.count(word)
                        temp_count[word] = temp_count[word] + line.count(word)
                # writes all the counts to excel
                    for word in word_vectors:
                        count_vector[word] = count_vector[word] + line.count(word)
                for item in count:
                    index = 0
                    for word in words:
                        if word == item:
                            # worksheet.write(row, col, count[words[index]])
                            worksheet.write(row, col, temp_count[words[index]])
                            col = col + 1
                        index = index + 1

                for item in count_vector:
                    index = 0
                    for word in word_vectors:
                        if word == item:
                            # worksheet.write(row, col, count[words[index]])
                            if(count[word_vectors[index]] > 0)
                                print word
                            worksheet.write(row, col, count_vector[word_vectors[index]])
                            col = col + 1
                        index = index + 1
                        
                row = row + 1
                for elem in words:
                    count[elem] = 0
                    temp_count[elem] = 0
                for elem in word_vectors:
                    count_vector[elem] = 0
            path = pathOriginal + '\\' +str(companyTicker) + '\\' + str(cik)
        path = pathOriginal + '\\' + str(companyTicker)
    path = pathOriginal


workbook.close()
