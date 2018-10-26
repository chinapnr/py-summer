from fishbase import logger as log
from application.controller.helloController import get_hello_content


class Hello:
    @staticmethod
    def get():
        return_data = get_hello_content()
        log.info("retuen data: {0}".format(return_data))
        return return_data, 200
