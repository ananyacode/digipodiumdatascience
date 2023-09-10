import requests 
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from database import Article

def opendb():
    # mysql connection
    engine = create_engine('sqlite:///articles.db',echo = True)
    return sessionmaker(bind=engine)() # this is called a factor function

def get_page():
    try:
        url= 'https://blog.jetbrains.com/kotlin/'
        page = requests.get(url)
        if page.status_code == 200:
            print(f'{page.status_code} Success!')
            return BeautifulSoup(page.content,'html.parser')
        if page.status_code == 404:
            print(f'{page.status_code} Page Not Found')
        if page.status_code == 403:
            print(f'{page.status_code} Internal Server Error')
        if page.status_code == 500:
            print(f'{page.status_code} Unknown Error')
    except Exception as e:
        print(f'⚠️ Error: \n"{e}')

def get_articles(soup):
    target = soup.find('div', class_='row latest latest_posts_section')
    if target:
        print("Target section found!")
        articles = target.find_all('div',class_='col')
        if articles:
            print('articles found!')
            print(f'Total Articles:{len(articles)}')
            
            for item in articles:
                heading= item.find('h3')
                publish= item.find('time')
                summary= item.find('p')
                author = item.find('span')

                try:
                    article = Article(
                       title = heading.text,
                       author = author.text,
                       pub_date = publish['datetime'],
                       summary = summary.text,
                    )
                    db = opendb()
                    db.add(article)
                    db.commit()
                    db.close()
                except Exception as e:
                    print(f'Error: \n{e}')
        else:
            print('I am doing something wrong 🥲🥹')
    else:
        print('I am doing something wrong 🥲🤬')

soup = get_page()
if soup:
    get_articles(soup)
else:
    print('I am doing something wrong 🥲🥶')
