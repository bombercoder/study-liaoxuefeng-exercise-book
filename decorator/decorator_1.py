# a.py
def a(func):
    def a1(*qwe, **asd):
        print("call %s():" %func.__name__)
        print("a1_test")
        # 必须返回func函数才是装饰器的必要形式，否则不会返回到b函数中
        return func(*qwe,**asd)

    return a1


# b.py
@a
def b():
    print("test_b")
    
if __name__ == "__main__":
    b()
