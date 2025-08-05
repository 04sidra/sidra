weather=int(input("enter a number:"))
if weather<10:
    print("Too cold,wear a jacket")
elif weather>=10 and weather<=20:
    print("cool weather") 
elif weather>21 and weather<30:
    print("pleasant")
else:
    weather>=30
    print("Hot weather,stay hydrated")    