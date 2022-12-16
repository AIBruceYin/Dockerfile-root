import os
import time
import sys
from loguru import logger
logger.add(sys.stderr, format="{time:UTC} {level} {message}", filter="my_module", level="INFO")

sleep_time = 5

def string_func(p1):
    logger.info("I am bit dizzy will sleep for another {} seconds".format(sleep_time))
    time.sleep(sleep_time)
    logger.info("I woke up now, i am printing the value which you have sent me \n {}".format(p1))
    logger.info("Ok, i am going back to sleep for {} seconds. Invoke me again.".format(sleep_time))
    time.sleep(sleep_time)

def print_env_variables():
    logger.info("I am printing env variables for this container. \n  {}".format(os.environ))
    logger.info("sleeping for {} seconds again".format(sleep_time))
    time.sleep(sleep_time)

def write_to_file(file_name):
    logger.info("Storing environment variables in the file")
    dir_name = "root_dir"
    if not os.path.exists("/opt/{}".format(dir_name)):
        os.mkdir("/opt/{}".format(dir_name))
    with open("/opt/{}/{}".format(dir_name, file_name), "w") as f:
        f.write("{}".format(os.environ))
    logger.info("content of files are as follows")
    with open("/opt/{}/{}".format(dir_name, file_name), "r") as f:
        logger.info(f.read())

string_func("Test 1")
print_env_variables()
write_to_file("writing_to_file.txt")

string_func("Test 2")
print_env_variables()
write_to_file("writing_to_file_1.txt")

string_func("Test 3")
print_env_variables()
write_to_file("writing_to_file_2.txt")

temp = True
i = 1
while(temp):
    logger.info("Time is {}, iteration is --> {}".format(time.time(), i))
    i+=1
    time.sleep(5)
    if i == 1000:
        logger.info("I am done, stopping the container after 8 mins. Good bye :)")
        break
