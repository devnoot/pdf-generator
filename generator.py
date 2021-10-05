from fpdf import FPDF
from random import randrange
from random import getrandbits

import lorem

# Get a random boolean
def get_random_boolean():
    return bool(getrandbits(1))

# Create 5 PDFs with random data
for i in range(5):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Randomly give PDF a title
    if get_random_boolean():
        pdf.set_title(lorem.sentence())

    # Randomly set the subject
    if get_random_boolean():
        pdf.set_subject(lorem.sentence())

    pages = randrange(1, 20)

    pdf.cell(200, 10, txt="Hello World! %s" % randrange(1, 100), ln=1, align="C")

    # Add a random number of pages
    for j in range(pages):
        pdf.add_page()
        pdf.write(10, lorem.paragraph())

    pdf.output("mypdf-%s.pdf" % i)
