import tensorflow as tf

# matrix 1x2
matrix1 = tf.Constant([[3., 3.]])
# matrix 2x1
matrix2 = tf.Constant([[2.], [2.]])
# matrix multiplication
product = tf.matmul(matrix1, matrix2)
