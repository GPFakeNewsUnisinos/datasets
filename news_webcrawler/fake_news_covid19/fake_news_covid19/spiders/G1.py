import scrapy
import csv

from fake_news_covid19.items import NewsItem

    
#TODO analyse all urls and create a generic function to attend all if its possible

class G1Spider(scrapy.Spider):
    name = 'G1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/fato-ou-fake/coronavirus'+'?sort=covid',
                  'http://g1.globo.com/fato-ou-fake/coronavirus'+'?sort=vacina']

   
    
    def parse(self, response):
        f= open('fake_news_covid19.csv', 'w', newline='', encoding='utf-8')
        w = csv.writer(f)
        self.log('ACESSANDO URL: %s' % response.url)
        for notice in response.css("div.feed-post"):
            link= notice.css('a.feed-post-link').xpath('@href')[0].extract()
            title = notice.css('div.feed-post-body-title a::text').extract()
           # author = notice.css()
            content = notice.css('div.feed-post-body-resumo::text').extract()
            #date = notice.css('div.excerpt::text')[0].extract()            
            mynews = NewsItem(link = link, title =  title, content = content)
            print(mynews)
        
        yield mynews
        w.writerow(mynews)
        w.close()
    
