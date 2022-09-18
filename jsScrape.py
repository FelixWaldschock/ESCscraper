from collections import namedtuple
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

from Vehicle import Vehicle

vehicles = {}  # store the data

DRIVER_PATH = './chromedriver'  # chromedriver for Chrome 105
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


def getData(row) -> tuple:
    try:
        position = row.findChild("td", {"class": "rrc-position"}).text
        marker = row.findChild("td", {"class": "rrc-marker"}).text
        startnumber = row.findChild("td", {"class": "rrc-startnumber"}).text
        state = row.findChild("td", {"class": "rrc-state"}).text
        teamname = row.findChild("td", {"class": "rrc-name"}).text
        class_ = row.findChild("td", {"class": "rrc-class"}).text
        position_in_class = row.findChild(
            "td", {"class": "rrc-position_in_class"}).text
        hole = row.findChild("td", {"class": "rrc-hole"}).text
        diff = row.findChild("td", {"class": "rrc-diff"}).text
        lastroundtime = row.findChild(
            "td", {"class": "rrc-lastroundtime"}).text
        fastestroundtime = row.findChild(
            "td", {"class": "rrc-fastestroundtime"}).text
        fastestroundnumber = row.findChild(
            "td", {"class": "rrc-fastestroundnumber"}).text
        sectortimes1 = row.findChildren(
            "td", {"class": "rrc-sectortimes"})[0].text
        sectortimes2 = row.findChildren(
            "td", {"class": "rrc-sectortimes"})[1].text
        sectortimes3 = row.findChildren(
            "td", {"class": "rrc-sectortimes"})[2].text
        sectionmarker = row.findChild(
            "td", {"class": "rrc-sectionmarker"}).text
        car = row.findChild("td", {"class": "rrc-car"}).text

    except:
        print("Error: Could not get data")

    Data = namedtuple('data', 'position marker startnumber state teamname class_ position_in_class hole diff lastroundtime fastestroundtime fastestroundnumber sectortimes1 sectortimes2 sectortimes3 sectionmarker car')

    return Data(position, marker, startnumber, state, teamname, class_, position_in_class, hole, diff, lastroundtime,
                fastestroundtime, fastestroundnumber, sectortimes1, sectortimes2, sectortimes3, sectionmarker, car)


def scrapeAndAddData():
    driver.get('https://livetiming.getraceresults.com/zolder#screen-results')

    soup = bs(driver.page_source, "html.parser")

    table = soup.findChildren("table", {"class": "resultsGrid"})[0]
    # print(table)  # LOGclea

    # Get the tbody
    tbody = table.findChildren("tbody")[0]
    # print(tbody)  # LOG

    rows = tbody.findChildren(["th", "tr"])
    print("Found {} rows".format(len(rows)))
    # print(rows)  # LOG

    # Get the data
    rowNum = 0
    for row in rows:
        data = getData(row)

        # print("------Row {}------".format(rowNum))
        # print(data)  # LOG

        # Create a vehicle object
        id = data.startnumber  # Car ID
        if(id not in vehicles):
            vehicles[id] = Vehicle(
                id, data.car, data.teamname)

        vehicles[id].setTotalLaps(data.hole)
        vehicles[id].setLastLap(data.lastroundtime)
        vehicles[id].addToAllLapsTime(data.lastroundtime)
        # PIT ?
        vehicles[id].addToSectorTimes(
            data.sectortimes1, data.sectortimes2, data.sectortimes3)

        rowNum += 1


def main():
    try:
        while True:
            scrapeAndAddData()
            sleep(30)  # scrape every 30 seconds
    except KeyboardInterrupt:
        pass

    with open('output.txt', 'w') as f:
        for v in vehicles.values():
            f.write(str(v) + '\n')


if __name__ == '__main__':
    main()
