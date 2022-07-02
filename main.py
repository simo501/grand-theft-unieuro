
from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve)

# url di esempio:      https://tracking.unieuro.it/?t=42638303

url = "https://tracking.unieuro.it/?t="
pagine_snz_tracking = 0

print("\n\n\ncaricamento gtu...")


for x  in range(30000000, 50000000):
    pgs_source = bs(urlopen(url + str(x)))

    if "Ops!" in str(pgs_source):
        print("analisi url -> " + url + str(x))
        print("[ nessun tracking per quest'ordine ]")
        pagine_snz_tracking =+ 1
    else:
        print("\n\n\nanalisi url -> " + url + str(x))
        print("\n\n###########\t" + pgs_source.select_one("span.panel-order__header-subTitle").text)
        print("###########\t" + pgs_source.select_one("span.track-date").text + "\n\n")

  