import edgar
company = edgar.Company("Oracle Corp", "0001341439")
tree = company.getAllFilings(filingType = "10-K")
docs = edgar.getDocuments(tree, noOfDocuments=2)

# https://github.com/joeyism/py-edgar

f = open("demofile.txt", "w")
f.write("%s" % docs)
