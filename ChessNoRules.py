#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pygame python-chess


# In[ ]:


pip install --upgrade pygame


# In[ ]:


import pygame

pygame.init()

tiles = 50
WIN = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chess")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


# In[1]:





# In[1]:


import pygame
pygame.init()
pygame.display.init()


tiles = 50
win = pygame.display.set_mode((400, 400))

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p'] * 8,
    [' '] * 8,
    [' '] * 8,
    [' '] * 8,
    [' '] * 8,
    ['P'] * 8,
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

font = pygame.font.SysFont("Cambria", 36)

def is_valid_move(start, end):
    return True


def draw_board(win, tiles, selected=None):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    highlight = (0, 255, 0)
    for i in range(8):
        for j in range(8):
            colour = white if (i + j) % 2 == 0 else blue
            pygame.draw.rect(win, colour, (i * tiles, j * tiles, tiles, tiles))
    if selected:
        # Highlight the selected square with a green border
        pygame.draw.rect(win, highlight, (selected[1] * tiles, selected[0] * tiles, tiles, tiles), 3)

def draw_pieces(win, board, font):
    for a in range(8):
        for b in range(8):
            piece = board[a][b]
            if piece != ' ':
                color = pygame.Color('black') if piece.isupper() else pygame.Color('gray')
                text = font.render(piece, True, color)
                win.blit(text, (b * tiles + 12, a * tiles + 8))


running = True
selected = None
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
          
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // tiles
            row = y // tiles
            pygame.display.update()

            if selected:
                # Attempt to move piece to (row, col)
                if is_valid_move(selected, (row, col)):
                    board[row][col] = board[selected[0]][selected[1]]
                    board[selected[0]][selected[1]] = ' '
                selected = None  # Reset selection after move
                pygame.display.update()
            else:
                # Select piece if present
                if board[row][col] != ' ':
                    selected = (row, col)
                    
    draw_board(win, tiles, selected)
    draw_pieces(win, board, font)
    pygame.display.update()

pygame.quit()
exit()


# In[ ]:


def draw_board(win, tiles, selected=None):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    highlight = (0, 255, 0)
    for i in range(8):
        for j in range(8):
            colour = white if (i + j) % 2 == 0 else blue
            pygame.draw.rect(win, colour, (i * tiles, j * tiles, tiles, tiles))
    if selected:
        # Highlight the selected square with a green border
        pygame.draw.rect(win, highlight, (selected[1] * tiles, selected[0] * tiles, tiles, tiles), 3)

def draw_pieces(win, board, font):
    for a in range(8):
        for b in range(8):
            piece = board[a][b]
            if piece != ' ':
                color = pygame.Color('black') if piece.isupper() else pygame.Color('gray')
                text = font.render(piece, True, color)
                win.blit(text, (b * tiles + 12, a * tiles + 8))

            

