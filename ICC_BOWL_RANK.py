import bs4
import requests
import sqlite3

def BOWL(url):
    ICC_ODI_RANKING = sqlite3.connect('ICC_ODI_RANKING.db')
    curICC_ODI_RANKING = ICC_ODI_RANKING.cursor()
    curICC_ODI_RANKING.execute('''CREATE TABLE ICC_ODI_RANKING_BOWL (
            RANK INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT (60) NOT NULL,
            TEAM TEXT (10) NOT NULL,
            RATING TEXT,
            CAREER_BEST_RATING TEXT);''')

    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # Banner name rank 1

    name_list_1 = soup.select(".rankings-block__banner--name-large")
    team_list_1 = soup.select(".rankings-block__banner--nationality")
    rating_list_1 = soup.select(".rankings-block__banner--rating")
    career_best_list_1 = soup.select(".rankings-block__career-best-text")

    # non banner names starting from 2nd Rank
    name_list = soup.select(".name a")
    team_list = soup.select(".table-body__logo-text")
    rating_list = soup.select(".rating")
    career_best_list = soup.select(".table-body__cell.u-hide-phablet")

    final_name_list = name_list_1 + name_list
    final_team_list = team_list_1 + team_list
    final_rating_list = rating_list_1 + rating_list
    final_career_best_list = career_best_list_1 + career_best_list

    for x in range(len(final_name_list)):
        print(
            f'Rank: {str(x + 1)} Name: {final_name_list[x].text} || Team: {final_team_list[x].text.strip()} || Rating: {final_rating_list[x].text} ||  Season\'s Best: {final_career_best_list[x].text}')
        curICC_ODI_RANKING.execute(
            "INSERT INTO ICC_ODI_RANKING_BOWL(NAME,TEAM,RATING, CAREER_BEST_RATING) VALUES(?,?,?,?);", (
            str(final_name_list[x].text.strip()), str(final_team_list[x].text.strip()),
            str(final_rating_list[x].text.strip()), str(final_career_best_list[x].text.strip())))
        ICC_ODI_RANKING.commit()

