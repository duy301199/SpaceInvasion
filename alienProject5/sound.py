import pygame as pg


class Sound:
    def __init__(self):
        pg.mixer.init()
        self.alien_move = pg.mixer.Sound('sounds/fastinvader1.wav')
        self.ship_move = pg.mixer.Sound('sounds/fastinvader2.wav')
        self.alien_killed = pg.mixer.Sound('sounds/invaderkilled.wav')
        self.explosion = pg.mixer.Sound('sounds/explosion.wav')
        self.fire = pg.mixer.Sound('sounds/shoot.wav')
        self.background = pg.mixer.Sound('sounds/background.wav')
        self.gameover = pg.mixer.Sound('sounds/gameover.wav')
        self.alien_phaser = pg.mixer.Sound('sounds/alien_phaser.wav')

    def play_music(self, music, volume=0.3):
        pg.mixer.music.unload()  # stop previous music playing before beginning another
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    def busy(self): return pg.mixer.get_busy()

    def play_sound(self, sound):
        pg.mixer.Sound.play(sound)

    def play_alien_move(self): self.play_sound(self.alien_move)

    def play_background(self): self.play_music('sounds/background.wav')
    def stop_bg(self): pg.mixer.music.stop()

    def play_gameover(self):
        self.stop_bg()
        self.play_sound(self.gameover)
        while self.busy():
            pass

    def play_ship_move(self): self.play_sound(self.ship_move)
    def play_alien_killed(self): self.play_sound(self.alien_killed)
    def play_explosion(self): self.play_sound(self.explosion)
    def play_fire(self): self.play_sound(self.fire)
    def play_fire_phaser(self): self.play_sound(self.alien_phaser)

    def play_ship_explosion(self):
        pg.mixer.stop()
        self.play_sound(self.explosion)
