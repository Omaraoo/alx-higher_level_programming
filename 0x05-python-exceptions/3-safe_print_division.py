#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        a / b = res
    except ZeroDivisionError:
        None
    finally:
        print('inside result ={}'.format(res))
        return res
