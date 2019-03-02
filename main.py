import pygame

WINDOW_RECT = ( 1200 , 1000 )
FIELD_COLOR = ( 0 , 255 , 0 )
BACKGROUND_COLOR = ( 255 , 255 , 255 )
FIELD_RECT = ( 120 , 80 )

def main ( ) :
  Screen = Initialize ( )
  RunGameLoop ( Screen )

def RunGameLoop ( Screen ) :
  while True :
    RunIteration ( Screen )

def RunIteration ( Screen ) :
  Draw ( Screen )

def Draw ( Screen ) :
  Clear ( Screen )
  DrawField ( Screen )
  pygame.display.flip()

def DrawField ( Screen ) :
  pygame.draw.rect(Screen, FIELD_COLOR, AdjustToWindow ( FIELD_RECT , WINDOW_RECT ) )

def AdjustToWindow ( Positions , WindowRect ) :
  NewVector = [ 0 , 0 ]
  for Element in Positions :
    NewVector . append ( Element * ( WindowRect [ 0 ] / Positions [ 0 ] ) )
  return NewVector

def Clear ( Screen ) :
  Screen . fill ( BACKGROUND_COLOR )

def Initialize ( ) :
  pygame . init ( )
  Screen = pygame . display . set_mode ( WINDOW_RECT )
  return Screen

main ( )
