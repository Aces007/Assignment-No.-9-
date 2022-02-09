import json
from fpdf import FPDF

with open ('isapang.json', 'r') as f:
    pass

Resume = FPDF('P', 'mm', 'Letter')

Resume.set_auto_page_break(auto = True, margin = 15)

Resume.add_page()

Resume.set_font('times', '', 18)

Resume.cell(200, 25, txt = "Personal Resume", 
        ln = 1, align = 'C')
Resume.cell(200, 1, txt = "Polytechnic University of the Philippines", 
        align = 'C')

Resume.output('CLAVANO, ACE LAWRENCE.pdf')

