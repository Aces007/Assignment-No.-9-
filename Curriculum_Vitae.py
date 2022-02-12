# Imports
import json
from fpdf import FPDF
from ctypes import alignment


# Calling PDF Generator, Rules, etc.
Resume = FPDF('P', 'mm', 'Letter')
Resume.set_auto_page_break(auto = True, margin = 15)
Resume.add_page()


# Reading
Curriculum_Vitae = open('SeanPaul.json', 'r')
Curri_Vitae = json.load(Curriculum_Vitae)
Curriculum_Vitae.close()


# Content section
for BasicInfo in Curri_Vitae:
        # First Four Lines (includes: NAME, PERMANENT ADDRESS, PHONE NUMBER, PERSONAL EMAIL, BIRTHDATE)
        Resume.set_font('times', 'B', 20)
        Resume.cell(270.5,10, f"{BasicInfo['Name']}", align= 'C', ln=True)
        Resume.set_font('times', '', 12)
        Resume.cell(290,5, f"Permanent Address: {BasicInfo['Permanent Address']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(230,8.8, f"{BasicInfo['Phone Number']}", align= 'C', ln=True)
        Resume.set_font('times', '', 12)
        Resume.cell(266.2,5, f"Email: {BasicInfo['Email']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(253.6,9, f"Birthdate: {BasicInfo['Birthdate']}", align= 'C', ln=1)
        Resume.ln (5)
        Resume.line(-1, 50, 10000, 0)


        # PERSONAL INFORMATION: (NICKNAME, AGE, WORK EMAIL, CIVIL STATUS, HOBBIES, SKILLS)
        Resume.set_font('times', 'B', 15)
        Resume.cell(69,5, "Personal Information", align= 'C', ln=1)
        Resume.ln (3)
        Resume.set_font('times', '', 12)
        Resume.cell(60.5,10, f"Nickname: {BasicInfo['Nickname']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(43.5,3.4, f"Age: {BasicInfo['Age']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(89.2,9.8, f"Work Email: {BasicInfo['WorkEmail']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(63.5,6, f"Civil Status: {BasicInfo['Civil Status']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(109.5,8.5, f"Hobbies: {BasicInfo['Hobbies']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(178.5,7.5, f"Skills: {BasicInfo['Skills']}", align= 'C', ln=1) 
        Resume.line(-2, 107, 110000, 100)


        # FAMILY INFORMATION: (FATHER:OCCUPATION, MOTHER:BUSINESS, BROTHER)
        Resume.set_font('times', 'B', 15)
        Resume.ln(8)
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
        Resume.ln(5.5)


        # EDUCATION: (TERTIARY, SECONDARY, PRIMARY)
        Resume.set_font('times', 'B', 15)
        Resume.cell(45,5, "Education", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(128.2, 18, f"Tertiary: {BasicInfo['Tertiary']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(115.2, 1.7, f"Secondary: {BasicInfo['Secondary']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(111.7, 18, f"Primary: {BasicInfo['Primary']}", align= 'C', ln=1)
        Resume.line(-2, 222, 110000, 158)
        Resume.set_font('times', 'B', 15)


        # WORK EXPERIENCE: (JOB, YEARS DONE, DESCRIPTION OF JOB)
        Resume.cell(61,8, "Work Experience", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(138,8, f"{BasicInfo['Work Experience']}", align= 'C', ln=1)
        Resume.set_font('times', '', 12)
        Resume.cell(138,8, f"{BasicInfo['Years']}", align= 'C', ln=1)
        Resume.set_font('times', 'BI', 13)
        Resume.cell(154,14, f"{BasicInfo['Description']}", align= 'C', ln=1) 


# PDF Name Format
Resume.output('CLAVANO, ACE LAWRENCE.pdf')