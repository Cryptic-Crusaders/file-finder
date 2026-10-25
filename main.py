import time
import glob as glob

# Create logging file (Just writing to file instead of using logging package for simplicity)
log_file = open("log_file.txt", "w")


def add_file_to_log(file):
    with open("log_file.txt", "a") as log:
        log.write(file)


def find_files():
    start_time = time.time()
    files_found = 0

    # List of file extensions
    photos = (
        glob.glob("**/*.png", recursive=True)
        + glob.glob("**/*.jpg", recursive=True)
        + glob.glob("**/*.jpeg", recursive=True)
        + glob.glob("**/*.svg", recursive=True)
    )

    videos = glob.glob("**/*.mp4", recursive=True) + glob.glob(
        "**/*.mov", recursive=True
    )

    audios = glob.glob("**/*.mp3", recursive=True) + glob.glob(
        "**/*.wav", recursive=True
    )

    programs = glob.glob("**/*.py", recursive=True) + glob.glob(
        "**/*.js", recursive=True
    )

    archives = (
        glob.glob("**/*.zip", recursive=True)
        + glob.glob("**/*.rar", recursive=True)
        + glob.glob("**/*.7z", recursive=True)
        + glob.glob("**/*.tar", recursive=True)
        + glob.glob("**/*.gz", recursive=True)
    )

    print("\nPhotos:")
    with open("log_file.txt", "a") as log:
        log.write("Photos:\n")
    for photo in photos:
        print(photo)
        add_file_to_log(photo)
        files_found += 1

    print("\nVideos:")
    with open("log_file.txt", "a") as log:
        log.write("\n\nVideos:\n")
    for video in videos:
        print(video)
        add_file_to_log(video)
        files_found += 1

    print("\nPrograms:")
    with open("log_file.txt", "a") as log:
        log.write("\n\nPrograms:\n")
    for program in programs:
        print(program)
        add_file_to_log(program)
        files_found += 1

    print("\nAudio:")
    with open("log_file.txt", "a") as log:
        log.write("\n\nAudio:\n")
    for audio in audios:
        print(audio)
        add_file_to_log(audio)
        files_found += 1
    with open("log_file.txt", "a") as log:
        log.write("\n")

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"\n{files_found} Files found in {time_taken} seconds.")


find_files()
