# Imports
import json
from fpdf import FPDF
from ctypes import alignment

# Calling PDF Generator, Rules, etc.
Resume = FPDF('P', 'mm', 'Letter')
Resume.set_auto_page_break(auto = True, margin = 15)
Resume.add_page()

# Reading
Curriculum_Vitae = open('isapang.json', 'r')
Curri_Vitae = json.load(Curriculum_Vitae)
Curriculum_Vitae.close()



# Content section
for BasicInfo in Curri_Vitae:
        Resume.set_font('times', 'B', 15)
        Resume.cell(77,5, "Personal Information", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(86.5,10, f"Name: {BasicInfo['Name']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(43.5,4, f"Age: {BasicInfo['Age']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(88,12, f"Email: {BasicInfo['Email']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(114.5,5, f"Permanent Address: {BasicInfo['Permanent Address']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(63.5,13, f"Civil Status: {BasicInfo['Civil Status']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(138.5,6, f"Hobbies: {BasicInfo['Hobbies']}", align= 'C', ln=1)
        Resume.cell (30)
        Resume.set_font('times', 'B', 15)
        Resume.cell(27,25, "Educational Background", align= 'C', ln=1)
        for EducBG in BasicInfo ['Education']:
                Resume.set_font('times', '', 12, )
                Resume.cell(140.5,9, f"Institution: {EducBG['Institution']}", align= 'C', ln=1)
                Resume.set_font('times', '', 12, )
                Resume.cell(165.5,9, f"School Year: {EducBG['A.Y']}", align= 'C', ln=1)
        

# PDF Name Format
Resume.output('CLAVANO, ACE LAWRENCE.pdf')



