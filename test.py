############################################
# Test install_local_packages
############################################
# from TestPackage.one import *
# print(test_function()) # test_function
# test_data_files() # display dataframe from test.csv

# from TestPackage.two import *
# two_instance = two_another_test()
# print(two_instance.print()) # Printing attribute: two_attribute
# print(two_instance.print_other()) # Printing attribute: attribute

############################################
# logger
############################################
# import logger.loggerUtil
# logger = logger.loggerUtil.get_logger(production=True)

# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")

############################################
# Celery
############################################
# try:
#     from python_celery.celery_worker import *
# except:
#     from dotenv import load_dotenv
#     load_dotenv("python_celery/.env")
#     from python_celery.celery_worker import *

# print("starting celery task3")
# x = task3.delay(x=1, y=2)
# print(x.get())

# print("starting celery task1")
# y = task1.delay(20)
# print(y.get())

# print("starting celery task2")
# import pandas as pd 
# df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
# df_dict = df.to_dict(orient="records")
# x = task2.delay(df_dict)
# print(x.get())

############################################
# Alembic
############################################
import json
try:
    from python_alembic.models import db_session, Sample_table
except:
    from dotenv import load_dotenv
    load_dotenv("python_alembic/.env")
    from python_alembic.models import db_session, Sample_table

db = db_session.session_factory() # start session instance
json_ob = {
    "1": 123,
    "city": [1,2,"123"]
}
add_obj = Sample_table(username="test", input=json_ob)
db.add(add_obj)
db.commit()
db.refresh(add_obj)

selected_id = add_obj._getdict()["id"]
x = db.query(Sample_table).get(selected_id)
y = x._getdict()["input"]
print(type(y))
print(json.dumps(y, indent=4, sort_keys=True))

x.username = "test2"
db.commit()