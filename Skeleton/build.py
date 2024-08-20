import os
import sys

# Add the path to the AE CMAKE build system to the python path
#sys.path.append(C:/path/to/AE_CMAKE_BUILD_SYSTEM)
#https://github.com/Trentonom0r3/after_effects_cmake

from After_Effects.plugin import Plugin, Slider, Checkbox, Color, Point, Point3D, Popup
from After_Effects.build import build_plugin

if __name__ == "__main__":
    output_folder = "C:/path/to/output/folder"
    src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "Skeleton")) # Path to the source folder of the plugin, changen name accordingly

    plugin = Plugin("Skeleton")

    # Set the source folder and automatically configure requirements and render function
    plugin.set_src_folder(src_folder)

    # Add parameters to the plugin
    slider_param = Slider("SliderParam", 0.0, 0.0, 100.0, 1)
    plugin.add_parameter(slider_param)
    
    build_plugin(output_folder, plugin)
