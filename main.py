from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(name='span', class_='titleline')
scores = soup.find_all(name='span', class_='score')

title_lst = []
url_lst = []
point_lst = [int(score.get_text().split()[0]) for score in scores]

for title in titles:
    title_lst.append(title.get_text())
    url_lst.append(title.find('a').get('href'))

highest_upvote_index = point_lst.index(max(point_lst))
print(title_lst[highest_upvote_index], url_lst[highest_upvote_index])
