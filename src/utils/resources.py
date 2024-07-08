#Aquivos do pygame que precisam ser inicializados, porém 1 vez inicializados, são estáticos pro resto do jogo
from pygame import transform, image, font

fonts:dict = {}
assets:dict = {}

def init():
    fonts['32'] = font.Font("fonts/fusion-pixel.ttf", 32)
    fonts['16'] = font.Font("fonts/fusion-pixel.ttf", 16)
    
    #assets do mapa
    assets["wall"] = image.load("assets/textures/wall.png")
    assets["wall_t"] = image.load("assets/textures/wall_t.png")
    assets["wall_side"] = [image.load(f"assets/textures/wall_side_{i}.png") for i in range(7)]
    assets["wall_top"] = image.load("assets/textures/wall_top.png")
    assets["floor"] = image.load("assets/textures/path.png")
    assets["spawn"] = image.load("assets/textures/spawn.png")
    assets["exit"] = image.load("assets/textures/exit.png")
    
    #assets de entidades
    assets["heart"] = transform.scale_by(image.load("assets/textures/heart.png"), 4)
    assets["clock"] = transform.scale_by(image.load("assets/textures/battery.png"), 3)
    assets["coin"] = transform.scale_by(image.load("assets/textures/paper.png"), 3)
    assets["bomb"] = transform.scale_by(image.load("assets/textures/bomb.png"), 3)
    assets["bomb_tick"] = transform.scale_by(image.load("assets/textures/bomb_tick.png"), 3)
    assets["ally"] = image.load("assets/textures/statue.png")
    
    #assets de UI
    assets["hit_points"] = transform.scale_by(image.load("assets/textures/heart.png"), 4)
    assets["book"] = transform.scale_by(image.load("assets/textures/book.png"), 3)
    assets["button"] = transform.scale_by(image.load("assets/textures/button.png"), 4)
    assets["back_button"] = transform.scale_by(image.load("assets/textures/back_button.png"), 3)
    assets["back_button_hover"] = transform.scale_by(image.load("assets/textures/back_button_hover.png"), 3)
    assets["trivia_button"] = transform.scale_by(image.load("assets/textures/button.png"), 3)
    assets["frame"] = transform.scale_by(image.load("assets/textures/frame.png"), 3)
    assets["hub"] = image.load("assets/textures/hub.png")

    assets["player_front"] = [image.load("assets/animations/player/front_0.png"), image.load("assets/animations/player/front_1.png"), image.load("assets/animations/player/front_0.png"), image.load("assets/animations/player/front_2.png")]
    assets["player_back"] = [image.load("assets/animations/player/back_0.png"), image.load("assets/animations/player/back_1.png"), image.load("assets/animations/player/back_0.png"), image.load("assets/animations/player/back_2.png")]
    assets["player_right"] = [image.load("assets/animations/player/right_0.png"), image.load("assets/animations/player/right_1.png"), image.load("assets/animations/player/right_0.png"), image.load("assets/animations/player/right_2.png")]
    assets["player_left"] = [image.load("assets/animations/player/left_0.png"), image.load("assets/animations/player/left_1.png"), image.load("assets/animations/player/left_0.png"), image.load("assets/animations/player/left_2.png")]
    assets["enemy_front"] = [image.load("assets/animations/enemy/front_0.png"), image.load("assets/animations/enemy/front_1.png"), image.load("assets/animations/enemy/front_0.png"), image.load("assets/animations/enemy/front_2.png")]
    assets["enemy_back"] = [image.load("assets/animations/enemy/back_0.png"), image.load("assets/animations/enemy/back_1.png"), image.load("assets/animations/enemy/back_0.png"), image.load("assets/animations/enemy/back_2.png")]
    assets["enemy_right"] = [image.load("assets/animations/enemy/right_0.png"), image.load("assets/animations/enemy/right_1.png"), image.load("assets/animations/enemy/right_0.png"), image.load("assets/animations/enemy/right_2.png")]
    assets["enemy_left"] = [image.load("assets/animations/enemy/left_0.png"), image.load("assets/animations/enemy/left_1.png"), image.load("assets/animations/enemy/left_0.png"), image.load("assets/animations/enemy/left_2.png")]
    assets["explosion"] = [transform.scale_by(image.load(f"assets/animations/explosion/frame{i:04d}.png"), 2) for i in range(46)]


