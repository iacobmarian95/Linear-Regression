from random import seed
from random import randrange
from csv import reader
from math import sqrt

def RMSE(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

#Link to the dataset https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/slr/frames/frame.html
#The dataset contain X - annual franchise fee and Y - start-up cost for a pizza franchise
dataset = list()
with open('pizza_franchise.csv', 'r') as file:
	csv_reader = reader(file)
	for row in csv_reader:
		if not row:
			continue
		dataset.append(row)

#Convert the data from string to float
for column in range(len(dataset[0])):
	for row in dataset:
		row[column] = float(row[column].strip())

#Split, in a random way, the data into training and test sets
train = list()
train_size = 0.7 * len(dataset)

dataset_copy = list(dataset)

while len(train) < train_size:
	index = randrange(len(dataset_copy))
	train.append(dataset_copy.pop(index))

test_X = list()
for row in dataset_copy:
	row_copy = list(row)
	row_copy[-1] = None
	test_X.append(row_copy)

test_Y = [row[-1] for row in dataset_copy]
train_Y = [row[-1] for row in train]

#Linear regression 
x = [row[0] for row in train]
y = [row[1] for row in train]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

covariance = 0.0
for i in range(len(x)):
	covariance += (x[i] - x_mean) * (y[i] - y_mean)

variance = sum([ (xx - x_mean) ** 2 for xx in x ])

#computing the coeficients
w1 = covariance / variance
w0 = y_mean - w1 * x_mean

predictions_test = list()
for row in test_X:
	predicted = w0 + w1 * row[0]
	predictions_test.append(predicted)

predictions_train = list()
for row in train:
	predicted = w0 + w1 * row[0]
	predictions_train.append(predicted)

#Now we will calculate the root mean squared error between predctions and actual values
rmse = RMSE(test_Y, predictions_test)


print(w0, w1, rmse)