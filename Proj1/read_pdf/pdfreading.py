import PyPDF2
from pypdf import PdfReader
import re


path_pdf = "C:\\Users\\e010846\\Downloads\\qaa.pdf"

reader = PdfReader(path_pdf)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

# print(text)
#extracting emails

rgx = r'(?:\.?)([\w\-_+#~!$&\'\.]+(?<!\.)(@|[ ]?\(?[ ]?(at|AT)[ ]?\)?[ ]?)(?<!\.)[\w]+[\w\-\.]*\.[a-zA-Z-]{2,3})(?:[^\w])'
matches = re.findall(rgx, text)
get_first_group = lambda y: list(map(lambda x: x[0], y))
emails = get_first_group(matches)
print(emails)