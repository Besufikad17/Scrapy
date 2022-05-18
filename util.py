from selenium import webdriver

path = "/home/besufikad/Documents/chromedriver"
driver = webdriver.Chrome(path)


def get_lyrics(link):
    driver.get(link)
    try:
        l = driver.find_element_by_class_name('poem')
        return l.text
    except:
        pass
