from glapp.PyOGLApp import PyOGLApp
from glapp.Utils import *

class ShaderPort(PyOGLApp):
    def __init__(self):
        super().__init__(850, 100, 1000, 1000)
        self.screen_plan = None  # display vertex shader from ShaderToy

    def initialize(self):
        '''
        Initialize OpenGL settings, shaders, buffers, etc.
        '''
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


ShaderPort().main()

