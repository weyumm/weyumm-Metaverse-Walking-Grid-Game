import pygame
import sys
import threading
import webbrowser  # 用于打开网页
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
initial_player1_pos = [grid_size // 2, grid_size // 2]  # 小人1从中心开始
initial_player2_pos = [grid_size // 2 - 1, grid_size // 2 - 1]  # 小人2初始位置不重叠
player1_pos = initial_player1_pos.copy()
player2_pos = initial_player2_pos.copy()

# 加载小人图片
player1_image = pygame.image.load('player1.jpg')
player1_image = pygame.transform.smoothscale(player1_image, (cell_size, cell_size))
player2_image = pygame.image.load('player2.jpg')
player2_image = pygame.transform.smoothscale(player2_image, (cell_size, cell_size))

# 加载事件贴图
event_image = pygame.image.load('book.jpg')
event_image = pygame.transform.smoothscale(event_image, (cell_size, cell_size))  # 缩放事件图片

# 加载事件所在格子的贴图
event_tile_image = pygame.image.load('book.jpg')
event_tile_image = pygame.transform.smoothscale(event_tile_image, (cell_size, cell_size))

# 创建时钟对象，控制帧率
clock = pygame.time.Clock()

# 事件触发格子位置
event_tile_pos = [0, grid_size - 1]  # 右上角格子 (0, 9)

# 事件触发标志
event_triggered = False

# 线程锁，确保线程安全
lock = threading.Lock()

def draw_grid():
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            if [x // cell_size, y // cell_size] == event_tile_pos:
                # 在事件所在的格子上绘制事件贴图
                screen.blit(event_tile_image, (x, y))  
            else:
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

def check_event_trigger(pos):
    return pos == event_tile_pos

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

            if not check_overlap(new_player1_pos, player2_pos):
                player1_pos = new_player1_pos
                if check_event_trigger(player1_pos):
                    trigger_event()

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

            if not check_overlap(new_player2_pos, player1_pos):
                player2_pos = new_player2_pos
                if check_event_trigger(player2_pos):
                    trigger_event()

        pygame.time.delay(100)

# 触发事件窗口
def trigger_event():
    global event_triggered
    event_triggered = True

# 事件弹窗界面绘制
def draw_event_popup():
    font = pygame.font.SysFont(None, 48)
    description_font = pygame.font.SysFont(None, 32)
    small_font = pygame.font.SysFont(None, 24)

    # 英文事件文本
    title_text = font.render("Event: Advanced Mathematics", True, (0, 0, 0))
    main_text = description_font.render("Congratulations, you have been hit by Advanced Mathematics!", True, (0, 0, 0))
    description_text = small_font.render("Vitality -10, Wisdom +5, Mood -3, Sanity -10", True, (0, 0, 0))

    # 按钮
    continue_button = small_font.render("Continue?", True, (255, 255, 255), (0, 128, 0))
    retry_button = small_font.render("Retry!", True, (255, 255, 255), (128, 0, 0))

    # 绘制弹窗背景
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 300, 200))
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 200), 2)

    # 绘制事件贴图
    screen.blit(event_image, (130, 80))  # 在弹窗上显示事件图片

    # 绘制文本
    screen.blit(title_text, (70, 60))
    screen.blit(main_text, (60, 120))
    screen.blit(description_text, (50, 160))

    # 绘制按钮
    pygame.draw.rect(screen, (0, 128, 0), (70, 220, 100, 40))
    pygame.draw.rect(screen, (128, 0, 0), (230, 220, 100, 40))
    screen.blit(continue_button, (80, 230))
    screen.blit(retry_button, (240, 230))

# 重置游戏
def reset_game():
    global player1_pos, player2_pos, event_triggered
    player1_pos = initial_player1_pos.copy()
    player2_pos = initial_player2_pos.copy()
    event_triggered = False  # 重置事件触发标志

# 启动两个线程
threading.Thread(target=player1_control, daemon=True).start()
threading.Thread(target=player2_control, daemon=True).start()

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event_triggered:
            mouse_pos = pygame.mouse.get_pos()
            if 70 <= mouse_pos[0] <= 170 and 220 <= mouse_pos[1] <= 260:
                webbrowser.open("https://gaoshutongbu.tongji.edu.cn/index.htm")  # 打开网页
            elif 230 <= mouse_pos[0] <= 330 and 220 <= mouse_pos[1] <= 260:
                reset_game()  # 重置游戏

    # 绘制背景和网格
    screen.fill((0, 0, 0))  # 填充黑色背景
    draw_grid()

    # 绘制小人1
    screen.blit(player1_image, (player1_pos[0] * cell_size, player1_pos[1] * cell_size))

    # 绘制小人2
    screen.blit(player2_image, (player2_pos[0] * cell_size, player2_pos[1] * cell_size))

    # 如果触发事件，则绘制事件弹窗
    if event_triggered:
        draw_event_popup()

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)
