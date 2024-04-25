import scrapy


class XiaomiSpider(scrapy.Spider):
    name = "Xiaomi"
    start_urls = ["https://lojamidobroficial.com/collections/smartphones"]

    def parse(self, response):
        nm = []
        for i in response.css('.col-lg-3'):
            name = i.css('.product-title span::text').get()
            nm.append(name)
            for y in range(len(nm)):
                x = nm[y].split()
                result = ' '.join(x)
                yield{
                    'Nome Do Produto' : result,
                    'Valor do produto' : i.css('.price-box span:nth-child(1)::text').get()
                }
            
            
        




           
            

      
      
      
      
      
      
      
      
      
      
      
        