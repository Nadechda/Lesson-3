class Horse:
    x_distance = 0 # пройденный путь
    sound = 'Frrr' # звук, который издаёт лошадь.
    def run(self, dx,dy): # dx - изменение дистанции
        self.dx=dx
        Horse.x_distance += dx
        super().fly(dx,dy)

class Eagle: #орел
    y_distance = 0 #высота полёта
    sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл
    def fly(self,dx, dy): #dy - изменение дистанции
        self.dy=dy
        Eagle.y_distance+=dy

class Pegasus(Horse,Eagle):
    def move(self, dx, dy):
        super().run(dx,dy)

    def get_pos(self):
        return Horse.x_distance, Eagle.y_distance

    def voice(self):
        print(Eagle.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

