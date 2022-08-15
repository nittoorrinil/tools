import pikepdf
import os

path = "C://Users/user/Desktop/Newfolder"   #Path where source pdfs are stored
pdf_path = 'C://Users/user/Desktop/Newfolder/'  #Path where source pdfs are stored
pdf_loc2 = 'C://Users/user/Desktop/NewFolder2/'  #Path where pdfs after password removal are stored
pdf_pass = 'PASSWORD'   #PDF's password
dir_list = os.listdir(path)

for i in dir_list:
    print ((pdf_path) + i)
    pdf = pikepdf.open((pdf_path) + i, password=pdf_pass)
    pdf.save(pdf_loc2 + '\\' + i)
