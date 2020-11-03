import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class point():

    def __init__(self, a, b):
        self.x_coordinate = a
        self.y_coordinate = b


class point_lists():
    def __init__(self):
        self.circle_coordinate = []
        self.line_coordinate = []
        self.transformation_coordinate = []
        self.tangential_coordinate = []
        self.biorthogonal_coordinate = []
        self.itr = 0
        self.circle = 0
        self.transformation = 0
        self.tangential = 0
        self.biorthogonal = 0
        self.phase = 0


    def translate(self):
        for i in range (len(self.circle_coordinate)):
            self.circle_coordinate[i].x_coordinate=self.circle_coordinate[i].x_coordinate+100
            self.circle_coordinate[i].y_coordinate = self.circle_coordinate[i].y_coordinate + 100
        for i in range (len(self.line_coordinate)):
            self.line_coordinate[i].x_coordinate=self.line_coordinate[i].x_coordinate+100
            self.line_coordinate[i].y_coordinate = self.line_coordinate[i].y_coordinate + 100



    def rotate(self):
        for i in range (len(self.circle_coordinate)):
            a = self.circle_coordinate[i].x_coordinate
            b = self.circle_coordinate[i].y_coordinate
            self.circle_coordinate[i].x_coordinate = a * math.cos((math.pi) * 0.05) - b * math.sin((math.pi) * 0.05)
            self.circle_coordinate[i].y_coordinate = a * math.sin((math.pi) * 0.05) + b * math.cos((math.pi) * 0.05)


        for i in range (len(self.line_coordinate)):
            a= self.line_coordinate[i].x_coordinate
            b = self.line_coordinate[i].y_coordinate
            self.line_coordinate[i].x_coordinate=a*math.cos((math.pi)*0.05)-b*math.sin((math.pi)*0.05)
            self.line_coordinate[i].y_coordinate = a*math.sin((math.pi)*0.05)+b*math.cos((math.pi)*0.05)




    def translate(self):
        for i in range (len(self.circle_coordinate)):
            self.circle_coordinate[i].x_coordinate=self.circle_coordinate[i].x_coordinate+100
            self.circle_coordinate[i].y_coordinate = self.circle_coordinate[i].y_coordinate + 100
        for i in range (len(self.line_coordinate)):
            self.line_coordinate[i].x_coordinate=self.line_coordinate[i].x_coordinate+100
            self.line_coordinate[i].y_coordinate = self.line_coordinate[i].y_coordinate + 100



    def rotatewithpoint(self ,c ,d):

        for i in range(len(self.circle_coordinate)):
            self.circle_coordinate[i].x_coordinate = self.circle_coordinate[i].x_coordinate - c
            self.circle_coordinate[i].y_coordinate = self.circle_coordinate[i].y_coordinate -d
        for i in range(len(self.line_coordinate)):
            self.line_coordinate[i].x_coordinate = self.line_coordinate[i].x_coordinate -c
            self.line_coordinate[i].y_coordinate = self.line_coordinate[i].y_coordinate -d



        for i in range (len(self.circle_coordinate)):
            a = self.circle_coordinate[i].x_coordinate
            b = self.circle_coordinate[i].y_coordinate
            self.circle_coordinate[i].x_coordinate = a * math.cos((math.pi) * 0.05) - b * math.sin((math.pi) * 0.05)
            self.circle_coordinate[i].y_coordinate = a * math.sin((math.pi) * 0.05) + b * math.cos((math.pi) * 0.05)

        for i in range (len(self.line_coordinate)):
            a= self.line_coordinate[i].x_coordinate
            b = self.line_coordinate[i].y_coordinate
            self.line_coordinate[i].x_coordinate=a*math.cos((math.pi)*0.05)-b*math.sin((math.pi)*0.05)
            self.line_coordinate[i].y_coordinate = a*math.sin((math.pi)*0.05)+b*math.cos((math.pi)*0.05)

        for i in range (len(self.circle_coordinate)):
            self.circle_coordinate[i].x_coordinate=self.circle_coordinate[i].x_coordinate+c
            self.circle_coordinate[i].y_coordinate = self.circle_coordinate[i].y_coordinate +d
        for i in range (len(self.line_coordinate)):
            self.line_coordinate[i].x_coordinate=self.line_coordinate[i].x_coordinate+ c
            self.line_coordinate[i].y_coordinate = self.line_coordinate[i].y_coordinate + d



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
        if self.Mypoint_lists.phase == 0:
            self.Mypoint_lists.line_coordinate.append(point(e.pos().x(), e.pos().y()))
            self.Mypoint_lists.itr = self.Mypoint_lists.itr + 1

        if self.Mypoint_lists.phase == 1:
            self.Mypoint_lists.circle_coordinate.append(point(e.pos().x(), e.pos().y()))
            self.Mypoint_lists.circle = self.Mypoint_lists.circle + 1
        if self.Mypoint_lists.phase == 2:
            self.Mypoint_lists.transformation_coordinate.append(point(e.pos().x(), e.pos().y()))
            self.Mypoint_lists.transformation = self.Mypoint_lists.transformation + 1
        if self.Mypoint_lists.phase == 3:
            self.Mypoint_lists.tangential_coordinate.append(point(e.pos().x(), e.pos().y()))
            self.Mypoint_lists.tangential = self.Mypoint_lists.tangential + 1
        if self.Mypoint_lists.phase == 4:
            self.Mypoint_lists.biorthogonal_coordinate.append(point(e.pos().x(), e.pos().y()))
            self.Mypoint_lists.biorthogonal = self.Mypoint_lists.biorthogonal + 1

        if self.Mypoint_lists.phase == 5:
            self.Mypoint_lists.rotatewithpoint(e.pos().x(), e.pos().y())
            self.draw()

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

        if self.Mypoint_lists.circle == 2:
            for i in range(len(self.Mypoint_lists.line_coordinate)):
                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.circle_coordinate[
                    len(self.Mypoint_lists.circle_coordinate) - 1].x_coordinate) < 10) &
                        (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.circle_coordinate[
                            len(self.Mypoint_lists.circle_coordinate) - 1].y_coordinate) < 10)):
                    self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 1].x_coordinate = self.Mypoint_lists.line_coordinate[i].x_coordinate
                    self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 1].y_coordinate =self.Mypoint_lists.line_coordinate[i].y_coordinate

                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.circle_coordinate[
                    len(self.Mypoint_lists.circle_coordinate) - 2].x_coordinate) < 10) &
                (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.circle_coordinate[
                    len(self.Mypoint_lists.circle_coordinate) - 2].y_coordinate) < 10) ):
                    self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 2].x_coordinate =self.Mypoint_lists.circle_coordinate[i].x_coordinate
                    self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 2].y_coordinate =self.Mypoint_lists.circle_coordinate[i].y_coordinate

                a = self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 1].x_coordinate
                b = self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 2].x_coordinate
                c = self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 1].y_coordinate
                d = self.Mypoint_lists.circle_coordinate[len(self.Mypoint_lists.circle_coordinate) - 2].y_coordinate
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
                r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
                painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
            self.update()
            self.Mypoint_lists.circle = 0

        if self.Mypoint_lists.transformation == 2:
            self.image.fill(Qt.white)
            self.update()

            for i in range(len(self.Mypoint_lists.line_coordinate)):

                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate -
                         self.Mypoint_lists.transformation_coordinate[
                             len(self.Mypoint_lists.transformation_coordinate) - 2].x_coordinate) < 10) &
                        (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate -
                             self.Mypoint_lists.transformation_coordinate[
                                 len(self.Mypoint_lists.transformation_coordinate) - 2].y_coordinate) < 10)):
                    self.Mypoint_lists.line_coordinate[i].x_coordinate = self.Mypoint_lists.transformation_coordinate[
                        len(self.Mypoint_lists.transformation_coordinate) - 1].x_coordinate
                    self.Mypoint_lists.line_coordinate[i].y_coordinate = self.Mypoint_lists.transformation_coordinate[
                        len(self.Mypoint_lists.transformation_coordinate) - 1].y_coordinate
            x = 2
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            while x < len(self.Mypoint_lists.line_coordinate) + 1:
                a = self.Mypoint_lists.line_coordinate[x - 1].x_coordinate
                b = self.Mypoint_lists.line_coordinate[x - 2].x_coordinate
                c = self.Mypoint_lists.line_coordinate[x - 1].y_coordinate
                d = self.Mypoint_lists.line_coordinate[x - 2].y_coordinate
                painter.drawLine(QPoint(a, c), QPoint(b, d))
                x = x + 2
                self.update()


            for i in range(len(self.Mypoint_lists.circle_coordinate)):
                if i % 2 == 1:
                    continue

                if ((abs(self.Mypoint_lists.circle_coordinate[i].x_coordinate -
                         self.Mypoint_lists.transformation_coordinate[
                             len(self.Mypoint_lists.transformation_coordinate) - 2].x_coordinate) < 10) & (
                        abs(self.Mypoint_lists.circle_coordinate[i].y_coordinate -
                            self.Mypoint_lists.transformation_coordinate[
                                len(self.Mypoint_lists.transformation_coordinate) - 2].y_coordinate) < 10)):
                    self.Mypoint_lists.circle_coordinate[i].x_coordinate = self.Mypoint_lists.transformation_coordinate[
                        len(self.Mypoint_lists.transformation_coordinate) - 1].x_coordinate
                    self.Mypoint_lists.circle_coordinate[i].y_coordinate = self.Mypoint_lists.transformation_coordinate[
                        len(self.Mypoint_lists.transformation_coordinate) - 1].y_coordinate

            x = len(self.Mypoint_lists.circle_coordinate)
            while x > 1:
                a = self.Mypoint_lists.circle_coordinate[x - 1].x_coordinate
                b = self.Mypoint_lists.circle_coordinate[x - 2].x_coordinate
                c = self.Mypoint_lists.circle_coordinate[x - 1].y_coordinate
                d = self.Mypoint_lists.circle_coordinate[x - 2].y_coordinate
                r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
                painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
                x = x - 2
                self.update()


            self.Mypoint_lists.transformation = 0

        if self.Mypoint_lists.tangential == 2:
            a = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].x_coordinate
            b = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate
            c = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].y_coordinate
            d = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate

            center=0
            for i in range(len(self.Mypoint_lists.circle_coordinate)):
                if ((i % 2) != 0):
                    continue
                if ((abs(self.Mypoint_lists.circle_coordinate[i].x_coordinate - a) < 10) & (
                    abs(self.Mypoint_lists.circle_coordinate[i].y_coordinate - c) < 10)):
                    center = i
                break
            self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].x_coordinate = self.Mypoint_lists.circle_coordinate[center].x_coordinate
            b = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate
            self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 1].y_coordinate = self.Mypoint_lists.circle_coordinate[center].y_coordinate
            d = self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate

            a = self.Mypoint_lists.circle_coordinate[center].x_coordinate
            b = self.Mypoint_lists.circle_coordinate[center + 1].x_coordinate
            c = self.Mypoint_lists.circle_coordinate[center].y_coordinate
            d = self.Mypoint_lists.circle_coordinate[center + 1].y_coordinate

            r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
            A = r * r - (a - self.Mypoint_lists.tangential_coordinate[
                len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate) * (
                        a - self.Mypoint_lists.tangential_coordinate[
                    len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate)
            B = (2) * (a - self.Mypoint_lists.tangential_coordinate[
                len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate) * (
                        c - self.Mypoint_lists.tangential_coordinate[
                    len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate)
            C = r * r - (c - self.Mypoint_lists.tangential_coordinate[
                len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate) * (
                        c - self.Mypoint_lists.tangential_coordinate[
                    len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate)

            m_1 = (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)
            m_2 = (-B - math.sqrt(B * B - 4 * A * C)) / (2 * A)

            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

            painter.drawLine(QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_1),
                             QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_1))
            painter.drawLine(QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_2),
                            QPoint(self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,self.Mypoint_lists.tangential_coordinate[len(self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_2))

            self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
                self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,
                                                            self.Mypoint_lists.tangential_coordinate[len(
                                                                self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_1))
            self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
                self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,
                                                            self.Mypoint_lists.tangential_coordinate[len(
                                                                self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_1))
            self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
                self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate + 1000,
                                                            self.Mypoint_lists.tangential_coordinate[len(
                                                                self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate + 1000 * m_2))
            self.Mypoint_lists.line_coordinate.append(point(self.Mypoint_lists.tangential_coordinate[len(
                self.Mypoint_lists.tangential_coordinate) - 2].x_coordinate - 1000,
                                                            self.Mypoint_lists.tangential_coordinate[len(
                                                                self.Mypoint_lists.tangential_coordinate) - 2].y_coordinate - 1000 * m_2))

            self.update()
            self.Mypoint_lists.tangential = 0

        if self.Mypoint_lists.biorthogonal == 2:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

            for i in range(len(self.Mypoint_lists.line_coordinate) - 1):
                if (i % 2) == 0:
                    continue
                if ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].x_coordinate) < 10) &
                        (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].y_coordinate) < 10) &
                        (abs(self.Mypoint_lists.line_coordinate[i - 1].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].x_coordinate) < 10) &
                        (abs(self.Mypoint_lists.line_coordinate[i - 1].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].y_coordinate) < 10)):

                    middle_x_coordinate = (self.Mypoint_lists.line_coordinate[i].x_coordinate + self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / 2
                    middle_y_coordinate = (self.Mypoint_lists.line_coordinate[i].y_coordinate + self.Mypoint_lists.line_coordinate[i - 1].y_coordinate) / 2
                    slope = (-1) * (self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / (self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.line_coordinate[i - 1].y_coordinate)
                    painter.drawLine(QPoint(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope), QPoint(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))
                    self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope))
                    self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))

                elif ((abs(self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].x_coordinate) < 10) &
                          (abs(self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 2].y_coordinate) < 10) &
                          (abs(self.Mypoint_lists.line_coordinate[i - 1].x_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].x_coordinate) < 10) &
                          (abs(self.Mypoint_lists.line_coordinate[i - 1].y_coordinate - self.Mypoint_lists.biorthogonal_coordinate[len(self.Mypoint_lists.biorthogonal_coordinate) - 1].y_coordinate) < 10)):
                    middle_x_coordinate = (self.Mypoint_lists.line_coordinate[i].x_coordinate + self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / 2
                    middle_y_coordinate = (self.Mypoint_lists.line_coordinate[i].y_coordinate + self.Mypoint_lists.line_coordinate[i - 1].y_coordinate) / 2
                    slope = (-1) * (self.Mypoint_lists.line_coordinate[i].x_coordinate - self.Mypoint_lists.line_coordinate[i - 1].x_coordinate) / (self.Mypoint_lists.line_coordinate[i].y_coordinate - self.Mypoint_lists.line_coordinate[i - 1].y_coordinate)
                    painter.drawLine(QPoint(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope), QPoint(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))
                    self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate + 1000, middle_y_coordinate + 1000 * slope))
                    self.Mypoint_lists.line_coordinate.append(point(middle_x_coordinate - 1000, middle_y_coordinate - 1000 * slope))

            self.update()
            self.Mypoint_lists.biorthogonal = 0


    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
          self.last_point = e.pos()



    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False
        if e.button() == Qt.RightButton:
            self.drawing = False


    def translate(self):
        self.Mypoint_lists.translate()
        self.draw()



    def rotate(self):
        self.Mypoint_lists.rotatewithpoint(500,500)
        self.draw()


    def draw(self):
        self.image.fill(Qt.white)
        self.update()

        x = 2
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

        while x < len(self.Mypoint_lists.line_coordinate) + 1:
            a = self.Mypoint_lists.line_coordinate[x - 1].x_coordinate
            b = self.Mypoint_lists.line_coordinate[x - 2].x_coordinate
            c = self.Mypoint_lists.line_coordinate[x - 1].y_coordinate
            d = self.Mypoint_lists.line_coordinate[x - 2].y_coordinate
            painter.drawLine(QPoint(a, c), QPoint(b, d))
            x = x + 2
            self.update()

        x = len(self.Mypoint_lists.circle_coordinate)
        while x > 1:
            a = self.Mypoint_lists.circle_coordinate[x - 1].x_coordinate
            b = self.Mypoint_lists.circle_coordinate[x - 2].x_coordinate
            c = self.Mypoint_lists.circle_coordinate[x - 1].y_coordinate
            d = self.Mypoint_lists.circle_coordinate[x - 2].y_coordinate
            r = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
            painter.drawEllipse(b - r, d - r, 2 * r, 2 * r)
            x = x - 2
            self.update()


    def clear(self):
        if self.Mypoint_lists.phase == 0:
            self.Mypoint_lists.phase = 1
        elif self.Mypoint_lists.phase == 1:
            self.Mypoint_lists.phase = 2
        elif self.Mypoint_lists.phase == 2:
            self.Mypoint_lists.phase = 3
        elif self.Mypoint_lists.phase == 3:
            self.Mypoint_lists.phase = 4
        elif self.Mypoint_lists.phase == 4:
            self.Mypoint_lists.phase = 5
        elif self.Mypoint_lists.phase == 5:
            self.Mypoint_lists.phase = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())