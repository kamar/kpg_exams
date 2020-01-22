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


import os
import sys
import requests
from kpglinks import languages


def download_files(*linkgroups):
    """
    Downloads the practice papers from past exams KPG.
    linkgroups: The language or languages who files downloads.
    Example: download_files('german')
             download_files('spanish', 'english')
             download_files('all') -> Downloads all available files.
    """
    
    if 'all' in linkgroups:
        linkgroups = [k for k in languages.keys()]

    for group in linkgroups:
        try:
            grouplist = languages[group]
            for link in grouplist:
            
                directory = link.split('/')[-2]
                file_name = link.split('/')[-1]
                response = requests.head(link)
                d = response.headers
                r = requests.get(link)
                save_path = '{0}/{1}'.format(str(group), directory)
                new_file_path = os.path.join(save_path, file_name)
                file_size = d.get('content-length')

                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                if not os.path.exists(new_file_path) or check_same_file(file_size, \
                    local_file_size(new_file_path)) == False:
                    
                    print("Το αρχείο {} αποθηκεύεται.".format(new_file_path), end ="\r")
                    with open(new_file_path, "wb") as fh:
                        for chunk in r.iter_content(chunk_size=2048):
                            if chunk:
                                fh.write(chunk)
                else:
                    print("Το αρχείο {} υπάρχει ήδη.".format(new_file_path), end="\r")
                    continue
        except KeyError:
            print("Η γλώσσα ({}) που επιθυμείτε δεν υπάρχει.".format(group))
            print("Οι διαθέσιμες γλώσσες είναι:")
            for k in languages.keys():
                print(k)
        continue
    print()

#TODO: Move functions to another file and import them.
def check_same_file(remote_s_info, local_s_info):
    if remote_s_info == local_s_info:
        return True
    else:
        return False


def local_file_size(fname):
    """
    Returns the file size in bytes.
    If file doesn't exists, returns -1
    PARAMETERS:statinfo.st_size
        fname: The path of the file.
    """
    try:
        statinfo = os.stat(fname)
        return statinfo.st_size
    except FileNotFoundError:
        return -1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        download_files(*sys.argv[1:])
    else:
        download_files('chinese', 'german', 'english')