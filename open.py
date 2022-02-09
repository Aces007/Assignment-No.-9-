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
        Resume.set_font('times', 'B', 17)
        Resume.cell(66.5,10, f"{BasicInfo['Name']}", align= 'C', ln=True)
        Resume.set_font('times', '', 12)
        Resume.cell(102,5, f"Permanent Address: {BasicInfo['Permanent Address']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(42,9, f"{BasicInfo['Phone Number']}", align= 'C', ln=True)
        Resume.set_font('times', '', 12)
        Resume.cell(76,5, f"Email: {BasicInfo['Email']}", align= 'C', ln=1)
        Resume.ln (12)
        Resume.line(-1, 45, 10000, 0)
        Resume.set_font('times', 'B', 15)
        Resume.cell(69,5, "Personal Information", align= 'C', ln=1)
        Resume.ln (3)
        Resume.set_font('times', '', 12)
        Resume.cell(60.5,10, f"Nickname: {BasicInfo['Nickname']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(43.5,3.4, f"Age: {BasicInfo['Age']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(92.5,9.8, f"Work Email: {BasicInfo['WorkEmail']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(63.5,6, f"Civil Status: {BasicInfo['Civil Status']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(109.5,8.5, f"Hobbies: {BasicInfo['Hobbies']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(178.5,7.5, f"Skills: {BasicInfo['Skills']}", align= 'C', ln=1) 
        Resume.line(-2, 107, 110000, 100)
        Resume.set_font('times', 'B', 15)
        Resume.ln(10)
        Resume.cell(64,5, "Family Information", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(77.2, 18, f"Father: {BasicInfo['Father']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(78.2, 1.7, f"Occupation: {BasicInfo['Occupation']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(80.2, 18, f"Mother: {BasicInfo['Mother']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(72.5, 1.7, f"Business: {BasicInfo['Business']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(79.2, 18, f"Brother: {BasicInfo['Brother']}", align= 'C', ln=1)
        Resume.line(-2, 176, 110000, 130)
        

# PDF Name Format
Resume.output('CLAVANO, ACE LAWRENCE.pdf')



