import scrapy
import urlparse

class News(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    
#TODO analyse all urls and create a generic function to attend all if its possible

class G1Spider(scrapy.Spider):
    name = 'G1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/fato-ou-fake/'+'?sort=covid']

    def parse(self, response):
        self.log('ACESSANDO URL: %s' % response.url)
        build_full_url = lambda link: urlparse.urljoin(response.url, link)
        for qsel in response.css("#fato-ou-fake> div"):
            it = News()
            it['link'] = build_full_url(
                qsel.css('.summary h3 > a').xpath('@href')[0].extract())
            it['title'] = qsel.css('.summary h3 &amp;amp;amp;gt; a::text')[0].extract()
            it['content'] = qsel.css('a.post-tag::text').extract()
            it['date'] = qsel.css('div.excerpt::text')[0].extract()
            yield it
