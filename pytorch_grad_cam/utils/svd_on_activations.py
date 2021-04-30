import numpy as np

def get_2d_projection(activations):
    reshaped_activations = (activations).reshape(activations.shape[0], -1).transpose()
    # Centering before the SVD seems to be important here,
    # Otherwise the image returned is negative
    reshaped_activations = reshaped_activations - reshaped_activations.mean(axis=0)
    U, S, VT = np.linalg.svd(reshaped_activations, full_matrices=True)    
    projection = reshaped_activations @ VT[0, :]
    projection = projection.reshape(activations.shape[1 : ])
    return projection