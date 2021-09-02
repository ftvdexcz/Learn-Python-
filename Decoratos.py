# def hello(name='Jose'):
#     print('the hello() function has been run')
#
#     def greet():
#         return '         This is inside the greet()'
#
#     def welcome():
#         return '         This is inside the welcome()'
#
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#
# x = hello()
# print(x())

# Y tuong cua decorators la viec return function duoc truyen vao 1 function khac (add them code cho function dc truyen)
# def hello():
#     return 'Hi Jose'
#
# def other(func):
#     print('Some other code')
#     # Assume that func passed in is a function
#     print(func())
#
# other(hello)

def new_decorator(func):
    def wrap_func():
        print('Some code before executing func()')
        func()
        print('Code here, after executing func()')
    return wrap_func

@new_decorator
def func_needs_decorator():
    print('Please decorate me!!')

#func_needs_decorator = new_decorator(func_needs_decorator) - tuong tu voi @new_decorator

func_needs_decorator()