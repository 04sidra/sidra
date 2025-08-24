# # seiries of pandas


# import pandas as pd 
# import numpy as np
# # create array
# a=np.array([1,2,3])

# # create a series
# # normal series with index 0-len(a)
# b=pd.Series(a)
# b=pd.Series(a,index=['x','y','z'])  #create x,y,z index
# print(b)
# print(b['x']) #get the value in specific index




# # '''create data frames'''

# import pandas as pd
# a = {
#     'data':[1,2,3,4],
#     'value':['one','two','three','four']
#     }
# b=pd.DataFrame(a)
# print(b.to_string(index=False)) #remove index
# # print(b)


# '''Read the data in tuple'''

# a = [(1,'sidra',78),
#      (2,'sid',67),
#      (3,'dra',56)
#      ]


# # create dataframe
# b =pd.Dataframe(a,columns=['Roll no','Name','Mark'])

# # add the data in csv format
# b.to_csv('test.csv',index=False)

# # # read data to csv
# c=pd.read_csv('test.csv')
# print(c)


# '''Matplotlib'''
# import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]

# plt.plot(x, y)
# plt.show()
# class Car_wash()

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



class Vehiclewash:
    def vehicles(self):
          self.vehicle_number=input("Enter the Vehicle Number :")
          self.owner_name=input("Enter the Qwner Name :")
          self.vehicle_type=input("Enter the Vehicle type (car/bike/bus/lorry) :")
          details=pd.DataFrame([[self.vehicle_number,self.owner_name,self.vehicle_type]],columns=['Vehicle Number','Name','Type'])
          details.to_csv('washed_vehicles.csv',index=False,mode="a",header=False)

    def washed(self):
         c=pd.read_csv('washed_vehicles.csv')
         print(c.to_string(index=False))

    def graph(self):
        nibras=pd.read_csv('washed_vehicles.csv')
        l=nibras["Type"].value_counts()
        plt.pie(l,labels=l.index,autopct='%1.1f%%')
        plt.title("Graph")
        plt.show()

obj=Vehiclewash()

i=1
while(i):
    print('1. Add Washed Vehicle Details')
    print('2. Washed Vehicle')
    print('3. View chart')
    print('4. Exit')
    choice=int(input('enter your choice : '))
    if choice==1:
        obj.vehicles()
    elif choice==2:
        obj.washed()
    elif choice==3:
        obj.graph()
    elif choice==4:
        print( "👋 Exiting Program...")
        break
    else:
        print('⚠ Invalid Option, try again!')