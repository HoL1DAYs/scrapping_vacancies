import requests
from bs4 import BeautifulSoup as bs



def get_data(specialization, level_of_programming, programming_language):
    url = f'https://nofluffjobs.com/pl/{specialization}?lang=ru&utm_source=youtube&utm_medium=refferal&utm_campaign=itboroda&page=1&criteria=seniority%3Dtrainee,{level_of_programming}%20requirement%3D{programming_language}%20jobLanguage%3Den,ru'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'
    }



    req = requests.get(url=url, headers=headers)
    response = req.text
    with open(f'index_{programming_language}.html', 'w', encoding='utf-8') as file:
        file.write(response)
    with open(f'index_{programming_language}.html', encoding='utf-8') as file:
        src = file.read()

    soup = bs(src, 'lxml')

    vacancies = soup.find('div', class_='list-container ng-star-inserted').findAll('a')
    for vacancy in vacancies:
        try:
            title = vacancy.find('h3').text.strip()
            url = 'https://nofluffjobs.com' + vacancy.get('href')
            company = vacancy.find('div').findNext().find('span').text.strip()
            salary = vacancy.find('div').findNext().find('span').findNext().find('span').text.strip()
            print(title)
            print(salary)
            print(company)
            print(url)
        except AttributeError:
            pass


def main():
    get_data(specialization='fullstack', level_of_programming='junior', programming_language='java')
if __name__ == '__main__':
    main()