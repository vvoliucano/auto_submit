from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib.parse import quote
from urllib import request
import os
import time
import warnings
import json
import random
warnings.filterwarnings('ignore')


def login(driver, userName, password, retry=0):
    if retry == 3:
        raise Exception('门户登录失败')

    print('门户登陆中...')

    appID = 'portal2017'
    iaaaUrl = 'https://iaaa.pku.edu.cn/iaaa/oauth.jsp'
    appName = quote('北京大学校内信息门户新版')
    redirectUrl = 'https://portal.pku.edu.cn/portal2017/ssoLogin.do'

    driver.get('https://portal.pku.edu.cn/portal2017/')
    driver.get(
        f'{iaaaUrl}?appID={appID}&appName={appName}&redirectUrl={redirectUrl}')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'logon_button')))
    driver.find_element(By.ID, 'user_name').send_keys(userName)
    time.sleep(0.1)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(0.1)
    driver.find_element(By.ID, 'logon_button').click()
    try:
        WebDriverWait(driver,
                      10).until(EC.visibility_of_element_located((By.ID, 'all')))
        print('门户登录成功！')
    except:
        print('Retrying...')
        login(driver, userName, password, retry + 1)


def go_to_simso(driver):
    button = driver.find_element_by_id('all')
    driver.execute_script("$(arguments[0]).click()", button)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'tag_s_stuCampusExEnReq')))
    driver.find_element(By.ID, 'tag_s_stuCampusExEnReq').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-card__body')))



def go_to_application_new(driver):
    go_to_simso(driver)
    driver.find_element(By.CLASS_NAME, 'el-card__body').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))
    
    time.sleep(7)
    driver.find_element(By.CLASS_NAME, 'el-dialog__body').find_element(By.CLASS_NAME, 'el-button--primary').click()


def go_to_application_out(driver):
    go_to_simso(driver)
    driver.find_element(By.CLASS_NAME, 'el-card__body').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))


def go_to_application_in(driver, userName, password):
    driver.back()
    time.sleep(0.5)
    driver.back()
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-card__body')))
        time.sleep(0.5)
        driver.find_element(By.CLASS_NAME, 'el-card__body').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))
    except:
        print('检测到会话失效，重新登陆中...')
        login(driver, userName, password)
        go_to_simso(driver)
        driver.find_element(By.CLASS_NAME, 'el-card__body').click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-select')))

# def 

def select_reason_new(driver, reason):
    driver.find_element(By.CLASS_NAME, 'el-select').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{reason}"]')))
    driver.find_element(By.XPATH, f'//li/span[text()="{reason}"]').click()


def select_choose(driver, idx = 1, text = "燕园"):
    driver.find_elements(By.CLASS_NAME, 'el-select')[idx].click()
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, f'//li/span[text()="{text}"]')))
    
    print(text)
    time.sleep(2)

    all_possible = driver.find_elements(By.XPATH, f'//li/span[text()="{text}"]')
    
    for element in all_possible:
        try:
            element.click()
        except:
            continue

    
    # all_dropdown = driver.find_elements(By.TAG_NAME, "li")

    # print(len(all_dropdown))

    # for i, element in enumerate(all_dropdown):
    #     print(i, element.get_attribute("innerText"))
    
    # for i, element in enumerate(all_dropdown):
    #     if (element.get_attribute("innerText") == text):
    #         try:
    #             element.click()
    #         except:
    #             continue

    # # driver.find_element(By.XPATH, f'//li/span[text()="{text}"]').click()

def select_in_out(driver, way):
    driver.find_element(By.CLASS_NAME, 'el-select').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{way}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{way}"]').click()


def select_campus_new(driver, campus):
    driver.find_elements(By.CLASS_NAME, 'el-select')[1].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{campus}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{campus}"]').click()

    

def select_campus(driver, campus):
    driver.find_elements_by_class_name('el-select')[1].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{campus}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{campus}"]').click()

    
def write_reason(driver, reason):
    driver.find_elements_by_class_name('el-select')[2].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{reason}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{reason}"]').click()
    
    
def select_destination(driver, destination):
    driver.find_elements_by_class_name('el-select')[3].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{destination}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{destination}"]').click()


def select_district(driver, district):
    driver.find_elements_by_class_name('el-select')[4].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li/span[text()="{district}"]')))
    driver.find_element_by_xpath(f'//li/span[text()="{district}"]').click()


def write_mail_address(driver, mail_address):
    driver.find_elements_by_class_name('el-input__inner')[2].clear()
    driver.find_elements_by_class_name('el-input__inner')[2].send_keys(
        f'{mail_address}')
    time.sleep(0.1)


def write_phone_number(driver, phone_number):
    driver.find_elements_by_class_name('el-input__inner')[3].clear()
    driver.find_elements_by_class_name('el-input__inner')[3].send_keys(
        f'{phone_number}')
    time.sleep(0.1)
    
    
def write_reason_detail(driver, detail):
    driver.find_element_by_class_name('el-textarea__inner').send_keys(
        f'{detail}')
    time.sleep(0.1)


def write_track(driver, track):
    driver.find_elements_by_class_name('el-textarea__inner')[1].send_keys(
        f'{track}')
    time.sleep(0.1)


def write_street(driver, street):
    driver.find_elements_by_class_name('el-textarea__inner')[1].send_keys(
        f'{street}')
    time.sleep(0.1)


def click_check(driver):
    driver.find_element_by_class_name('el-checkbox__label').click()
    time.sleep(0.1)


def click_inPeking(driver):
    driver.find_element_by_class_name('el-radio__inner').click()
    time.sleep(0.1)


def submit(driver):
    driver.find_element_by_xpath(
        '//button/span[contains(text(),"保存")]').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '(//button/span[contains(text(),"提交")])[3]')))
    driver.find_element_by_xpath(
        '(//button/span[contains(text(),"提交")])[3]').click()
    time.sleep(0.1)


def fill_out(driver, campus, mail_address, phone_number, reason, detail, destination, track):
    print('开始填报出校备案')

    print('选择出校/入校    ', end='')
    select_in_out(driver, '出校')
    print('Done')

    print('选择校区    ', end='')
    select_campus(driver, campus)
    print('Done')

    print('填写邮箱    ', end='')
    write_mail_address(driver, mail_address)
    print('Done')

    print('填写手机号    ', end='')
    write_phone_number(driver, phone_number)
    print('Done')

    print('填写出入校事由    ', end='')
    write_reason(driver, reason)
    print('Done')
    
    print('填写出入校事由详细描述    ', end='')
    write_reason_detail(driver, detail)
    print('Done')

    print('选择出校目的地    ', end='')
    select_destination(driver, destination)
    print('Done')

    print('填写出校行动轨迹    ', end='')
    write_track(driver, track)
    print('Done')

    click_check(driver)
    submit(driver)

    print('出校备案填报完毕！')

def fill_new(driver, reason = "其他必要事项", start = "燕园", end = "校外（社会面）", gate = "东南门", reason_detail = "科研", country = "中国", province = "北京市", city = "市辖区", district = "海淀区", track = "海淀路", jiedao = "海淀街道"):
    print('开始填报入校备案')

    print('选择原因   ', end='')
    select_reason_new(driver, reason)
    print('Done')
    time.sleep(0.3)

    print('选择起点   ', end='')
    select_choose(driver, 1, start)
    # select_campus_new(driver, "万柳园区")
    time.sleep(0.3)
    
    select_choose(driver, 2, end)
    time.sleep(0.3)

    select_choose(driver, 3, gate)
    time.sleep(1.4)

    driver.find_elements(By.CLASS_NAME, 'el-textarea__inner')[0].send_keys(
        reason_detail) # 出入校具体事项
    time.sleep(0.4)

    select_choose(driver, 4, country)
    time.sleep(1.4)

    select_choose(driver, 5, province)
    time.sleep(1.4)

    select_choose(driver, 6, city)
    time.sleep(1.4)

    select_choose(driver, 7, district)
    time.sleep(1.4)


    driver.find_elements(By.CLASS_NAME, 'el-textarea__inner')[1].send_keys(
        track) # 详细轨道
    time.sleep(0.4)

    driver.find_elements(By.CLASS_NAME, 'el-input__inner')[9].clear()
    driver.find_elements(By.CLASS_NAME, 'el-input__inner')[9].send_keys(
        jiedao) # 街道
    time.sleep(1)
    
    submit(driver)


    print('Done')

def screen_capture(driver, path):
    driver.back()
    time.sleep(0.5)
    driver.back()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'el-card__body')))
    driver.find_elements_by_class_name('el-card__body')[1].click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(text(),"已提交")]')))
    driver.maximize_window()
    time.sleep(0.1)
    driver.save_screenshot(os.path.join(path, 'result.png'))
    print('备案历史截图已保存')


def wechat_notification(userName, sckey):
    with request.urlopen(
            quote('https://sctapi.ftqq.com/' + sckey + '.send?title=成功报备&desp=学号' +
                  str(userName) + '成功报备',
                  safe='/:?=&')) as response:
        response = json.loads(response.read().decode('utf-8'))
    # if response['error'] == 'SUCCESS':
    #     print('微信通知成功！')
    # else:
    #     print(str(response['errno']) + ' error: ' + response['errmsg'])


def run(driver, userName, password, reason, start, end, gate, reason_detail, country, province, city, district, jiedao, track):


    login(driver, userName, password)
    print('=================================')

    go_to_application_new(driver)

    fill_new(driver, reason, start, end, gate, reason_detail, country, province, city, district, track, jiedao)

    # if capture:
    #     screen_capture(driver, path)
    #     print('=================================')

    # if wechat:
    #     # wechat_notification(userName, sckey)
    #     print('发送微信通知')
    #     print('=================================')

    print('报备成功！\n')


if __name__ == '__main__':
    pass
