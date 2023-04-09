import requests as r
import re
from lxml import etree
from tortoise import Tortoise
import asyncio
import alpha.model as model
from alpha.config.tortoise import TORTOISE_ORM


# $(".wqxw_dl1 > a").each((idx, el) => {console.log(el.href)})
sites = [
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=244&id=34486",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=79&id=34485",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=79&id=34483",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=244&id=34484",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=79&id=34481",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=244&id=34480",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=207&id=34482",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=79&id=34478",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=79&id=34477",
    "http://www.eweiqi.com/index.php?m=content&c=index&a=show&catid=206&id=34476",
]
def getArticle(url):
    resp = r.get(url).text

    html = etree.HTML(resp)
    res = re.findall( r'<!--(.*?)-->',resp, re.S)

    blog = max(res, key=lambda x: sum([('\u4e00'<=ch<='\u9fff') for ch in x]))
    title = html.xpath("/html/body/div[2]/div[2]/div[2]/div/div/h3")[0].text
    return title, blog

async def init():
	await Tortoise.init(config=TORTOISE_ORM)
	await Tortoise.generate_schemas()
        
async def main():
    await init()
    for url in sites:
        title, blog = getArticle(url)
        await model.ArticleModel(
            title=title,
            content=blog,
        ).save()
        print("success")
    print("exit")
    exit(0)
if __name__ == "__main__":

    asyncio.run(
        main()
    )