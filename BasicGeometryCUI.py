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
        a=self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()
        b=self.get_end_point().get_x_coordinate()-self.get_start_point().get_x_coordinate()
        c=(self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate())*(-1)*(self.get_start_point().get_x_coordinate())+(self.get_start_point().get_y_coordinate())*(self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate())
        d=circle.get_radius()
        l=abs(a*circle.get_center().get_x_coordinate()+b*circle.get_center().get_y_coordinate()+c)/(math.sqrt(a*a+b*b))
        if l>d:
            return False
        elif (circle.get_center().distance_to_another_point(self.get_start_point())<d)&(circle.get_center().distance_to_another_point(self.get_end_point())<d):
            return False
        
        elif ((not self.is_divided_by_center_normal_line(circle))&(circle.get_center().distance_to_another_point(self.get_start_point())>d)&(circle.get_center().distance_to_another_point(self.get_end_point())>d)):
            return False
        else:
            return True





    def Is_print(self, circle):
        a=self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()
        b=self.get_end_point().get_x_coordinate()-self.get_start_point().get_x_coordinate()
        c=(self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate())*(-1)*(self.get_start_point().get_x_coordinate())+(self.get_start_point().get_y_coordinate())*(self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate())
        l=abs(a*circle.get_center().get_x_coordinate()+b*circle.get_center().get_y_coordinate()+c)/(math.sqrt(a*a+b*b))
        print(l)


    

    def is_divided_by_center_normal_line(self, circle):
        a=self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate()
        b=self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()
        c=-(circle.get_center().get_x_coordinate()*(self.get_start_point().get_x_coordinate()-self.get_end_point().get_x_coordinate())+circle.get_center().get_y_coordinate()*(self.get_start_point().get_y_coordinate()-self.get_end_point().get_y_coordinate()))


        if (a*self.get_start_point().get_x_coordinate()+b*self.get_start_point().get_y_coordinate()+c)*(a*self.get_end_point().get_x_coordinate()+b*self.get_end_point().get_y_coordinate()+c)<0:
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
        self.Debugging_list=[]
        self.Debugging_itr=0
        self.full_read=[]
        self.full_read_itr=0
        self.initUI()
        

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        translate_action = QAction('Translate', self)
        translate_action.setShortcut('Ctrl+T')
        translate_action.triggered.connect(self.translate)
        
        
        rotate_action = QAction('Rotate', self)
        rotate_action.setShortcut('Ctrl+R')
        rotate_action.triggered.connect(self.rotate)

        write_action=QAction('Write', self)
        write_action.setShortcut('Ctrl+W')
        write_action.triggered.connect(self.write)


        filemenu.addAction(translate_action)
        filemenu.addAction(rotate_action)
        filemenu.addAction(write_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(900, 900, 1800, 1000)
        self.show()


    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())


   
    def translate(self):
        
        # shapelist=[]
        
       
        # circle = Circle2D(Point2D(500, 500),1/math.sqrt(5.1))
        # line=Line2D(Point2D(500,501),Point2D(499.5,500))

        # shapelist.append(circle)
        # shapelist.append(line)


        # print(line.Is_Intersect_Circle(circle))
        # line.Is_print(circle)
        


        
        
        # painter = QPainter(self.image)
        # painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        # for i in range(len(shapelist)):
        #     if(str(type(shapelist[i])) == "<class '__main__.Circle2D'>") :
        #         painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(),shapelist[i].get_radius(),shapelist[i].get_radius() )
        #         self.update()

        #     elif(str(type(shapelist[i])) == "<class '__main__.Line2D'>") :
        #         painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
        #         self.update()
            
        #     elif(str(type(shapelist[i])) == "<class '__main__.Point2D'>") :
        #         self.update()



        self.image.fill(Qt.white)
        self.update()
        
        
        shapelist=[]
        
        circle = Circle2D(Point2D(uniform(500,1000), uniform(500,1000)),uniform(0.1, 100))
        
        
        while len(shapelist)<50:
            shapelist.append(Line2D(Point2D(uniform(500,1000), uniform(500,1000)),Point2D(uniform(500,1000), uniform(500,1000))))
            
            for i in range(len(shapelist)-1):
                if shapelist[len(shapelist)-1].Is_Intersect(shapelist[i]) :
                    shapelist.pop()
                    break
                

            if shapelist[len(shapelist)-1].Is_Intersect_Circle(circle):
                shapelist.pop()
                continue


            
        shapelist.append(circle)

        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        for i in range(len(shapelist)):
            if(str(type(shapelist[i])) == "<class '__main__.Circle2D'>") :
                painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(), shapelist[i].get_radius()*2.0, shapelist[i].get_radius()*2.0 )
                self.update()

            elif(str(type(shapelist[i])) == "<class '__main__.Line2D'>") :
                painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                self.update()
            
            elif(str(type(shapelist[i])) == "<class '__main__.Point2D'>") :
                self.update()

            print(circle.get_center().get_x_coordinate())
            print(circle.get_center().get_y_coordinate())
            print(circle.get_radius())

        for i in range(len(shapelist)-1):
            print(shapelist[i].Is_Intersect_Circle(circle))
            shapelist[i].Is_print(circle)
            print(shapelist[i].get_start_point().get_x_coordinate())
            print(shapelist[i].get_start_point().get_y_coordinate())
            print(shapelist[i].get_end_point().get_x_coordinate())
            print(shapelist[i].get_end_point().get_y_coordinate())
            


        self.Debugging_list=shapelist
        self.Debugging_itr=0


        

    def rotate(self):
        self.image.fill(Qt.white)
        self.update()
        f = open("C:\\Users\\com\\Desktop\\Debugging.txt", 'a')
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        if(str(type(self.Debugging_list[self.Debugging_itr])) == "<class '__main__.Circle2D'>") :
                painter.drawEllipse(self.Debugging_list[self.Debugging_itr].get_center().get_x_coordinate()-self.Debugging_list[self.Debugging_itr].get_radius(), self.Debugging_list[self.Debugging_itr].get_center().get_y_coordinate()-self.Debugging_list[self.Debugging_itr].get_radius(),self.Debugging_list[self.Debugging_itr].get_radius()*2.0,self.Debugging_list[self.Debugging_itr].get_radius()*2.0 )
                self.update()

        elif(str(type(self.Debugging_list[self.Debugging_itr])) == "<class '__main__.Line2D'>") :
                painter.drawLine(QPoint(self.Debugging_list[self.Debugging_itr].get_start_point().get_x_coordinate(),self.Debugging_list[self.Debugging_itr].get_start_point().get_y_coordinate()),QPoint(self.Debugging_list[self.Debugging_itr].get_end_point().get_x_coordinate(),self.Debugging_list[self.Debugging_itr].get_end_point().get_y_coordinate()))
                self.update()
            
        elif(str(type(self.Debugging_list[self.Debugging_itr])) == "<class '__main__.Point2D'>") :
                self.update()

        if(str(type(self.Debugging_list[len(self.Debugging_list)-1])) == "<class '__main__.Circle2D'>") :
                painter.drawEllipse(self.Debugging_list[len(self.Debugging_list)-1].get_center().get_x_coordinate()-self.Debugging_list[len(self.Debugging_list)-1].get_radius(), self.Debugging_list[len(self.Debugging_list)-1].get_center().get_y_coordinate()-self.Debugging_list[len(self.Debugging_list)-1].get_radius(),self.Debugging_list[len(self.Debugging_list)-1].get_radius()*2.0,self.Debugging_list[len(self.Debugging_list)-1].get_radius()*2.0 )
                self.update()

        elif(str(type(self.Debugging_list[len(self.Debugging_list)-1])) == "<class '__main__.Line2D'>") :
                painter.drawLine(QPoint(self.Debugging_list[len(self.Debugging_list)-1].get_start_point().get_x_coordinate(),self.Debugging_list[len(self.Debugging_list)-1].get_start_point().get_y_coordinate()),QPoint(self.Debugging_list[len(self.Debugging_list)-1].get_end_point().get_x_coordinate(),self.Debugging_list[len(self.Debugging_list)-1].get_end_point().get_y_coordinate()))
                self.update()
            
        elif(str(type(self.Debugging_list[len(self.Debugging_list)-1])) == "<class '__main__.Point2D'>") :
                self.update()


        f.write(str(self.Debugging_list[len(self.Debugging_list)-1].get_radius())+"\n")
        #self.Debugging_list[self.Debugging_itr].Is_print(self.Debugging_list[len(self.Debugging_list)-1])
        f.write(str(self.Debugging_list[len(self.Debugging_list)-1].get_center().get_x_coordinate())+"\n")
        f.write(str(self.Debugging_list[len(self.Debugging_list)-1].get_center().get_y_coordinate())+"\n")
        
        #print(self.Debugging_list[self.Debugging_itr].Is_Intersect_Circle(self.Debugging_list[len(self.Debugging_list)-1]))
        f.write(str(self.Debugging_list[self.Debugging_itr].get_start_point().get_x_coordinate())+"\n")
        f.write(str(self.Debugging_list[self.Debugging_itr].get_start_point().get_y_coordinate())+"\n")
        f.write(str(self.Debugging_list[self.Debugging_itr].get_end_point().get_x_coordinate())+"\n")
        f.write(str(self.Debugging_list[self.Debugging_itr].get_end_point().get_y_coordinate())+"\n")
            

        self.Debugging_itr= self.Debugging_itr +1

        


        f.close()
            


    def write(self):
        self.image.fill(Qt.white)
        self.update()
        f = open("C:\\Users\\com\\Desktop\\ErrorSet.txt", 'r')
        line=[]
        
        while True:
            a=f.readline()
            if not a:
                break
            self.full_read.append(float(a))





        for i in range(7):
            line.append(self.full_read[self.full_read_itr*7+i]) 
            print(line[i])

        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        
        painter.drawEllipse(line[1]-line[0], line[2]-line[0],line[0]*2.0, line[0]*2.0)
        self.update()

        
        painter.drawLine(QPoint(line[3],line[4]),QPoint(line[5],line[6]))
        self.update()
            
        self.full_read_itr=self.full_read_itr+1
        f.close()




if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
    
