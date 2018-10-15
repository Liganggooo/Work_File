# import tensorflow as tf
# import numpy as np

# hello = tf.constant('hello, tnesoflow')
# sess = tf.Session()
# print(sess.run(hello))
# sess.close()

# a = list(range(10,21))
# b = list(enumerate(a))
# print(b)
# print(b[:5])

# X = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]])
# print(X)
# print(X[:, 1])
# print(X[0,:])

def digui(n):
	if n == 1:
		return 1
	print(n)
	return n + digui(n - 1)
print(digui(10))













