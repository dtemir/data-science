import scrapy
import re

BASE_URL = 'http://en.wikipedia.org'


class NWinnerItemBio(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
    mini_bio = scrapy.Field()
    image_urls = scrapy.Field()
    bio_image = scrapy.Field()
    images = scrapy.Field()


class NWinnerSpiderBio(scrapy.Spider):
    """ Scrapes the Nobel prize biography pages for portrait images and a biographical snippet """

    name = 'nwinners_minibio'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        "http://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country?"
    ]

    custom_settings = {
        'ITEM_PIPELINES': {'nobel_winners.pipelines.NobelImagesPipeline': 1},
    }

    def parse(self, response):
        filename = response.url.split('/')[-1]
        h3s = response.xpath('//h3')

        for h3 in h3s:
            country = h3.xpath('span[@class="mw-headline"]/text()').extract()
            if country:
                winners = h3.xpath('following-sibling::ol[1]')
                for w in winners.xpath('li'):
                    wdata = {}
                    wdata['link'] = BASE_URL + w.xpath('a/@href').extract()[0]
                    print(wdata)
                    request = scrapy.Request(wdata['link'],
                                             callback=self.get_mini_bio,
                                             dont_filter=True)
                    request.meta['item'] = NWinnerItemBio(**wdata)
                    yield request


    def get_mini_bio(self, response):
        BASE_URL_ESCAPED = 'http:\/\/en.wikipedia.org'
        item = response.meta['item']
        # cache image
        item['image_urls'] = []

        # Get the URL of the winner's picture, contained in the infobox table
        img_src = response.xpath('//table[contains(@class,"infobox")]//img/@src')
        if img_src:
            item['image_urls'] = ['http:' + img_src[0].extract()]
        mini_bio = ''
        # Get the paragraphs in the biography's body-text
        ps = response.xpath('//*[@id="mw-content-text"]/div/p[text() or  normalize-space(.)=""]').extract()

        # Add introductory biography paragraph (only the first one)
        mini_bio += ps[1]

        # correct for wiki-links
        mini_bio = mini_bio.replace('href="/wiki', 'href="' + BASE_URL + '/wiki')
        mini_bio = mini_bio.replace('href="#', 'href="' + item['link'] + '#')
        item['mini_bio'] = mini_bio
        yield item