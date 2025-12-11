import os
from pypdf import PdfWriter, PdfReader, generic

os.chdir(r"C:\Users\edoua_itw4d03\Documents\SIO SLAM première année\Mini-Entreprise\Python")

reader = PdfReader('output2.pdf')
writer = PdfWriter()


for page in reader.pages:
    writer.add_page(page)

if "/AcroForm" in reader.trailer["/Root"]: #/AcroForm contient tous les formulaires du doc | .trailer = les infos essentielles du pdf, accompagné de root qui contient toute les infos du pdf.
    writer._root_object.update({ #créer le root du pdf final et le met à jour avec .update
        generic.NameObject("/AcroForm"): reader.trailer["/Root"]["/AcroForm"] #convertit une tring python pour qu'elle soit compatible pdf. | reader.trailer prend toute les infos du pdf d'origine
    })
    writer._root_object["/AcroForm"].update({generic.NameObject("/NeedAppearances"): generic.BooleanObject(True)})#needappearances remplace le /V generic.BooleanObject(True) sert à y appliquer true et donc afficher les champs.

fields = reader.get_fields() #créer un dictionnaire avec tous les noms des champs
field_values = {name: name for name in fields.keys()} 

for page in writer.pages:
    writer.update_page_form_field_values(page, field_values) #remplace tous les champs par le nom du champ.

with open('output.pdf', 'wb') as f: #créer le pdf
    writer.write(f)
