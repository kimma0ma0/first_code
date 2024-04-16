#추가문제

class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브 클래스")

myCar=Car()
mySedan=Sedan()
myCar.method()
mySedan.method()

#결과 3번(슈퍼클래스 서브클래스)

#Car의 상속을 받는 RVCar클래스를 정의하는 코드 빈칸채우기

class Car:
    speed=0

    def upSpeed(self,value):
        self.speed=self.speed+value

    def RVCar(Car):
        seatNum=0

        def getSeatNum(self):
            return self.seatNum
