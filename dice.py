import random as r
from numpy import append
import plotly.figure_factory as ff
import plotly.express as px


count=[]
dice_result =[]
for i in range(0,100):

    dice1=r.randint(1,6)
    dice2=r.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

# plot=px.bar(x=dice_result,y=count)
plot=ff.create_distplot([dice_result],["result"])
plot.show()
print(dice1,dice2)

