import math


class Point2D() :
    def __init__(self,x_coordinate, y_coordinate):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate=x_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.__y_coordinate=y_coordinate
    #
    def distance_between_points(self, point):
        distance= math.sqrt(( point.get_x_coordinate() - self.get_x_coordinate() )**2+( point.get_y_coordinate() - self.get_y_coordinate() )**2)
        return distance

    def magnitude(self):
        magnitude=math.sqrt(self.get_x_coordinate()**2+self.get_y_coordinate()**2)
        return magnitude

    def unit_vector(self):
        x_direction = self.get_x_coordinate()/self.magnitude()
        y_direction = self.get_y_coordinate()/self.magnitude()
        temp_point=Point2D(0,0)
        temp_point.set_x_coordinate(x_direction)
        temp_point.set_y_coordinate(y_direction)
        return temp_point
    #
    def inner_product(self, point):
        inner_product=self.get_x_coordinate()*point.get_x_coordinate()+self.get_y_coordinate()*point.get_y_coordinate()
        return inner_product
    #
    def cross_product(self, point):
        cross_product=self.get_x_coordinate()*point.get_y_coordinate()-self.get_y_coordinate()*point.get_x_coordinate()
        return cross_product    


class Circle2D():
    #center == Point2D
    def __init__(self, center:Point2D, radius):
        self.__center=center
        self.__radius= radius

    def get_center(self):
        return self.__center
    def get_radius(self):
        return self.__radius
    def set_center(self, center:Point2D):
        self.__center=center
    def set_radius(self, radius):
        self.__radius=radius

    
    def area(self):
        return ((math.pi)*self.get_radius()*self.get_radius())

    def perimeter(self):
        return (2*(math.pi)*self.get_radius())
    #
    def is_contain_circle(self, circle):
        if((self.get_center().distance_between_points(circle.get_center())+circle.get_radius())<self.get_radius()):
            return True
        else:
            return False


    #내용과 함수이름을 좀 개선할것
    def distance_from_boundary_to_point(self,point):
        tmp_distance= self.get_center().distance_between_points(point)-self.get_radius()
        if tmp_distance>0:
            return tmp_distance
        else:
            return(-tmp_distance)
    #(new)겹치는 원끼리도 거리를 구하나???
    def distance_from_boundary_to_circle(self,circle):
        if(self.get_center().distance_between_points(circle.get_center())<(self.get_radius()+circle.get_radius())):
            return 0
        else:
            return(self.get_center().distance_between_points(circle.get_center())-(self.get_radius()+circle.get_radius()))


class Line2D:
    def __init__(self, start_point: Point2D, end_point:Point2D):
        self.__start_point=start_point
        self.__end_point=end_point
    #위키피디아에 영어버전 이름지을때 참조
    def get_start_point(self):
        return self.__start_point

    def get_end_point(self):
        return self.__end_point

    
    def set_start_point(self, point:Point2D):
        self.__start_point=point

    def set_end_point(self, point:Point2D):
        self.__end_point=point

    def length(self):
       return self.get_start_point().distance_between_points(self.get_end_point())


if __name__ is "__main__":
    point1=Point2D(3,4)
    point2=Point2D(0,0)

    line1=Line2D(point1,point2)

    print(line1.length())