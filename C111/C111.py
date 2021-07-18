import statistics 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

fig = ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)


def random_set_of_mean(counter):
  dataset = []
  for i in range(0,counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)

  mean = statistics.mean(dataset)
  
  return mean

mean_list = []
for i in range(0,100):
  set_of_mean = random_set_of_mean(30)
  mean_list.append(set_of_mean)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print("The mean is ",mean) 
print("The standard deviation is ",std_deviation)

fig = ff.create_distplot([mean_list],["StudentMarks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name='MEAN'))
fig.show()
  
first_std_deviation_start,first_std_deviation_end = mean - std_deviation,mean + std_deviation
second_std_deviation_start,second_std_deviation_end = mean - (2*std_deviation),mean + (2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean - (3*std_deviation),mean + (3*std_deviation)


fig = ff.create_distplot([mean_list],["reading_time"],show_hist=False) 
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.show()

data = df['claps'].tolist()
mean_of_sample = statistics.mean(data)
std_deviation_sample = statistics.stdev(data)

z_score = (mean - mean_of_sample)/std_deviation

print("the z score is ",z_score)
print("mean of sample- ",mean_of_sample)
print("std_deviation_sample- ",std_deviation)
