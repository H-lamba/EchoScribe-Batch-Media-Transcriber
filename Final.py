import os
import whisper
def searchfile():
    directory = r"D:\Pyhton Projects"  
    media_extensions = ('.mp3',  '.mp4', '.mkv')
    media_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(media_extensions):
                media_files.append(os.path.join(root, file))
    print(media_files)
    return media_files
def scriptwriter(media_file):
    if media_file:
        model = whisper.load_model("base")
        result = model.transcribe(media_file, fp16=False)
        print(result["text"])
        
        base_name = os.path.basename(media_file)
        directory = os.path.dirname(media_file)
        transcription_file = os.path.splitext(base_name)[0] + ".txt"
        transcription_path = os.path.join(directory, transcription_file)
        with open(transcription_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
    else:
        print("No media files found.")
def main():
    media_files = searchfile()
    for media_file in media_files:
        scriptwriter(media_file)

if __name__ == "__main__":
    main()