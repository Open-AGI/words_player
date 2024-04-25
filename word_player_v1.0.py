#极简单词播放器，作者：susan zhang
import tkinter as tk
import os
from pygame import mixer

def display_words(word_list):
    def play_mp3(word):
        mp3_file = f"/root/Music/eng/eng_350w/eng120w/0/{word}.mp3"
        if os.path.exists(mp3_file):
            mixer.music.load(mp3_file)
            mixer.music.play()
            while mixer.music.get_busy():pass# 等待当前MP3文件播放完毕

    font_size = 12  # 初始字体大小

    window = tk.Tk()
    window.geometry("400x540")  # 设置窗口大小
    window.configure(bg="black")  # 设置窗口背景色为黑色

    word_labels = []  # 存储单词标签的列表

    for word in word_list:
        label = tk.Label(window, text=word, font=("Helvetica", font_size), fg="white")
        label.pack(pady=5)
        word_labels.append(label)

    mixer.init()  # 初始化音频播放器

    for j in range(len(word_list) - 2):
        # 滑动窗口队列  遍历元素时保持窗口的大小为19 先进先出
        elements = word_list[j:j+19]
        for k, word in enumerate(elements):
            word_labels[k].config(text=word, font=("Helvetica", font_size), fg="white", bg="black")
            word_labels[8].config(font=("Helvetica", font_size+5, "bold"))
        window.update()
        play_mp3(word_list[j+8])

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# 调用函数，传入单词集文本文件的路径
word_list = read_word_list('1325_marry')
display_words(word_list)
