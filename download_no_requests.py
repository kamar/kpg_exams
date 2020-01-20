import os
import urllib.request
import urllib.parse
from kpglinks import languages


def download_files(*linkgroups):
    for group in linkgroups:
        try:
            grouplist = languages[group]
            for link in grouplist:
            
                directory = link.split('/')[-2]
                file_name = link.split('/')[-1]
                save_path = '{0}/{1}'.format(str(group), directory)
                new_file_path = os.path.join(save_path, file_name)
                link = urllib.parse.unquote(link)
                site = urllib.request.urlopen(link)
                r = site.info()
                block_size = 2048
                file_size = int(r.get('Content-Length'))
                file_seek = 0

                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                if not os.path.exists(new_file_path):
                    megethos_ak = 0
                    with open(new_file_path, "wb") as fh:
                        while True:
                            site.read(file_seek)
                            buffer = site.read(block_size)
                            if not buffer:
                                break
                            megethos_ak += len(buffer)
                            prcnt = (megethos_arxeiou_kt / file_size)
                            katastasi = "{0:>6,d}kb {1:.2%}".format(round(megethos_at/1024),\
                                                        prcnt)
                            katastasi = katastasi + " " + "=" * int(prcnt * 100 / 2) + ">"
                            print("Κατέβηκαν: {}".format(katastasi), end="\r")
        except:
            pass
        print()
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)
        download_files(*sys.argv[1:])
    else:
        download_files('spanish')