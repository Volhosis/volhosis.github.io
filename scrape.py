from bs4 import BeautifulSoup
import requests, re, bs4

def get_directors():
    res = requests.get(f"https://www.theyshootpictures.com/gf1000_startinglist_table.php").text
    soup = BeautifulSoup(res, 'html.parser')

    directors = soup.find_all(class_="csv_column_4")
    positions = soup.find_all(class_="csv_column_1")
    countries = soup.find_all(class_="csv_column_6")

    dir_dict = {}

    for i in range(len(directors)):
        if directors[i].string not in dir_dict and countries[i].string:
            dir_dict[directors[i].string] = 0
        if directors[i].string in dir_dict and countries[i].string:
            dir_dict[directors[i].string] += 1/(int(positions[i].string))

    dir_list = sorted(dir_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(100):
        print(dir_list[i][0])

def get_movies():
    res = requests.get(f"https://www.theyshootpictures.com/gf1000_startinglist_table.php").text
    soup = BeautifulSoup(res, 'html.parser')

    movies = soup.find_all(class_="csv_column_3")
    countries = soup.find_all(class_="csv_column_6")
    years = soup.find_all(class_="csv_column_5")

    options = ["USA","UK","Australia","Ireland","Canada","New Zealand"]

    year_list = [x for x in range(1800,2022)]

    movie_list = []

    f = open("movie_list.txt", "w")

    for i in range(len(movies)):
        if (countries[i].string in options) & (years[i].string in str(year_list)):
            movie_list.append(movies[i].string + " (" + years[i].string + ")")
    for i in range(len(movie_list)):
        f.write(movie_list[i] + "\n")

    f.close()

def get_actors():
    res = requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=1").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=2").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=3").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=4").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=5").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=6").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=7").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=8").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=9").text + requests.get(f"https://www.imdb.com/list/ls041826871/?sort=list_order,asc&st_dt=&mode=detail&page=10").text
    res = res.replace("\r\n", "")
    actorRegex = re.compile(r'li_st_0">.+<')
    actors = actorRegex.findall(res)

    print(len(actors))

    act_dict = {}

    for i in range(len(actors)):
        if actors[i] not in act_dict:
            act_dict[actors[i]] = 0
        if actors[i] in act_dict:
            act_dict[actors[i]] += 1/(i+1)

    act_list = sorted(act_dict.items(), key=lambda x: x[1], reverse=True)

    for actor in act_list:
        print(actor)

def get_decades():
    res = requests.get(f"https://www.theyshootpictures.com/gf1000_startinglist_table.php").text
    soup = BeautifulSoup(res, 'html.parser')

    years = soup.find_all(class_="csv_column_5")
    positions = soup.find_all(class_="csv_column_1")
    countries = soup.find_all(class_="csv_column_6")

    options = ["Norway"]

    year_dict = {}

    for i in range(len(years)):
        if years[i].string[:3] not in year_dict and len(years[i].string) == 4 and countries[i].string in options:
            year_dict[years[i].string[:3]] = 0
        if years[i].string[:3] in year_dict and len(years[i].string) == 4 and countries[i].string in options:
            year_dict[years[i].string[:3]] += 1/(int(positions[i].string))

    year_list = sorted(year_dict.items(), key=lambda x: x[1], reverse=True)

    for decade in year_list:
        print(decade[0] + '0s : ' + decade[1])

def get_countries():
    res = requests.get(f"https://www.theyshootpictures.com/gf1000_startinglist_table.php").text
    soup = BeautifulSoup(res, 'html.parser')

    positions = soup.find_all(class_="csv_column_1")
    countries = soup.find_all(class_="csv_column_6")

    count_dict = {}

    for i in range(len(countries)):
        if countries[i].string not in count_dict:
            count_dict[countries[i].string] = 0
        if countries[i].string in count_dict:
            count_dict[countries[i].string] += 1/(int(positions[i].string))

    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    for country in count_list:
        print(country[0])

def get_artists():
    res = requests.get(f"http://acclaimedmusic.net/year/alltime_songs.htm").text
    soup = BeautifulSoup(res, 'html.parser')

    artistRegex = re.compile(r'..artist/.+\">(.+)<')
    positions = soup.find_all(class_="font12")
    artists = artistRegex.findall(res)

    art_dict = {}

    for i in range(len(artists)):
        if artists[i] not in art_dict:
            art_dict[artists[i]] = 0
        if artists[i] in art_dict:
            art_dict[artists[i]] += 1/(int(positions[i].string))

    art_list = sorted(art_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(100):
        print(art_list[i][0][:-4])

def get_authors():
    res = ''
    # for i in range(1, 28):
        # res += requests.get(f"https://thegreatestbooks.org/nonfiction?page=" + str(i)).text
    for i in range(1, 55):
        res += requests.get(f"https://thegreatestbooks.org/?page=" + str(i)).text
    soup = BeautifulSoup(res, 'html.parser')

    authorRegex = re.compile(r'/authors/.+\">(.+)<')
    positionRegex = re.compile(r'<h4>\s+\d+')
    positions = positionRegex.findall(res)
    authors = authorRegex.findall(res)

    aut_dict = {}

    for i in range(len(authors)):
        if authors[i] not in aut_dict:
            aut_dict[authors[i]] = 0
        if authors[i] in aut_dict:
            aut_dict[authors[i]] += 1/(int(positions[i][4:].strip()))

    aut_list = sorted(aut_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(102):
        print(aut_list[i][0])

get_movies()