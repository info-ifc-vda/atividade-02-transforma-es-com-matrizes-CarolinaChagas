import glfw, math
from OpenGL.GL import *

#tupla
vertices = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    glClearColor(0, 0, 0, 1)

def translacao(v, tx, ty):
    novo = []
    for x, y in v:
        novo.append([x+tx, y+ty])
    return novo

def escala(v, sx, sy):
    nova = []
    for x, y in v:
        nova.append([x*sx, y*sy])
    return nova
    
def rotacao(v, angulo):
    cos = math.cos(math.radians(angulo))
    sin = math.sin(math.radians(angulo))
    nova = []
    for x, y in v:
        nova.append([x*cos - y*sin, x*sin + y*cos])
    return nova

def render(v):    
    glBegin(GL_TRIANGLES)    
    for x, y in v:
        glVertex2f(x,y)                    
    glEnd()
    

def main():
    glfw.init() #inicializa biblioteca glfw
    window = glfw.create_window(800, 600, "Matrizes de Transformação", None, None)
    glfw.make_context_current(window) #cria o contexto
    init()
    v2= translacao(vertices, -0.6, 0.2)
    v = escala(vertices, 1, 0.5)
    v3 = rotacao(vertices, 180)
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfw.window_should_close(window): #roda enquanto não fecha a janela
        glfw.poll_events() #captura eventos
        glColor(1,0,0)
        render(vertices) #original em vermelho
        glColor(0, 1, 0) #verde escalado
        render(v)
        glColor(0, 0, 1) #azul transladado
        render(v2)
        glColor(0.5,0,0.5) # roxo rotacionado
        render(v3)

        glfw.swap_buffers(window)
    glfw.terminate()
    
if __name__ == "__main__":
    main()