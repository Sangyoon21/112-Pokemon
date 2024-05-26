from cmu_graphics import *


class Npc:
  onOff = 1
  app.background = 'skyBlue'
  app.width = 800
  app.height = 800
  cnt = 0
  num = 0

  def onAppStart():
     pass
#   def drawImage(self, strlink):
#      img = Image(strlink, 225, 0)


  def setText(self, mystr):
     app.group.clear()
     #self.setImage('Professor_Oak_XY.png')
     l = str(mystr).split("\n")
     print(l)
     count = 0
     y = 800
     y -= (len(l) * 50)
     cnt = 0
     for i in l:
        Label(i, 400, y + (50 * count), font='D2Coding', fill=None, border='black', borderWidth=1, size=20)
        count += 1
        cnt += 1

  def onKeyPress(self,app,key):
     if Npc.onOff == 1:
        self.setText(self.decText[Npc.num, Npc.cnt])
        Npc.cnt += 1
        

  decText = {}
  decText[0, 0] = "Hello, young trainer!\n This is Professor Oak's laboratory in Palette Town.\n The owner has just turned 10 years old\n and is about to take his first steps as a Pokemon trainer."
  # "안녕하십니까, 젊은 트레이너님! 여기는 팔레트 타운의 오박사 연구소입니다. \n 주인님께서는 갓 10살이 되어 포켓몬 트레이너로서의 첫 걸음을 내딛으려고 하시는군요."
  decText[0, 1] = "The owner's first Pokemon are the fire-type Charmander,\n the water-type Squirtle, and the grass-type."
  # "주인님의 첫 포켓몬으로 불꽃 타입의 파이리, 물 타입의 꼬부기, 그리고 풀 타입의 이상해씨 중에서 하나를 선택하셔야 합니다."
  decText[0, 2] = "You must choose one of the Bulbasaur.\n Which Pokémon would you choose as your companion?"
  # "어떤 포켓몬을 동반자로 선택하시겠습니까?"