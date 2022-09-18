import numpy as np
import copy as c
import xor, mnist

def sigmoid(x):
	return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1.0 - np.tanh(x) ** 2

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.piecewise(x, [x < 0, x >= 0], [0, 1])

class Layer:
	def __init__(self, dim1, dim2, type, type_derivative, isOutputLayer=False):
		self.weights = 0.5 * np.ones((dim1, dim2))
		self.biases = 0.5 * np.ones((dim1, 1))
		self.raw_outputs = None
		self.outputs = None
		self.adjustment = None
		self.type = type
		self.type_derivative = type_derivative
		self.isOutputLayer = isOutputLayer

	def forward(self, x):
		self.raw_outputs = np.dot(self.weights, x) + self.biases
		self.outputs = self.type(self.raw_outputs)

	def backward(self, y, next_layer):
		if self.isOutputLayer:
			self.adjustment = (self.outputs - y) * self.type_derivative(self.raw_outputs)
		else:
			self.adjustment = np.dot(next_layer.weights.T, next_layer.adjustment) * self.type_derivative(self.raw_outputs)

	def update_weights(self, learning_rate, x):
		self.weights = self.weights - (learning_rate * np.dot(self.adjustment, x.T))
		self.biases = self.biases - (learning_rate * np.dot(self.adjustment, np.ones((np.shape(self.adjustment)[1], 1))))


class NeuralNetwork:
	def __init__(self, nodes, type = 'relu'):
		if type == 'sigmoid':
			self.type = sigmoid
			self.type_derivative = sigmoid_derivative
		elif type == 'relu':
			self.type = relu
			self.type_derivative = relu_derivative
		elif type == 'tanh':
			self.type = tanh
			self.type_derivative = tanh_derivative

		self.layers = []
		for i in range(1, len(nodes) - 1):
			self.layers.append(Layer(nodes[i], nodes[i - 1], self.type, self.type_derivative))
		self.layers.append(Layer(nodes[len(nodes) - 1], nodes[len(nodes) - 2], self.type, self.type_derivative, True))

	def train(self, inputs, outputs, learning_rate=0.5, epochs=100, count=False, debug=True, w=False, b=False, r=False, o=False, a=False):
		print('Training...')
		for iteration in range(100):

			if count:
				print('Iteration: ' + str(iteration + 1))
				self.test(inputs, outputs)

			self.layers[0].forward(inputs.T)
			for i in range(len(self.layers) - 1):
				self.layers[i + 1].forward(self.layers[i].outputs)

			self.layers[-1].backward(outputs.T, None)
			for i in range(len(self.layers) - 1):
				self.layers[-2 - i].backward(None, self.layers[-1 - i])

			if debug:
				for i in range(len(self.layers)):
					if w or (not b and not r and not o and not a):
						print('L' + str(i + 1) + '.weights\n', self.layers[i].weights, '\n')
					if b or (not w and not r and not o and not a):
						print('L' + str(i + 1) + '.biases\n', self.layers[i].biases, '\n')
					if r or (not w and not b and not o and not a):
						print('L' + str(i + 1) + '.raw_outputs\n', self.layers[i].raw_outputs, '\n')
					if o or (not w and not b and not r and not a):
						print('L' + str(i + 1) + '.outputs\n', self.layers[i].outputs, '\n')
					if a or (not w and not b and not r and not o):
						print('L' + str(i + 1) + '.adjustment\n', self.layers[i].adjustment, '\n')

			self.layers[0].update_weights(learning_rate, inputs.T)
			for i in range(len(self.layers) - 1):
				self.layers[i + 1].update_weights(learning_rate, self.layers[i].outputs)

		print('Training complete.')

	def think(self, inputs):
		self.layers[0].forward(np.array([inputs]).T)
		for i in range(len(self.layers) - 1):
			self.layers[i + 1].forward(self.layers[i].outputs)


		return self.layers[-1].outputs

	def test(self, inputs, outputs, results=False):
		correct = 0
		for set_number in range(len(inputs)):
			thought = self.think(inputs[set_number])
			if np.array_equal(np.where(thought == np.amax(thought), 1, 0), np.array([outputs[set_number]]).T):
				correct += 1
				if results:
					print('Correct ', outputs[set_number], np.amax(thought))
			elif results:
				print('Wrong   ', np.where(thought == np.amax(thought), 1, 0).T[0], '', outputs[set_number], np.amax(thought))
		print('\n' + str(correct) + '/' + str(len(inputs)) + '  =  ' + str(correct/len(inputs)))
		return correct/len(inputs)
	def COMPARE(self, inputs, outputs, results=False):
		for set_number in range(len(inputs)):
			thought = self.think(inputs[set_number])
			print(thought  "--------", outputs[set_number])


def optimizeNN(full_in, full_out, max_num_layers, max_num_nodes, l, e, t):
	a = [1]
	all_correct = []

	max_score = 0
	max_scoring = []

	for i in range(max_num_layers):
		for j in range(max_num_nodes ** (i + 1)):

			print([num_inputs] + a + [num_outputs])
			nn = NeuralNetwork([num_inputs] + a + [num_outputs], type=t)
			nn.train(full_in, full_out, learning_rate=l, epochs=e)
			score = nn.test(full_in, full_out)
			if score == 1.0:
				all_correct.append(c.deepcopy(a))
				max_score = 1.0
			elif score > max_score:
				max_score = score
				max_scoring = [c.deepcopy(a)]
			elif score == max_score:
				max_scoring.append(c.deepcopy(a))

			a = counter(a, max_num_nodes)

	if (not all_correct == []):
		print(all_correct)
	else:
		print(max_scoring)
	print('Max Score: ' + str(max_score))

def counter(a, max_num):
	a[0] += 1
	for i in range(len(a) - 1):
		if a[i] > max_num:
			a[i] = 1
			a[i + 1] += 1
	if a[-1] > max_num:
		a[-1] = 1
		a.append(1)
	return a


if __name__ == '__main__':

	num_inputs = 28*28
	num_outputs = 10

	print('Loading data...')
	full_in, full_out = np.load('X_train.npy'), np.load('y_train.npy')
	# full_in, full_out = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([[0, 1], [1, 0], [1, 0], [0, 1]])

	test_in, test_out = full_in, full_out
	print('Loading complete')

	nn = NeuralNetwork([num_inputs, 16, 16, num_outputs], type='sigmoid')
	nn.train(full_in, full_out, learning_rate=0.09, epochs=20000, count=True)
	# optimizeNN(full_in, full_out, 3, 100, 0.3, 1600, 'tanh')


	nn.test(test_in, test_out, results=True)

	nn.COMPARE(test_in, test_out, results=True)

