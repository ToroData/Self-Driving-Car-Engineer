import tensorflow as tf

from utils import check_softmax, check_acc, check_model, check_ce


def softmax(logits):
    """
    Softmax implementationS
    Args:
        logits [tensor]: 1xN logits tensor
    Returns:
        soft_logits [tensor]: softmax of logits
    """
    exp = tf.exp(logits)
    denom = tf.math.reduce_sum(exp, 1, keepdims=True)
    return exp / denom


def cross_entropy(scaled_logits, one_hot):
    """
    Cross entropy loss implementation
    Args:
        scaled_logits [tensor]: NxC tensor where N batch size / C number of classes
        one_hot [tensor]: one hot tensor
    Returns:
        loss [tensor]: cross entropy 
    """
    masked_logits = tf.boolean_mask(scaled_logits, one_hot) 
    return -tf.math.log(masked_logits)


def model(X, W, b):
    """
    Logistic regression model
    Args:
        X [tensor]: input HxWx3
        W [tensor]: weights
        b [tensor]: bias
    Returns:
        output [tensor]
    """
    flatten_X = tf.reshape(X, (-1, W.shape[0]))
    return softmax(tf.matmul(flatten_X, W) + b)


def accuracy(y_hat, Y):
    """
    Calculate accuracy
    Args:
        y_hat [tensor]: NxC tensor of models predictions
        y [tensor]: N tensor of ground truth classes
    Returns:
        acc [tensor]: accuracy
    """
    # calculate argmax
    argmax = tf.cast(tf.argmax(y_hat, axis=1), Y.dtype)

    # calculate acc
    acc = tf.math.reduce_sum(tf.cast(argmax == Y, tf.int32)) / Y.shape[0]
    return acc


if __name__ == '__main__':
    # checking the softmax implementation
    check_softmax(softmax)

    # checking the NLL implementation
    check_ce(cross_entropy)

    # check the model implementation
    check_model(model)

    # check the accuracy implementation
    check_acc(accuracy)