import requests
from bs4 import BeautifulSoup as bs


# def saveHTML(html, filename):
#     with open(filename, 'w') as f:
#         f.write(html)


# URL = "https://livetiming.getraceresults.com/zolder"
URL = "https://livetiming.getraceresults.com/demo#screen-results"

CLASS_NAMES = ["rrc-name", "rrc-team", "rrc-laps", "rrc-last-lap",
               "rrc-lap-times", "rrc-lap-pits", "rrc-sector-times"]

data = []


# Get the HTML from the page
r = requests.get(URL)

if (r.status_code != 200):
    print("Error: Could not get page")
    exit(1)

# Safe code:
# saveHTML(r.text, "page.html")

# Parse the HTML
soup = bs(r.text, "html.parser")
# print(soup.prettify()) #LOG

# Get the table
table = soup.findChildren("table", {"class": "resultsGrid"})[0]
print(table)  # LOG

# Get the tbody
tbody = table.findChildren("tbody")[0]
# print(tbody)  # LOG

rows = tbody.findChildren(["th", "tr"])
print("Found {} rows".format(len(rows)))
print(rows)  # LOG

# Get the data
# for row in rows:
# TODO

# def main():
#     r_current = requests.get(URL).__hash__()

#     while True:
#         r = requests.get(URL)

#         if r.__hash__() != r_current:
#             print("Page has changed")
#             r_current = r.__hash__()
#             getTables()

#         print("Page has not changed")


# if __name__ = "__main__":
#     main()
