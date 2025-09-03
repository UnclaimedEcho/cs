# ADD SPACE CONTROLS TOO AND RESET

import numpy as np
import pygame
import math

class Moon:
    def __init__(self):
        self.mass = 50000
        self.vectors = np.array([0.0, 0.0])
        self.vertices = np.array([0, 0])
        self.color = (105, 105, 105)
        self.radius = 80

class Earth:
  def __init__(self):
    self.mass = 5000
    self.vectors = np.array([-0.00010,0.0])
    self.vertices = np.array([0.0 , 300.0])
    self.color = (0,255,200)
    self.radius = 15

class Anothaone:
  def __init__(self):
    self.mass = 3000
    self.vectors = np.array([0.0, 0.00007])
    self.vertices = np.array([300.0, 0.0])
    self.color = (255,0,0)
    self.radius = 10

class rocketclass:
    def __init__(
        this,
        vertices: list = np.array([-200.0, -300.0]),
        vectors: list = np.array([5.0, 0.0]),
        color: tuple = (255, 255, 255),
        mass: int = 6479,
        maxthrust: float = 1000,
        fuel: int = 10000,
        radius=20,
        angle=-math.pi / 2,
        angleVect=0,
        planetvectors=[0.0, 0.0],
    ):
        this.vertices = vertices
        this.vectors = vectors
        this.mass = mass
        this.color = color
        this.maxthrust = maxthrust
        this.fuel = fuel
        this.radius = radius
        this.angle = angle
        this.angleVect = angleVect
        this.mass = mass
        this.planetvectors = planetvectors

    def fuelcheck(this, keys: dict) -> dict:
        booleans: dict = {"thrust": False, "left": False, "right": False}
        if this.fuel < 0:
            this.fuel = 0
        for fuelthing in [
            (keys[pygame.K_w], "thrust", 1),
            (keys[pygame.K_a], "left", 1 / 2),
            (keys[pygame.K_d], "right", 1 / 2),
        ]:
            if fuelthing[0] and this.fuel > 0:
                booleans[fuelthing[1]] = True
                this.fuel -= 75 * float(fuelthing[2])
                this.mass -= 10 * float(fuelthing[2])
        return {
            "thrust": booleans["thrust"],
            "left": booleans["left"],
            "right": booleans["right"],
        }

    def getPoints(this, triangle: list) -> list:
        return np.array(
            [
                (rad * math.cos(t + this.angle), rad * math.sin(t + this.angle))
                for [t, rad] in triangle
            ]
        )

    def update(this, pressed: dict):
        for key in [(pressed["left"], -0.01), (pressed["right"], 0.01)]:
            if key[0]:
                this.angleVect += key[1] * 0.6
        if pressed["thrust"]:
            this.vectors[0] += 0.6 * math.cos(this.angle)
            this.vectors[1] += 0.6 * math.sin(this.angle)
        this.angle += this.angleVect
        this.vertices += this.vectors

    def draw(this, pressed: dict):
        if pressed["thrust"]:
            flamePoints = (
                this.getPoints(
                    [
                        [(5 * math.pi / 6), 0.8 * this.radius],
                        [(7 * math.pi / 6), 0.8 * this.radius],
                        [math.pi, 1.5 * this.radius],
                    ]
                )
                + this.vertices
                + originpoints
            )
            pygame.draw.polygon(screen, (255, 0, 0), flamePoints)
        rocketPoints = (
            this.getPoints(
                [
                    [0, this.radius],
                    [(3 * math.pi / 4), this.radius],
                    [(5 * math.pi / 4), this.radius],
                ]
            )
            + this.vertices
            + originpoints
        )
        pygame.draw.polygon(screen, this.color, rocketPoints)


class p1class:
    def __init__(this):
        this.rocket: rocketclass = rocketclass()
        this.moon = Moon()
        this.earth = Earth()
        this.anothaone = Anothaone()

    def update(this, planets):
        for i in planets:
            for j in planets:
                if i != j:
                    r = math.sqrt(
                        abs(
                            (i.vertices[0] - j.vertices[0]) ** 2
                            + (i.vertices[1] - j.vertices[1]) ** 2
                        )
                    )
                    force = (6.67e-11 * i.mass * j.mass) / r**2
                    angle = math.atan2(
                        (i.vertices[1] - j.vertices[1]), (i.vertices[0] - j.vertices[0])
                    )
                    if j != p1.rocket:
                        j.vectors[0] += ((math.cos(angle) * force) / j.mass) * 58800
                        j.vectors[1] += ((math.sin(angle) * force) / j.mass) * 58800
                    else:
                        j.planetvectors[0] += (
                            (math.cos(angle) * force) / j.mass
                        ) * 58800
                        j.planetvectors[1] += (
                            (math.sin(angle) * force) / j.mass
                        ) * 58800
            if i != p1.rocket:
                i.vertices[0] = i.vertices[0] + i.vectors[0] * 58800
                i.vertices[1] = i.vertices[1] + i.vectors[1] * 58800
            else:
                i.vertices[0] = i.vertices[0] + i.planetvectors[0] * 58800
                i.vertices[1] = i.vertices[1] + i.planetvectors[1] * 58800
        this.moon.vertices = np.array([0, 0])

    def draw(this, screen, planets, origin):
        for i in planets:
            if i == p1.anothaone:
                screen.blit(meme1, p1.anothaone.vertices+origin-75)
            elif i == p1.earth:
                screen.blit(meme2, p1.earth.vertices+origin-50)
            elif i == p1.moon:
                screen.blit(meme3, p1.moon.vertices+origin-40)
            elif i != p1.rocket:
                pygame.draw.circle(
                    screen,
                    i.color,
                    ((i.vertices[0]) + width / 2, (i.vertices[1]) + height / 2),
                    i.radius,
                )


class landerclass:
    def __init__(this):
        this.top = halfLanderClass(
            np.array(
                [
                    (485.0, 50.0),
                    (515.0, 50.0),
                    (535.0, 65.0),
                    (535.0, 95.0),
                    (515.0, 110.0),
                    (485.0, 110.0),
                    (465.0, 95.0),
                    (465.0, 65.0),
                ]
            ),
            emptyVectors.copy(),
            (74, 74, 74),
            2445,
            15000,
            8376,
        )
        this.bottom = halfLanderClass(
            np.array(
                [
                    (485.0, 110.0),
                    (515.0, 110.0),
                    (550.0, 135.0),
                    (540.0, 135.0),
                    (505.0, 115.0),
                    (495.0, 115.0),
                    (460.0, 135.0),
                    (450.0, 135.0),
                ]
            ),
            emptyVectors.copy(),
            (255, 255, 255),
            2034,
            45000,
            8248,
        )

    def update(
        this, split: bool, crash: bool, pressed: dict
    ) -> tuple[bool, bool, int, int]:
        totalmass = this.top.mass + this.bottom.mass if not split else this.top.mass
        finalthrust = 3000 / totalmass if not split else 2175 / totalmass
        objlist = [this.top] if split else [this.bottom, this.top]
        downforce = this.bottom.vectors[5][1] * totalmass
        sideforce = this.bottom.vectors[5][0] * totalmass

        for i in range(8):
            for key in [
                (pressed["thrust"], 1, 1),
                (pressed["left"], 0, 1 / 2),
                (pressed["right"], 0, -1 / 2),
                (
                    True if this.top.vertices[7][1] < 685 else False,
                    1,
                    -1.62 / 4 / finalthrust,
                ),
            ]:
                if key[0]:
                    for obj in objlist:
                        obj.vectors[i][key[1]] -= finalthrust * key[2]

        if not split:
            if this.top.vertices[7][1] < 685:
                for obj in objlist:
                    obj.vertices += obj.vectors
            else:
                if downforce < 15000 and abs(sideforce) < 5000:
                    split = True
                    this.top.vectors = emptyVectors.copy()
                else:
                    crash = True
        elif split:
            this.top.vertices += this.top.vectors
        return (split, crash, downforce, sideforce)

    def draw(this, split: bool, pressed: dict):
        pygame.draw.rect(screen, (148, 148, 148), pygame.Rect(0, 760, 1500, 800))
        screen.blit(meme2, (100,100))
        screen.blit(meme3, (1300,50))
        screen.blit(meme1, (300,300))
        if pressed["thrust"]:
            pygame.draw.polygon(
                screen,
                (255, 0, 0),
                (
                    [
                        (this.top.vertices[1][0], this.top.vertices[1][1] + 55),
                        (this.top.vertices[1][0] - 30, this.top.vertices[1][1] + 55),
                        (this.top.vertices[1][0] - 15, this.top.vertices[1][1] + 100),
                    ]
                ),
            )
        for x in [(pressed["left"], 2, 3, 1), (pressed["right"], 7, 6, -1)]:
            if x[0]:
                pygame.draw.polygon(
                    screen,
                    (255, 0, 0),
                    (
                        [
                            (
                                this.top.vertices[x[1]][0],
                                this.top.vertices[x[1]][1] + 10,
                            ),
                            (
                                this.top.vertices[x[2]][0],
                                this.top.vertices[x[2]][1] - 10,
                            ),
                            (
                                this.top.vertices[x[1]][0] + 10 * x[3],
                                this.top.vertices[x[1]][1] + 15,
                            ),
                        ]
                    ),
                )
        for obj in [this.bottom, this.top]:
            pygame.draw.polygon(screen, obj.color, (obj.vertices))
        show = this.bottom if split == False else this.top
        Text = font.render("Fuel: " + str(show.fuel), False, (255, 255, 255))
        screen.blit(Text, (20, 20))

    def drawaftercrash(this, num: int, downforce: float, sideforce: float) -> int:
        pygame.draw.rect(screen, (148, 148, 148), pygame.Rect(0, 760, 1500, 800))
        pygame.draw.circle(screen, (0, 0, 0), (this.top.vertices[1][0] - 15, 500), 290)
        if num < 200:
            num += 10
            for obj, value in [(this.bottom, 3), (this.top, 5)]:
                pygame.draw.polygon(
                    screen, obj.color, (obj.vertices - num * obj.vectors[5][1] / value)
                )
            for num2, color in [
                (0, (255, 0, 0)),
                (30, (255, 80, 0)),
                (100, (255, 120, 0)),
            ]:
                if num > num2:
                    pygame.draw.circle(
                        screen, color, (this.top.vertices[1][0] - 15, 670), num - num2
                    )
        if downforce > 15000 and abs(sideforce) > 5000:
            Text = smallfont.render(
                "Both your sideforce and downforce were too high so you crashed!",
                False,
                (255, 255, 255),
            )
        else:
            for force, limit, text in [
                (downforce, 15000, "downforce"),
                (sideforce, 5000, "sideforce"),
            ]:
                if abs(force) > limit:
                    Text = smallfont.render(
                        "Your " + text + " was too high so you crashed!",
                        False,
                        (255, 255, 255),
                    )
        screen.blit(Text, (20, 20))
        return num


class halfLanderClass:
    def __init__(
        this,
        vertices: list,
        vectors: list,
        color: tuple,
        mass: int,
        maxthrust: float,
        fuel: int,
        radius=20,
        angle=-math.pi / 2,
        angleVect=0,
    ):
        this.vertices = vertices
        this.vectors = vectors
        this.mass = mass
        this.color = color
        this.maxthrust = maxthrust
        this.fuel = fuel
        this.radius = radius
        this.angle = angle
        this.angleVect = angleVect
        this.mass = mass

    def fuelcheck(this, keys: dict) -> dict:
        booleans = {"thrust": False, "left": False, "right": False}
        if this.fuel < 0:
            this.fuel = 0
        for fuelthing in [
            (keys[pygame.K_w], "thrust", 1),
            (keys[pygame.K_a], "left", 1 / 2),
            (keys[pygame.K_d], "right", 1 / 2),
        ]:
            if fuelthing[0] and this.fuel > 0:
                booleans[fuelthing[1]] = True
                this.fuel -= 75 * float(fuelthing[2])
                this.mass -= 10 * float(fuelthing[2])
        return {
            "thrust": booleans["thrust"],
            "left": booleans["left"],
            "right": booleans["right"],
        }


def getDistance(obj1, obj2):
    return math.dist(obj1.vertices, obj2.vertices)


width = 1500
height = 800
run = True
FPS = 30
num = int(1)
# Using blit to copy content from one surface to other

emptyVectors = np.array(
    [
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
    ]
)
phase = "p1"
originpoints = [width / 2, height / 2]
split, crash, wreset = False, False, False
p1: p1class = p1class()
lander: landerclass = landerclass()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lunar Lander")
font = pygame.font.Font(None, 50)
smallfont = pygame.font.Font(None, 35)
planets = [p1.moon, p1.rocket, p1.earth, p1.anothaone]


meme1 = pygame.image.load("./meme.png").convert()
meme1 = pygame.transform.scale(meme1, (100, 100))

meme2 = pygame.image.load("./meme2.jpg").convert()
meme2 = pygame.transform.scale(meme2, (80, 80))

meme3 = pygame.image.load("./meme3.jpg").convert()
meme3 = pygame.transform.scale(meme3, (150, 150))


from pygame import mixer 

mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(1)
mixer.music.play()
2
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            run = False
    pygame.time.Clock().tick(FPS)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if phase == "p1":
        pressed = p1.rocket.fuelcheck(keys)
        p1.rocket.update(pressed)
        p1.rocket.draw(pressed)
        p1.update(planets)
        p1.draw(screen, planets, originpoints)
        if getDistance(p1.moon, p1.rocket) <= 100:
            angle = math.atan2(
                (p1.rocket.vertices[1] - p1.moon.vertices[1]), (p1.rocket.vertices[0] - p1.moon.vertices[0])
            )
            for obj in [lander.top, lander.bottom]:
                for i in range(8):
                    obj.vectors[i][0] += math.cos(angle) * 5
                    obj.vectors[i][1] += math.sin(angle) * 5
                    # obj.vectors[i][0] += p1.rocket.planetvectors[0] * 70000
                    # obj.vectors[i][1] += (
                    #     p1.rocket.vectors[1] + p1.rocket.planetvectors[1] * 70000
                    # )
            phase = "p2"
    elif phase == "p2":
        if crash == False:
            pressed = (lander.bottom if split == False else lander.top).fuelcheck(keys)
            split, crash, downforce, sideforce = lander.update(split, crash, pressed)
            lander.draw(split, pressed)
        else:
            num = lander.drawaftercrash(num, downforce, sideforce)
    pygame.display.update()