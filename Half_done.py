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

class point_lists():
    def __init__(self):
        self.__circle_list = []
        self.__line_list = []
        self.__transformation_list = []
        self.__tangential_list = []
        self.__biorthogonal_list = []
        self.__itr = 0
        self.__circle = 0
        self.__transformation = 0
        self.__tangential = 0
        self.__biorthogonal = 0
        self.__phase = 0


    def get_circle_list(self):
        return self.__circle_list

    def get_line_list(self):
        return self.__line_list

    def get_transformation_list(self):
        return self.__transformation_list

    def get_tangential_list(self):
        return self.__tangential_list

    def get_biorthogonal_list(self):
        return self.__biorthogonal_list


    def get_itr(self):
        return self.__itr

    def get_circle(self):
        return self.__circle

    def get_transformation(self):
        return self.__transformation

    def get_tangential(self):
        return self.__tangential

    def get_biorthogonal(self):
        return self.__biorthogonal    
    
    def get_phase(self):
        return self.__phase   

    
    
    
    def set_circle_list(self, circle_list):
        self.__circle_list=circle_list

    def set_line_list(self, line_list):
        self.__line_list=line_list


    def set_transformation_list(self, transformation_list):
        self.__transformation_list=transformation_list

    def set_tangential_list(self, tangential_list):
        self.__tangential_list=tangential_list

    def set_biorthogonal_list(self, biorthogonal_list):
        self.__biorthogonal_list=biorthogonal_list


    def set_itr(self,itr):
        self.__itr=itr

    def set_circle(self, circle):
        self.__circle=circle

    def set_transformation(self, transformation):
        self.__transformation=transformation

    def set_tangential(self, tangential):
        self.__tangential=tangential

    def set_biorthogonal(self, biorthogonal):
        self.__biorthogonal= biorthogonal    
    
    def set_phase(self, phase):
        self.__phase=phase   


    


    def translate(self):
        for i in range (len(self.get_circle_list())):
            center=self.get_circle_list()[i].get_center()    
            center.set_x_coordinate(center.get_x_coordinate()+100)
            center.set_y_coordinate(center.get_y_coordinate()+100)
            self.get_circle_list()[i].set_center(center)
        for i in range (len(self.get_line_list())):
            startpoint=self.get_line_list()[i].get_start_point()
            endpoint=self.get_line_list()[i].get_end_point()
            
            startpoint.set_x_coordinate(startpoint.get_x_coordinate()+100)
            startpoint.set_y_coordinate(startpoint.get_y_coordinate()+100)
            endpoint.set_x_coordinate(endpoint.get_x_coordinate()+100)
            endpoint.set_y_coordinate(endpoint.get_y_coordinate()+100)
            
            self.get_line_list()[i].set_start_point(startpoint)
            self.get_line_list()[i].set_end_point(endpoint)

            

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
        self.Mypoint_lists = point_lists()
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

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(translate_action)
        filemenu.addAction(rotate_action)
        filemenu.addAction(clear_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(900, 900, 1800, 1000)
        self.show()


    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())


    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.reference_point = e.pos()
        
        
        if self.Mypoint_lists.get_phase() == 0:
            if  self.Mypoint_lists.get_itr()==0: 
                    list=self.Mypoint_lists.get_line_list()
                    list.append(Line2D(Point2D(e.pos().x(), e.pos().y()),Point2D(0,0)))
                    self.Mypoint_lists.set_line_list(list)
                    self.Mypoint_lists.set_itr(self.Mypoint_lists.get_itr() + 1)
            elif self.Mypoint_lists.get_itr()==0: 
                    list=self.Mypoint_lists.get_line_list()
                    list[len(list)-1].set_last_point(Point2D(e.pos().x(), e.pos().y()))
                    self.Mypoint_lists.set_line_list(list)
                    self.Mypoint_lists.set_itr(self.Mypoint_lists.get_itr() + 1)
        
        
        # if self.Mypoint_lists.get_phase() == 1 & self.Mypoint_lists.get_itr()==0:
        #     self.Mypoint_lists.get_circle_list().append(point(e.pos().x(), e.pos().y()))
        #     self.Mypoint_lists.circle = self.Mypoint_lists.circle + 1
        
        # if self.Mypoint_lists.get_phase() == 2 & self.Mypoint_lists.get_itr()==0:
        #     self.Mypoint_lists.transformation_coordinate.append(point(e.pos().x(), e.pos().y()))
        #     self.Mypoint_lists.transformation = self.Mypoint_lists.transformation + 1
        
        # if self.Mypoint_lists.get_phase() == 3 & self.Mypoint_lists.get_itr()==0:
        #     self.Mypoint_lists.tangential_coordinate.append(point(e.pos().x(), e.pos().y()))
        #     self.Mypoint_lists.tangential = self.Mypoint_lists.tangential + 1
        
        # if self.Mypoint_lists.get_phase() == 4 & self.Mypoint_lists.get_itr()==0:
        #     self.Mypoint_lists.biorthogonal_coordinate.append(point(e.pos().x(), e.pos().y()))
        #     self.Mypoint_lists.biorthogonal = self.Mypoint_lists.biorthogonal + 1

        # if self.Mypoint_lists.get_phase() == 5& self.Mypoint_lists.get_itr()==0:
        #     self.Mypoint_lists.rotatewithpoint(e.pos().x(), e.pos().y())
        #     self.draw()

        
        
        if self.Mypoint_lists.itr == 2:
            a = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].x_coordinate
            b = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].x_coordinate
            c = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].y_coordinate
            d = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].y_coordinate

            for i in range(len(self.Mypoint_lists.line_coordinate) - 2):
                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - b) < 20) & (
                        abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - d) < 20)):
                    self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].x_coordinate = self.Mypoint_lists.line_coordinate[i].x_coordinate
                    self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].y_coordinate = self.Mypoint_lists.line_coordinate[i].y_coordinate
                    break
            for i in range(len(self.Mypoint_lists.line_coordinate) - 2):
                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - a) < 20) & (
                        abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - c) < 20)):
                    self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].x_coordinate = self.Mypoint_lists.line_coordinate[i].x_coordinate
                    self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].y_coordinate = self.Mypoint_lists.line_coordinate[i].y_coordinate
                    break

            a = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].x_coordinate
            b = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].x_coordinate
            c = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 1].y_coordinate
            d = self.Mypoint_lists.line_coordinate[len(self.Mypoint_lists.line_coordinate) - 2].y_coordinate

            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(QPoint(a, c), QPoint(b, d))
            self.Mypoint_lists.itr = 0
            self.update()

        # if self.Mypoint_lists.circle == 2:
        #     for i in range(len(self.Mypoint_lists.line_coordinate)):
        #         if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.get_circle_list()[
        #             len(self.Mypoint_lists.get_circle_list()) - 1].x_coordinate) < 10) &
        #                 (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.get_circle_list()[
        #                     len(self.Mypoint_lists.get_circle_list()) - 1].y_coordinate) < 10)):
        #             self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 1].x_coordinate = self.Mypoint_lists.line_coordinate[i].x_coordinate
        #             self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 1].y_coordinate =self.Mypoint_lists.line_coordinate[i].y_coordinate

        #         if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.get_circle_list()[
        #             len(self.Mypoint_lists.get_circle_list()) - 2].x_coordinate) < 10) &
        #         (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.get_circle_list()[
        #             len(self.Mypoint_lists.get_circle_list()) - 2].y_coordinate) < 10) ):
        #             self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 2].x_coordinate =self.Mypoint_lists.get_circle_list()[i].x_coordinate
        #             self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 2].y_coordinate =self.Mypoint_lists.get_circle_list()[i].y_coordinate

        #         a = self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 1].x_coordinate
        #         b = self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 2].x_coordinate
        #         c = self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 1].y_coordinate
        #         d = self.Mypoint_lists.get_circle_list()[len(self.Mypoint_lists.get_circle_list()) - 2].y_coordinate
        #         painter = QPainter(self.image)
        #         painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        #         r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
        #         painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
        #     self.update()
        #     self.Mypoint_lists.circle = 0

        # if self.Mypoint_lists.transformation == 2:
        #     self.image.fill(Qt.white)
        #     self.update()

        #     for i in range(len(self.Mypoint_lists.line_coordinate)):

        #         if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate -
        #                  self.Mypoint_lists.transformation_coordinate[
        #                      len(self.Mypoint_lists.transformation_coordinate) - 2].x_coordinate) < 10) &
        #                 (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate -
        #                      self.Mypoint_lists.transformation_coordinate[
        #                          len(self.Mypoint_lists.transformation_coordinate) - 2].y_coordinate) < 10)):
        #             self.Mypoint_lists.line_coordinate[i].x_coordinate = self.Mypoint_lists.transformation_coordinate[
        #                 len(self.Mypoint_lists.transformation_coordinate) - 1].x_coordinate
        #             self.Mypoint_lists.line_coordinate[i].y_coordinate = self.Mypoint_lists.transformation_coordinate[
        #                 len(self.Mypoint_lists.transformation_coordinate) - 1].y_coordinate
        #     x = 2
        #     painter = QPainter(self.image)
        #     painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        #     while x < len(self.Mypoint_lists.line_coordinate) + 1:
        #         a = self.Mypoint_lists.line_coordinate[x - 1].x_coordinate
        #         b = self.Mypoint_lists.line_coordinate[x - 2].x_coordinate
        #         c = self.Mypoint_lists.line_coordinate[x - 1].y_coordinate
        #         d = self.Mypoint_lists.line_coordinate[x - 2].y_coordinate
        #         painter.drawLine(QPoint(a, c), QPoint(b, d))
        #         x = x + 2
        #         self.update()


        #     for i in range(len(self.Mypoint_lists.get_circle_list())):
        #         if i % 2 == 1:
        #             continue

        #         if ((abs(self.Mypoint_lists.get_circle_list()[i].x_coordinate -
        #                  self.Mypoint_lists.transformation_coordinate[
        #                      len(self.Mypoint_lists.transformation_coordinate) - 2].x_coordinate) < 10) & (
        #                 abs(self.Mypoint_lists.get_circle_list()[i].y_coordinate -
        #                     self.Mypoint_lists.transformation_coordinate[
        #                         len(self.Mypoint_lists.transformation_coordinate) - 2].y_coordinate) < 10)):
        #             self.Mypoint_lists.get_circle_list()[i].x_coordinate = self.Mypoint_lists.transformation_coordinate[
        #                 len(self.Mypoint_lists.transformation_coordinate) - 1].x_coordinate
        #             self.Mypoint_lists.get_circle_list()[i].y_coordinate = self.Mypoint_lists.transformation_coordinate[
        #                 len(self.Mypoint_lists.transformation_coordinate) - 1].y_coordinate

        #     x = len(self.Mypoint_lists.get_circle_list())
        #     while x > 1:
        #         a = self.Mypoint_lists.get_circle_list()[x - 1].x_coordinate
        #         b = self.Mypoint_lists.get_circle_list()[x - 2].x_coordinate
        #         c = self.Mypoint_lists.get_circle_list()[x - 1].y_coordinate
        #         d = self.Mypoint_lists.get_circle_list()[x - 2].y_coordinate
        #         r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
        #         painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
        #         x = x - 2
        #         self.update()


        #     self.Mypoint_lists.transformation = 0

        # if self.Mypoint_lists.tangential == 2:
        #     a = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].x_coordinate
        #     b = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate
        #     c = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].y_coordinate
        #     d = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate

        #     center=0
        #     for i in range(len(self.Mypoint_lists.get_circle_list())):
        #         if ((i % 2) != 0):
        #             continue
        #         if ((abs(self.Mypoint_lists.get_circle_list()[i].x_coordinate - a) < 10) & (
        #             abs(self.Mypoint_lists.get_circle_list()[i].y_coordinate - c) < 10)):
        #             center = i
        #         break
        #     self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].x_coordinate = self.Mypoint_lists.get_circle_list()[center].x_coordinate
        #     b = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate
        #     self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].y_coordinate = self.Mypoint_lists.get_circle_list()[center].y_coordinate
        #     d = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate

        #     a = self.Mypoint_lists.get_circle_list()[center].x_coordinate
        #     b = self.Mypoint_lists.get_circle_list()[center + 1].x_coordinate
        #     c = self.Mypoint_lists.get_circle_list()[center].y_coordinate
        #     d = self.Mypoint_lists.get_circle_list()[center + 1].y_coordinate

        #     r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
        #     A = r * r - (a - self.Mypoint_lists.tangential_coordinate[
        #         len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate) * (
        #                 a - self.Mypoint_lists.tangential_coordinate[
        #             len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate)
        #     B = (2) * (a - self.Mypoint_lists.tangential_coordinate[
        #         len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate) * (
        #                 c - self.Mypoint_lists.tangential_coordinate[
        #             len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate)
        #     C = r * r - (c - self.Mypoint_lists.tangential_coordinate[
        #         len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate) * (
        #                 c - self.Mypoint_lists.tangential_coordinate[
        #             len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate)

        #     m_1 = (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)
        #     m_2 = (-B - math.sqrt(B * B - 4 * A * C)) / (2 * A)

        #     painter = QPainter(self.image)
        #     painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

        #     painter.drawLine(QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_1),
        #                      QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_1))
        #     painter.drawLine(QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_2),
        #                     QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_2))

        #     self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
        #         self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,
        #                                                     self.Mypoint_lists.tangential_coordinate[len(
        #                                                         self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_1))
        #     self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
        #         self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,
        #                                                     self.Mypoint_lists.tangential_coordinate[len(
        #                                                         self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_1))
        #     self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
        #         self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,
        #                                                     self.Mypoint_lists.tangential_coordinate[len(
        #                                                         self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_2))
        #     self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
        #         self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,
        #                                                     self.Mypoint_lists.tangential_coordinate[len(
        #                                                         self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_2))

        #     self.update()
        #     self.Mypoint_lists.tangential = 0

        # if self.Mypoint_lists.biorthogonal == 2:
        #     painter = QPainter(self.image)
        #     painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

        #     for i in range(len(self.Mypoint_lists.line_coordinate) - 1):
        #         if (i % 2) == 0:
        #             continue
        #         if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].x_coordinate) < 10) &
        #                 (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].y_coordinate) < 10) &
        #                 (abs(self.Mypoint_lists.line_coordinate[i - 1].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].x_coordinate) < 10) &
        #                 (abs(self.Mypoint_lists.line_coordinate[i - 1].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].y_coordinate) < 10)):

        #             middle_x_coordinate = (self.Mypoint_lists.line_coordinate[i].x_coordinate + self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / 2
        #             middle_y_coordinate = (self.Mypoint_lists.line_coordinate[i].y_coordinate + self.Mypoint_lists.line_coordinate[i - 1].y_coordinate) / 2
        #             slope = (-1) * (self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / (self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.line_coordinate[i - 1].y_coordinate)
        #             painter.drawLine(QPoint(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope), QPoint(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))
        #             self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope))
        #             self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))

        #         elif ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].x_coordinate) < 10) &
        #                   (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].y_coordinate) < 10) &
        #                   (abs(self.Mypoint_lists.line_coordinate[i - 1].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].x_coordinate) < 10) &
        #                   (abs(self.Mypoint_lists.line_coordinate[i - 1].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].y_coordinate) < 10)):
        #             middle_x_coordinate = (self.Mypoint_lists.line_coordinate[i].x_coordinate + self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / 2
        #             middle_y_coordinate = (self.Mypoint_lists.line_coordinate[i].y_coordinate + self.Mypoint_lists.line_coordinate[i - 1].y_coordinate) / 2
        #             slope = (-1) * (self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / (self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.line_coordinate[i - 1].y_coordinate)
        #             painter.drawLine(QPoint(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope), QPoint(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))
        #             self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope))
        #             self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))

        #     self.update()
        #     self.Mypoint_lists.biorthogonal = 0


    # def mouseMoveEvent(self, e):
    #     if (e.buttons() & Qt.LeftButton) & self.drawing:
    #       self.last_point = e.pos()



    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         self.drawing = False
    #     if e.button() == Qt.RightButton:
    #         self.drawing = False


    def translate(self):
        self.Mypoint_lists.translate()
        self.draw()



    # def rotate(self):
    #     self.Mypoint_lists.rotatewithpoint(500,500)
    #     self.draw()


    # def draw(self):
    #     self.image.fill(Qt.white)
    #     self.update()

    #     x = 2
    #     painter = QPainter(self.image)
    #     painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

    #     while x < len(self.Mypoint_lists.line_coordinate) + 1:
    #         a = self.Mypoint_lists.line_coordinate[x - 1].x_coordinate
    #         b = self.Mypoint_lists.line_coordinate[x - 2].x_coordinate
    #         c = self.Mypoint_lists.line_coordinate[x - 1].y_coordinate
    #         d = self.Mypoint_lists.line_coordinate[x - 2].y_coordinate
    #         painter.drawLine(QPoint(a, c), QPoint(b, d))
    #         x = x + 2
    #         self.update()

    #     x = len(self.Mypoint_lists.get_circle_list())
    #     while x > 1:
    #         a = self.Mypoint_lists.get_circle_list()[x - 1].x_coordinate
    #         b = self.Mypoint_lists.get_circle_list()[x - 2].x_coordinate
    #         c = self.Mypoint_lists.get_circle_list()[x - 1].y_coordinate
    #         d = self.Mypoint_lists.get_circle_list()[x - 2].y_coordinate
    #         r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
    #         painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
    #         x = x - 2
    #         self.update()


    def clear(self):
        if self.Mypoint_lists.get_phase() == 0:
            self.Mypoint_lists.set_phase(1)
        elif self.Mypoint_lists.get_phase() == 1:
            self.Mypoint_lists.set_phase(2)
        elif self.Mypoint_lists.get_phase() == 2:
            self.Mypoint_lists.set_phase(3)
        elif self.Mypoint_lists.get_phase() == 3:
            self.Mypoint_lists.set_phase(4)
        elif self.Mypoint_lists.get_phase() == 4:
            self.Mypoint_lists.set_phase(5)
        elif self.Mypoint_lists.get_phase() == 5:
            self.Mypoint_lists.set_phase(0)











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
        tmp=0
        tmpp=0
        for i in range(50):
            tmp=randint(0,2)
            if tmp==0 :
                shapelist.append(Point2D(uniform(500,1000), uniform(500,1000)))
            elif tmp==1:
                shapelist.append(Line2D(Point2D(uniform(500,1000), uniform(500,1000)),Point2D(uniform(500,1000), uniform(500,1000))))
                tmpp=len(shapelist)
                shapelist.append(shapelist[tmpp-1].get_start_point())
                shapelist.append(shapelist[tmpp-1].get_end_point())
            elif tmp==2:
                shapelist.append(Circle2D(Point2D(uniform(500,1000), uniform(500,1000)),uniform(0.1, 100)))
                tmpp=len(shapelist)
                shapelist.append(shapelist[tmpp-1].get_center())
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        
        for i in range(len(shapelist)):
            if(str(type(shapelist[i])) == "<class '__main__.Circle2D'>") :
                painter.drawEllipse(shapelist[i].get_center().get_x_coordinate()-shapelist[i].get_radius(), shapelist[i].get_center().get_y_coordinate()-shapelist[i].get_radius(),shapelist[i].get_radius(),shapelist[i].get_radius() )
                self.update()

            elif(str(type(shapelist[i])) == "<class '__main__.Line2D'>") :
                print(1)
                painter.drawLine(QPoint(shapelist[i].get_start_point().get_x_coordinate(),shapelist[i].get_start_point().get_y_coordinate()),QPoint(shapelist[i].get_end_point().get_x_coordinate(),shapelist[i].get_end_point().get_y_coordinate()))
                self.update()
            
            elif(str(type(shapelist[i])) == "<class '__main__.Point2D'>") :
                print(1)
                self.update()





if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
    
    




    a=34