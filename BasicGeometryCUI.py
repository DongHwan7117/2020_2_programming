from __future__ import annotations
from random import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
   #naming
    def distance_to_another_point(self, point : Point2D):
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
    
    def inner_product(self, point: Point2D):
        inner_product=self.get_x_coordinate()*point.get_x_coordinate()+self.get_y_coordinate()*point.get_y_coordinate()
        return inner_product
    
    def cross_product(self, point: Point2D):
        cross_product=self.get_x_coordinate()*point.get_y_coordinate()-self.get_y_coordinate()*point.get_x_coordinate()
        return cross_product 

    def print_name(self):
        print("Point2D")

class Circle2D():
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
   
    def is_contain_circle(self, circle: Circle2D):
        if((self.get_center().distance_between_points(circle.get_center())+circle.get_radius())<self.get_radius()):
            return True
        else:
            return False


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
    def print_name(self):
        print("Circle2D")


    
    
class Line2D:
    def __init__(self, start_point: Point2D, end_point:Point2D):
        self.__start_point=start_point
        self.__end_point=end_point
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
    def print_name(self):
        print("Line2D")


    def Is_Intersect(self, line):
        x11=self.get_start_point().get_x_coordinate()
        x12=self.get_end_point().get_x_coordinate()
        x21=line.get_start_point().get_x_coordinate()
        x22=line.get_end_point().get_x_coordinate()
        y11=self.get_start_point().get_y_coordinate()
        y12=self.get_end_point().get_y_coordinate()
        y21=line.get_start_point().get_y_coordinate()
        y22=line.get_end_point().get_y_coordinate()
        
        
        
        f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
        f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
        f3= (x21-x22)*(y12-y22) - (y21-y22)*(x12-x22)
        f4= (x21-x22)*(y11-y22) - (y21-y22)*(x11-x22)
        
        if (f1*f2 < 0) & (f3*f4<0 ):
            return True
        else:
            return False
    def Is_Intersect_Circle(self, circle):
        Point_temp=Point2D((self.get_start_point().get_x_coordinate()+self.get_end_point().get_x_coordinate())/2,(self.get_start_point().get_y_coordinate()+self.get_end_point().get_y_coordinate())/2)
        
        
        if (circle.get_center().distance_to_another_point(self.get_start_point())>circle.get_radius())&(circle.get_center().distance_to_another_point(self.get_end_point())>circle.get_radius())&(circle.get_center().distance_to_another_point(Point_temp)>circle.get_radius()) :
             return False
        else :
            return True

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(1800, 1000), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 1
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.reference_point = QPoint()
       
        self.initUI()


    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        translate_action = QAction('Translate', self)
        translate_action.setShortcut('Ctrl+T')
        translate_action.triggered.connect(self.translate)

        filemenu.addAction(translate_action)
        

        self.setWindowTitle('Simple Painter')
        self.setGeometry(900, 900, 1800, 1000)
        self.show()


    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())


   
    def translate(self):
        
        shapelist=[]
        
        circle = Circle2D(Point2D(uniform(500,1000), uniform(500,1000)),uniform(0.1, 100))



        while len(shapelist)<10:
            shapelist.append(Line2D(Point2D(uniform(500,1000), uniform(500,1000)),Point2D(uniform(500,1000), uniform(500,1000))))
            
            for i in range(len(shapelist)):
                if shapelist[len(shapelist)-1].Is_Intersect(shapelist[i]) :
                    shapelist.pop()
                    break

            if shapelist[len(shapelist)-1].Is_Intersect_Circle(circle):
                shapelist.pop()



            # 추가한 선과 이전 선들과 원이 겹치는지 확인하는 조건, 반복문
            #shapelist.pop()
        
            
        shapelist.append(circle)
        





        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        for i in range(len(shapelist)):
            if(str(type(shapelist[i])) == "<class '__main__.Circle2D'>") :
                painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(),shapelist[i].get_radius(),shapelist[i].get_radius() )
                self.update()

            elif(str(type(shapelist[i])) == "<class '__main__.Line2D'>") :
                painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                self.update()
            
            elif(str(type(shapelist[i])) == "<class '__main__.Point2D'>") :
                self.update()







        # painter = QPainter(self.image)
        # painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        # linelist=[]

        # circle=Circle2D(Point2D(uniform(500,1000),uniform(500,1000)), uniform(0.1,100))
        
        # painter.drawEllipse(circle.get_center().get_x_coordinate()-circle.get_radius(), circle.get_center().get_y_coordinate()-circle.get_radius(),circle.get_radius(),circle.get_radius() )
        # self.update()



        # for i in range(10):
        #     linelist.append(Line2D(Point2D(uniform(500,1000), uniform(500,1000)),Point2D(uniform(500,1000), uniform(500,1000))))
            
            
           
        # for i in range(len(linelist)):
        #      painter.drawLine(QPoint(linelist[i].get_start_point().get_x_coordinate(),linelist[i].get_start_point().get_y_coordinate()),QPoint(linelist[i].get_end_point().get_x_coordinate(),list[i].get_end_point().get_y_coordinate()))
        #      self.update()
            






if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
    
