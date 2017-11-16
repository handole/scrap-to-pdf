from bs4 import BeautifulSoup
import requests
import pdfkit

def scrape():
    p = []
    for page in range(0, 3):
        page = page + 1
        base_url = "https://simpleisbetterthancomplex.com/archive/"

        r = requests.get(base_url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_items = soup.find_all("div", {"class": "eight"})

        for item in all_items:
            d= {}

            item_name = item.find("a")
            item_link = 'https://simpleisbetterthancomplex.com/' + str(item_name.get('href'))
            item_name = item_name.text.replace('\n', "").strip()
            d['item_link'] = item_link
            d['item_name'] = item_name
            pdfkit.from_url(item_link, (item_name + '.pdf'))

            p.append(d)

    return p

if __name__ == '__main__':
    app.run(scrape)
