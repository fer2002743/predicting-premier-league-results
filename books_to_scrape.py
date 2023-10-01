url = "https://books.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


#geting all the links of all the categores
links = []
final_links = []
for link in soup.find_all("a"):
    getting_links = link.get("href")
    if "catalogue/category/books/" in getting_links:
        links.append(getting_links)
#now we need to create the links that will take me to each category
for link in links:
    new_link = "https://books.toscrape.com/" + link
    final_links.append(new_link)


#lists to store all the information gathered
books_ratings = []
books_titles = []
books_prices = []
stock_availability = []


#entering into each category to scrape all the data
for category in final_links:
    page = requests.get(category)
    soup = BeautifulSoup(page.text, "html.parser")
    #scraping all the info. of the initial page
    books = soup.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for elements in books:
        #selecting the rating
        rating_element = elements.select_one("p.star-rating")
        rating_class = rating_element["class"][1]
        rating = rating_class.lower()
        books_ratings.append(rating)
        #getting books titles
        title_of_the_book = elements.h3.a
        books_titles.append(title_of_the_book["title"])
        #getting prices
        price_book = elements.find("p", class_ = "price_color")
        books_prices.append(price_book.text)
        #stock availability
        availability = elements.find("p", class_ = "instock availability").text.strip()
        stock_availability.append(availability)

    #scraping in case there is more than just one page
    next_page = soup.find("li", class_ = "next")
    if next_page:
        number_of_pages = soup.find("li", class_ = "current")
        limit = number_of_pages.text.split()[-1]
        number_page = 2
        while number_page <= int(limit):
            #I need to get the category out of each link
            final_category = category.split("/")[-2]#getting the text of the category
            following_page = f"https://books.toscrape.com/catalogue/category/books/{final_category}/page-{number_page}.html"
            page1 = requests.get(following_page)
            soup1 = BeautifulSoup(page1.text, "html.parser")
            books = soup1.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            for elements in books:
                #geting the rating
                rating_element = elements.select_one("p.star-rating")
                rating_class = rating_element["class"][1]
                rating = rating_class.lower()
                books_ratings.append(rating)
                #getting books titles
                title_of_the_book = elements.h3.a
                books_titles.append(title_of_the_book["title"])
                #getting prices
                price_book = elements.find("p", class_ = "price_color")
                text_price_book = price_book.text
                books_prices.append(text_price_book)
                #stock availability
                availability = elements.find("p", class_ = "instock availability").text.strip()
                stock_availability.append(availability)
            number_page += 1


#storing the data acquired
df = pd.DataFrame(columns = ["Title", "Price", "Rating", "Availability"])
df["Title"] = books_titles
df["Price"] = books_prices
df["Rating"] = books_ratings
df["Availability"] = stock_availability


#creating the csv file
df.to_csv("books.csv")
