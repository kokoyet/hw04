import whisper
import pyaudio
import numpy as np
import wave
import threading
import time
import sys

# 音频参数
CHUNK = 1024  # 每次读取的音频帧数
FORMAT = pyaudio.paInt16  # 16位深度
CHANNELS = 1  # 单声道
RATE = 16000  # 采样率，16kHz是Whisper的要求
RECORD_SECONDS = 5  # 每段录音的时长（秒），用于实时分段识别

def record_audio(stream, duration):
    """从麦克风流中录制指定时长的音频"""
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / 32768.0
    return audio_data

def main():
    print("正在加载轻量级模型（tiny）用于实时识别...")
    model = whisper.load_model("tiny")

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("麦克风已启动，开始实时语音识别（每5秒处理一次）...")
    print("请开始说话，按 Ctrl+C 停止程序。")

    try:
        while True:
            # 录制一段音频
            audio_segment = record_audio(stream, RECORD_SECONDS)
            # 使用模型进行识别
            result = model.transcribe(audio_segment, language="zh", fp16=False)
            # 打印识别出的文本
            if result["text"]:
                print(f"识别: {result['text']}")
    except KeyboardInterrupt:
        print("\n程序已停止。")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
