import whisper

def main():
    # 加载模型，可选 'tiny', 'base', 'small', 'medium', 'large-v3'
    # 根据你的设备性能选择，'base' 是速度和精度的良好平衡点
    print("正在加载模型...")
    model = whisper.load_model("base")

    # 任务二导出的音频文件路径
    audio_path = "voice_clone.mp3"
    print(f"正在识别音频文件: {audio_path}")

    # 执行识别，指定语言为中文，可以提高准确率
    result = model.transcribe(audio_path, language="zh")

    # 输出识别结果
    print("\n--- 识别结果 ---")
    print(result["text"])
    print("--- 识别结束 ---")

if __name__ == "__main__":
    main()
