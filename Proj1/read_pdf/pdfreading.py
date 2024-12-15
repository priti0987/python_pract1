import PyPDF2
from pypdf import PdfReader


path_pdf = "C:\\Users\\e010846\\Downloads\\PRITI BHUSHAN FUSE(E010846) (1).pdf"

reader = PdfReader(path_pdf)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)