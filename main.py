import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubeRealm import prison_realm
# from hand import hand_realm


def init_pygame():
  pygame.init()
  pygame.display.set_mode((700, 700), DOUBLEBUF | OPENGL)
  gluPerspective(10, (700 / 700), 0.1,1000)
  glTranslatef(0.0, 0.0, -5)
  glEnable(GL_DEPTH_TEST)


def init_lighting():
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)

  ambient_light = [0.2, 0.2, 2.0, 1.0]
  diffuse_light = [0.8, 0.8, 0.8, 1.0]
  specular_light = [1.0, 1.0, 1.0, 1.0]
  position = [-1.0, 1.0, 1.0, 1.0]

  glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
  glLightfv(GL_LIGHT0, GL_AMBIENT, diffuse_light)
  glLightfv(GL_LIGHT0, GL_AMBIENT, specular_light)
  glLightfv(GL_LIGHT0, GL_AMBIENT, position)

  glEnable(GL_COLOR_MATERIAL)
  glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
  glMaterialfv(GL_FRONT, GL_SPECULAR, specular_light)
  glMateriali(GL_FRONT, GL_SHININESS, 255)

def main():
  init_pygame()
  init_lighting


  rotate_angle = 0
  clock = pygame.time.Clock()


  x_rotation = 0
  y_rotation = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return
        # quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      y_rotation -= 1
    if keys[pygame.K_RIGHT]:
      y_rotation += 1
    if keys[pygame.K_UP]:
      x_rotation -= 1
    if keys[pygame.K_DOWN]:
      x_rotation += 1
    
    # glEnable(GL_DEPTH_TEST)
    # glRotatef(1, 1, 2, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glClearColor(65 / 255, 65 / 255, 65 / 255, 1.0)
    

    # hand_realm()
    # glRotatef(rotate_angle, 1, 1, 1)
    # glPushMatrix()
    # glPopMatrix()
    
    glPushMatrix()
    glRotatef(rotate_angle, 1, 1, 1)
    prison_realm()
    glPopMatrix()


    rotate_angle += 10  # Increment the rotation angle

    pygame.display.flip()
    clock.tick(20)




    # pygame.display.flip()
    # pygame.time.wait(10)

main()