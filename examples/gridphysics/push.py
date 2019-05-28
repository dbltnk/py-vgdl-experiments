# run this using 'python -m examples.gridphysics.push' from py-vgdl-experiments root
# based on https://github.com/schaul/py-vgdl
# documentation at https://github.com/EssexUniversityMCTS/gvgai/wiki/VGDL-Language

'''
Push: A simple board game

@author: Alexander Zacherl
'''

box_level = """
wwwwwwwww
w       w
w   C   w
w   x   w
w  xxx  w
w   x   w
w       w
wwwwwwwww
"""

push_game = """
BasicGame frame_rate=30
    SpriteSet
        cursor > CursorAvatar stype=marker cooldown=10 singleton=True
        marker > Marker stype=cursor
        piece > Piece
        pieceSelected > SelectedPiece cooldown=10 singleton=True color=BLUE stype=piece
        test > Passive color=GREEN
    LevelMapping
        x > piece
        C > cursor
    InteractionSet
        cursor wall > stepBack
        piece piece > bounceForward
        piece wall > killSprite
        marker piece > killSprite
        piece marker > transformTo stype=pieceSelected
        piece pieceSelected > bounceForward
        pieceSelected wall > stepBack
    TerminationSet
        SpriteCounter stype=piece limit=0 win=False
"""

if __name__ == "__main__":
    from vgdl.core import VGDLParser
    VGDLParser.playGame(push_game, box_level)
