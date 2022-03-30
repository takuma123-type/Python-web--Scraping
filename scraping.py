url_ec = 'https://scraping.official.ec/'
res =  requests.get(url_ec)
soup = BeautifulSoup(res.text, 'html.parser')