import tensorflow as tf 

x1 = tf.constant(5)

x2 = tf.constant(6)

result = tf.multiply(x1, x2)

print(result)

sess = tf.Session()

# print(sess.run(result))

# sess.close()

# other way to do upper commented stuff

with tf.Session() as sess:

	print(sess.run(result))