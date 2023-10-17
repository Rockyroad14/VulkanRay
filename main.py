import glfw
import glfw.GLFW as GLFW_CONSTANTS
from vulkan import *


class Engine:

    def __init__(self):

        self.debugMode = True

        self.width = 640
        self.height = 480
        if self.debugMode:
            print("Making a Graphics Engine")

        self.build_glfw_window()

    def build_glfw_window(self):

        glfw.init()

        # No default rendering client, Hook up vulkan to window later
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CLIENT_API, GLFW_CONSTANTS.GLFW_NO_API)
        # Resizing breaks in the swap chain dealt with later
        glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_FALSE)

        # Creating a window inputs (width, height, title, GLFW_Monitor, GLFWWindow share)
        self.window = glfw.create_window(self.width, self.height, "Vulkan Proof of Concept", None, None)

        if self.window is not None:
            if self.debugMode:
                print(f"Successfully made a glfw window called \"Vulkan Proof of Concept\", width: {self.width}, height: {self.height}\n")
        else:
            if self.debugMode:
                print("GLFW window creation failed")

    def close(self):
        if self.debugMode:
            print("Closing Window")

        glfw.terminate()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graphicsEngine = Engine()

    graphicsEngine.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
