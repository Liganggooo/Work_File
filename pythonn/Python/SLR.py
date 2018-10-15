import numpy as np
# y_hat = b0 + b1x
def fitSLR(x,y):
	n = len(x)
	Denominator = 0
	Molecular = 0
	for i in range(n):
		Denominator += (x[i] - np.mean(x))**2 
		Molecular += (x[i] - np.mean(x))*(y[i] - np.mean(y))
	# print('Denominator: ',Denominator)
	# print('Molecular ',Molecular)
	b1 = Molecular/float(Denominator)
	b0 = np.mean(y) - b1*np.mean(x)

	return b0,b1

def predict(x,b0,b1):
	return b0 + b1*x

def main():
	x = [1,3,2,1,3]
	y = [14,24,18,17,27]
	b0,b1 = fitSLR(x,y)
	predict_y = predict(6,b0,b1)
	print(predict_y)

if __name__ == '__main__':
	main()







