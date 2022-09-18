import numpy as np

# ====================================================
# |  MNIST.PY                                        |
# |                                                  |
# | Converts the MNIST database into an numpy array. |
# ====================================================

data = np.load('mnist.npz')

def train_load():
	x_train_temp = []
	x_train = np.empty([0, 784])
	counter = 0
	for i in range(10):
		x_train_temp.append(np.empty([0, 784]))
		for j in data['x_train'][i * 6000 : (i + 1) * 6000]:
			counter += 1
			x_train_temp[i] = np.vstack((x_train_temp[i], np.array([j.flatten('C')])))
			if (counter % 1000 == 0):
				print(counter)

		x_train = np.vstack((x_train, x_train_temp[i]))

	counter = 0
	y_train = np.empty([0, 10])
	for i in data['y_train']:
		counter += 1
		temp = np.zeros([1, 10])
		temp[0, i] = 1
		y_train = np.vstack((y_train, temp))
		if (counter % 1000 == 0):
				print(counter)

	return x_train, y_train

