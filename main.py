import requests
from bs4 import BeautifulSoup

links = []

limit_sq_price = int(input("What is the max price per square meter you are "
                       "willing to pay in forints?: "))


page_number = 1

headers = {
"User-Agent": "Mozilla/5.0"
}

while page_number < 5:
    try:
        url = "https://ingatlan.com/lista/elado+lakas+gyor?page=" + \
              str(page_number)
        response = requests.get(url, headers=headers)
        page = response.text

        soup = BeautifulSoup(page, "html.parser")
        listings = soup.find_all(name="div", class_="listing js-listing")
        for listing in listings:
            sq_price = listing.find(name="div", class_="price--sqm").getText().split()
            sq_price.remove('Ft/m2')
            sq_price = int("".join(sq_price))
            if sq_price < limit_sq_price:
                link = (listing.find(name="a"))
                links.append("https://ingatlan.com" + link["href"])
        page_number = page_number+1
    except:
        pass

import smtplib

contents = ""
# my_email = "SENDEREMAIL"
# password = "SENDERPASSWORD"

for link in links:
    contents = contents + link + "\n"

contents = contents + f"number of results: {len(links)}"


message = f"Subject: Real estate near you\n\n{contents}"

# connection = smtplib.SMTP("YOURSMTP")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="RECEIVEREMAIL",
#                     msg=message)

print(message)
# connection.close()






