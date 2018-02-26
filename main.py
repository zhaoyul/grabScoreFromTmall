from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




browser = webdriver.Chrome()

urls = {
        "海尔官方旗舰店": 'https://haier.tmall.com',
        "GREE格力官方旗舰店": 'https://gree.tmall.com',
        "美的官方旗舰店": 'https://midea.tmall.com',
        #"海信冰洗官方旗舰店": 'https://hisensebx.tmall.com',
        "TCL官方旗舰店": 'https://tcldq.tmall.com',
        #"创维官方旗舰店": 'https://skyworth.tmall.com',
        #"三星官方旗舰店": 'https://samsung.tmall.com',
        "西门子家电官方旗舰店": 'https://siemens-home.tmall.com',
        "松下电器旗舰店": 'https://panasonic.tmall.com',
        "康佳官方旗舰店": 'https://konka.tmall.com',
        "方太官方旗舰店": 'https://fotile.tmall.com',
        "三洋官方旗舰店": 'https://sanyo.tmall.com',
        "荣事达官方旗舰店": 'https://royalstar.tmall.com',
        "夏普官方旗舰店": 'https://sharp.tmall.com',
        "LG官方旗舰店": 'https://lg.tmall.com',
        "新飞官方旗舰店": 'https://frestech.tmall.com',
        "美菱旗舰店": 'https://meilingdq.tmall.com',
        "小天鹅官方旗舰店": 'https://littleswan.tmall.com',
        "容声官方旗舰店": 'https://ronshen.tmall.com',
        "格兰仕官方旗舰店": 'https://galanz.tmall.com',
        "奥马官方旗舰店": 'https://homa.tmall.com'
}

def wuliu_score(name, desc):
    import re

    wuliumatchObj = re.search(u'物流.*', desc)
    wuliu_text = wuliumatchObj.group()
    score_search = re.search(u'([0-9.]+)分', text)
    score = score_search.group(1)
    status = '持平'
    status_scroe = '0.0%'
    compare = re.search(u'持平', wuliu_text)
    if(compare):
        status = '持平'
        status_scroe = '0.0%'
    else:
        compare = re.search(u'(高|低)([0-9.%]+)', wuliu_text)

        status = compare.group(1)
        status_scroe = compare.group(2)

    print(name, score, status, status_scroe)


def grab(name, url):
    try:
        browser.get(url)
    except Exception:
        pass
        #print (url + ":loading timeout")

    wait = WebDriverWait(browser, 10)
    top_bar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'main-info')))

    #top_bar = browser.find_element_by_class_name("main-info")
    action = ActionChains(browser)
    action.move_to_element(top_bar).perform()
        #print (url + ": find element timeout")

    meta = browser.find_element_by_name("description")
    store_desc = meta.get_attribute('content')

    wuliu_score(name,store_desc)


    origin_image = name + ".png"

    browser.get_screenshot_as_file(origin_image)

    from PIL import Image
    croped_image = "croped"+ name + ".png"
    img = Image.open(origin_image)
    img2 = img.crop((0, 0, 1300, 900))
    img2.save(croped_image)

# from IPython.display import Image
# Image(filename='haier1.png')


for name,url in urls.items():
    grab(name, url)

