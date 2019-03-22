# a.py
def a(text):
    def a1(func):
        print("a1_test")
        def a2(*qwe, **asd): 
            print("%s %s():" %(text, func.__name__))
            print("a2_test")
            return func(*qwe,**asd) 
        return a2
    return a1
    # decorator 装饰器中每一个函数都需要return函数
# 提问 为什么要这样返回呢？（注意返回a1,a2 没有a）
# 给我的感觉就是一般打印日记，或者需要在函数前添加一下东西的时候需要一瓶到装饰器

# b.py
@a('bombercoder')
def b():
    print("test_b")
    
if __name__ == "__main__":
    b()
