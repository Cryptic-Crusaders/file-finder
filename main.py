import glob as glob

photos = glob.glob('**/*.png' or '**/*.jpg' or '**/*.jpeg' or '**/*.svg')
videos = glob.glob('**/*.mp4' or '**/*.mov')
programs = glob.glob('**/*.py' or '**/*.js')
audios = glob.glob('**/*.mp3' or '**/*.wav')

print('\nPhotos:')
for photo in photos:
    print(photo)

print('\nVideos:')
for video in videos:
    print(video)

print('\nPrograms:')
for program in programs:
    print(program)

print('\nAudio:')
for audio in audios:
    print(audio)
