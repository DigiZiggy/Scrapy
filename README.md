**Project title**

Program to crawl over https://ordi.eu website and scrape the site
for all the computers names, prices and product photos.

**Project description**

Task Create a Python spider for page:

https://ordi.eu/lauaarvutid?___store=en&___from_store=et (English)
or
https://ordi.eu/lauaarvutid (Estonian)

Grab all computers from all pages and create JSON file with attributes:
{Product name: '', Price: '', Picture href: ''}

You may use Scrapy library or Beautiful Soup library.

**Code Example**

Name of the Spider and URL to start crawling from
```angular2
name = "get_computers_spider"
    start_urls = ['https://ordi.eu/lauaarvutid?___store=en&___from_store=et']
```

If to look at the HTML of the page, we can see that each computer 
is specified with the class 'item'. Since we're looking for a class, 
we'd use .item for our CSS selector. 
All we have to do is pass that selector into the response object
```angular2
SET_SELECTOR = '.item'
```

Looping over the 'item' we can pass in selectors to locate wanted child elements,
in this case the name od product, price of the product and a picture
```angular2
NAME_SELECTOR = 'h2 a::text'
PRICE_SELECTOR = '.price-box span::text'
IMAGE_SELECTOR = '.product-image img::attr(src)'
```

After successfully extracted data from the initial page, we’re progressing 
past it to see the rest of the results. 
The whole point of a spider is to detect and traverse links to other pages 
and grab data from those pages too
```angular2
NEXT_PAGE_SELECTOR = '.next::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).get()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
```


**How to use?**

Install Scrapy crawler if you don't have it already
```angular2
cd Scrapy
pip install Scrapy
```

To run the program and write the result into file
```angular2
scrapy runspider -o result.json the_scraper.py
```

**Credits**

to lecturer Einar Kivisalu for the code snippets used within this program
https://enos.itcollege.ee/~eikivi/python/lecture5/scraper3.py

**License**

MIT © Sigrid Närep