import logging

class WriteLog:
    logging.basicConfig(filename="salaryLogs.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')


    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)