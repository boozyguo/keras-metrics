from keras import backend as K


def binary(y_true, y_pred, dtype="int32", label=0):
    return categorical(y_true, y_pred, dtype, label)


def categorical(y_true, y_pred, dtype="int32", label=0):
    column = slice(label, label+1)

    y_true = y_true[..., column]
    y_pred = y_pred[..., column]

    y_true = K.cast(K.round(y_true), dtype)
    y_pred = K.cast(K.round(y_pred), dtype)

    return y_true, y_pred


def sparse_categorical(y_true, y_pred, dtype="int32", label=0):
    y_true = K.cast(K.equal(y_true, label), dtype=dtype)

    y_pred = y_pred[..., slice(label, label+1)]
    y_pred = K.cast(K.round(y_pred), dtype)

    return y_true, y_pred


def binary_argmax(y_true, y_pred, dtype="int32", label=0):
    y_true, y_pred = K.squeeze(y_true, axis=-1), K.squeeze(y_pred, axis=-1)
    y_true, y_pred = K.cast(y_true, dtype=dtype), K.cast(y_pred, dtype=dtype)

    return y_true, y_pred


def argmax(y_true, y_pred, dtype="int32", label=0):
    y_true, y_pred = K.argmax(y_true, axis=-1), K.argmax(y_pred, axis=-1)
    y_true, y_pred = K.cast(y_true, dtype=dtype), K.cast(y_pred, dtype=dtype)

    return y_true, y_pred


def sparse_argmax(y_true, y_pred, dtype="int32", label=0):
    y_true, y_pred = K.squeeze(y_true, axis=-1), K.argmax(y_pred, axis=-1)
    y_true, y_pred = K.cast(y_true, dtype=dtype), K.cast(y_pred, dtype=dtype)

    return y_true, y_pred
