import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber
from time import strftime
import matplotlib.pyplot as plt

import time
# with pdfplumber.open("sample.pdf") as pdf, open('sample.txt', 'a') as out_file:
#     first_page = pdf.pages[0]
#     txt_file = first_page.extract_text()
#     out_file.write(txt_file)
    
# with pdfplumber.open("sample2.pdf") as pdf, open('sample2.txt', 'a') as out_file:
#     first_page = pdf.pages[0]
#     txt_file = first_page.extract_text()
#     out_file.write(txt_file)

#def get_timestamp():
    #t = time.localtime()
    #print(time.strftime('%Y-%m-%d %H:%M:%S', t))

t1 = int(round(time.time() * 1000))


count = 0
directory = "E:/Plag_check/plag_check1/"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    #filename = file.decode("utf-8")
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
               #print( single_page_text )
               # separate each page's text with newline
               all_text = all_text + '\n' + single_page_text
            #print(all_text)
            # print(text) - comment out or remove line
        # with pdfplumber.open(directory + filename, "r") as pdf:
        #     first_page = pdf.pages[0]
        #     text = first_page.extract_text()
        #     print(text)
            
        with open(directory + str(count) + filename.replace('.pdf', '.txt'), "w", encoding = "ISO-8859-1", errors="ignore") as write_file:
            write_file.write(all_text)


sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
sample_contents = [open(File).read() for File in sample_files]
 
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
 
vectors = vectorize(sample_contents)
s_vectors = list(zip(sample_files, vectors))
 
def check_plagiarism():
    results = set()
    global s_vectors
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = (similarity(text_vector_a, text_vector_b)[0][1])*100
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], abs(sim_score)
            results.add(score)    
             
    return results
    
    


t2 = int(round(time.time() * 1000))



for data in check_plagiarism():
    #print(strftime("%H:%M:%S"), " pdf  -> txt ")
    
    print(data)    
print (((t2-t1)/1000))

    
 