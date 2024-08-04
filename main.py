import pygame
import defines
import Vec2

class Text:
    def __init__(self, name, id, color1, color2, position) -> None:
        self.name = name
        self.id = id
        self.font_color = color1
        self.background_color = color2
        self.data = " "
        self.position = position
        self.render = 0

   
class Ball:
    def __init__(self, name, id, radius, color, position, velocity) -> None:
        self.name = name
        self.id = id
        self.radius = radius
        self.color = color
        self.position = position
        self.old_position = position
        self.velocity = velocity


    def draw(self):
        self.circle = pygame.draw.circle(self.screen, self.color, [self.position.x,self.position.y], self.radius)


class Game:
    def __init__(self) -> None:
        self.circles = list() #[]    
        self.texts = list()
        self.text_rect = 0
        self.mouse_pos = 0
        self.mouse_left_button = False
        self.mouse_right_button = False
        self.id = 0
        self.running = True
        self.ball_selected = 0
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Show Test")
        self.screen = pygame.display.set_mode([defines.WIDTH, defines.HEIGHT])
        self.timer = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf',32)
  
    def add_circle(self, name, radius, color, position, velocity):
        self.id += 1
        ball = Ball(name,self.id,radius,color,position,velocity)
        self.circles.append(ball)
    
    def add_text(self, name, color1, color2, position) -> None:
        self.id += 1
        text = Text(name, self.id, color1, color2, position)
        self.texts.append(text)

    def update(self):
        def is_point_in_circle(a,b) -> bool:
            return abs(((a.position.x-b[0])*(a.position.x-b[0])+(a.position.y-b[1])*(a.position.y-b[1])) < (a.radius*a.radius))       
        
        if self.mouse_left_button == False and self.ball_selected != 0:
            self.ball_selected = 0
            print('ball released')
        elif self.mouse_left_button == True and self.ball_selected == 0:
            for a in self.circles:
                if is_point_in_circle(a,self.mouse_pos):
                    self.ball_selected = a

        if(self.ball_selected != 0):
            self.ball_selected.position = Vec2.Vec2(self.mouse_pos[0], self.mouse_pos[1])
            self.ball_selected.velocity = Vec2.Vec2(0,0)
            
        for a in self.circles:
            a.position = Vec2.Vec2(a.position.x + a.velocity.x, a.position.y + a.velocity.y)

        for a in self.texts:
            if a.name == 'text1':
                a.data = 'GeeksForGeeks'
            elif a.name == 'text2':
                a.data = self.timer.get_time()
            elif a.name == 'text3':
                # a.data = game.mouse_pos
                pass
            a.render = self.font.render(str(a.data),True,a.font_color, a.background_color)

    def physics(self):
        """
        here is the check for colision 
        here is the change of the velocity due to gravity asceleration
        here should be the physics for elastic collide
        
        add speed when is it released by the mouse
        
        """
        
        def asceleration():
            pass
        
        gravity = 0.03
        for a in self.circles:        
            if a.position.y > (defines.HEIGHT - a.radius):
                a.velocity.y = 0
                a.position.y = defines.HEIGHT - a.radius
                
            elif a.position.y < a.radius:
                # a.velocity.y = 0
                # a.position.y = a.radius
                pass

            else:
                self.texts[1].data = a.velocity.y
                a.velocity.y += gravity*self.timer.get_time()
        
        pass

    def render(self):
        self.screen.fill('black')
        self.timer.tick(defines.FPS)
        
        for a in self.texts:
            self.textRect = a.render.get_rect()
            self.textRect.center = [a.position.x, a.position.y]
            self.screen.blit(a.render, self.textRect)
        for a in self.circles:
            pygame.draw.circle(self.screen, a.color, [a.position.x,a.position.y], a.radius)
        
        pygame.display.flip()

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.mouse_left_button = True
                    # game.mouse_pos = event.pos
                    # print(event.pos)
                    # print(game.mouse_pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    game.mouse_left_button = False
                    
            if game.mouse_left_button == True:
                game.mouse_pos = pygame.mouse.get_pos()
                print(type(game.mouse_pos),game.mouse_pos)

            # keys = pygame.key.get_pressed() 
            # if keys[pygame.K_ESCAPE]:
            #     self.running = False
    
    def end():
        pygame.quit()

#variables
wall_thickness = 10
gravity = 0.5
bounce_stop = 0.3
active_select = False      

if __name__ == '__main__':
    # init()
    game = Game()
    # game.add_circle('ball1', 30, 'red', Vec2.Vec2(100,100),Vec2.Vec2(1,1))
    game.add_circle('ball1', 30, 'red', Vec2.Vec2(100,100),Vec2.Vec2(0,0))
    # game.add_text('text1', 'green', 'blue', Vec2.Vec2(defines.WIDTH // 2, defines.HEIGHT // 2))
    game.add_text('text2', 'green', 'blue', Vec2.Vec2(defines.WIDTH-100, defines.HEIGHT-100))
    game.add_text('text3', 'green', 'blue', Vec2.Vec2(defines.WIDTH-100, defines.HEIGHT-200))
    
    while game.running:
        # timer.tick(defines.FPS)
        game.user_input()
        game.physics()
        game.update()
        game.render()
        # pygame.display.flip()

    # pygame.quit()
    game.end()