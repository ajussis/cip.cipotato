#!/usr/local/bin/python
# coding: utf-8
import csv, string
data = csv.reader(open("staff3.csv", "rU"), delimiter=";")
ofile  = open('persons.csv_NEW', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
m = 0
row2 = []
row2.append('"_path","title","_type","firstname","lastname","head","position","section","subsection","joinedcip","leftcip","funded","joint","country","bio","areas","email","tel","skype","languages","publications","elsewhere"')
rowtemp = []
postemp = []
path = ""
subsection = ""
type = "Person"
firstname = ""
lastname = ""
position = ""
startdate = ""
leftdate = ""
section = ""
subsection = ""
count = 0

for row in data:
    for i in row:
        if m == 0:
            firstname = i.strip(" ").split(" ")
            ff = 0
            for k in firstname:
                firstname[ff] = k.capitalize()
                ff += 1
            firstname = " ".join(firstname)
        elif m == 1:
            lastname = i.capitalize()
            path = "/about-cip/staff/%s-%s" % (firstname.strip(" ").replace(" ", "-").lower(), lastname.strip(" ").replace(" ", "-").lower())
            rowtemp.extend(path)
            rowtemp.extend("%s %s" % (firstname, lastname))
            rowtemp.extend("Person")
            rowtemp.extend(firstname)
            rowtemp.extend(lastname)
        elif m == 2:
            position = i.strip(" ").split(" ")
            postemp = []
            for k in position:
                k = k.lower()
                if (k not in ["or", "OR", "and", "AND"]):
                    postemp.append(k.capitalize())
                else:
                    postemp.append(k)
            position = " ".join(postemp)
            rowtemp.extend(position)
        elif m == 4:
            startdate = i.split("/")
            try:
                startdate = startdate[2]+"-"+startdate[0]+"-"+startdate[1]
            except:
                continue
        elif m == 5:
            leftdate = i.split("/")
            if (len(leftdate) == 3):
                leftdate = leftdate[2]+"-"+leftdate[0]+" "+leftdate[1]
        elif m == 6:
            section = ""
            subsection = ""
            i = i.strip(" ")
            if (i == "ACCOUNTING"):
                section = "Director General's office"
                subsection = i.capitalize()
            elif (i == "DIRECTOR GENERAL'S OFFICE"):
                section = "Director General's office"
                subsection = string.capwords(i)
            elif (i == "ACQUISITION & DISTRIBUTION UNIT"):
                section = "Director General's office"
                subsection = "Adquisition & Distribution Unit"
            elif (i == "COMMUNICATIONS & PUBLIC AWARENESS DEPARTMENT"):
                section = "Director General's office"
                subsection = "Communications and Public Awareness Department"
            elif (i == "ADMINISTRATION OFFICE"):
                section = "Director General's office"
                subsection = "Administration Office"
            elif (i == "AIR CONDITIONING"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "APPLIED BIOTECHNOLOGY LAB."):
                section = "Director General's office"
                subsection = "Division 3: Germplasm Enhancement and Crop Improvement"
            elif (i == "BUDGET"):
                section = "Director General's office"
                subsection = "Finances"
            elif (i == "BUILDING MAINTENANCE"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "GRANTS & CONTRACTS"):
                section = "Director General's office"
                subsection = "Grants and Contracts"
            elif (i == "FINANCES"):
                section = "Director General's office"
                subsection = "FINANCES"
            elif (i == "ENTOMOLOGY"):
                section = "Director General's office"
                subsection = "Division 4: Crop Management and Production Systems"
            elif (i == "DIVISION 4(Crop Management)"):
                section = "Divisions"
                subsection = "Division 4: Crop Management and Production Systems"
            elif (i == "DIVISION 4 (CROP MANAGEMENT& PROD. SYSTEMS"):
                section = "Divisions"
                subsection = "Division 4: Crop Management and Production Systems"
            elif (i == "DIVISION 5(Production Systems and the Environment)"):
                section = "Divisions"
                ssplit = i.split("(")
                ssplit[0] = ssplit[0].capitalize()
                ssplit[1] = ssplit[1].replace(")","")
                subsection = ": ".join(ssplit)
            elif (i == "DIVISION  1(Impact Enhancement)"):
                section = "Divisions"
                subsection = "Division 1: Social and Health Science"
            elif (i == "DIVISION 3(Genetic Enhancement & Crop Improvement"):
                section = "Divisions"
                subsection = "Division 3: Germplasm Enhancement and Crop Improvement"
            elif (i == "DIVISION 2 (Genetic Resources Conservation & Chara"):
                section = "Divisions"
                subsection = "Division 2: Genetic Resources"
            elif (i == "DIVISION 2 (GENETIC RESOURCES)"):
                section = "Divisions"
                subsection = "Division 2: Genetic Resources"
            elif (i == "DIVISION 6 (Agriculture and Human Health)"):
                section = "Divisions"
                subsection = "Division 1: Social and Health Science"
            elif (i == "DIVISION 1 (SOCIAL & HEALTH SCIENCES"):
                section = "Divisions"
                subsection = "Division 1: Social and Health Science"
            elif (i == "HUMAN RESOURCES"):
                section = "Director General's office"
                subsection = "Human Resources"
            elif (i == "LIASION OFFICE UGANDA"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Kampala, Uganda"
            elif (i == "RESEARCH INFORMATICS UNIT"):
                section = "Director General's office"
                subsection = "Research Informatics Unit"
            elif (i == "DEPUTY DIRECTOR GENERAL FOR RESEARCH OFFICE"):
                section = "Director General's office"
                subsection = "Deputy Director General's For Research"
            elif (i == "REGIONAL OFFICE INDIA"):
                section = "Regional offices - SWCA"
                subsection = "Regional Office, New Delhi, India"
            elif (i == "LIAISON OFFICE CHINA"):
                section = "Regional offices - ESEAP"
                subsection = "Liaison Office, Beijing, China"
            elif (i == "PAPA ANDINA/INCOPA"):
                section = "Partnership programs"
                subsection = "Papa Andina"
            elif (i == "VIROLOGY"):
                section = "Director General's office"
                subsection = "Division 4: Crop Management and Production Systems"
            elif (i == "PATHOLOGY"):
                section = "Director General's office"
                subsection = "Division 4: Crop Management and Production Systems"
            elif (i == "INFORMATION TECHNOLOGY UNIT"):
                section = "Director General's office"
                subsection = "Information Technology Unit"
            elif (i == "LODGING & FOOD SERVICES"):
                section = "Director General's office"
                subsection = "Lodging and Food Services"
            elif (i == "RESEARCH SUPPORT - Huancayo"):
                section = "Director General's office"
                subsection = "Research Support - Huancayo"
            elif (i == "SPECIAL PROJECTS"):
                section = "Director General's office"
                subsection = string.capwords(i)
            elif (i == "MALAWI'S OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Lilongwe, Malawi"
            elif (i == "WAREHOUSE"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "REGIONAL OFFICE INDONESIA"):
                section = "Regional offices - ESEAP"
                subsection = "Regional Office, Lembang, Indonesia"
            elif (i == "LIAISON OFFICE VIETNAM"):
                section = "Regional offices - ESEAP"
                subsection = "Liaison Office, Hanoi, Vietnam"
            elif (i == "ETHIOPIA OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Ethiopia"
            elif (i == "SECURITY"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "DORMITORIES"):
                section = "Director General's office"
                subsection = "Lodging and Food Services"
            elif (i == "MOZAMBIQUE OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Mozambique"
            elif (i == "ECUADOR LIAISON OFFICE"):
                section = "Regional offices - Latin America"
                subsection = "Liaison Office, Quito, Ecuador"
            elif (i == "TREASURY"):
                section = "Director General's office"
                subsection = "Finances"
            elif (i == "CONDESAN"):
                section = "Partnership programs"
                subsection = i
            elif (i == "ICRAF"):
                section = "Partnership programs"
                subsection = "ICRAF"
            elif (i == "DIRECTOR FOR FINANCE & ADMINISTRATION OFFICE"):
                section = "Director General's office"
                subsection = "Director Finance and Administration Office"
            elif (i == "SOUTH WEST & CENTRAL ASIA (SWCA)"):
                section = "Regional offices - SWCA"
                subsection = "Regional Office, New Delhi, India"
            elif (i == "EXECUTIVE ASSISTANT DG'S OFFICE"):
                section = "Director General's office"
                subsection = "Director General's office"
            elif (i == "UZBEKISTAN OFFICE"):
                section = "Regional offices - SWCA"
                subsection = "Liaison Office, Tashkent, Uzbekistan"
            elif (i == "COMPENSATION &BENEFITS"):
                section = "Director General's office"
                subsection = "Human Resources"
            elif (i == "REGIONAL OFFICE KENYA"):
                section = "Regional offices - SWCA"
                subsection = "Regional Office, New Delhi, India"
            elif (i == "MOTOR POOL & TRANSPORTATION"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "ELECTROMECHANIC/ELECTRONIC"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "RESEARCH SUPPORT - La Molina"):
                section = "Divisions"
                subsection = "Research Support ‚Äì La Molina"
            elif (i == "DEVELOPMENT"):
                section = "Director General's office"
                subsection = "Information Technology Unit"
            elif (i == "EXTERNAL RELATIONS & IRS"):
                section = "Director General's office"
                subsection = "External Relations"
            elif (i == "ALTAGRO PROJECT"):
                section = "Divisions"
                subsection = "ALTAGRO Project"
            elif (i == "SERVER ADMINISTRATION"):
                section = "Director General's office"
                subsection = "Information Technology Unit"
            elif (i == "HELPDESK"):
                section = "Director General's office"
                subsection = "Information Technology Unit"
            elif (i == "ANGOLA OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Huambo, Angola"
            elif (i == "REGIONAL OFFICE PHILIPPINES"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Huambo, Angola"
            elif (i == "GHANA OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Ghana"
            elif (i == "LOGISTICS UNIT"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "CAPACITY STRENGTHENING DEPARTMENT"):
                section = "Director General's office"
                subsection = "Communications and Public Awareness Department"
            elif (i == "VISITOR'S OFFICE"):
                section = "Director General's office"
                subsection = "Director General's office"
            elif (i == "SOCIAL WELFARE & HEALTH"):
                section = "Director General's office"
                subsection = "Human Resources"
            elif (i == "ANGOLA OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Huambo, Angola"
            elif ("RESEARCH SUPPORT - San Ram" in i):
                section = "Divisions"
                subsection = "Research Support ‚Äì San Ramon"
            elif (i == "PLUMBING"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "DESIGN & ART"):
                section = "Director General's office"
                subsection = "Communications and Public Awareness Department"
            elif (i == "MAINTENANCE"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "PURCHASING"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "LIBRARY"):
                section = "Director General's office"
                subsection = "Library"
            elif (i == "RECEPTION"):
                section = "Director General's office"
                subsection = "Logistics"
            elif (i == "BENIN OFFICE"):
                section = "Regional offices - SSA"
                subsection = "Liaison Office, Huambo, Angola"
            else:
                print ""
            print "-" * 100
            print "_path:" + path 
            print "_type: Person"
            print "Firstname: %s" % (firstname)
            print "Lastname: %s" % (lastname)
            print "Position: %s" % (position)
            print "Startdate: %s" % (startdate)
            print "Enddate: %s" % (leftdate)
            print "Section: %s" % (section)
            print "Subsection: %s" % (subsection)
            print i
            count = count+1
            print count
        m = m + 1
    writer.writerow(rowtemp)
    m = 0
