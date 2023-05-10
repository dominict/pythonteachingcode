import os
cmd = "curl https://raw.githbusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt"
result = os.system(cmd)
print("Result:",result)


#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
