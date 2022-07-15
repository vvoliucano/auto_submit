# -*- coding: utf-8
from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options
from argparse import ArgumentParser
from func import *
import warnings
import sys
import os
import re
import random
warnings.filterwarnings('ignore')

# reason = "其他必要事项", start = "燕园", end = "校外（社会面）", gate = "东南门", reason_detail = "科研", country = "中国", province = "北京市", city = "市辖区", district = "海淀区", track = "海淀路", jiedao = "海淀街道"

def go(config):
    conf = ConfigParser()
    conf.read(config, encoding='utf8')

    reason, start, end, gate, reason_detail, country, province, city, district, jiedao, track, wechat = dict(conf['common']).values()

    reason_detail = random.choice(reason_detail.split("，"))
    print(reason_detail)

    gate = random.choice(gate.split('，'))
    print(gate)

    track = random.choice(track.split('，'))

    print(track)
    print(reason, start, end, gate, reason_detail, country, province, city, district, jiedao, track, wechat)

    run(driver_pjs, argconf.ID, argconf.PASSWORD, reason, start, end, gate, reason_detail, country, province, city, district, jiedao, track)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--ID', type=str)
    parser.add_argument('--PASSWORD', type=str)
    # parser.add_argument('--MAIL_ADDRESS', type=str)
    # parser.add_argument('--PHONE_NUMBER', type=str)
    # parser.add_argument('--SENDKEY', type=str)
    argconf = parser.parse_args()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_pjs = webdriver.Edge(
            options=chrome_options,
            executable_path='/usr/bin/chromedriver',
            service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    # driver_pjs = webdriver.Chrome(
    #         options=chrome_options,
    #         executable_path='/usr/bin/chromedriver',
    #         service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    # driver_pjs = webdriver.Chrome()

    print('Driver Launched\n')

    go('config.ini')

    driver_pjs.quit()

