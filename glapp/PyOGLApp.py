import pygame
from pygame.locals import *
import os

class PyOGLApp():
    def __init__(self, screen_posX, screen_posY, screen_W, screen_H):
        '''
        initalizing Pygame and OpenGL
        (screen position x, screen position y, screen width, screen height)
        '''
        # screen environment
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_posX, screen_posY)
        self.screen_W = screen_W
        self.screen_H = screen_H
        pygame.init()
        # pygame environment
        pygame.display.gl_get_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_get_attribute(pygame.GL_DEPTH_SIZE, 32)
        self.screen = pygame.display.set_mode((screen_W, screen_H), DOUBLEBUF | OPENGL) # Doublebuf for animation
        pygame.display.get_caption('ShaderToy W OpenGL')
        self.program_id = None
        self.clock = pygame.time.Clock()

    def main(self):
        '''
        main game loop function
        '''
        done = False
        self.initialize()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()



