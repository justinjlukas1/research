# -*- coding:utf-8 -*-
import time
from crawler import SecCrawler

import edgar
import io
import xlrd
import xlwt


def test():
    t1 = time.time()
    # file containig company name and corresponding cik codes
    seccrawler = SecCrawler()

    company_code_list = list()   # company code list
    cik_list = list()            # cik code list
    date_list = list()           # pror date list
    count_list = list()

    try:
        f = open("data.txt", "w")
    except:
            print ("No input file found")

    try:
        workbook = xlrd.open_workbook('listofITfirms.xls')
    except:
        print ("No input file found")

    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0, 0)

    # Extracting number of rows
    print(sheet.nrows)
    f.write("Quote   CIK        priorto(YYYYMMDD) Count\n")
    sheet.cell_value(0, 4)

    for i in range(1, sheet.nrows):
            # f.write("%s,%s\n" % sheet.cell_value(i, 1))
            if sheet.cell_value(i, 1) and sheet.cell_value(i, 4):
                f.write("%s   %d   199980101   100\n" % (sheet.cell_value(i, 1), sheet.cell_value(i, 4)))
    f.close()

    try:
        crs = open("data.txt", "r")
    except:
        print ("No input file Found")


    # get the comapny  quotes and cik number from the file.
    for columns in (raw.strip().split() for raw in crs):
        company_code_list.append(columns[0])
        cik_list.append(columns[1])
        date_list.append(columns[2])
        count_list.append(columns[3])

    # call different  API from the crawler
    for i in range(1, len(cik_list)):
        seccrawler.filing_SD(str(company_code_list[i]), str(cik_list[i]),
            str(date_list[i]), str(count_list[i]))
        seccrawler.filing_10K(str(company_code_list[i]), str(cik_list[i]),
            str(date_list[i]), str(count_list[i]))
        # seccrawler.filing_8K(str(company_code_list[i]), str(cik_list[i]),
        #     str(date_list[i]), str(count_list[i]))
        # seccrawler.filing_10Q(str(company_code_list[i]), str(cik_list[i]),
        #     str(date_list[i]), str(count_list[i]))

    t2 = time.time()
    print ("Total Time taken: "),
    print (t2 - t1)
    crs.close()

if __name__ == '__main__':
    test()
