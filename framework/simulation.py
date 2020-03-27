import numpy as np
import pygame
import individual


class Simulation():
    """Simulation handles pygame and important variables"""

    def __init__(self):
        pygame.init()
        self.size = 700
        self.display = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Natural Selection")
     
        self.population = []

    def run(self):
        """ Main loop """
        self.spawn(15)

        run = True
        while run:
            time = pygame.time.get_ticks()  # Gets the total elapsed time (milliseconds)

            for event in pygame.event.get():    # Listen for pygame events
                if event.type == pygame.QUIT:
                    run = False

            self.act()
            self.draw()

        pygame.quit()

    def spawn(self, num):
        """ Adds a number of individuals to our population at randon positions """
        for _ in range(num):
            pos = np.random.random(2) * self.size
            self.population.append(individual.Individual(pos))

    def act(self):
        """ Executes all the individual processes """
        for individual in self.population:
            individual.move()

    def draw(self):
        """ Draws each frame """
        self.display.fill((0, 0, 0))

        for individual in self.population:
            individual.draw(self.display)
        pygame.display.update()


if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()
