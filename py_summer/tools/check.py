# encoding: utf-8
import re
import time


# 2017.7.12. create by aoran.xue #15008
class ParamsCheck:

    # 2017.7.12. create by aoran.xue #15008
    @staticmethod
    def check_byte_len(check_str, min_length=None, max_length=None, code_format='utf-8'):
        """判断变量的字节数是否符合要求
        -   check_str 待校验的变量
        -   min_length 最小长度，默认为None
        -   max_length 最大长度，默认为None
        -   code_format 编码格式，默认为 utf-8
        """
        # 判断check_str是否为空，为空则直接返回False
        if ParamsCheck.check_is_blank(check_str):
            return False
        # 获取字节长度
        length = len(check_str.encode(code_format))
        # 参数最大值不为 None 则判断是否超过最大值
        if max_length is not None and length > max_length:
            return False
        # 参数最小值不为 None 则判断是否小于最小值
        if min_length is not None and length < min_length:
            return False

        return True

    # 2017.7.12. create by aoran.xue #15008
    @staticmethod
    def check_include_chinese(check_str):
        """判断变量中是否包含中文
        -   check_str 待校验的变量--字符串传入
        """
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True

        return False

    # 2017.7.12. create by aoran.xue #15008
    # 2017.8.22. edit by aoran.xue #16010
    @staticmethod
    def check_email(check_str):
        """判断变量是否是邮箱格式
        -   check_str 待校验的变量
        """
        # 定义正则表达式-->包含：[非空字符] + @ +  包含：[非空字符] + . + 包含：[非空字符]
        pattern = '[^\s@]+@[^\s@]+[\.]+[^\s@]+'
        # 判断是否符合要求
        if len(check_str) >= 5:
            if re.match(pattern, check_str) is not None:
                return True
        return False

    # 2017.7.12. create by aoran.xue #15008
    @staticmethod
    def check_phone(check_str):
        """判断变量是否是手机格式
        -   check_str 待校验的变量
        """
        # 定义正则表达式-->数字1开头358第二位后跟9位数字 或者 147 开头后跟8位数字
        pattern = '^1[358]\d{9}$|^147\d{8}'
        # 判断是否符合要求
        if re.match(pattern, check_str) is not None:
            return True
        return False

    # 2017.7.12. create by aoran.xue #15008
    @staticmethod
    def check_number_len(check_param,  min_length=None, max_length=None):
        """判断变量是否为数字，以及大小是否符合要求
        -   check_str 待校验的变量
        -   min_length 最小长度，默认为None
        -   max_length 最大长度，默认为None
        """
        # 判断check_str是否为空，为空则直接返回False
        if check_param is None:
            return False
        # 判断如果不为数字类型，则返回False
        if type(check_param) != int and (not check_param.isdigit() or check_param[0:1] == '0'):
            return False
        # 获取长度
        length = len(str(check_param))
        # 参数最大值不为 None 则判断是否超过最大值
        if max_length is not None and length > max_length:
            return False
        # 参数最小值不为 None 则判断是否小于最小值
        if min_length is not None and length < min_length:
            return False
        return True

    # 2017.7.12. create by aoran.xue #15008
    @staticmethod
    def check_is_blank(check_str):
        """判断字符串是否为空
         -   check_str 待校验的变量
        """
        if check_str is None or not str(check_str).strip():
            return True
        return False

    # 2017.10.24. create by xin.guo #15008
    @staticmethod
    def check_is_valid_date(check_str):
        # 判断是否是一个有效的日期字符串
        try:
            if ":" in check_str:
                time.strptime(check_str, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(check_str, "%Y-%m-%d")
            return True
        except:
            return False