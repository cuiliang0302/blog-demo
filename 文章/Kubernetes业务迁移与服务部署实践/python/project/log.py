import os.path
from loguru import logger

info_log = os.path.join("./log", "info.log")
# logger配置
config = {
    "rotation": "00:00",  # 每天0点生成新文件
    "encoding": "utf-8",
    "retention": "7 days",
    "backtrace": True,  # 异常回溯
    "diagnose": True
}
logger.add(info_log, level='INFO', **config)