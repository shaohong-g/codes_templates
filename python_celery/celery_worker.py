# import json
import logging
import os
import uuid

from celery import Celery
from celery.schedules import crontab
from celery.signals import after_setup_logger
from celery.utils.log import get_task_logger

celery = Celery(f"app_{uuid.uuid4()}")

# Configure broker and backend
# # if .env file is in parent directory
# dir_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, dir_path)
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv(".env")
try:
    REDIS_HOST = os.environ["REDIS_HOST"]
    REDIS_PORT = os.environ["REDIS_PORT"]
    REDIS_DB =os.environ["REDIS_DB"]
except KeyError:
    raise Exception("Please set REDIS_HOST, REDIS_PORT, REDIS_DB in .env file")

celery.conf.broker_url = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
celery.conf.result_backend = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB )

# configure logger
from celery.signals import after_setup_task_logger
from celery.signals import after_setup_logger

@after_setup_logger.connect
@after_setup_task_logger.connect
def setup_loggers(logger, production=True, *args, **kwargs):
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(f"./celery.log")

    # Set level
    if production:
        logger.setLevel(logging.INFO)
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

    # Create formatters and add to handlers
    c_format = logging.Formatter('%(asctime)s::%(name)s::%(levelname)s - %(message)s', datefmt='%m-%d %H:%M:%S')
    f_format = logging.Formatter('%(asctime)s::%(name)s::%(funcName)s::%(lineno)d::%(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

logger = get_task_logger(__name__)

# configure queue
celery.conf.timezone = 'UTC'
celery.conf.update({
    'task_routes': {
        'scheduled_tasks': {'queue': 'scheduled_tasks'},
        'other_tasks': {'queue': 'other_tasks'},
        'test': {'queue': 'other_tasks'},
    }
})

# Tasks setup

@celery.task(name='scheduled_tasks')
def task1(max_number):
    """Given a random number, check if it is even or odd"""
    logger.info("This is task1")
    from random import randint

    num = randint(1, max_number)
    with open('output.txt', 'a') as f:
        f.write(f"{num % 2 == 0} {num}\n")

    if num % 2 == 0:
        logger.info("This is an EVEN number!")
    else:
        logger.info(f"This is an ODD number!")
    return num


@celery.task(bind=True, name="other_tasks")
def task2(self, df_dict):
    """Given a dataframe, print the dataframe"""
    logger.info("This is task2")
    import pandas as pd
    from IPython.display import display

    df = pd.DataFrame.from_dict(df_dict)
    display(df.head())
    return f"Length of df: {len(df)}"

@celery.task(bind=True, name="test")
def task3(self, x = None, y=None):
    """Given two numbers, check if x is greater than y"""
    logger.info("This is task3")
    if x == y:
        logger.info("x and y are equal")
    elif x > y:
        logger.info("x is greater than y")
        return True
    else:
        logger.info("x is less than y")
    return False

# Schedule set-up
# # https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
celery.conf.beat_schedule = {
    "every-one-minutes": {
        "task": f"scheduled_tasks",
        "schedule": crontab(minute='*/1'),
        'options': {'queue' : 'scheduled_tasks'},
        # 'kwargs': json.jumps({'max': 10})
        "args": (10,)
    }
}


if __name__ == "__main__":
    # Two ways of invoking celery asynchronously
    task1.apply_async(args=(10,))

    result = task1.delay(10)
    print(result.get())

    # print(__name__)
    # print(__file__)
    # print(os.path.dirname(os.path.realpath(__file__)))
    pass
