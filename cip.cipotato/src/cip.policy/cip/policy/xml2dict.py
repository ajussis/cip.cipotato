import xml.etree.ElementTree as etree

categories = ["anual_report.xml", "brochures_fact_sheets.xml"]

for i in categories:
    tree = etree.parse(i)
    root = tree.getroot()

def xml_to_dict(el):
    d={}
    if el.text:
      d[el.tag] = el.text
    else:
      d[el.tag] = {}
    children = el.getchildren()
    if children:
      d[el.tag] = map(xml_to_dict, children)
    return d