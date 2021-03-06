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
    'spanish': 'Ισπανικά',
    'turkish': "Τούρκικα"
}

t = []

fh = open("kpgexamslinks.rst", "w") 
fh.write("**Υπερσύνδεσμοι για τα αρχεία προηγούμενων εξετάσεων του ΚΠΓ.**\n")
fh.write('#'*len('**Υπερσύνδεσμοι για τα αρχεία προηγούμενων εξετάσεων του ΚΠΓ.**'))
fh.write('\n\n')

for k in languages.keys():
    t.append('{}_'.format(lang_description[k]))
fh.write(', '.join(t))
fh.write('\n\n\n')

for key in languages.keys():
    fh.write('.. _{}:\n\n'.format(lang_description[key]))

    kefalida = "**{}**".format(lang_description[key])
    fh.write(kefalida+'\n')
    fh.write('-'*len(kefalida))
    fh.write('\n\n')

    for link in languages[key]:
        fh.write("  - {}\n".format(link))
    fh.write("\n"*2)
fh.close()