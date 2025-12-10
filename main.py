import time
import glob as glob

# Create logging file (Just writing to file instead of using logging package for simplicity)
log_file = open("log_file.txt", "w")


def add_file_to_log(file):
    with open("log_file.txt", "a") as l:
        l.write(file)


def find_files():
    start_time = time.time()
    files_found = 0

    photos = glob.glob("**/*.png" or "**/*.jpg" or "**/*.jpeg" or "**/*.svg")
    videos = glob.glob("**/*.mp4" or "**/*.mov")
    programs = glob.glob("**/*.py" or "**/*.js")
    audios = glob.glob("**/*.mp3" or "**/*.wav")

    print("\nPhotos:")
    for photo in photos:
        print(photo)
        add_file_to_log(photo)
        files_found += 1

    print("\nVideos:")
    for video in videos:
        print(video)
        add_file_to_log(video)
        files_found += 1

    print("\nPrograms:")
    for program in programs:
        print(program)
        add_file_to_log(program)
        files_found += 1

    print("\nAudio:")
    for audio in audios:
        print(audio)
        add_file_to_log(audio)
        files_found += 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\n{files_found} Files found in {time_taken} seconds.")


find_files()
