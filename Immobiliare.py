import requests, bs4, pandas, time

def print_results():
    frame = {'Title': title, 'Price': price, 'Description': par}
    data = pandas.DataFrame(frame)
    data.to_excel(f'immobiliare {city}.xlsx', index=False)
    new_search = input('\n\nWould you scrape another site? ("yes" to continue) \n').lower()

    if new_search == 'yes':
        print()
        start()

    else:
        print('\nGoodbye!')
        time.sleep(3)
        exit()


def check(website):
    page_check = website.find('div', {'class': "in-pagination__item in-pagination__item--disabled"})

    if page_check is not None and page_check.text == 'Successiva':
        print_results()

    else:
        index = int(website.find('div', {"class": "in-pagination__item in-pagination__item--current"}).text)
        next_ = bs4.BeautifulSoup(requests.get(f'https://www.immobiliare.it/affitto-case/{city}/?criterio=rilevanza&pag={index + 1}').content, 'html.parser')
        crawl(next_)


def crawl(website):
    t, pr, p = [], [], []

    for i in website.findAll('a', {"class": "in-card__title"}):
        new = bs4.BeautifulSoup(requests.get(i['href']).content, 'html.parser')
        t.append(new.find('span', {'class': "im-titleBlock__title"}))
        pr.append(new.find('div', {'class': "im-mainFeatures__title"}))
        p.append(new.find('div', {'class': "im-description__text js-readAllText"}))

    for i in range(len(t)):
        title.append(t[0].text.replace('\n', '').strip()) if t[0] is not None else title.append('N/A'), t.pop(0)
        price.append(pr[0].text.replace('\n', '').strip()) if pr[0] is not None else price.append('N/A'), pr.pop(0)
        par.append(p[0].text.replace('\n', '').strip()) if p[0] is not None else par.append('N/A'), p.pop(0)

    print(f'Page {website.find("div", {"class":"in-pagination__item in-pagination__item--current"}).text} completed')
    check(website)


def immobiliare(locality):
    global title, price, par, city

    city = locality
    title, price, par = [], [], []
    connect_city = requests.get(f'https://www.immobiliare.it/affitto-case/{city}/?criterio=rilevanza').content
    scrape = bs4.BeautifulSoup(connect_city, 'html.parser')
    crawl(scrape)


title, price, par = [], [], []
city = ''

