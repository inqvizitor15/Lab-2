import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()


dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
books_dict = ()

rez = []
for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Nominal':
                if int(child.firstChild.data) == 1:
                    flag = True
            if child.tagName == 'Name' and flag:
                rez.append(child.firstChild.data)
    flag = 0

print(rez)