import pygame

WINDOW_SIZE = ( 1200 , 1000 )
FIELD_COLOR = ( 0 , 255 , 0 )
BACKGROUND_COLOR = ( 255 , 255 , 255 )
FIELD_RECT = ( 0 , 0 , 120 , 80 )
PLAYER_RADIUS = 0.5
NUMBER_UNITS_ON_TEAM = 11

class TEAM_COLORS :
  RED = 0
  BLUE = 1

TEAM_DRAW_COLORS = {
  TEAM_COLORS . RED : [ 255 , 0 , 0 ] ,
  TEAM_COLORS . BLUE : [ 0 , 0 , 255 ]
}

def main ( ) :
  Screen , MainField = Initialize ( )
  RunGameLoop ( Screen , MainField )

def RunGameLoop ( Screen , MainField ) :
  while True :
    RunIteration ( Screen , MainField )

def RunIteration ( Screen , MainField ) :
  Draw ( Screen , MainField )

def Draw ( Screen , MainField ) :
  Clear ( Screen )
  MainField . Draw ( Screen )
  pygame.display.flip()

def AdjustToWindow ( InRect ) :
  NewVector = [ ]
  for Element in InRect :
    NewVector . append ( int ( Element * GetPixelsPerMeter ( ) ) )
  return NewVector

def GetPixelsPerMeter ( ) :
  return float ( WINDOW_SIZE [ 0 ] ) / FIELD_RECT [ 2 ]

def Clear ( Screen ) :
  Screen . fill ( BACKGROUND_COLOR )

def Initialize ( ) :
  pygame . init ( )
  Screen = pygame . display . set_mode ( WINDOW_SIZE )
  MainField = Field ( )
  return Screen, MainField


class Team:
  def __init__ ( self , Color ) :
    self . Color = Color
    self . Units = [ ]
    self . InitUnits ( Color )
  
  def InitUnits ( self , Color ) :
    for index in range ( NUMBER_UNITS_ON_TEAM ) :
      self . Units . append ( Unit ( Color ) )
  
  def Draw ( self , Screen ) :
    self . DrawUnits ( Screen )
  
  def DrawUnits ( self , Screen ) :
    for Unit in self . Units :
      Unit . Draw ( Screen )

class Unit :
  def __init__ ( self , Color ) :
    self . Position = [ 0 , 0 ]
    self . Color = Color
  
  def SetPosition ( Position ) :
    self . Position = Position
    
  def Draw ( self , Screen ) :
    print ( AdjustToWindow ( self . Position ) , PLAYER_RADIUS * GetPixelsPerMeter ( ) , GetPixelsPerMeter ( ) )
    pygame.draw.circle(Screen, TEAM_DRAW_COLORS [ self . Color ] , AdjustToWindow ( self . Position ) ,
      int ( PLAYER_RADIUS * GetPixelsPerMeter ( ) ) )
    

class Field:
  def __init__ ( self ) :
    self . DrawRectangle = AdjustToWindow ( FIELD_RECT )
    self . FieldRectangle = FIELD_RECT
    self . Teams = [ Team ( TEAM_COLORS . RED ) , Team ( TEAM_COLORS . BLUE ) ]

  def Draw ( self , Screen ) :
    pygame.draw.rect(Screen, FIELD_COLOR, self . DrawRectangle )
    self . DrawTeams ( Screen )
  
  def DrawTeams ( self , Screen ) :
    for Team in self . Teams :
      Team . Draw ( Screen )
    


main ( )
