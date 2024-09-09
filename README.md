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
