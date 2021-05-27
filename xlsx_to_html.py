# approach 1
# xlsx2html directly converts the table as it is to html. This is faster and looks more neat.
from xlsx2html import xlsx2html

xlsx2html('/home/adminp/Documents/NLP/sample.xlsx', '/home/adminp/Documents/NLP/output.html')
# approach 2
# We can use pandas when the excel sheet has no empty rows or columns as they are represented by NaN values

import pandas as pd  # need to install 'pip install openpyxl'

wb = pd.read_excel('/home/adminp/Documents/NLP/sample.xlsx') # This reads in your excel doc as a pandas DataFrame
wb.to_html('/home/adminp/Documents/NLP/sample_output.html')



