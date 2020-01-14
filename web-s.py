from bs4 import BeautifulSoup as bs
import requests as req
import csv

url_movies = 'https://www.ranker.com/list/best-1-word-title-movies/amylindorff'
url_sports = 'https://7esl.com/sports-and-games-vocabulary/'

movies_list = []
sports_list = []

def get_soup(url):
	results = req.get(url)
	soup = bs(results.text, "lxml")
	return soup

def get_word_list(genre_content):
	return_list = []
	for entry in genre_content:
		word = entry.text
		if word.endswith(' '):
			word = word[:-1]
		if ' ' in word:
			continue
		return_list.append((''.join(ch for ch in word if ch.isalnum())).lower())
	return return_list

def create_csv(genre, word_list):
	filename = genre + '.csv'
	with open(filename, 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(word_list)
    	

soup = get_soup(url_movies)
movies_content = soup.find_all('a', { "class" : "listItem__title listItem__title--link black"})
movies_list = get_word_list(movies_content)
create_csv('movies', movies_list)

soup = get_soup(url_sports)
sports_content = soup.find_all('h4')
sports_list = get_word_list(sports_content)
create_csv('sports', sports_list)



