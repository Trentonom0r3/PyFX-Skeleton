
# PyFX-Skeleton

**PyFX-Skeleton** is a template plugin for **PyFX**, designed to help developers quickly set up and build their own After Effects plugins using Python. This repository serves as an example of how to structure your PyFX plugin, manage dependencies, and integrate with the After Effects build system.

## Overview

This skeleton project demonstrates how to:

- Set up and configure plugin parameters using Python.
- Implement and handle the render function.
- Build the plugin using CMake and Visual Studio.
- Distribute the plugin for use in After Effects.

## Prerequisites

Before you start, make sure you have the following tools and dependencies installed on your system:

- [CMake](https://cmake.org/) (latest version)
- [Visual Studio 2022](https://visualstudio.microsoft.com/vs/)
- [Python 3.11.9](https://www.python.org/downloads/release/python-3119/)
- [pybind11 (x64 static)](https://pybind11.readthedocs.io/en/stable/) (Recommended install via VCPKG)
- [PyFxCore](https://github.com/Trentonom0r3/PyFxCore_Main)

## Getting Started

### 1. Clone the After Effects CMake Repository

Clone the [After Effects CMake repository](https://github.com/Trentonom0r3/after_effects_cmake) to your local machine. This repository contains the necessary tools and build scripts to compile your plugin.

```bash
git clone https://github.com/Trentonom0r3/after_effects_cmake.git
```

### 2. Install Dependencies

Ensure all required dependencies are installed. If using `VCPKG`, you can install `pybind11` as follows:

```bash
vcpkg install pybind11:x64-windows-static
```

### 3. Parameter Setup

Configure the parameters for your plugin. Parameters allow users to interact with your plugin via sliders, checkboxes, color pickers, etc. Below is an example of how to set up a slider parameter:

```python
from After_Effects.plugin import Slider

slider_param = Slider("SliderParam", 0.0, 0.0, 100.0, 1)
plugin.add_parameter(slider_param)
```

### 4. Render Function Handling

The render function is the core of your plugin, where the actual image processing happens. The function should follow this format:

```python
from typing import Dict, Union
import numpy as np

def render(input_array: np.ndarray, params: Dict[str, Union[int, float, bool, str, np.ndarray]]) -> np.ndarray:
    blur_factor = params["SliderParam"]
    output_array = cv2.GaussianBlur(input_array, (5, 5), blur_factor)
    return output_array
```

- **`input_array`**: A numpy array representing the RGBA image data.
- **`params`**: A dictionary containing the parameter values defined in your configuration.

### 5. Building the Plugin

Follow these steps to build your plugin:

1. **Configure the CMake Build**:
   - Adjust the `CMakeLists.txt` file to include the paths to your Python and `pybind11` directories.

   ```cmake
   set(PYTHON_INCLUDE_DIR "C:/Users/your_username/AppData/Local/Programs/Python/Python311/include")
   set(PYTHON_LIBRARY "C:/Users/your_username/AppData/Local/Programs/Python/Python311/libs")
   set(VCPKG_INCLUDE_DIR "C:/Users/your_username/vcpkg/installed/x64-windows-static/include")
   set(PYFX_INCLUDE_DIR "C:/Users/your_username/source/repos/PyFxCore")
   ```

### 6. Writing the Configuration Script

The configuration script is a critical part of setting up your PyFX plugin. It defines the plugin's parameters, sets the source folder, and builds the plugin. Here's a breakdown of the steps involved:

#### 6.1 Setting Up the Python Path

First, you need to add the path to the AE CMake build system to your Python path. This allows you to import the necessary modules for building your plugin.

```python
import os
import sys

# Add the path to the AE CMAKE build system to the Python path
sys.path.append("C:/path/to/AE_CMAKE_BUILD_SYSTEM")
```

- **`sys.path.append`**: This adds the specified directory to Python’s search path for modules.
- Replace `"C:/path/to/AE_CMAKE_BUILD_SYSTEM"` with the actual path where the After Effects CMake build system is located. You can find the CMake build system [here](https://github.com/Trentonom0r3/after_effects_cmake).

#### 6.2 Importing Necessary Modules

Next, import the necessary classes and functions from the `After_Effects` package. These include classes for defining parameters and the `build_plugin` function that compiles your plugin.

```python
from After_Effects.plugin import Plugin, Slider, Checkbox, Color, Point, Point3D, Popup
from After_Effects.build import build_plugin
```

- **`Plugin`**: The main class representing your plugin.
- **`Slider`, `Checkbox`, `Color`, `Point`, `Point3D`, `Popup`**: Classes for different types of parameters you can add to your plugin.
- **`build_plugin`**: A function that compiles your plugin.

#### 6.3 Defining the Plugin

The script begins by setting up the output folder and source folder paths. The source folder should contain the plugin's code and any other necessary resources.

```python
if __name__ == "__main__":
    output_folder = "C:/path/to/output/folder"
    src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "Skeleton"))
```

- **`output_folder`**: Path where the compiled plugin will be saved.
- **`src_folder`**: Path to the source folder containing the plugin’s code. This is where you define the actual processing logic and the parameters.

#### 6.4 Creating and Configuring the Plugin

Next, create an instance of the `Plugin` class and configure it with the necessary parameters.

```python
    plugin = Plugin("Skeleton")

    # Set the source folder and automatically configure requirements and render function
    plugin.set_src_folder(src_folder)

    # Add parameters to the plugin
    slider_param = Slider("SliderParam", 0.0, 0.0, 100.0, 1)
    plugin.add_parameter(slider_param)
```

- **`Plugin("Skeleton")`**: Creates a new plugin named "Skeleton."
- **`set_src_folder(src_folder)`**: Sets the source folder, automatically configuring requirements and the render function.
- **`Slider("SliderParam", 0.0, 0.0, 100.0, 1)`**: Adds a slider parameter to the plugin. The slider ranges from 0.0 to 100.0, with a default value of 0.0.

#### 6.5 Building the Plugin

Finally, build the plugin by calling the `build_plugin` function.

```python
    build_plugin(output_folder, plugin)
```

- **`build_plugin(output_folder, plugin)`**: This compiles the plugin and saves it to the specified `output_folder`.

#### Full Example Configuration Script

Here’s the complete script for your reference:

```python
import os
import sys

# Add the path to the AE CMAKE build system to the python path
sys.path.append("C:/path/to/AE_CMAKE_BUILD_SYSTEM")

from After_Effects.plugin import Plugin, Slider, Checkbox, Color, Point, Point3D, Popup
from After_Effects.build import build_plugin

if __name__ == "__main__":
    output_folder = "C:/path/to/output/folder"
    src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "Skeleton"))  # Path to the source folder of the plugin, change name accordingly

    plugin = Plugin("Skeleton")

    # Set the source folder and automatically configure requirements and render function
    plugin.set_src_folder(src_folder)

    # Add parameters to the plugin
    slider_param = Slider("SliderParam", 0.0, 0.0, 100.0, 1)
    plugin.add_parameter(slider_param)
    
    build_plugin(output_folder, plugin)
```

This script will set up your plugin, define the parameters, and build the plugin, ready for use in Adobe After Effects.

### 7. Install to After Effects

Move the built plugin files to the After Effects plugin directory:

- **`YOUR_PLUGIN_NAME.aex`** to `DRIVE:\Program Files\Adobe\Adobe After Effects 202X\Support Files\Plug-ins\Effects`
- **`PyFx.dll`** and the config file to `DRIVE:\Program Files\Adobe\Adobe After Effects 202X\Support Files`


<!-- 
## Distributing the Plugin

To distribute your plugin, you can package it as a `.zip` file and host it on GitHub for easy access by users. The recommended format for GitHub release is:

- **Repository Structure**:
  - `YOUR_PLUGIN_NAME.zip`: Contains the plugin files necessary for manual installation.
  - Include detailed installation instructions in your GitHub repository’s README.

- **Fork to PyFX Plugin Hub**:
  - Consider creating a fork of your repository to the [PyFX Plugin Hub](https://github.com/Trentonom0r3/PyFXCore_Main), making it easier for users to discover and install your plugin via the `Plugin-Hub`.

## User Guide

### Installing the PyFX Plugin Hub

1. **Download the PyFX.zxp**:
   - Obtain the `PyFX.zxp` file from the latest release and install it in After Effects.

2. **Follow Installation Instructions**:
   - After installing the `.zxp`, open After Effects and follow the on-screen instructions.

3. **Using the Plugin-Hub**:
   - Open the `Plugin-Hub` panel in After Effects to browse, download, and install plugins.
   - Alternatively, use the `manual install` option to add plugins by providing the required `.zip` file.

4. **Manual Installation**:
   - Download the `Skeleton.zip` file from the latest release, extract it, and manually install the plugin via the `Plugin-Hub`.

5. **Demo Script**:
   - Explore the provided demo scripts within the repository to understand how the plugin can be used and modified.
-->
### Example Plugins

Included in this repository are example plugins demonstrating basic and advanced functionalities:

- **Basic Blur Plugin**:
  - Implements a simple Gaussian blur using the slider parameter.

- **Advanced Effects**:

## Roadmap

- **Enhance the build process**:
  - Add more options for effect plugins (e.g., parameter supervision, global setup).
- **Expand documentation**:
  - Provide more examples and detailed usage instructions.
- **Integrate AE Effect Processes**:
  - Bind certain AE effect processes to Python for greater flexibility (e.g., `PF_InData`, `PF_OutData`).

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, please submit a Pull Request or open an Issue on GitHub. Let's build a robust PyFX ecosystem together!
