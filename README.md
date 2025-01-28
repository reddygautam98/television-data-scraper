# 📺 Amazon TV Scraper  

## 🌟 Overview  
**Amazon TV Scraper** is a powerful Python-based web scraping solution designed to extract key product data from Amazon, such as pricing, ratings, and reviews. Leveraging **BeautifulSoup** and **Requests**, this tool automates data collection to deliver actionable insights for 📊 price comparison, 📈 market analysis, and 🛒 competitive intelligence.  

---

## 🛠️ Business Problem Addressed  
In today's fast-paced e-commerce landscape, businesses and consumers face:  
- 🚫 Difficulty in tracking real-time pricing trends for televisions and electronics.  
- 🕵️‍♂️ Inefficient manual efforts to gather detailed product information.  
- ⚖️ Inability to benchmark competitor pricing, reviews, and ratings effectively.  

**Amazon TV Scraper** solves these problems by:  
- 🏷️ Monitoring competitor prices for smarter marketing strategies.  
- 📖 Analyzing customer sentiment through product reviews to refine offerings.  
- 💡 Enabling curated price comparisons to elevate customer experience.  

---

## ✨ Features  
- 🔄 **Dynamic User-Agent Rotation**: Prevents blocking by simulating browser requests.  
- 🔍 **Flexible Data Extraction**: Scrapes ASIN, title, price, ratings, review count, and product links.  
- 🛡️ **Robust Error Handling**: Handles failed requests and ensures data quality.  
- 📂 **CSV Export**: Saves the extracted data in timestamped CSV files for easy analysis.  

---

## ⚙️ Technologies Used  
- 🐍 **Python**: Core programming language.  
- 🌐 **BeautifulSoup**: HTML parsing and DOM navigation.  
- 📡 **Requests**: HTTP requests with custom headers and timeouts.  
- 📋 **CSV Module**: Exports structured data for reporting.  

---

## 🚀 How It Works  
1. 🏁 **Initialization**: Scraper fetches data from Amazon's search results page.  
2. 🔄 **Header Randomization**: Rotates User-Agent headers to avoid detection.  
3. 📤 **Data Parsing**: Extracts product details like price, title, ratings, and reviews.  
4. ✅ **Validation**: Ensures the data is accurate and formatted for use.  
5. 💾 **Export**: Saves all product details into a timestamped CSV file.  

---

## 🖥️ Setup and Usage  

### 🛑 Prerequisites  
- 🐍 Python 3.7 or higher  
- 📦 Libraries: BeautifulSoup, Requests  

### 📥 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/amazon-tv-scraper.git
   cd amazon-tv-scraper
