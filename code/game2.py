import pygame
import sys
import threading
import keyboard  # 导入keyboard库

# 初始化 Pygame
pygame.init()

# 设置窗口大小 (10x10 的格子，每个格子大小为 80x80 像素)
grid_size = 10
cell_size = 80
window_size = grid_size * cell_size
screen = pygame.display.set_mode((window_size, window_size))

# 设置颜色
WHITE = (255, 255, 255)

# 小人的初始位置
player1_pos = [grid_size // 2, grid_size // 2]  # 小人1从中心开始
player2_pos = [grid_size // 2 - 1, grid_size // 2 - 1]  # 小人2初始位置不重叠

# 加载小人图片
player1_image = pygame.image.load('player1.jpg')
player1_image = pygame.transform.smoothscale(player1_image, (cell_size, cell_size))
player2_image = pygame.image.load('player2.jpg')
player2_image = pygame.transform.smoothscale(player2_image, (cell_size, cell_size))

# 创建时钟对象，控制帧率
clock = pygame.time.Clock()

# 线程锁，确保线程安全
lock = threading.Lock()

def draw_grid():
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, WHITE, rect, 1)

def move_player(player_pos, direction):
    new_pos = player_pos.copy()
    if direction == 'up' and player_pos[1] > 0:
        new_pos[1] -= 1
    elif direction == 'down' and player_pos[1] < grid_size - 1:
        new_pos[1] += 1
    elif direction == 'left' and player_pos[0] > 0:
        new_pos[0] -= 1
    elif direction == 'right' and player_pos[0] < grid_size - 1:
        new_pos[0] += 1
    return new_pos

def check_overlap(pos1, pos2):
    return pos1 == pos2

# 小人1控制的线程 (上下左右)
def player1_control():
    global player1_pos
    while True:
        with lock:
            new_player1_pos = player1_pos.copy()
            if keyboard.is_pressed('up'):
                new_player1_pos = move_player(player1_pos, 'up')
            elif keyboard.is_pressed('down'):
                new_player1_pos = move_player(player1_pos, 'down')
            elif keyboard.is_pressed('left'):
                new_player1_pos = move_player(player1_pos, 'left')
            elif keyboard.is_pressed('right'):
                new_player1_pos = move_player(player1_pos, 'right')

            # 检查是否和小人2重叠
            if not check_overlap(new_player1_pos, player2_pos):
                player1_pos = new_player1_pos

        pygame.time.delay(100)

# 小人2控制的线程 (WASD)
def player2_control():
    global player2_pos
    while True:
        with lock:
            new_player2_pos = player2_pos.copy()
            if keyboard.is_pressed('w'):
                new_player2_pos = move_player(player2_pos, 'up')
            elif keyboard.is_pressed('s'):
                new_player2_pos = move_player(player2_pos, 'down')
            elif keyboard.is_pressed('a'):
                new_player2_pos = move_player(player2_pos, 'left')
            elif keyboard.is_pressed('d'):
                new_player2_pos = move_player(player2_pos, 'right')

            # 检查是否和小人1重叠
            if not check_overlap(new_player2_pos, player1_pos):
                player2_pos = new_player2_pos

        pygame.time.delay(100)

# 启动两个线程
threading.Thread(target=player1_control, daemon=True).start()
threading.Thread(target=player2_control, daemon=True).start()

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制背景和网格
    screen.fill((0, 0, 0))  # 填充黑色背景
    draw_grid()

    # 绘制小人1
    screen.blit(player1_image, (player1_pos[0] * cell_size, player1_pos[1] * cell_size))

    # 绘制小人2
    screen.blit(player2_image, (player2_pos[0] * cell_size, player2_pos[1] * cell_size))

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)
