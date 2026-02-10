import random
import time

import httpx
from log import logger


def get_data():
    req_id = random.randint(0, 99)
    logger.info("获取的数据ID:%s" % req_id)
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/' + str(req_id)
    res = httpx.get(pokemon_url, timeout=30)
    res_data = res.json()
    logger.info("获取的name值:%s" % res_data['name'])
    return res_data


def save_data(data):
    filename = data['name'] + str(int(time.time())) + '.txt'
    file = open('./data/' + filename, 'w')
    file.write(str(data))
    logger.info("文件写入完成，文件名:%s" % filename)


if __name__ == '__main__':
    logger.info("爬虫程序开始执行")
    data = get_data()
    save_data(data)
    logger.info("爬虫程序执行完成")
