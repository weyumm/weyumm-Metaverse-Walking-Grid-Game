# weyumm-Metaverse-Walking-Grid-Game
同济大学选修课：文化元宇宙课程作业，包含：Python生成PPT模版，Latex课程论文模版，小游戏demo

## 使用GPT-4o的辅助编程

要使用 `conda` 创建一个专门用于元宇宙 demo 项目的虚拟环境，可以按照以下步骤进行：

### 步骤 1：安装 Miniconda 或 Anaconda
如果还没有安装 `conda`，你需要先安装 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 或 [Anaconda](https://www.anaconda.com/)，这两个工具都包含了 `conda` 包管理器。

### 步骤 2：创建虚拟环境
1. **打开终端或命令提示符**。
2. **运行以下命令来创建虚拟环境**：

   ```bash
   conda create --name metaverse_demo python=3.8
   ```

   - `--name metaverse_demo`：指定虚拟环境的名称为 `metaverse_demo`。
   - `python=3.8`：指定 Python 版本为 3.8（可以根据需求修改）。

3. **激活虚拟环境**：

   在虚拟环境创建完成后，使用以下命令激活它：

   ```bash
   conda activate metaverse_demo
   ```

   激活成功后，您会看到命令提示符前缀更改为 `(metaverse_demo)`。

### 步骤 3：安装项目相关依赖
在激活的虚拟环境中，您可以安装项目所需的库。例如，为了编写元宇宙 demo，可能需要 `pygame` 等相关库：

```bash
conda install pygame
```

或者，如果需要用 pip 安装其他库：

```bash
pip install some_other_package
```

### 步骤 4：查看已安装的包
在虚拟环境中，您可以使用以下命令查看已安装的所有包：

```bash
conda list
```

### 步骤 5：退出虚拟环境
完成工作后，您可以通过以下命令退出虚拟环境：

```bash
conda deactivate
```

### 额外提示：
如果需要在未来重现相同的环境，可以将环境导出到文件：

```bash
conda env export > environment.yml
```

此文件可以在其他系统中通过以下命令重新创建环境：

```bash
conda env create -f environment.yml
``` 

这样，您就可以管理并独立处理与元宇宙 demo 相关的依赖和包，确保环境清晰且独立。


要给小人添加一个贴图，您可以使用 `pygame.image.load()` 函数加载一个图片文件作为小人的贴图，并使用 `blit()` 将图像绘制到屏幕上。

### 实现步骤：

1. **准备图片**：
   - 确保有一个小人形状的图片文件（例如 `player.png`），并将其放在项目的同一目录下，或者指定图片的路径。

2. **加载并使用贴图**：
   在代码中使用 `pygame.image.load()` 函数加载小人的贴图，并使用 `blit()` 函数来显示它。

### 修改后的代码：

```python
import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小 (10x10 的格子，每个格子大小为 40x40 像素)
grid_size = 10
cell_size = 40
window_size = grid_size * cell_size
screen = pygame.display.set_mode((window_size, window_size))

# 设置颜色
WHITE = (255, 255, 255)

# 小人的初始位置
player_pos = [grid_size // 2, grid_size // 2]  # 从中心开始

# 加载小人图片
player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (cell_size, cell_size))  # 调整图片大小到格子大小

# 创建时钟对象，控制帧率
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, window_size, cell_size):
        for y in range(0, window_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, WHITE, rect, 1)

def move_player(key):
    if key == pygame.K_w or key == pygame.K_UP:
        if player_pos[1] > 0:  # 向上移动
            player_pos[1] -= 1
    elif key == pygame.K_s or key == pygame.K_DOWN:
        if player_pos[1] < grid_size - 1:  # 向下移动
            player_pos[1] += 1
    elif key == pygame.K_a or key == pygame.K_LEFT:
        if player_pos[0] > 0:  # 向左移动
            player_pos[0] -= 1
    elif key == pygame.K_d or key == pygame.K_RIGHT:
        if player_pos[0] < grid_size - 1:  # 向右移动
            player_pos[0] += 1

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            move_player(event.key)

    # 绘制背景和网格
    screen.fill((0, 0, 0))  # 填充黑色背景
    draw_grid()

    # 绘制小人图片
    screen.blit(player_image, (player_pos[0] * cell_size, player_pos[1] * cell_size))

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)
```

### 关键改动：
1. **加载图片**：
   ```python
   player_image = pygame.image.load('player.png')
   ```
   将 `player.png` 文件加载到 `player_image` 变量中。确保 `player.png` 文件在同一目录下，或者使用绝对路径。

2. **调整图片大小**：
   使用 `pygame.transform.scale()` 将图片调整到格子的大小：
   ```python
   player_image = pygame.transform.scale(player_image, (cell_size, cell_size))
   ```

3. **绘制贴图**：
   使用 `screen.blit()` 将图片绘制在屏幕上代替原来的矩形绘制：
   ```python
   screen.blit(player_image, (player_pos[0] * cell_size, player_pos[1] * cell_size))
   ```

通过这种方法，您可以给游戏中的角色添加图片，增强视觉效果。

如果您加载的图片像素较小，导致在游戏中显示时显得模糊，您可以尝试以下几种方法来改善图片的显示质量：

### 1. **使用高清图片**：
   如果可能，尝试使用更高分辨率的图片来代替现有的图片。图片本身的分辨率越高，缩放时显示效果越好。

### 2. **调整缩放算法**：
   Pygame 中的 `pygame.transform.scale()` 方法默认使用线性插值来缩放图片，这可能会导致图片模糊。您可以尝试使用 `pygame.transform.smoothscale()`，它使用更高级的插值算法来缩放图片，从而减少模糊效果。

   替换如下代码：
   ```python
   player_image = pygame.transform.smoothscale(player_image, (cell_size, cell_size))
   ```

### 3. **抗锯齿处理**：
   如果图像大小和细节无法改变，可以通过增加抗锯齿（Anti-Aliasing）效果来减少模糊。虽然 Pygame 本身不直接提供抗锯齿的功能，但是可以通过平滑缩放 (`smoothscale`) 和优化图像资源来实现相似的效果。

### 4. **图像处理工具优化图片**：
   在外部图像编辑软件（如 Photoshop、GIMP 等）中预处理图片，增强图片的清晰度和对比度，保证缩放后细节不易丢失。

通过这些方法，您可以有效减少图像模糊问题，增强游戏中小人图片的显示效果。如果仍然不满意，可以考虑重新设计图片资源，确保分辨率适合游戏中的展示比例。

要使用 `keyboard` 库来替换当前代码中的按键检测逻辑，首先需要安装 `keyboard` 库。然后可以使用该库来监听按键的状态，而不是通过 Pygame 的 `KEYDOWN` 和 `KEYUP` 事件来控制小人的移动。

### 安装 `keyboard` 库

首先，确保安装 `keyboard` 库：

```bash
pip install keyboard
```

### 使用 `keyboard` 库的修改版代码

```python
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
```

### 代码说明：
1. **替换按键检测逻辑**：原本的 `pygame.KEYDOWN` 和 `KEYUP` 事件检测被 `keyboard.is_pressed()` 替代，来全局监听按键状态，简化了代码。
   - `keyboard.is_pressed('up')` 监听是否按下了 `上箭头`。
   - `keyboard.is_pressed('w')` 监听是否按下了 `W` 键。
   
2. **多线程**：每个小人控制仍然在独立的线程中处理，通过锁（`lock`）来确保小人位置更新时不会发生冲突。

### 优点：
- 使用 `keyboard` 库简化了按键检测，不依赖 Pygame 的事件循环，可以全局检测按键。
- 两个小人的移动可以独立控制，并且可以同时移动。

运行此代码后，您可以通过 `上下左右` 控制小人1，通过 `WASD` 控制小人2，同时进行独立的移动操作。


将事件的中文内容改为英文后，您可以按照以下代码更新文本内容：

```python
# 事件弹窗界面绘制
def draw_event_popup():
    font = pygame.font.SysFont(None, 48)
    description_font = pygame.font.SysFont(None, 32)
    small_font = pygame.font.SysFont(None, 24)

    # 事件文本（英文版）
    title_text = font.render("Event: Advanced Mathematics", True, (0, 0, 0))
    main_text = description_font.render("Congratulations, you have been hit by Advanced Mathematics!", True, (0, 0, 0))
    description_text = small_font.render("Vitality -10, Wisdom +5, Mood -3, Sanity -10", True, (0, 0, 0))

    # 按钮
    continue_button = small_font.render("Continue?", True, (255, 255, 255), (0, 128, 0))
    retry_button = small_font.render("Retry!", True, (255, 255, 255), (128, 0, 0))

    # 绘制弹窗背景
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 300, 200))
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 200), 2)

    # 绘制文本
    screen.blit(title_text, (70, 60))
    screen.blit(main_text, (60, 120))
    screen.blit(description_text, (50, 160))

    # 绘制按钮
    pygame.draw.rect(screen, (0, 128, 0), (70, 220, 100, 40))
    pygame.draw.rect(screen, (128, 0, 0), (230, 220, 100, 40))
    screen.blit(continue_button, (80, 230))
    screen.blit(retry_button, (240, 230))
```

### 说明：
1. **事件标题**：从“事件：高等数学”改为“Event: Advanced Mathematics”。
2. **主要内容**：将中文内容“恭喜，你被高等数学砸中了！”改为英文“Congratulations, you have been hit by Advanced Mathematics!”。
3. **属性变化描述**：将“活力值-10，智慧值+5，心情-3，san值暴跌”改为“Vitality -10, Wisdom +5, Mood -3, Sanity -10”。
4. **按钮文本**：把“继续？”和“重来！”分别改为“Continue?”和“Retry!”。

此更改后，事件的弹窗将显示英文版本的内容。


为了在 HTML 中实现和显示贴图，可以使用 JavaScript 在 `<canvas>` 元素中绘制图片，而不是简单的颜色填充。这里我修改了之前的代码，使其支持图片贴图（比如玩家和事件格子的贴图）。

### 1. HTML
```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>带贴图的网格游戏</title>
    <style>
        canvas {
            background-color: black;
            display: block;
            margin: 0 auto;
        }
        #eventPopup {
            display: none;
            position: absolute;
            top: 30%;
            left: 50%;
            transform: translate(-50%, -30%);
            background-color: white;
            border: 2px solid black;
            padding: 20px;
            text-align: center;
        }
        #eventPopup button {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<canvas id="gameCanvas" width="800" height="800"></canvas>

<div id="eventPopup">
    <h2>事件：高等数学</h2>
    <p>恭喜，你被高等数学砸中了！</p>
    <p>活力值-10，智慧值+5，心情-3，san值暴跌</p>
    <button onclick="retryGame()">重来</button>
    <button onclick="continueGame()">继续</button>
</div>

<script src="game.js"></script>
</body>
</html>
```

### 2. JavaScript (game.js)
```javascript
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const gridSize = 10;
const cellSize = 80;
const player1 = { x: 4, y: 4 };
const player2 = { x: 3, y: 3 };
const eventTile = { x: 9, y: 0 };
let eventTriggered = false;

const player1Image = new Image();
player1Image.src = 'player1.jpg'; // 替换为你的图片路径

const player2Image = new Image();
player2Image.src = 'player2.jpg'; // 替换为你的图片路径

const eventTileImage = new Image();
eventTileImage.src = 'eventTile.jpg'; // 替换为事件格子图片路径

document.addEventListener('keydown', movePlayer);

function drawGrid() {
    for (let x = 0; x < gridSize; x++) {
        for (let y = 0; y < gridSize; y++) {
            ctx.strokeStyle = 'white';
            ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);

            // 在事件格子上绘制事件贴图
            if (x === eventTile.x && y === eventTile.y) {
                ctx.drawImage(eventTileImage, x * cellSize, y * cellSize, cellSize, cellSize);
            }
        }
    }
}

function drawPlayers() {
    ctx.drawImage(player1Image, player1.x * cellSize, player1.y * cellSize, cellSize, cellSize);
    ctx.drawImage(player2Image, player2.x * cellSize, player2.y * cellSize, cellSize, cellSize);
}

function movePlayer(e) {
    if (eventTriggered) return;

    switch (e.key) {
        case 'ArrowUp':
            if (player1.y > 0) player1.y--;
            break;
        case 'ArrowDown':
            if (player1.y < gridSize - 1) player1.y++;
            break;
        case 'ArrowLeft':
            if (player1.x > 0) player1.x--;
            break;
        case 'ArrowRight':
            if (player1.x < gridSize - 1) player1.x++;
            break;
        case 'w':
            if (player2.y > 0) player2.y--;
            break;
        case 's':
            if (player2.y < gridSize - 1) player2.y++;
            break;
        case 'a':
            if (player2.x > 0) player2.x--;
            break;
        case 'd':
            if (player2.x < gridSize - 1) player2.x++;
            break;
    }

    checkEventTrigger();
    renderGame();
}

function checkEventTrigger() {
    if ((player1.x === eventTile.x && player1.y === eventTile.y) ||
        (player2.x === eventTile.x && player2.y === eventTile.y)) {
        triggerEvent();
    }
}

function triggerEvent() {
    eventTriggered = true;
    document.getElementById('eventPopup').style.display = 'block';
}

function retryGame() {
    player1.x = 4;
    player1.y = 4;
    player2.x = 3;
    player2.y = 3;
    eventTriggered = false;
    document.getElementById('eventPopup').style.display = 'none';
    renderGame();
}

function continueGame() {
    window.location.href = "https://gaoshutongbu.tongji.edu.cn/index.htm";
}

function renderGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawGrid();
    drawPlayers();
}

renderGame();
```

### 3. 实现说明：
1. **图片加载**：使用 `new Image()` 对象加载图片资源，分别为玩家1、玩家2和事件格子贴图。
2. **绘制贴图**：在 `drawGrid` 函数中，事件格子使用 `ctx.drawImage(eventTileImage, ...)` 绘制，在 `drawPlayers` 函数中用同样的方法绘制玩家。
3. **玩家移动**：通过按下箭头键和 WASD 键来控制玩家移动，事件格子中的玩家会触发弹窗。

现在，玩家、事件格子和弹窗的图片贴图都能正确显示，并且通过 JavaScript 控制。


Python 提供了多个库用于生成和处理 PowerPoint 演示文稿 (PPT)。其中最流行的库是 **python-pptx**，它提供了丰富的 API 来创建、修改和处理 PowerPoint 文件 (.pptx 格式)。下面是对常用 Python PPT 库的介绍：

### 1. **python-pptx**
   **python-pptx** 是最常用的库，专门用于创建和操作 PowerPoint 文件。它可以生成新的演示文稿，也可以编辑现有的 PPT 文件。该库主要支持以下功能：
   
   - **创建演示文稿**：创建新的幻灯片，并添加文本、图片、图表、表格等内容。
   - **幻灯片布局**：支持多种幻灯片布局，如标题幻灯片、内容幻灯片、图片幻灯片等。
   - **文本和段落格式化**：自定义文本的字体、颜色、对齐方式等。
   - **图形**：在幻灯片中添加形状（如矩形、圆形等）并进行格式化。
   - **图片和媒体文件**：插入图片、背景以及其他多媒体文件。
   - **表格和图表**：添加和修改表格及图表，支持多种图表类型，如条形图、折线图等。

   **示例代码：**
   ```python
   from pptx import Presentation

   # 创建一个新的演示文稿
   prs = Presentation()

   # 添加标题幻灯片
   slide_layout = prs.slide_layouts[0]
   slide = prs.slides.add_slide(slide_layout)
   title = slide.shapes.title
   subtitle = slide.placeholders[1]

   title.text = "Hello, World!"
   subtitle.text = "python-pptx 简单示例"

   # 保存演示文稿
   prs.save('test.pptx')
   ```

   **优点**：
   - 支持丰富的格式化选项。
   - 可以创建复杂的 PPT 内容，包括图表和表格。

   **缺点**：
   - 不支持 .ppt 格式（只能处理 .pptx 格式）。
   - 不支持动画和幻灯片转换效果。

   [GitHub 链接](https://github.com/scanny/python-pptx)

### 2. **PptxGenJS（用于前端）**
   尽管不直接是 Python 库，但如果你需要通过 web 应用生成 PowerPoint 幻灯片，可以使用 **PptxGenJS**，一个 JavaScript 库，用于生成 PPT 文件。Python 后端可以和前端 web 应用集成来使用这个库。

   - 提供丰富的 API 来处理图片、表格、图表等。
   - 支持创建演示文稿、添加幻灯片以及对文本和图形进行格式化。
   
   [PptxGenJS GitHub 链接](https://github.com/gitbrent/PptxGenJS)

### 3. **unoconv**
   如果你需要将 PPT 文件转换为其他格式（如 PDF、HTML 等），你可以使用 **unoconv**。它通过 LibreOffice 进行文件格式转换，支持 .ppt 和 .pptx 文件的读取和处理。

   **优点**：
   - 支持广泛的文件格式转换。
   
   **缺点**：
   - 需要安装 LibreOffice，配置可能相对复杂。

   [unoconv GitHub 链接](https://github.com/unoconv/unoconv)

### 总结：
- **python-pptx** 是目前处理 PowerPoint 文件的主流 Python 库，适用于创建和操作 PPT 文件。
- 如果你需要集成到 Web 应用中，**PptxGenJS** 是不错的选择。
- **unoconv** 适合需要格式转换的场景。

对于大多数 PPT 生成需求，**python-pptx** 是最推荐的库。



为了解决背景图片被文字遮盖的问题，您需要将背景图片设置为幻灯片的底层，并确保文本位于其上层。通过调整 `add_picture()` 函数的位置，可以确保背景图片被置于底层，而文字位于顶层。

### 修改后的代码：

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# 创建PPT对象
prs = Presentation()

# 添加背景图片的方法
def set_slide_background(slide, image_path):
    left = top = 0
    slide_width = prs.slide_width
    slide_height = prs.slide_height
    # 背景图片应首先添加，以确保它在底层
    background = slide.shapes.add_picture(image_path, left, top, slide_width, slide_height)
    # 将背景置于底层
    slide.shapes._spTree.remove(background._element)  # 从当前位置移除
    slide.shapes._spTree.insert(2, background._element)  # 插入到底层

# 创建文本框并设置为白色
def add_white_textbox(slide, title_text, content_text):
    # 标题
    title = slide.shapes.title
    title.text = title_text
    for paragraph in title.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = RGBColor(255, 255, 255)  # 设置为白色字体
    
    # 内容
    textbox = slide.shapes.placeholders[1]
    textbox.text = content_text
    for paragraph in textbox.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = RGBColor(255, 255, 255)  # 设置为白色字体

# 封面
slide_layout = prs.slide_layouts[0]  # 封面布局
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "元宇宙视角下开放世界探索游戏的开发前景"
subtitle.text = "张恒祯\n同济大学汽车院"
for paragraph in title.text_frame.paragraphs + subtitle.text_frame.paragraphs:
    for run in paragraph.runs:
        run.font.color.rgb = RGBColor(255, 255, 255)  # 白色文字

# 幻灯片 1: 论文摘要
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
add_white_textbox(slide, "论文摘要", 
                  ("元宇宙的兴起正在改变游戏行业，开放世界探索游戏因其高度自由度和沉浸感，"
                   "在元宇宙环境中具有巨大前景。本文从技术特性、用户需求、"
                   "以及市场发展等角度，探讨了开放世界探索游戏在未来开发中的机遇与挑战。"))

# 幻灯片 2: 引言
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
add_white_textbox(slide, "引言", 
                  ("元宇宙是集虚拟现实、增强现实、区块链等技术于一体的数字生态系统。"
                   "开放世界探索游戏与元宇宙的契合在于其高度自由和沉浸体验的结合，"
                   "使玩家能够在虚拟世界中自由探索、互动，并创造个性化体验。\n"
                   "研究聚焦技术创新、用户需求变化和市场潜力的深度挖掘。"))

# 幻灯片 3: 元宇宙的技术特性
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
add_white_textbox(slide, "元宇宙的技术特性", 
                  ("1. 虚拟现实（VR）技术：\n"
                   "   - 提供了沉浸式体验，通过VR设备，玩家可以进入到与现实高度相似的虚拟世界中进行探索。\n"
                   "2. 增强现实（AR）技术：\n"
                   "   - 将虚拟物体叠加在现实世界中，未来有望在开放世界游戏中引入AR功能，让游戏与现实无缝融合。\n"
                   "3. 区块链技术：\n"
                   "   - 元宇宙中的去中心化经济依赖于区块链，确保虚拟物品的独立所有权，玩家可以安全地进行虚拟资产的交易。"))

# 幻灯片 4: 用户需求的变化
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
add_white_textbox(slide, "用户需求的变化", 
                  ("传统的线性剧情游戏已经无法满足现代玩家的需求，"
                   "开放世界探索游戏的高度自由让玩家能够根据自己的兴趣选择探索路径、"
                   "进行自主决策。\n"
                   "元宇宙为玩家提供了更多的创造力空间，使得用户不仅仅是体验者，更是世界的构建者。"
                   "例如，《原神》和《崩坏：星穹铁道》通过开放世界设计，满足了玩家的高度个性化需求。"))

# 更多幻灯片...
# 幻灯片 5: 市场趋势与发展潜力
slide = prs.slides.add_slide(slide_layout)
set_slide_background(slide, 'PPT背景.jpg')
add_white_textbox(slide, "市场趋势与发展潜力", 
                  ("元宇宙为开放世界游戏引入了新型的商业模式，尤其是在虚拟资产和NFT（非同质化代币）方面。"
                   "未来的开放世界游戏将支持虚拟土地、角色和物品的交易，这些虚拟资产的所有权通过区块链技术得到保障。"
                   "\n\n5G 技术与云计算技术的普及，极大推动了大规模在线游戏的发展，尤其是在开放世界游戏中，玩家可以体验到"
                   "无缝在线互动，享受沉浸式体验。"))

# 保存PPT文件
prs.save('元宇宙视角下开放世界探索游戏.pptx')

print("PPT 已成功生成")
```

### 主要更新点：
1. **将背景图片置于底层**：通过 `slide.shapes._spTree.insert(2, background._element)` 将背景图片放置在幻灯片的最底层，确保文字始终显示在图片之上。
2. **文本颜色设置为亮白色**：依然保持使用 `RGBColor(255, 255, 255)` 来确保文字清晰可见。

通过这段代码，您可以确保背景图片不会覆盖文字，且 PPT 文字能够正确显示在顶层。
