# A python script that parses account names and email information from 
# HTML code (taken from iCloud's Hide My Email) and writes these to a CSV file.

from bs4 import BeautifulSoup
import csv

# Create a new soup object to use for parsing
with open("emails.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

# A list that holds service names (i.e. iCloud, Amazon, Adobe, etc.)
service_names = []
for service_name in soup.find_all("div", class_="card-title"):
    service_names += [service_name.string]

# A list that holds the respective email for a service
emails = []
for email in soup.find_all("div", class_="card-line"):
    emails += [email.string]

# Plop the service name and emails into a dictionary
accounts = {}
for i in range(len(emails)):
    key=service_names[i]
    value=emails[i]
    accounts[key]=value

# Write the accounts dictionary to a CSV file
print ("Writing to accounts.csv ...")
with open ("accounts.csv", 'w') as cf:
    csvwriter = csv.writer(cf)
    for account, email in accounts.items():
        csvwriter.writerow([account, email])
