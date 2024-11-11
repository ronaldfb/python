from pygame import mixer
mixer.init()
mixer.music.load('desafio021.mp3')
mixer.music.play()
x = input('Digite algo para parar...')