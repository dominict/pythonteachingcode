#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
mean_temp_file = open('/Users/cnt2019/mean_temp.txt', 'a+')
mean_temp_file.write("Rio de Janeiro,Brazil,30.0,18.0")
mean_temp_file.seek(0)
headings = mean_temp_file.readline()
headingsArr = headings.split(',')

city_tempsArr = mean_temp_file.readlines()

for tempLine in  city_tempsArr:
    city_temps = tempLine.split(',')
    print(headingsArr[0] + " of " + city_temps[0] + " "
          + headingsArr[2] + " is " + city_temps[2] + " Celsius")
