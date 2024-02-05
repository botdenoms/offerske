import scrapy

from offerske.items import OfferskeItem


class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["www.jumia.co.ke"]
    start_urls = ["https://www.jumia.co.ke/flash-sales/"]

    def parse(self, response):
        productsurls = response.css('article.prd._fb._p.col.c-prd > a::attr(href)').extract()
        if productsurls:
            for prd in productsurls:
                yield response.follow(prd, callback=self.product_page_handler)

        # next_page = response.xpath('//ul[@class="pages"]/li[@class="next"]/a')
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

    def product_page_handler(self, response):
        item = OfferskeItem()
        item['url'] = response.url
        item['name'] = response.css('h1.-fs20.-pts.-pbxs::text').get()
        item['offer'] = response.css('span.-b.-ltr.-tal.-fs24.-prxs::text').get()
        item['price'] = response.css('span.-tal.-gy5.-lthr.-fs16.-pvxs::text').get()
        item['off'] = response.css('span.bdg._dsct._dyn.-mls::text').get()
        items_left = response.css('span.-fsh0.-prs.-fs12::text').get()
        item['left'] = items_left.split(" ")[0]
        item['thumb'] = response.css('div.sldr._img._prod.-rad4.-oh.-mbs').css('a::attr(href)').get()

        item['description'] = response.css('div.markup.-mhm.-pvl.-oxa.-sc *::text').extract()
        item['images'] = response.css('div.markup.-mhm.-pvl.-oxa.-sc').css('img::attr(src)').extract()

        specs = response.css('div.card-b.-fh') # list of items
        if specs and len(specs) == 3:
            item['features'] = specs[0].css('h2::text').get()
            item['features_items'] = specs[0].css('div.markup.-pam *::text').extract()
            item['box'] = specs[1].css('h2::text').get()
            item['box_items'] = specs[1].css('div.markup.-pam *::text').extract()
            # 3rd items // specifications
            item['specs'] = specs[2].css('h2::text').get()
            temp = []
            spcs = specs[2].css('ul *::text').extract()
            for i in range(0, len(spcs), 2):
                temp.append(spcs[i] + spcs[i + 1])
            item['specs_items'] = temp

        # verrts = response.css('h2.-fs14.-m.-upp.-pvm::text').get() # opt 1
        rts = response.css('p.-fs16.-pts::text').get() # opt 2
        item['ratings'] = rts.split(" ")[0]
        item['stars'] = ''.join(response.css('div.-fs29.-yl5.-pvxs *::text').extract())
        yield item
