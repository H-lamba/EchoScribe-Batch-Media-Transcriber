# 🎙️ EchoScribe: Batch Media Transcriber

A simple yet powerful Python tool that automatically finds all your media files (MP4, MP3, MKV) in a specified directory and transcribes them into text files or timed `.srt` captions using OpenAI's Whisper.

Turn your entire video and audio library into a searchable, caption-ready text archive with a single command\!

-----

## ✨ Features

  * **Automatic Discovery:** Recursively scans a root directory and all its subfolders to find every media file.
  * **Batch Processing:** Queues up all found files and transcribes them one by one.
  * **Powered by Whisper:** Uses OpenAI's robust `whisper` model for high-quality, accurate transcriptions.
  * **Flexible Output:**
      * Save transcriptions as simple `.txt` files (default).
      * Save transcriptions as timed `.srt` caption files (with a simple code edit).
  * **Organized Output:** Saves each transcription right next to its original media file, keeping your folders tidy.
  * **Supports Common Formats:** Works out-of-the-box with `.mp3`, `.mp4`, and `.mkv` files.

-----

## 🚀 Use Cases

This tool is a powerful automator for turning unstructured audio/video data into structured, usable text.

### 1\. ✍️ Automate Caption & Subtitle Creation

  * **The Problem:** You have hours of video content and need captions. Manually typing them is slow and tedious.
  * **How This Tool Helps:** Run the script (especially the `.srt` version) to generate a "first draft" of your timed captions. This file can be directly uploaded to YouTube or opened in a subtitle editor for quick review and correction, saving you 90% of the work.

### 2\. 🔍 Create a Searchable Media Archive

  * **The Problem:** You have 50 video lectures and *know* one of them mentions a specific topic (e.g., "Logistic Regression"), but you can't find it.
  * **How This Tool Helps:** Run the script on your `Lectures` folder. You'll get 50 `.txt` files. Now, you can use your computer's built-in search to instantly find the exact file (and thus, the exact video) that contains your search term.

### 3\. ♻️ Repurpose Content for Marketing & Blogs

  * **The Problem:** You recorded a 1-hour podcast (`.mp3`) and want to turn it into a blog post, show notes, and social media quotes.
  * **How This Tool Helps:** The generated `.txt` file is a 90%-complete draft of your blog post. You can scan it for powerful quotes, pull out the main topics for show notes, and get a full-text version for SEO.

### 4\. 📚 Generate Study Guides & Meeting Minutes

  * **The Problem:** You have hours of recorded Zoom meetings or college lectures and need to review them for an exam or find a key decision.
  * **How This Tool Helps:** Transcribe your `Recordings` folder. You can now read a 2-hour lecture in 15 minutes or use `Ctrl+F` to find the exact moment the "project deadline" was finalized.

-----

## ⚙️ How It Works

1.  **Search:** The script starts at a directory you define (e.g., `D:\Pyhton Projects`) and searches through all subfolders.
2.  **Filter:** It gathers a list of all files ending in `.mp3`, `.mp4`, or `.mkv`.
3.  **Transcribe:** It loops through this list, loading each file into the `whisper` model.
4.  **Save:** The resulting text is saved as a new file. For example, a video at `D:\Lectures\MyLecture.mp4` will have its transcription saved as `D:\Lectures\MyLecture.txt`.

-----

## 🚀 Getting Started

### 1\. Prerequisites

  * **Python 3.x**
  * **`ffmpeg`:** This is a **critical** dependency for Whisper to process audio and video. You must install it on your system and ensure it's available in your system's PATH.
      * **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html).
      * **macOS (using Homebrew):** `brew install ffmpeg`
      * **Linux (using apt):** `sudo apt update && sudo apt install ffmpeg`

### 2\. Installation

1.  **Download the Script:**
    Save the code as `Final.py` (or any name you like) on your computer.

2.  **Install the Python Library:**
    You only need the `openai-whisper` library. Open your terminal or command prompt and run:

    ```bash
    pip install openai-whisper
    ```

-----

## 💻 How to Use

### 1\. Configure Your Media Folder

Before you run the script, you **must** edit one line to tell it where to find your media files.

Open `Final.py` and change the `directory` variable in the `searchfile()` function:

```python
def searchfile():
    # 👇 --- EDIT THIS LINE --- 👇
    directory = r"D:\Pyhton Projects"  # Change this to your root media folder
    
    media_extensions = ('.mp3',  '.mp4', '.mkv')
    media_files = []
# ...
```

> **Tip:** Using `r"..."` (a raw string) is helpful on Windows to prevent backslashes `\` from being misinterpreted.

### 2\. Run the Script

Once you've set your directory, just run the script from your terminal:

```bash
python Final.py
```

The script will first print a list of all media files it found. Then, it will start transcribing them one by one.

-----
