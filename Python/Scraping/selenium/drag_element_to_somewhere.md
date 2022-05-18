## 1. 代码如下

    #大牛测试：轻轻松松自动化
    #QQ:2574674466
    #专注自动化测试技术传播
    from selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    driver.get("https://passport.ctrip.com/user/reg/home")
    driver.find_element_by_css_selector("#agr_pop > div.pop_footer > a.reg_btn.reg_agree").click()

    sour = driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
    print(sour.size['width'])
    print(sour.size['height'])

    ele =driver.find_element_by_css_selector("#slideCode > div.cpt-drop-box > div.cpt-bg-bar")
    print(ele.size['width'])
    print(ele.size['height'])
    time.sleep(2)
    ActionChains(driver).drag_and_drop_by_offset(sour,ele.size["width"],0).perform()
