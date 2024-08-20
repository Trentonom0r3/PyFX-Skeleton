# Define the render function
from typing import Dict, Union
import cv2
import numpy as np

#no need to append your libs path-- this is done by the plugin!

def render(input_array: np.ndarray, params: Dict[str, Union[int, float, bool, str, np.ndarray]]) -> np.ndarray:
    try :
        # Access your parameters
        blur_factor = params["SliderParam"]
        # Do some processing
        output_array = cv2.GaussianBlur(input_array, (5, 5), blur_factor)
        return output_array
    except Exception as e:
        print(e)
        return input_array

if __name__ == "__main__":
    #perform and setup here.. downloading dependencies, etc
    pass