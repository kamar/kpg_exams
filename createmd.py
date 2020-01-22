###########################################################################
# KPG Past Exams Files Downoload
#    Copyright (C) <2020>  <Konstas Marmatakis> <email:marmako@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###########################################################################
from kpglinks import languages

lang_description = {
    'german': 'Γερμανικά',
    'english': 'Αγγλικά',
    'french': 'Γαλλικά',
    'italian': 'Ιταλικά',
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