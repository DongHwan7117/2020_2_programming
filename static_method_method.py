import math
class Circle:
    count = 0  # 클래스 변수
 
    # 생성자(initializer)
    def __init__(self, radius):
        # self.* : 인스턴스변수
        self.radius = radius
        # 클래스 변수 접근 예
        Circle.count += 1
    
    # 메서드
    def calc_area(self):
        return math.pi*self.radius * self.radius

    # 클래스 메서드
    @classmethod
    def print_count(cls):
        return cls.count

figure1 =Circle(3)
figure2 =Circle(4)
print(figure1.count)
print(figure1.calc_area())
print(figure2.calc_area())
print(Circle.print_count()) # 2
print(figure1.print_count()) # 2