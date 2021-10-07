from bs4 import BeautifulSoup
import requests
import openpyxl

excel =openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title ='Top 250 movies'
print(sheet.title)
sheet.append(['Rank','Movie Name','Year of Release','ImDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    # print(source.text)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    movies = soup.find('tbody', class_="lister-list").findAll('tr')
    # print(len(movies))

    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        # print(rank,name,year,rating)
        # break
        sheet.append([rank,name,year,rating])

except Exception as e:
    print(e)

excel.save("ImDB-Movie_rating.xlsx")
