n=int(input("enter the number(1 to 10):"))
number_words={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",}
if n in number_words:
    print(number_words[n])
else:
    print("out of range")    