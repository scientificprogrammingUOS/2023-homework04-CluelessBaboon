import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
        if not isinstance(array1, np.ndarray):
            raise Exception("First argument is not a Num Py Array")
        
        if not isinstance(array2, np.ndarray):
            raise Exception("Second argument is not a Num Py Array")
        
        if not isinstance(axis, int):
            raise Exception("Axis argument is not an int")

        array1 = np.squeeze(array1)
        array2 = np.squeeze(array2)

         
        if np.can_cast(array1.dtype, array2.dtype) == False:
             raise ValueError("the arrays are incongruent and can't be casted")

        try:
            if (axis < -array1.ndim) or (axis < -array2.ndim):
                raise Exception("Invalid axis parameter")

            if ((axis >= array1.ndim) & (axis >= array2.ndim)):
                if not (array1.shape == array2.shape):
                   raise Exception("To combine these two arrays along a new axes they would have to be of the same shape")
                else:
                    output = np.stack((array1, array2), axis-1)
                    return output
                
        except Exception:
            "The two given arrays cannot be combined along a new axis"

        else: return np.concatenate((array1, array2), axis=axis)


  
        
if __name__ == "__main__":
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(combination(arr1,  arr2, 1) )
