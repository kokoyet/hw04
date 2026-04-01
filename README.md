# 《人工智能导论》HW04 作业目录

本目录包含课程作业04的所有提交内容，涵盖大模型文稿生成、剪映声音克隆、开源语音识别（ASR）的调研与实现。

## 目录结构
hw04/
├── README.md                # 本文件，目录总览与运行说明
├── text_gen.md              # 任务一：大模型生成文稿
├── jianying.md              # 任务二：剪映声音克隆步骤与说明
├── voice_clone.mp3          # 任务二：克隆声音生成的配音音频
├── asr_report.md            # 任务三：ASR方案对比与选型报告
├── experiment_log.md        # 任务三：ASR实验记录（环境、结果、结论）
├── requirements.txt         # 任务三：ASR代码依赖列表
├── asr_audio.py             # 任务三：音频文件识别脚本
└── asr_real_time.py         # 任务三：麦克风实时识别脚本

## 快速开始（ASR部分复现）

1.  **环境准备**：确保已安装Python 3.8+。
2.  **安装依赖**：在终端中进入 `hw04` 目录，运行以下命令安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
    *注意：`whisper` 和 `ffmpeg-python` 依赖于 `ffmpeg`，请确保系统已安装 [ffmpeg](https://ffmpeg.org/download.html) 并添加到环境变量中。*
3.  **运行音频识别**：
    ```bash
    python asr_audio.py
    ```
4.  **运行实时麦克风识别**：
    ```bash
    python asr_real_time.py
    ```
    (该脚本会实时识别麦克风输入的语音，按 `Ctrl+C` 停止)

## 各任务对应文件

| 任务 | 对应文件 | 说明 |
| :--- | :--- | :--- |
| **任务一** | `text_gen.md` | 大模型生成的文稿、所用模型及Prompt说明。 |
| **任务二** | `jianying.md`， `voice_clone.mp3` | 剪映声音克隆的详细步骤和导出的音频文件。 |
| **任务三** | `asr_report.md`， `experiment_log.md`， `requirements.txt`， `asr_audio.py`， `asr_real_time.py` | ASR方案对比、选型理由、实验记录以及可复现的代码。 |
