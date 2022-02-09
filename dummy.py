from ctypes import alignment
import json
from fpdf import FPDF

#PDF Format
pdf = FPDF('P', 'cm', 'A4') 
pdf.add_page()


#Read Informations
Curriculum_Vitae= open('isapang.json', 'r')
Curri_Vitae= Curriculum_Vitae.read()
Curriculum_Vitae.close()

#Informations
for BasicInfo in Curri_Vitae:
    pdf.set_font('times', 'B', 40)
    pdf.cell(18.5,1, f"{BasicInfo['Name']}", align= "C", ln=1)
    pdf.set_font('times', 'I', 12)
    pdf.cell(18.5,2, (BasicInfo['Age']), align= "C", ln=1)
    pdf.set_font('times', "B", 15)
    pdf.cell(5.25,1,"Personal Information", border= 1, ln=1)
    pdf.set_font('helvetica', "", 10)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Permanent Address: {BasicInfo['Address']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Email Address: {BasicInfo['Email']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Birthdate: {BasicInfo['Birthdate']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Gender: {BasicInfo['Sex']}",align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Hobbies: {BasicInfo['Hobbies']}", align="C", ln=1)
    pdf.cell(8.5,1,"", )
    pdf.cell(2,1, f"Civil Status: {BasicInfo['Civil Status']}", align="C", ln=1)
    pdf.set_font('times', "B", 15)
   
    pdf.cell(1.75,1,"Skills", border=1, ln=1)
    pdf.set_font('helvetica', "", 10)
    # for skills in Information_User ['skills']:
    #     pdf.cell(8.5,1,"", )
    #     pdf.cell(2,1, (skills), align="C", ln=1)
    # pdf.set_font('times', "B", 15)
   
    # pdf.cell(3.5,1,"Achievements", border=1, ln=1)
    # pdf.set_font('helvetica', "", 10)
    # for achievements in Information_User ['achievements']:
    #     pdf.cell(8.5,1,"", )
    #     pdf.cell(2,1, (achievements), align="C", ln=1)
    # pdf.set_font('times', "B", 15)
    # pdf.cell(6,1,"Educational Background", border=1, ln=1)
    # pdf.set_font('helvetica', "", 10)
    # for educationalbg in Information_User ['educationalbg']:
    #     pdf.cell(8.5,1,"", )
    #     pdf.cell(2,1, (educationalbg['School']), align="C", ln=1) 
    #     pdf.cell(8.5,1,"",)
    #     pdf.cell(2,1, (educationalbg['AcadYear']), align="C", ln=1) 

#PDF Maker
pdf.output('Murallos_SOLANA')



# # Calling font size for the header
# def Headerhehe():
#         Resume.set_font('times', 'B', 20)
#         Resume.cell(200, 25, txt = "Curriculum Vitae", 
#                 ln = 1, align = 'C')
#         Resume.set_font('times', '', 16)        
#         Resume.cell(200, 1, txt = "Polytechnic University of the Philippines", 
#                 align = 'C')