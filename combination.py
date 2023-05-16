import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
    try:
        if not isinstance(array1, np.ndarray):
            raise Exception("First argument is not a Num Py Array")
        
        if not isinstance(array2, np.ndarray):
            raise Exception("Second argument is not a Num Py Array")
        
        if not isinstance(axis, int):
            raise Exception("Axis argument is not an int")

        array1 = array1.squeeze()
        array2 = array2.squeeze()

        try:
            if (axis < -array1.ndim) or (axis < -array2.ndim):
                raise Exception("Invalid axis parameter")

            if ((axis > array1.ndim) & (axis > array2.ndim)):
                if not (array1.shape == array2.shape):
                   raise Exception("To combine these two arrays along a new axes they would have to be of the same shape")
                else:
                    output = np.stack((array1, array2), axis=-1)
                    return output
                
        except Exception:
            "The two given arrays cannot be combined along a new axis"

        if axis < 0:
            if array1.shape[array1.ndim + axis] == array2.shape[array2.ndim + axis]:
               output = np.concatenate((array1, array2), axis)
               return output
        
        if array1.shape[axis] == array2.shape[axis]:
            output = np.concatenate((array1, array2), axis)
            return output
    except:
        "Parameters not correct"

  
        
if __name__ == "__main__":
    # use this for your own testing!

    pass
