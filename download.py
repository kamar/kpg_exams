import os
import sys
import requests
from kpglinks import languages


def download_files(*linkgroups):
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

                if not os.path.exists(new_file_path):
                    
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


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        download_files(*sys.argv[1:])
    else:
        download_files('chinese', 'german', 'english')