import time
from selenium import webdriver
from cookieInjection import cookieInjection


def run(list, nowpage=0):
    if (nowpage > 1):
        nowpage = (nowpage - 1) * 29
    for x in range(0, len(list)):

        list[x].click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        print("已投递人数", (nowpage + (x+1)), "请及时给与别人回复")
        driver.implicitly_wait(3)
        if (driver.find_element_by_class_name('btn-container').text == '立即沟通'):
            driver.find_element_by_class_name('btn-container').click()
            try:
                if (driver.find_element_by_class_name("dialog-container")):
                    raise Exception("到达人数上限")
            except Exception as err:
                if (err.__str__() == "到达人数上限"):
                    print("汪")
                    raise
        driver.close()
        driver.switch_to.window(handles[0])
        driver.implicitly_wait(3)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhipin.com/")
driver.delete_all_cookies()
cookieInjection.Injection(driver)

driver.get(
    "https://www.zhipin.com/c101280600/d_202/?query=Java%E9%AB%98%E7%BA%A7%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&ka=sel-degree-202")

time.sleep(3)
run(driver.find_elements_by_class_name("job-primary"))


while (True):

    driver.find_element_by_class_name('next').click()
    run(driver.find_elements_by_class_name("job-primary"),eval(driver.find_element_by_class_name('page').find_element_by_class_name('cur').text))
    driver.implicitly_wait(3)
