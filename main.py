import time
import glob as glob

# Create logging file (Just writing to file instead of using logging package for simplicity)
log_file = open("log_file.txt", "w")


def add_file_to_log(file):
    with open("log_file.txt", "a") as log:
        log.write(file)
        log.write("\n")


def find_files():
    start_time = time.time()
    files_found = 0

    # List of file extensions
    photos = (
        glob.glob("**/*.png", recursive=True)
        + glob.glob("**/*.jpg", recursive=True)
        + glob.glob("**/*.jpeg", recursive=True)
        + glob.glob("**/*.gif", recursive=True)
        + glob.glob("**/*.bmp", recursive=True)
        + glob.glob("**/*.tif", recursive=True)
        + glob.glob("**/*.tiff", recursive=True)
        + glob.glob("**/*.webp", recursive=True)
        + glob.glob("**/*.svg", recursive=True)
        + glob.glob("**/*.heic", recursive=True)
        + glob.glob("**/*.heif", recursive=True)
        + glob.glob("**/*.ico", recursive=True)
        + glob.glob("**/*.raw", recursive=True)
    )

    videos = (
        glob.glob("**/*.mp4", recursive=True)
        + glob.glob("**/*.mov", recursive=True)
        + glob.glob("**/*.avi", recursive=True)
        + glob.glob("**/*.mkv", recursive=True)
        + glob.glob("**/*.wmv", recursive=True)
        + glob.glob("**/*.flv", recursive=True)
        + glob.glob("**/*.webm", recursive=True)
        + glob.glob("**/*.mpeg", recursive=True)
        + glob.glob("**/*.mpg", recursive=True)
        + glob.glob("**/*.m4v", recursive=True)
        + glob.glob("**/*.3gp", recursive=True)
    )

    audios = (
        glob.glob("**/*.mp3", recursive=True)
        + glob.glob("**/*.wav", recursive=True)
        + glob.glob("**/*.flac", recursive=True)
        + glob.glob("**/*.aac", recursive=True)
        + glob.glob("**/*.ogg", recursive=True)
        + glob.glob("**/*.m4a", recursive=True)
        + glob.glob("**/*.wma", recursive=True)
        + glob.glob("**/*.aiff", recursive=True)
        + glob.glob("**/*.alac", recursive=True)
        + glob.glob("**/*.opus", recursive=True)
    )

    programs = (
        glob.glob("**/*.py", recursive=True)
        + glob.glob("**/*.js", recursive=True)
        + glob.glob("**/*.ts", recursive=True)
        + glob.glob("**/*.jsx", recursive=True)
        + glob.glob("**/*.tsx", recursive=True)
        + glob.glob("**/*.java", recursive=True)
        + glob.glob("**/*.c", recursive=True)
        + glob.glob("**/*.cpp", recursive=True)
        + glob.glob("**/*.cc", recursive=True)
        + glob.glob("**/*.h", recursive=True)
        + glob.glob("**/*.hpp", recursive=True)
        + glob.glob("**/*.cs", recursive=True)
        + glob.glob("**/*.go", recursive=True)
        + glob.glob("**/*.rs", recursive=True)
        + glob.glob("**/*.rb", recursive=True)
        + glob.glob("**/*.php", recursive=True)
        + glob.glob("**/*.swift", recursive=True)
        + glob.glob("**/*.kt", recursive=True)
        + glob.glob("**/*.sh", recursive=True)
        + glob.glob("**/*.bash", recursive=True)
        + glob.glob("**/*.zsh", recursive=True)
        + glob.glob("**/*.ps1", recursive=True)
        + glob.glob("**/*.bat", recursive=True)
        + glob.glob("**/*.cmd", recursive=True)
        + glob.glob("**/*.pl", recursive=True)
        + glob.glob("**/*.lua", recursive=True)
        + glob.glob("**/*.r", recursive=True)
    )

    archives = (
        glob.glob("**/*.zip", recursive=True)
        + glob.glob("**/*.rar", recursive=True)
        + glob.glob("**/*.7z", recursive=True)
        + glob.glob("**/*.tar", recursive=True)
        + glob.glob("**/*.gz", recursive=True)
        + glob.glob("**/*.tgz", recursive=True)
        + glob.glob("**/*.bz2", recursive=True)
        + glob.glob("**/*.xz", recursive=True)
        + glob.glob("**/*.lz", recursive=True)
        + glob.glob("**/*.lzma", recursive=True)
        + glob.glob("**/*.cab", recursive=True)
        + glob.glob("**/*.iso", recursive=True)
        + glob.glob("**/*.dmg", recursive=True)
    )

    documents = (
        glob.glob("**/*.pdf", recursive=True)
        + glob.glob("**/*.doc", recursive=True)
        + glob.glob("**/*.docx", recursive=True)
        + glob.glob("**/*.odt", recursive=True)
        + glob.glob("**/*.rtf", recursive=True)
        + glob.glob("**/*.txt", recursive=True)
        + glob.glob("**/*.md", recursive=True)
    )

    spreadsheets = (
        glob.glob("**/*.xls", recursive=True)
        + glob.glob("**/*.xlsx", recursive=True)
        + glob.glob("**/*.xlsm", recursive=True)
        + glob.glob("**/*.csv", recursive=True)
        + glob.glob("**/*.ods", recursive=True)
    )

    presentations = (
        glob.glob("**/*.ppt", recursive=True)
        + glob.glob("**/*.pptx", recursive=True)
        + glob.glob("**/*.pptm", recursive=True)
        + glob.glob("**/*.odp", recursive=True)
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
