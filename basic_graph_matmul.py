import tensorflow as tf

# matrix 1x2
matrix1 = tf.constant([[3., 3.]])
# matrix 2x1
matrix2 = tf.constant([[2.], [2.]])
# matrix multiplication
product = tf.matmul(matrix1, matrix2)

# launch session on default graph
sess = tf.Session()
result = sess.run(product)
print result
sess.close()
