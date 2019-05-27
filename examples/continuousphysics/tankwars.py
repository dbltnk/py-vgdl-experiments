'''
VGDL example: another simple artillery game similar to "Tank Wars".

@author: Tom Schaul and Julian Togelius
'''


tankwars_game = """
BasicGame
    SpriteSet    
        pad    > Immovable color=BLUE 
        tank > AimedFlakAvatar  orientation=UP
            avatar > alternate_keys=True stype=mybullet 
            otheravatar > color=RED stype=otherbullet
        bullet > Missile physicstype=GravityPhysics speed=20 draw_arrow=True
            mybullet > singleton=True color=WHITE
            otherbullet > singleton=True color=RED
        lift  > Conveyor 
            liftup > orientation=UP
            pushdown > orientation=DOWN
            
    TerminationSet
        SpriteCounter stype=otheravatar win=True     
        SpriteCounter stype=avatar win=False     
           
    InteractionSet
        otheravatar mybullet > killSprite
        avatar otherbullet > killSprite 
        bullet wall > killSprite 
        wall bullet > killSprite
        bullet EOS > killSprite
        tank wall > stepBack
        tank EOS > stepBack
        tank lift  > conveySprite
        
    LevelMapping
        a > otheravatar
        + > liftup
        - > pushdown
"""

tankwars_level = """
w                w           w
w   w       w                w
w                     w      w
w               w            w
w                            w
w                            w
w       w                    w
w                   w        w
w          www               w
w         wwwwww             w
w       wwwwwwww             w
wA     wwwwwwwwwwwww        aw
"""

if __name__ == "__main__":
    from vgdl.core import VGDLParser
    VGDLParser.playGame(tankwars_game, tankwars_level)
        