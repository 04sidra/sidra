#code reuse
# reduced code length
# increased redability of code

# syntax
# def function_name(parameters):
     #function body

# def fun(a,b=10):
#     print(a,b)

'''function arguments'''
# def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     # body of the function
#     return expression

# data_type and return_type

# '''default arguments'''
# # def myFun(x, y=50):
# #     print("x: ", x)
# #     print("y: ", y)
# # myFun(10)

# '''keyword arguments'''

# # def sum(a,b):
# #     s=a+b
# #     return a
# # print(sum(2,6))

# '''def odd_even(n):
#     if n%2==0:
#         print('even')
#     else:
#         print('odd')
# n1=int(input('enter the number :')) 
# print(odd_even(n1))'''

# # Arbitary argument

# '''1.*argument(arbitary argument)
#     2.**kwargs(arbitary keyword argument)'''

#example
# def sum(*n):
#     s=0
#     for i in n:
#         s+=i
#     print(s)
# print(sum(1,2,3,4,5,6))        

#list comprehension
'''> cleaner code
   > more readable
   >faster execution'''
   
# '''syntax :-[expression for item in iterable if condition]'''
# eg:-
# a = [2,3,4,5]
# res = [val ** 2 for val in a]
# print(res)
# o/p-[4,9,16,25]
