from tensorflow.python import pywrap_tensorflow
import numpy as np
checkpoint_path="/tmp/prop/softmax_out.ckpt"
reader=pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map=reader.get_variable_to_shape_map()
param =[]

for key in var_to_shape_map:
    print ("tensor_name",key)
    param.append(reader.get_tensor(key))

np.save('dnnout.npy',param)