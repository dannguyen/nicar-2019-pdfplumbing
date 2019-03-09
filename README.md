# Using Python to help deal with PDFs (NICAR 2019)

Presented by Dan Nguyen (@dancow on Twitter / dannguyen on Github)

> **Note:** 
>
> This Steven Rich tweet applies to this class: https://twitter.com/dataeditor/status/1103703146319142912 
> 
> For non-trivial PDFs, there aren't any perfect solutions that don't require some work to fix up, even if you go the Python scripting route -- which, no matter how good pdfplumber gets, will always be more difficult than web-scraping. The [California WARN PDF](https://www.edd.ca.gov/jobs_and_training/Layoff_Services_WARN.htm) is one example where writing a PDF extraction routine in Python might be justified -- there's not a spreadsheet/CSV version of it already, and a reporter may want to automate the process.




This lesson focuses on the [pdfplumber library by jsvine](https://github.com/jsvine/pdfplumber) and its options for dealing with the complexities of PDFs. However, [Tabula](https://tabula.technology/) and [Camelot](https://camelot-py.readthedocs.io/en/master/) are also good options, with the latter arguably having more active development, along with extensive [documentation and comparisons](https://github.com/socialcopsdev/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools#pdfplumber).

For pdfplumber, Jeremy Singer-Vine has provided helpful examples which we'll be revisit in some detail today:

- [CA WARN](https://github.com/jsvine/pdfplumber/blob/master/examples/notebooks/extract-table-ca-warn-report.ipynb)
- [FBI Instant Criminal Background Sample](https://github.com/jsvine/pdfplumber/blob/master/examples/notebooks/extract-table-nics.ipynb)


## Examples

Examples of PDFs we'll try out are in the [pdfs](pdfs) directory.


### Class walkthrough starter


Basic example of using pdf plumber and writing to CSV: [basic.py](basic.py)

[Quickie example on CA WARN pdf](pdfs/ca-warn-multipage.ipynb)


Looking at GSK Grants: [pdfs/in-class-gsk-grants.ipynb](pdfs/in-class-gsk-grants.ipynb)

- `pdftotext -layout`: [pdfs/gsk-grants-2017.txt](pdfs/gsk-grants-2017.txt)
- ABBYY result: [pdfs/abbyyfr-gsk-grants-2017.xlsx](pdfs/abbyyfr-gsk-grants-2017.xlsx)
- pdfplumber result: [pdfs/gsk-grants-pdfplumber-output.csv](pdfs/gsk-grants-pdfplumber-output.csv)

