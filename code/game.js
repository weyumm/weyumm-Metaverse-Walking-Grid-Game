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
eventTileImage.src = 'book.jpg'; // 替换为事件格子图片路径

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
