from bs4 import BeautifulSoup
import requests

source = requests.get('https://command-center.support.aws.a2z.com/supportDashboard#/dashboard/?profileName=Linux&supportRegion=NA&supportType=PS')
print(source.text)