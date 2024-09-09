import pygame
import sys
import keyboard  # 导入keyboard库

# 初始化 Pygame
pygame.init()

# 设置窗口大小 (10x10 的格子，每个格子大小为 40x40 像素)
grid_size = 10
cell_size = 80
window_size = grid_size * cell_size
screen = pygame.display.set_mode((window_size, window_size))

# 设置颜色
WHITE = (255, 255, 255)

# 小人的初始位置
player_pos = [grid_size // 2, grid_size // 2]  # 从中心开始

# 加载小人图片
player_image = pygame.image.load('player.jpg')
player_image = pygame.transform.smoothscale(player_image, (cell_size, cell_size))  # 使用平滑缩放减少模糊

# 创建时钟对象，控制帧率
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, WHITE, rect, 1)

def move_player():
    # 使用keyboard库检测WASD键
    if keyboard.is_pressed('w'):
        if player_pos[1] > 0:  # 向上移动
            player_pos[1] -= 1
    if keyboard.is_pressed('s'):
        if player_pos[1] < grid_size - 1:  # 向下移动
            player_pos[1] += 1
    if keyboard.is_pressed('a'):
        if player_pos[0] > 0:  # 向左移动
            player_pos[0] -= 1
    if keyboard.is_pressed('d'):
        if player_pos[0] < grid_size - 1:  # 向右移动
            player_pos[0] += 1

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 调用 move_player 函数
    move_player()

    # 绘制背景和网格
    screen.fill((0, 0, 0))  # 填充黑色背景
    draw_grid()

    # 绘制小人图片
    screen.blit(player_image, (player_pos[0] * cell_size, player_pos[1] * cell_size))

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)
