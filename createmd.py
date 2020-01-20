from kpglinks import languages

lang_description = {
    'german': 'Γερμανικά',
    'english': 'Αγγλικά',
    'france': 'Γαλλικά',
    'italic': 'Ιταλικά',
    'spanish': 'Ισπανικά'
}

fh = open("kpgexamslinks.md", "w") 
fh.write("# Υπερσύνδεσμοι για τα αρχεία προηγούμενων εξετάσεων του ΚΠΓ.\n\n")

for key in languages.keys():
    fh.write("## {}\n\n".format(lang_description[key]))
    for link in languages[key]:
        fh.write("  - {}\n".format(link))
    fh.write("\n"*2)
fh.close()