filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    # .replace() is a method that returns a new string
    filename = filename.replace('.','-',1)
    # rename()
    # tuples can not be modified