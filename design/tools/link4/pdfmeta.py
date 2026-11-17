# pdfmeta.py <pdf> <title>: sets the document title and author, and clears the browser user agent.
import sys
from pypdf import PdfReader, PdfWriter
p, t = sys.argv[1:3]
w = PdfWriter(clone_from=PdfReader(p))
w.add_metadata({'/Title': t, '/Author': 'Credalio design team', '/Creator': 'Credalio design team', '/Producer': 'Credalio'})
w.write(p)
