#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import csv, string, translitcodec

def all_staff_entries():
    data_initial = open("staff.csv", "r")
    data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",", quotechar = '"')
    ofile  = open('staffimport.csv', "w+")
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    m = 0
    row2 = ["_path","title","_type","firstname","lastname","head","position","joinedcip","section","subsection","leftcip","funded","joint","country","bio","email","areas","tel","skype","languages","publicationsout","publications","elsewhere"]
    #row2.append('"_path","title","_type","firstname","lastname","head","position","section","subsection","joinedcip","leftcip","funded","joint","country","bio","areas","email","tel","skype","languages","publications","elsewhere"')
    writer.writerow(row2)
    postemp = []
    path = ""
    type = "Person"
    firstname = ""
    lastname = ""
    position = ""
    startdate = ""
    leftdate = ""
    count = 0
    #print data
    for row in data:
        rowtemp = []
        for i in row:
            if m == 0:
                firstrow = []
                firstname = i.strip(" ").split(" ")
                for k in firstname:
                    ss = k.capitalize()
                    firstrow.append(ss)
                firstname = " ".join(firstrow)
                #firstname = firstname.encode("utf-8")
                firstname = unicode(firstname, "utf-8")
            elif m == 1:
                lastrow = []
                lastname = i.strip(" ").split(" ")
                for k in lastname:
                    #print k
                    #kk = unicode(k, "latin-1")
                    #print kk
                    #kk = kk.encode("utf-8")
                    k = unicode(k, "utf-8")
                    ss = k.capitalize()
                    lastrow.append(ss)
                lastname = " ".join(lastrow)
                path = "/about-cip/staff/%s-%s" % (firstname.encode("translit/short").strip(" ").replace(" ", "-").lower(), lastname.encode("translit/short").strip(" ").replace(" ", "-").lower())
                lastname = lastname.encode("utf-8")
                firstname = firstname.encode("utf-8")
                rowtemp.append(path)
                rowtemp.append("%s %s" % (firstname, lastname))
                rowtemp.append("Person")
                rowtemp.append(firstname)
                rowtemp.append(lastname)
                rowtemp.append("")
            elif m == 2:
                position = i.strip(" ").split(" ")
                postemp = []
                for k in position:
                    k = k.lower()
                    if "Ñ" in k:
                        k = k.replace("Ñ", "ñ")
                    if (k in ["ssa", "jpo", "cccap", "swca", "cip", "pc"]):
                        postemp.append(k.upper())
                    elif (k not in ["or", "and", "de", "y", "no"]):
                        postemp.append(k.capitalize())
                    else:
                        postemp.append(k)
                position = " ".join(postemp)

                rowtemp.append(position)
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
                    subsection = "Finances"
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
                    subsection = "Research Support - La Molina"
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
                    subsection = "Research Support - San Ramon"
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
                rowtemp.append(section)
                rowtemp.append(subsection)
            elif m == 4:
                try:
                    date = i.split("-")
                    startdate = date[2].split(" ")[0] + "/" + date[1] + "/" + date[0]
                    rowtemp.append(startdate)
                except:
                    continue
            elif m == 5:
                date = i.split("-")
                if (date[0] != 'NULL'):
                    leftdate = date[2].split(" ")[0] + "/" + date[1] + "/" + date[0]
                    rowtemp.append(leftdate)
                else:
                    leftdate=""
            elif m == 7:
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                if ("@" in i):
                    email = i.strip(" ").lower()
                    rowtemp.append(email)
                if ("@" not in i):
                    email = ""
                    rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                rowtemp.append("")
                """print "-" * 100
                print "_path:" + path 
                print "_type: Person"
                print "Firstname: %s" % (firstname)
                print "Lastname: %s" % (lastname)
                print "Position: %s" % (position)
                print "Startdate: %s" % (startdate)
                print "Enddate: %s" % (leftdate)
                print "Section: %s" % (section)
                print "Subsection: %s" % (subsection)
                print "Email: %s" % (email)
                count = count+1
                print count"""
            m = m + 1
        m = 0
        count += 1
        writer.writerow(rowtemp)
        #print rowtemp
    ofile.close()
    data = csv.reader(open("staffimport.csv", "rb"))
    #for i in data:
    #    print i
    

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

    

def get_staff_duplicates():
    """
    Find out if there are duplicate entries in the csv file. Looking for duplicate email addresses.
    """
    data = csv.reader(open("staff.csv", "rb"))
    ofile  = open('compares.csv', "wb")
    for row in data:
        m = 0
        data2 = csv.reader(open("staff.csv", "rb"))
        for i in data2:
            if ((i[7].lower() == row[7].lower()) and (row != i) and ("@" in i[7])):
                print i[7] #i[7].strip(" ").lower()
            
            #if ((row[0].split(" ")[0].lower() in i[0].lower()) and (row[1].split(" ")[0].lower() in i[1].lower()) and (row != i)):
            #    print row

def test_rows():
    """
    Just print the rows
    """
    data = csv.reader(open("staff.csv", "rb"))
    ofile  = open('testing.csv', "wb")
    writer = csv.writer(ofile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in data:
        row[1] = row[1] + "heiheihei"
        writer.writerow(row)
    ofile.close()
    data = csv.reader(open("testing.csv", "rb"))
    for i in data:
        print i

def main():
    print "hello"
    #get_staff_duplicates() # check for duplicate email addresses
    all_staff_entries() # list all entries 
    #test_rows()

if __name__ == '__main__':
    main()
