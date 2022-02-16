import pygame
from pygame.constants import K_ESCAPE, K_RIGHT, QUIT
pygame.init()


class Player1:
    def __init__(self, X_or_O, player_num):
        """Initialization of Player 1 choice"""
        self.X_or_O = X_or_O
        self.player_num = player_num
    def player_number(self):
        return self.player_num
    def player_choice(self):
        print(f"Player {self.player_num}'s choice is {self.X_or_O}.")
    def player_XorO(self):
        return self.X_or_O

class Player2(Player1):
    def __init__(self, X_or_O, player_num):
        """Initialization of Player 2 choice, same as Player 1"""
        self.X_or_O = X_or_O
        self.player_num = player_num
# PyGame Variables
display_width, display_height = 500, 500
x=40
y=10

"""Colors"""
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
transparent = (0, 0, 0, 0)


pygame.display.set_caption("Tic-Tac-Toe")
win = pygame.display.set_mode((display_width, display_height))
# game_screen = pygame.Surface((display_width, display_height))
# game_screen.set_alpha(0)
win.fill((255, 255, 255))
pygame.display.update()

font_size = 30
font = pygame.font.SysFont(None, font_size)

def reset_screen():
    win.fill(white)
    pygame.display.update()

def draw_text(msg, rect_color, text_color, left_gap, x, y):
    screen_text = font.render(msg, True, text_color)
    pygame.draw.rect(win, rect_color, (x-left_gap, y, display_width/2+left_gap+10, 30))
    win.blit(screen_text, [x, y+8])
    pygame.display.update()

def draw_line(line_color, coord1, coord2, thicc):
    pygame.draw.line(win, line_color, coord1, coord2, thicc)
    pygame.display.update()

def draw_grid():
    draw_line(black, (100, 150), (400, 150), 5)
    draw_line(black, (100, 250), (400, 250), 5)
    draw_line(black, (200, 50), (200, 350), 5)
    draw_line(black, (300, 50), (300, 350), 5)

def draw_x(x, y):
    draw_line(black, (x, y), (x+100, y+100), 5)
    draw_line(black, (x+100, y), (x, y+100), 5)

def draw_o(color, x, y, width):
    pygame.draw.circle(win, color, (x, y), 50, width=width)
    pygame.display.update()

def draw_rect(color, x, y, width, height):
    pygame.draw.rect(win, color, pygame.Rect(x, y, width, height))
    pygame.display.update()

def show_grid():
    print('{:-<10}'.format(""))
    print(f"{grid_spaces[0]} | {grid_spaces[1]} | {grid_spaces[2]}\n{grid_spaces[3]} | {grid_spaces[4]} | {grid_spaces[5]}\n{grid_spaces[6]} | {grid_spaces[7]} | {grid_spaces[8]}")
    print('{:-<10}'.format(""))

def check_grid_spot(spot_index): 
    """True if spot_index not taken"""
    if spot_index in grid_spaces:
        return True
    else:
        print("Space already taken! Choose another.")
        return False

def start_screen():
    """Display starting screen, then flip screen"""
    draw_text("Welcome to Tic-Tac-Toe", white, black, 10, display_width/4, display_height/4)
    draw_text("Press Any Button to Start", red, black, 10, (display_width/4), display_height/2)
    pygame.display.update()

def player1_win_screen():
    """Display Win Screen for Player 1"""
    draw_text("Player 1 Wins!", white, black, 10, display_width/3, display_height/4)
    pygame.display.update()

def player2_win_screen():
    """Display Win Screen for Player 2"""
    draw_text("Player 2 Wins!", white, black, 10, display_width/3, display_height/4)
    pygame.display.update()

def tie_end_screen():
    """End Screen when tie occurs"""
    draw_text("No One Wins!", white, black, 10, display_width/3, display_height/4)
    pygame.display.update()

def win_game():
    """Check if the player won the game"""
    """
       grid example
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8
    """
    # Player 1
    if grid_spaces[0] == 'X' and grid_spaces[1] == 'X' and grid_spaces[2] == 'X': # Top Row
        return 1
    elif grid_spaces[3] == 'X' and grid_spaces[4] == 'X' and grid_spaces[5] == 'X': # Middle Row
        return 1
    elif grid_spaces[6] == 'X' and grid_spaces[7] == 'X' and grid_spaces[8] == 'X': # Bottom Row
        return 1
    elif grid_spaces[0] == 'X' and grid_spaces[4] == 'X' and grid_spaces[8] == 'X': # Top Left to Bottom Right
        return 1
    elif grid_spaces[6] == 'X' and grid_spaces[4] == 'X' and grid_spaces[2] == 'X': # Bottom Left to Top Right
        return 1
    elif grid_spaces[0] == 'X' and grid_spaces[3] == 'X' and grid_spaces[6] == 'X': # Left Column
        return 1
    elif grid_spaces[1] == 'X' and grid_spaces[4] == 'X' and grid_spaces[7] == 'X': # Middle Column
        return 1
    elif grid_spaces[2] == 'X' and grid_spaces[5] == 'X' and grid_spaces[8] == 'X': # Right Column
        return 1   

    # Player 2
    elif grid_spaces[0] == 'O' and grid_spaces[1] == 'O' and grid_spaces[2] == 'O': # Top Row
        return 2
    elif grid_spaces[3] == 'O' and grid_spaces[4] == 'O' and grid_spaces[5] == 'O': # Middle Row
        return 2
    elif grid_spaces[6] == 'O' and grid_spaces[7] == 'O' and grid_spaces[8] == 'O': # Bottom Row
        return 2
    elif grid_spaces[0] == 'O' and grid_spaces[4] == 'O' and grid_spaces[8] == 'O': # Top Left to Bottom Right
        return 2
    elif grid_spaces[6] == 'O' and grid_spaces[4] == 'O' and grid_spaces[2] == 'O': # Bottom Left to Top Right
        return 2
    elif grid_spaces[0] == 'O' and grid_spaces[3] == 'O' and grid_spaces[6] == 'O': # Left Column
        return 2
    elif grid_spaces[1] == 'O' and grid_spaces[4] == 'O' and grid_spaces[7] == 'O': # Middle Column
        return 2
    elif grid_spaces[2] == 'O' and grid_spaces[5] == 'O' and grid_spaces[8] == 'O': # Right Column
        return 2
    else:
        return False # NO MATCHES



grid_spaces = ["-" for i in range(9)]
p1 = Player1("X", 1)
p2 = Player2("O", 2)

def main():
    start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                reset_screen()
                running = False
            elif event.type == pygame.KEYDOWN:
                reset_screen()
                running = False
    draw_text("Player 1: X   Player 2: O", white, red, 10, display_width/4, 0)
    draw_grid()
    # Game Variables
           
    p1.player_choice()
    p2.player_choice()

    running = True
    current_turn = 0
    while running:
        """If all spots are taken"""
        if not "-" in grid_spaces:
            running = False
        elif win_game():
            running = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                    print("Exit Game.")
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        print("Exit Game.")
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if current_turn == 0:
                        if event.button == 1:
                            mouse_pos = pygame.mouse.get_pos()
                            print(mouse_pos)
                            if mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(50, 150):
                                print("P1 TL")
                                draw_x(100, 50)
                                grid_spaces[0] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(50, 150):
                                print("P1 TM")
                                draw_x(200, 50)
                                grid_spaces[1] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(50, 150):
                                print("P1 TR")
                                draw_x(300, 50)
                                grid_spaces[2] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(150, 250):
                                print("P1 ML")
                                draw_x(100, 150)
                                grid_spaces[3] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(150, 250):
                                print("P1 M")
                                draw_x(200, 150)
                                grid_spaces[4] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(150, 250):
                                print("P1 MR")
                                draw_x(300, 150)
                                grid_spaces[5] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(250, 350):
                                print("P1 BL")
                                draw_x(100, 250)
                                grid_spaces[6] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(250, 350):
                                print("P1 BM")
                                draw_x(200, 250)
                                grid_spaces[7] = 'X'
                                show_grid()
                                current_turn = 1
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(250, 350):
                                print("P1 BR")
                                draw_x(300, 250)
                                grid_spaces[8] = 'X'
                                show_grid()
                                current_turn = 1
                            
                    else:
                        if event.button == 1:
                            mouse_pos = pygame.mouse.get_pos()
                            print(mouse_pos)
                            if mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(50, 150):
                                print("P2 TL")
                                draw_o(black, 150, 100, 5)
                                grid_spaces[0] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(50, 150):
                                print("P2 TM")
                                draw_o(black, 250, 100, 5)
                                grid_spaces[1] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(50, 150):
                                print("P2 TR")
                                draw_o(black, 350, 100, 5)
                                grid_spaces[2] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(150, 250):
                                print("P2 ML")
                                draw_o(black, 150, 200, 5)
                                grid_spaces[3] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(150, 250):
                                print("P2 M")
                                draw_o(black, 250, 200, 5)
                                grid_spaces[4] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(150, 250):
                                print("P2 MR")
                                draw_o(black, 350, 200, 5)
                                grid_spaces[5] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(100, 200) and mouse_pos[1] in range(250, 350):
                                print("P2 BL")
                                draw_o(black, 150, 300, 5)
                                grid_spaces[6] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(200, 300) and mouse_pos[1] in range(250, 350):
                                print("P2 BM")
                                draw_o(black, 250, 300, 5)
                                grid_spaces[7] = 'O'
                                show_grid()
                                current_turn = 0
                            elif mouse_pos[0] in range(300, 400) and mouse_pos[1] in range(250, 350):
                                print("P2 BR")
                                draw_o(black, 350, 300, 5)
                                grid_spaces[8] = 'O'
                                show_grid()
                                current_turn = 0
                            
    if win_game() == False:
        print("Game Over. No One Wins!")
        pygame.time.wait(1500)
        reset_screen()
        tie_end_screen()
        pygame.time.wait(3000)
    elif win_game() == 1:
        print("Player 1 Wins!")
        pygame.time.wait(1500)
        reset_screen()
        player1_win_screen()
        pygame.time.wait(3000)
    elif win_game() == 2:
        print("Player 2 Wins!")
        pygame.time.wait(1500)
        reset_screen()
        player2_win_screen()
        pygame.time.wait(3000)
    elif win_game() == 3:
        print("Game Exit.")


    pygame.quit()

if __name__ == "__main__":
    main()