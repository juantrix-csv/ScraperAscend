import requests
from bs4 import BeautifulSoup

BASE_URL = "https://wakomercadonatural.com/tienda/"


def fetch_products(page=1):
    url = BASE_URL
    if page > 1:
        url = f"{BASE_URL}page/{page}/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    products = []
    seen = set()
    for prod in soup.select("div.product-small"):
        name_el = prod.select_one("div.title-wrapper p.name a")
        price_el = prod.select_one("span.price span.woocommerce-Price-amount")
        if not (name_el and price_el):
            continue
        url = name_el.get("href")
        if url in seen:
            continue
        seen.add(url)
        name = name_el.get_text(strip=True)
        price = price_el.get_text(strip=True)
        products.append({"name": name, "price": price, "url": url})
    return products


def scrape_all_pages(max_pages=1):
    page = 1
    all_products = []
    while True:
        products = fetch_products(page)
        if not products:
            break
        all_products.extend(products)
        page += 1
        if max_pages and page > max_pages:
            break
    return all_products


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Scrape product prices")
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of pages to scrape (default: 1)",
    )
    args = parser.parse_args()

    products = scrape_all_pages(args.pages)
    for product in products:
        print(f"{product['name']} - {product['price']}")


if __name__ == "__main__":
    main()
