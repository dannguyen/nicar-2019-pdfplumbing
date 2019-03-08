# Using Python to help deal with PDFs (NICAR 2019)

This lesson focuses on the [pdfplumber library by jsvine](https://github.com/jsvine/pdfplumber) and its options for dealing with the complexities of PDFs. However, [Tabula](https://tabula.technology/) and [Camelot](https://camelot-py.readthedocs.io/en/master/) are also good options, with the latter arguably having more active development, along with extensive [documentation and comparisons](https://github.com/socialcopsdev/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools#pdfplumber).

For pdfplumber, Jeremy Singer-Vine has provided helpful examples which we'll be revisit in some detail today:

- [CA WARN](https://github.com/jsvine/pdfplumber/blob/master/examples/notebooks/extract-table-ca-warn-report.ipynb)
- [FBI Instant Criminal Background Sample](https://github.com/jsvine/pdfplumber/blob/master/examples/notebooks/extract-table-nics.ipynb)

Note: for non-trivial PDFs, there aren't any perfect solutions that don't require some work to fix up, even if you go the Python scripting route -- which, no matter how good pdfplumber gets, will always be more difficult than web-scraping. The [California WARN PDF](https://www.edd.ca.gov/jobs_and_training/Layoff_Services_WARN.htm) is one example where writing a PDF extraction routine in Python might be justified -- there's not a spreadsheet/CSV version of it already, and a reporter may want to automate the process.




## Examples

Examples of PDFs we'll try out are in the [pdfs](pdfs) directory.


### Class walkthrough starter

Looking at GSK Grants: [pdfs/in-class-gsk-grants.ipynb](pdfs/in-class-gsk-grants.ipynb)

Basic example of using pdf plumber and writing to CSV: [basic.py](basic.py)





