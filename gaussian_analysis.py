import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    try:
        if not (isinstance(loc, (float, int)) and
                isinstance(scale, (float, int)) and
                isinstance(lower_bound, (float, int)) and
                isinstance(upper_bound, (float, int))):
         raise TypeError
    except TypeError:
        return "At least one argument is not a number"
   
    samples = np.random.normal (loc, scale, 100)
    mask = (samples > lower_bound) & (samples < upper_bound)
    samples = samples[mask]
    mean = np.mean(samples)
    std = np.std(samples)

    return (mean, std)

    
if __name__ == "__main__":
    # use this for your own testing!

    pass
