import sys
from threading import Thread
from numpy import random
import pygame
from pygame.locals import *
from model.DataCenter import DataCenter
from algorithms.search.HillClimbing import HillClimbing
from algorithms.search.SimulatedAnnealing import SimulatedAnnealing
from algorithms.search.TabuSearch import TabuSearch
from algorithms.genetic.GeneticAlgorithm import GeneticAlgorithm


WHITE = '#FFFFFF'
DARK_BLUE = '#306A8A'
GREY = '#4A5D68'
BLUE = '#5A9BC0'
BG_COLOR = '#1E4154'
RED = '#FF0000'
YELLOW = '#FFFF00'
GREEN = '#00FF00'
PINK = '#FFC0CB'
ORANGE = '#FFA500'
PURPLE = '#6A0DAD'
BLACK = '#000000'
BASE_COLOR = (48, 106, 138)

SCREEN = pygame.display.set_mode((1800, 900))

class Gui():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Optimization problem")

        self.width, self.height = 1800, 900
        self.screen = SCREEN
        self.clock = pygame.time.Clock()

        self.menu = MainMenu()

    def check_events(self):
        new_menu = self.menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                new_menu = self.menu.click_events(event)
                continue
            if event.type == pygame.KEYDOWN:
                self.menu.key_events(event)
                continue
            if event.type == pygame.MOUSEMOTION:
                self.menu.hover_events(event)

        self.menu = new_menu

    def loop(self):
        while True:
            self.screen.fill(BG_COLOR)
            self.check_events()
            self.menu.draw()

            pygame.display.flip()
            self.clock.tick(60)

class Menu():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        pass

    def click_events(self, event):
        pass

    def key_events(self, event):
        pass

    def hover_events(self, event):
        pass

    def draw_main_menu_button(self, offset_y=0):
        font = pygame.font.SysFont('gillsans', 40)
        self.mainMenuButton = pygame.Rect(1400, 20 - offset_y, 210, 70)
        pygame.draw.rect(self.display_surface, BLUE,
                         self.mainMenuButton, 0, 10)
        mainMenuText = font.render('Main Menu', True, WHITE)
        self.display_surface.blit(
            mainMenuText, (1505 - (mainMenuText.get_width()/2), 55 - offset_y - (mainMenuText.get_height()/2)))

class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.user_text = 'input.txt'
        self.input_rect = pygame.Rect(1250, 700, 140, 55)
        self.start_circle = pygame.Rect(800, 450, 280, 100)
        self.input_circle = pygame.Rect(1250, 700, 120, 80)
        self.info_circle = pygame.Rect(1200, 250, 180, 80)

    def draw(self):
        font = pygame.font.SysFont('gillsans', 80)

        pygame.draw.circle(self.display_surface, DARK_BLUE, (900, 500), 200)
        pygame.draw.circle(self.display_surface, GREY, (1400, 700), 160)
        pygame.draw.circle(self.display_surface, BLUE, (1300, 300), 110)

        title_1 = font.render('OPTIMIZE A DATA', True, WHITE)
        title_2 = font.render('CENTER', True, WHITE)
        self.display_surface.blit(title_1, (20, 40))
        self.display_surface.blit(title_2, (20, 110))

        start = font.render('START', True, WHITE)
        self.display_surface.blit(start, (800, 450))

        font = pygame.font.SysFont('gillsans', 40)
        info_1 = font.render('Additional', True, WHITE)
        info_2 = font.render('info', True, WHITE)
        self.display_surface.blit(info_1, (1220, 250))
        self.display_surface.blit(info_2, (1270, 280))

        pygame.draw.rect(self.display_surface, GREY, self.input_rect, 1)
        text_surface = font.render(self.user_text, True, WHITE)
        self.display_surface.blit(
            text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        self.input_rect.w = max(100, text_surface.get_width()+10)

    def click_events(self, event):
        if self.start_circle.collidepoint(event.pos):
            return AlgorithmMenu(self.user_text)
        elif self.info_circle.collidepoint(event.pos):
            return InstructionsMenu()
        return self

    def key_events(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.user_text = self.user_text[:-1]
        elif len(self.user_text) <= 15:
            self.user_text += event.unicode

    def hover_events(self, event):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.start_circle.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.input_circle.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        elif self.info_circle.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

class AlgorithmMenu(Menu):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.hill_climbing_rect = pygame.Rect(225, 300, 700, 130)
        self.simulated_annealing_rect = pygame.Rect(225, 500, 700, 130)
        self.genetic_rect = pygame.Rect(975, 300, 700, 130)
        self.tabu_search_rect = pygame.Rect(975, 500, 700, 130)
        self.rect_collision = [False for _ in range(4)]
        self.data_center = DataCenter(file)

    def draw(self):
        font = pygame.font.SysFont('gillsansnegrito', 80)
        title = font.render('Algorithms', True, WHITE)
        self.display_surface.blit(title, (20, 40))

        self.draw_main_menu_button()

        pygame.draw.rect(self.display_surface, GREY, self.hill_climbing_rect,
                         0 if self.rect_collision[0] else 1, 10)
        pygame.draw.rect(self.display_surface, GREY, self.simulated_annealing_rect,
                         0 if self.rect_collision[1] else 1, 10)
        pygame.draw.rect(self.display_surface, GREY, self.genetic_rect,
                         0 if self.rect_collision[2] else 1, 10)
        pygame.draw.rect(self.display_surface, GREY, self.tabu_search_rect,
                         0 if self.rect_collision[3] else 1, 10)

        algorithms = [('Hill climbing', 575, 320), ('Simulated Annealing',
                                                    575, 520), ('Genetic', 1325, 320), ('Tabu Search', 1325, 520)]
        font = pygame.font.SysFont('gillsansnegrito', 70)

        for algorithm in algorithms:
            alg_text, x, y = algorithm

            text = font.render(alg_text, True, WHITE)
            x -= text.get_size()[0] // 2
            self.display_surface.blit(text, (x, y))

    def click_events(self, event):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.hill_climbing_rect.collidepoint(event.pos):
            return SolutionMenu(HillClimbing(self.data_center.solution))
        elif self.simulated_annealing_rect.collidepoint(event.pos):
            return SolutionMenu(SimulatedAnnealing(self.data_center.solution))
        elif self.genetic_rect.collidepoint(event.pos):
            return SolutionMenu(GeneticAlgorithm(self.data_center.solution))
        elif self.tabu_search_rect.collidepoint(event.pos):
            return SolutionMenu(TabuSearch(self.data_center.solution))
        elif self.mainMenuButton.collidepoint(event.pos):
            return MainMenu()
        return self

    def key_events(self, event):
        pass

    def hover_events(self, event):
        self.rect_collision = [False for _ in range(4)]
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.hill_climbing_rect.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.rect_collision[0] = True

        elif self.simulated_annealing_rect.collidepoint(event.pos):
            self.rect_collision[1] = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif self.genetic_rect.collidepoint(event.pos):
            self.rect_collision[2] = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif self.tabu_search_rect.collidepoint(event.pos):
            self.rect_collision[3] = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif self.mainMenuButton.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

class InstructionsMenu(Menu):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('gillsans', 40)

    def draw(self):
        font = pygame.font.SysFont('gillsansnegrito', 80)
        title = font.render('Instructions', True, WHITE)
        self.display_surface.blit(title, (20, 40))

        self.draw_main_menu_button()

        inst_array = []
        inst_array.append(self.font.render(
            'Given a schema of a data center and a list of available servers, the goal is to assign servers to slots', True, WHITE))
        inst_array.append(self.font.render(
            'within the rows and to logical pools so that the lowest guaranteed capacity of all pools is maximized.', True, WHITE))
        inst_array.append(self.font.render(
            'Servers are physically divided into rows.', True, WHITE))
        inst_array.append(self.font.render(
            'Rows share resources, therefore if a resource fails in a row, all servers in that row become unavailable.', True, WHITE))
        inst_array.append(self.font.render(
            'Servers are also logically divided into pools. Each server belongs to exactly one pool, and provides it', True, WHITE))
        inst_array.append(self.font.render(
            'with some amount of computing resources, called capacity, c.', True, WHITE))
        inst_array.append(self.font.render(
            'The capacity of a pool is the sum of the capacities, ci, of the available servers in that pool.', True, WHITE))
        inst_array.append(self.font.render(
            'To ensure reliability of a pool, it is therefore desirable to distribute its servers between different rows.', True, WHITE))
        inst_array.append(self.font.render(
            'The guaranteed capacity of a pool is the minimum capacity it will have when at most one data center', True, WHITE))
        inst_array.append(self.font.render('row goes down.', True, WHITE))

        for i, text in enumerate(inst_array):
            self.display_surface.blit(text, (40, 150 + 50 * i))

    def click_events(self, event):
        if self.mainMenuButton.collidepoint(event.pos):
            return MainMenu()
        return self

    def key_events(self, event):
        pass

    def hover_events(self, event):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.mainMenuButton.collidepoint(event.pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

class SolutionMenu(Menu):
    def __init__(self, algorithm):
        super().__init__()
        self.algorithm = algorithm
        self.loading = True

        self.offset = pygame.math.Vector2(0, 0)
        self.font = pygame.font.SysFont('gillsansnegrito', 80)

        thread = Thread(target=self.algorithm.execute,
                        args=[self.finish_execute])
        thread.start()

    def finish_execute(self, solution):
        self.solution = solution
        print(solution)
        self.loading = False
        self.set_max_offset()
        self.set_pool_colors()

    def set_pool_colors(self):
        self.pool_color = [list(random.choice(range(256), size=3))
                           for _ in range(self.solution.pools)]

    def set_max_offset(self):
        rows = self.solution.rows
        max_offset_y = max(len(rows), self.solution.pools)
        max_offset = pygame.math.Vector2(
            250 + len(rows[0].slots) * 60, 250 + max_offset_y * 60)
        self.max_offset = max_offset - pygame.math.Vector2(1800, 900)

    def draw(self):
        if self.loading:
            title = self.font.render('Calculating best solution', True, WHITE)
            self.display_surface.blit(title, (700, 400))
            return

        self.input()

        font = pygame.font.SysFont('gillsans', 40)
        small_font = pygame.font.SysFont('gillsans', 20)

        self.draw_main_menu_button(self.offset.y)

        title = self.font.render('Solution', True, WHITE)
        self.display_surface.blit(title, (20, 40-self.offset.y))
        rows, servers = self.solution.rows, self.solution.servers

        evaluation = font.render(
            f'Minimum guaranteed capacity is {self.solution.evaluation}', True, WHITE)
        self.display_surface.blit(evaluation, (120, 120-self.offset.y))

        for row_idx, row in enumerate(rows):
            for slot_idx, slot in enumerate(row.slots):
                rect = pygame.Rect(
                    200 + (slot_idx*60) - self.offset.x, 200 + (row_idx*60) - self.offset.y, 50, 50)
                if slot == -2:
                    color = RED
                elif slot == -1:
                    color = BLACK
                else:
                    color = self.pool_color[servers[slot].pool]

                pygame.draw.rect(self.display_surface, color, rect, 0, 10)

                if slot >= 0:  # Draw server text
                    server_text = small_font.render(f'S {slot}', True, WHITE)
                    self.display_surface.blit(
                        server_text, (rect.left + 5, rect.bottom - server_text.get_height()))

        for pool in range(self.solution.pools):
            color = self.pool_color[pool]

            rect = pygame.Rect(100 - self.offset.x, 200 +
                               (pool*60) - self.offset.y, 50, 50)
            pygame.draw.rect(self.display_surface, color, rect, 0, 10)

            pool_txt = font.render(f'P {pool}', True, WHITE)
            self.display_surface.blit(
                pool_txt, (15 - self.offset.x, 200 + (pool*60)-self.offset.y))

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.offset.x = new_offset if (
                new_offset := self.offset.x - 20) >= 0 else self.offset.x
        elif keys[pygame.K_RIGHT]:
            self.offset.x = new_offset if (
                new_offset := self.offset.x + 20) <= self.max_offset.x else self.offset.x
        if keys[pygame.K_UP]:
            self.offset.y = new_offset if (
                new_offset := self.offset.y - 20) >= 0 else self.offset.y
        elif keys[pygame.K_DOWN]:
            self.offset.y = new_offset if (
                new_offset := self.offset.y + 20) <= self.max_offset.y else self.offset.y

    def click_events(self, event):
        if self.loading:
            return self

        if self.mainMenuButton.collidepoint(event.pos):
            return MainMenu()
        return self

    def key_events(self, event):
        pass

    def hover_events(self, event):
        if self.loading:
            return

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if hasattr(self, 'mainMenuButton'):
            if self.mainMenuButton.collidepoint(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
