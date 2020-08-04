# This script only works if the IP assigned to the user is in the same range
# as this webserver. It should fail gracefully if the user is on an "invalid"
# IP range, but I haven't been able to test this functionality, yet.

from decimal import Decimal as d
from colors import red, green
from bs4 import BeautifulSoup as BS
from datetime import datetime
import re
import requests

ipurl = 'https://ifconfig.me/ip'
url = 'http://122.160.230.125:8080/gbod/'

ipdata = 'IP: {}'.format(requests.get(ipurl).text)

try:
    soup = BS(requests.get(url).text, "html.parser")

    # ASSIGNMENT
    dt = datetime.now().strftime("%H:%M:%S %B %d, %Y")
    days = soup.find("div", {"class": "DatablockSectionThird accordianblock"})
    days = int(days.text.strip()) + 1
    data = soup.find("div", {"class": "DatablockSectionSecond"}).text
    data = re.sub(' +', ' ', data)
    data = data.splitlines()[2].split()
    left = data[0]
    total = data[3]

    # MATH
    used = round(d(total) - d(left), 1)
    rollover = d(total) - 330
    perleft = round(d(left) / d(total) * 100, 1)
    perused = round(100 - perleft, 1)

    # FORMATTING
    bar = red("█"*int(round(perused, 0))) + green("█"*int(round(perleft, 0)))
    dt = '[{}]'.format(dt)
    days_left = '[{} days left]'.format(days)
    total = 'Total: {} GB'.format(total)
    used = 'Used: {} GB, {}%'.format(used, perused)
    left = 'Left: {} GB, {}%'.format(left, perleft)
    rollover = 'Rollover data: {} GB'.format(rollover)
    center = '{}, {}'.format(total, rollover)

    # ALIGNMENT
    str_1 = '{:<30}{:^40}{:>30}'.format(dt, ipdata, days_left)
    str_2 = '{:<30}{:^40}{:>30}'.format(used, center, left)

    # OUTPUT
    print('\n')
    print(str_1)
    print(bar)
    print(str_2)
except requests.exceptions.RequestException as err:
    print(ipdata)
    print("Error: {}".format(err))
