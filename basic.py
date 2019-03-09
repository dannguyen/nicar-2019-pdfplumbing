import csv
from pdfplumber import pdfplumber

IN_PATH = 'pdfs/funstuff.pdf'
OUT_PATH = '/tmp/funstuff-first-page.csv'

# open the pdf and get the pages
the_pdf = pdfplumber.open(IN_PATH)

# there's only one page, but .pages always returns a list
# even if that list just as one item
pages = the_pdf.pages
pg = pages[0]

# the function call that does most of the work
pg_table = pg.extract_table()

# open a file to write to:
out_file = open(OUT_PATH, 'w')
outc = csv.writer(out_file)
outc.writerows(pg_table)
out_file.close()
