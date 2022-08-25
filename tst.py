"""import pdfplumber
import PyPDF2
import os

count = 0
directory = "E:/Plag_check/plag_check1/"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        count += 1
        #text=''
        #pdfFileObject = open(directory + filename, 'r')
        #pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        #for i in range (0,pdfReader.numPages):
            #pageObj = pdfReader.getPage(i)

        all_text = '' # new line
        with pdfplumber.open(file) as pdf:
            # page = pdf.pages[0] - comment out or remove line
            # text = page.extract_text() - comment out or remove line
            for pdf_page in pdf.pages:
               single_page_text = pdf_page.extract_text()
               print( single_page_text )
               # separate each page's text with newline
               all_text = all_text + '\n' + single_page_text
            print(all_text)
            # print(text) - comment out or remove line
        # with pdfplumber.open(directory + filename, "r") as pdf:
        #     first_page = pdf.pages[0]
        #     text = first_page.extract_text()
        #     print(text)
            
        with open(directory + str(count) + filename.replace('.pdf', '.txt'), "w") as write_file:
            write_file.write(all_text)"""


"""import os
import pdfplumber
import PyPDF2

#count = 0
listfiles = os.listdir(r"E:\Plag_check\plag_check1")

for f in listfiles:
     if f.endswith(".pdf"):
         try:
             infile = pdfplumber.open(f, 'r')
             fnew=f.split(".")[0]
             outfile = open(fnew +'.txt', 'w')

             

             processed = infile.pages[0].extract_text()

             outfile.write(processed)

            
         except:
 
             print ('Error!')"""

""" import os
from os import chdir, getcwd, listdir, path
import codecs
import PyPDF2
from time import strftime

def check_path(prompt):
    ''' (str) -> str
    Verifies if the provided absolute path does exist.
    '''
    abs_path = raw_input(prompt)
    while path.exists(abs_path) != True:
        print "\nThe specified path does not exist.\n"
        abs_path = raw_input(prompt)
    return abs_path  

#print "\n"

folder = "E:/Plag_check/plag_check1/"

list=[]
directory=folder
for root,dirs,files in os.walk(directory):
    for filename in files:
        if filename.endswith('.pdf'):
            t=os.path.join(directory,filename)
            list.append(t)

m=len(list)
i=0
while i<=len(list):

    path=list[i]
    head,tail=os.path.split(path)
    var="\\"

    tail=tail.replace(".pdf",".txt")
    name=head+var+tail



    content = ""
    # Load PDF into pyPDF
    pdf = PyPDF2.PdfFileReader(files(path, "rb"))
    # Iterate pages
    for j in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(j).extractText() + "\n"
    print(strftime("%H:%M:%S"), " pdf  -> txt ")
    f=open(name,'w')
    #f.write(content.encode('UTF-8'))
    f.close
    i+=1 """
import time
from time import strftime

print(strftime("%H:%M:%S"))


 x = sample_pair
            range = (0, 100)
            bins = 10

            plt.hist(x, bins, range, color = 'green', histtype = 'bar', rwidth = 0.8) 

            plt.xlabel('Pair of Files')
# frequency label
            plt.ylabel('Plagiarism percentage')
# plot title
            plt.title('Plagiarsim histogram')
  
# function to show the plot
            plt.show()