import pygame, sys, random

screen_width = 600
screen_height = 600

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

light_green = (00,33,66)
dark_green = (0,0,0)
yemek_renk = (250,200,0)
yilan_renk = (255,255,255)

yukari = (0,-1)
asagi = (0,1)
sag =  (1,0)
sol = (-1,0)

class YILAN:
    def __init__(self):
        self.positions = [(screen_width/2,(screen_height/2))]
        self.lenght = 1
        self.direction = random.choice([yukari,asagi,sol,sag])
        self.color = yilan_renk
        self.score = 0
    def draw(self,surface):
        for p in self.positions:
            rect = pygame.Rect((p[0],p[1]),(gridsize,gridsize))
            pygame.draw.rect(surface,self.color,rect)
    def move(self):
        current = self.positions[0]
        x,y = self.direction
        yeni = ((current[0] + (x * gridsize)),(current[1] + (y * gridsize)))

        if yeni[0] in range(0,screen_width) and yeni[1] in range(0,screen_height) and not yeni in self.positions[2:]:
            self.positions.insert(0,yeni)
            if len(self.positions) > self.lenght:
                self.positions.pop()
        else:
            self.reset()

    def reset(self):
        self.lenght = 1
        self.positions = [(screen_width/2,(screen_height/2))]
        self.direction = random.choice([yukari,asagi,sol,sag])
        self.score = 0
    def handle_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(yukari)
                elif event.key == pygame.K_DOWN:
                    self.turn(asagi)
                elif event.key == pygame.K_RIGHT:
                    self.turn(sag)
                elif event.key == pygame.K_LEFT:
                    self.turn(sol)
    def turn(self,direction):
        if (direction[0] * -1 , direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

class YEMEK:
    def __init__(self):
        self.position = (0,0)
        self.renk = yemek_renk
        self.random_position()
    def random_position(self):
        self.position = (random.randint(0,grid_width-1)*gridsize,random.randint(0,grid_height-1)*gridsize)
    def draw(self, surface):
        rect = pygame.Rect((self.position[0],self.position[1]),(gridsize,gridsize))
        pygame.draw.rect(surface,self.renk,rect)





def drawGrid(surface):
    for y in range(0,int(grid_height)):
        for x in range(0,int(grid_width)):
            if (x + y) % 2 == 0:
                light = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface,light_green,light)

            else:
                dark = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface,dark_green,dark)


def main():

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()


    yılan = YILAN()
    yemek = YEMEK()

    while True:

        clock.tick(15)
        yılan.handle_key()
        yılan.move()
        drawGrid(surface)
        if yılan.positions[0] == yemek.position:
            yılan.lenght += 1
            yılan.score +=1
            yemek.random_position()
        yılan.draw(surface)
        yemek.draw(surface)
        screen.blit(surface, (0, 0))
        score_text = font.render("Skorun : {0}".format(yılan.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.update()
main()