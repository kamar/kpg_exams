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
import logging
import urllib.request
import urllib.parse
from stat import ST_SIZE
from kpglinks import languages


def download_files(*linkgroups):
    """
    Downloads the practice papers from past exams KPG.
    linkgroups: The language or languages who files downloads.
    Example: download_files('german')
             download_files('spanish', 'english')
             download_files('all') -> Downloads all available files.
    """

    logging.basicConfig(filename='kpglinks.log',format='%(levelname)s: %(asctime)s %(message)s', level=logging.WARNING)
    error_signal = False

    if 'all' in linkgroups:
        linkgroups = [k for k in languages.keys()]

    for group in linkgroups:
        try:
            grouplist = languages[group]
            for link in grouplist:
            
                try:
                    directory = link.split('/')[-2]
                    file_name = link.split('/')[-1]
                    save_path = 'pastpapers/{0}/{1}'.format(str(group), directory)
                    new_file_path = os.path.join(save_path, file_name)
                    link = urllib.parse.unquote(link)
                    site = urllib.request.urlopen(link)
                    r = site.info()
                    block_size = 2048
                    try:
                        file_size = int(r.get('Content-Length'))
                    except TypeError:
                        logging.warning("Ο σύνδεσμος {} δημιούργησε σφάλμα.".format(link))
                        error_signal = True
                        continue
                    file_seek = 0

                    if not os.path.exists(save_path):
                        os.makedirs(save_path)

                    if not os.path.exists(new_file_path) or check_same_file(file_size, \
                        local_file_size(new_file_path)) == False:
                        megethos_ak = 0
                        with open(new_file_path, "wb") as fh:
                            while True:
                                site.read(file_seek)
                                buffer = site.read(block_size)
                                if not buffer:
                                    break
                                megethos_ak += len(buffer)
                                fh.write(buffer)
                                prcnt = (megethos_ak / file_size)
                                katastasi = "{0:>6,d}kb {1:.2%}".format(round(megethos_ak/1024),\
                                                            prcnt)
                                katastasi = katastasi + " " + "=" * int(prcnt * 100 / 4) + ">"
                                print("{} κατέβηκαν: {}".format(file_name, katastasi), end="\r")
                                print(""*150, end="\r")
                    else:
                        print("Το αρχείο {} υπάρχει ήδη.".format(new_file_path))
                        continue        
                except urllib.error.HTTPError as e:
                    print(e)
                    print("Ο σύνδεσμος δεν καταλήγει σε αρχείο.\n({})".format(link))
                    logging.warning('{}: {}'.format(e, link))
                    error_signal = True
                    continue
        except KeyError:
            print("Η γλώσσα ({}) που επιθυμείτε δεν υπάρχει.".format(group))
            print("Οι διαθέσιμες γλώσσες είναι:")
            for k in languages.keys():
                print(k)
        except KeyboardInterrupt:
            print("\nΠατήθηκε Ctrl + C. Έξοδος")
            os.remove(new_file_path)
            sys.exit()
        print()
    if error_signal:
        print("Παρουσιάστηκαν σφάλματα. Παρακαλώ διαβάστε το αρχείο καταγραφών.")


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
        # print(sys.argv)
        download_files(*sys.argv[1:])
    else:
        print("Κατεβάζω όλα τα αρχεία.")
        download_files('all')