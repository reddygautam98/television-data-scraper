import requests
from bs4 import BeautifulSoup
import time
import random
import csv
from datetime import datetime

def get_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    return headers

def scrape_amazon():
    # Create a list to store all products
    all_products = []
    
    try:
        time.sleep(random.uniform(1, 3))
        
        url = 'https://www.amazon.in/s?k=television+for+small+tv&i=computers'
        print("Making request...")
        
        session = requests.Session()
        response = session.get(
            url,
            headers=get_headers(),
            timeout=30
        )
        print(f"Response status code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: Got status code {response.status_code}")
            return
            
        print("\nParsing content...")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print("\nSearching for elements...")
        products = soup.select('div[data-asin]:not([data-asin=""])') or \
                  soup.find_all('div', {'data-component-type': 's-search-result'}) or \
                  soup.select('.s-result-item')
        
        print(f"Found {len(products)} products")
        
        if len(products) == 0:
            print("\nNo products found. Debug information:")
            print("Available classes in the page:")
            print([tag.get('class') for tag in soup.find_all(class_=True)[:5]])
            return
            
        print("\nExtracting product data...")
        for product in products:
            try:
                # Get product ASIN
                asin = product.get('data-asin', 'No ASIN found')
                
                # Multiple selectors for title
                title = product.select_one('.a-text-normal') or \
                        product.select_one('h2 a span') or \
                        product.select_one('h2')
                title_text = title.text.strip() if title else "No title found"
                
                # Multiple selectors for price
                price = product.select_one('.a-price-whole') or \
                        product.select_one('.a-price .a-offscreen')
                price_text = price.text.strip() if price else "No price found"
                
                # Multiple selectors for link
                link = product.select_one('h2 a') or \
                       product.select_one('a.a-link-normal')
                link_href = "https://www.amazon.in" + link['href'] if link and 'href' in link.attrs else "No link found"
                
                # Get ratings
                rating = product.select_one('.a-icon-star-small .a-icon-alt') or \
                        product.select_one('.a-icon-star .a-icon-alt')
                rating_text = rating.text.split()[0] if rating else "No rating found"
                
                # Get number of reviews
                reviews = product.select_one('.a-size-base.s-underline-text') or \
                         product.select_one('.a-size-base')
                reviews_text = reviews.text.strip() if reviews else "No reviews found"
                
                if title_text != "No title found" or price_text != "No price found":
                    product_data = {
                        'ASIN': asin,
                        'Title': title_text,
                        'Price': price_text.replace(',', ''),
                        'Rating': rating_text,
                        'Reviews': reviews_text,
                        'Link': link_href
                    }
                    all_products.append(product_data)
                
            except Exception as e:
                print(f"Error processing product: {e}")
                continue
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'amazon_products_{timestamp}.csv'
        
        # Save to CSV
        if all_products:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=all_products[0].keys())
                writer.writeheader()
                writer.writerows(all_products)
            print(f"\nData successfully saved to {filename}")
        else:
            print("\nNo products were collected to save")
                
    except requests.RequestException as e:
        print(f"Error making request: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return all_products

if __name__ == "__main__":
    print("Starting scraper...")
    products = scrape_amazon()
    print(f"\nTotal products scraped: {len(products)}")
    
    