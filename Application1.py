from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(994, 624)
        Application.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #1e1e2f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Application)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
"    background-color: #598BAF;\n"
" border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color:  #1e1e2f;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"   background-color: #1e1e2f;\n"
"    border: none;\n"
"padding-right: 2px;\n"
"padding-left:2px;\n"
" margin-right: 10px;\n"
"margin-left: 10px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.design_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.design_tab.setPalette(palette)
        self.design_tab.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.design_tab.setObjectName("design_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.design_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.design_box = QtWidgets.QGroupBox(self.design_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.design_box.setFont(font)
        self.design_box.setStyleSheet("border: none;")
        self.design_box.setObjectName("design_box")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.design_box)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Zplane_box = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Zplane_box.sizePolicy().hasHeightForWidth())
        self.Zplane_box.setSizePolicy(sizePolicy)
        self.Zplane_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Zplane_box.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Zplane_box.setObjectName("Zplane_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Zplane_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.Zplane_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.z_plane = PlotWidget(self.Zplane_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_plane.sizePolicy().hasHeightForWidth())
        self.z_plane.setSizePolicy(sizePolicy)
        self.z_plane.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.z_plane.setObjectName("z_plane")
        self.verticalLayout_4.addWidget(self.z_plane)
        self.verticalLayout_3.addWidget(self.Zplane_box)
        self.preferenceBox = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preferenceBox.sizePolicy().hasHeightForWidth())
        self.preferenceBox.setSizePolicy(sizePolicy)
        self.preferenceBox.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.preferenceBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.preferenceBox.setObjectName("preferenceBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.preferenceBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.preferenceBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.preferenceBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.Clear_combobox = QtWidgets.QComboBox(self.preferenceBox)
        self.Clear_combobox.setEditable(True)
        self.Clear_combobox.setObjectName("Clear_combobox")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.Clear_combobox)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.confirm_button = QtWidgets.QPushButton(self.preferenceBox)
        self.confirm_button.setMaximumSize(QtCore.QSize(86, 16777215))
        self.confirm_button.setStyleSheet("background-color: #00A86B;\n"
"      color: white;\n"
"      border: none;\n"
"      padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_9.addWidget(self.confirm_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zeros_button = QtWidgets.QRadioButton(self.preferenceBox)
        self.zeros_button.setObjectName("zeros_button")
        self.horizontalLayout_5.addWidget(self.zeros_button)
        self.phase_button = QtWidgets.QRadioButton(self.preferenceBox)
        self.phase_button.setObjectName("phase_button")
        self.horizontalLayout_5.addWidget(self.phase_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.preferenceBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.mag_slider = QtWidgets.QSlider(self.preferenceBox)
        self.mag_slider.setOrientation(QtCore.Qt.Horizontal)
        self.mag_slider.setObjectName("mag_slider")
        self.horizontalLayout_6.addWidget(self.mag_slider)
        self.mag_LCD = QtWidgets.QLCDNumber(self.preferenceBox)
        self.mag_LCD.setObjectName("mag_LCD")
        self.horizontalLayout_6.addWidget(self.mag_LCD)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.preferenceBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.phase_slider = QtWidgets.QSlider(self.preferenceBox)
        self.phase_slider.setOrientation(QtCore.Qt.Horizontal)
        self.phase_slider.setObjectName("phase_slider")
        self.horizontalLayout_7.addWidget(self.phase_slider)
        self.phase_LCD = QtWidgets.QLCDNumber(self.preferenceBox)
        self.phase_LCD.setObjectName("phase_LCD")
        self.horizontalLayout_7.addWidget(self.phase_LCD)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.preferenceBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.add_conjugates = QtWidgets.QPushButton(self.preferenceBox)
        self.add_conjugates.setStyleSheet("background-color: #00A86B;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.add_conjugates.setObjectName("add_conjugates")
        self.horizontalLayout_8.addWidget(self.add_conjugates)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.preferenceBox)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.magBox = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magBox.sizePolicy().hasHeightForWidth())
        self.magBox.setSizePolicy(sizePolicy)
        self.magBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.magBox.setObjectName("magBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.magBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.magBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Magnitude_graph = PlotWidget(self.magBox)
        self.Magnitude_graph.setObjectName("Magnitude_graph")
        self.verticalLayout.addWidget(self.Magnitude_graph)
        self.verticalLayout_5.addWidget(self.magBox)
        self.phasebox = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phasebox.sizePolicy().hasHeightForWidth())
        self.phasebox.setSizePolicy(sizePolicy)
        self.phasebox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.phasebox.setObjectName("phasebox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.phasebox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.phasebox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.Phase_graph = PlotWidget(self.phasebox)
        self.Phase_graph.setObjectName("Phase_graph")
        self.verticalLayout_6.addWidget(self.Phase_graph)
        self.verticalLayout_5.addWidget(self.phasebox)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addWidget(self.design_box, 0, 0, 1, 1)
        self.tabWidget.addTab(self.design_tab, "")
        self.correction_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.correction_tab.setPalette(palette)
        self.correction_tab.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.correction_tab.setObjectName("correction_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.correction_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.correction_tab)
        self.groupBox.setStyleSheet("border: none;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.Zplane_box_2 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Zplane_box_2.sizePolicy().hasHeightForWidth())
        self.Zplane_box_2.setSizePolicy(sizePolicy)
        self.Zplane_box_2.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Zplane_box_2.setObjectName("Zplane_box_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Zplane_box_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.Zplane_box_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        spacerItem5 = QtWidgets.QSpacerItem(188, 5, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.z_plane_2 = PlotWidget(self.Zplane_box_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_plane_2.sizePolicy().hasHeightForWidth())
        self.z_plane_2.setSizePolicy(sizePolicy)
        self.z_plane_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.z_plane_2.setObjectName("z_plane_2")
        self.verticalLayout_11.addWidget(self.z_plane_2)
        self.horizontalLayout_21.addWidget(self.Zplane_box_2)
        self.mag_box = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mag_box.sizePolicy().hasHeightForWidth())
        self.mag_box.setSizePolicy(sizePolicy)
        self.mag_box.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.mag_box.setObjectName("mag_box")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mag_box)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.mag_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        spacerItem6 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.Magnitude_graph_2 = PlotWidget(self.mag_box)
        self.Magnitude_graph_2.setObjectName("Magnitude_graph_2")
        self.verticalLayout_10.addWidget(self.Magnitude_graph_2)
        self.horizontalLayout_21.addWidget(self.mag_box)
        self.phase_box = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_box.sizePolicy().hasHeightForWidth())
        self.phase_box.setSizePolicy(sizePolicy)
        self.phase_box.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.phase_box.setObjectName("phase_box")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.phase_box)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(self.phase_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        spacerItem7 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.corrected_phase = PlotWidget(self.phase_box)
        self.corrected_phase.setObjectName("corrected_phase")
        self.verticalLayout_12.addWidget(self.corrected_phase)
        self.horizontalLayout_21.addWidget(self.phase_box)
        self.gridLayout_6.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.customBox = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customBox.sizePolicy().hasHeightForWidth())
        self.customBox.setSizePolicy(sizePolicy)
        self.customBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.customBox.setObjectName("customBox")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.customBox)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lineEdit = QtWidgets.QLineEdit(self.customBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_20.addWidget(self.lineEdit)
        self.apply_custom_filter = QtWidgets.QPushButton(self.customBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_custom_filter.sizePolicy().hasHeightForWidth())
        self.apply_custom_filter.setSizePolicy(sizePolicy)
        self.apply_custom_filter.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.apply_custom_filter.setFont(font)
        self.apply_custom_filter.setStyleSheet("background-color: #00A86B;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.apply_custom_filter.setObjectName("apply_custom_filter")
        self.horizontalLayout_20.addWidget(self.apply_custom_filter)
        self.gridLayout_6.addWidget(self.customBox, 2, 0, 1, 1)
        self.filterBox = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterBox.sizePolicy().hasHeightForWidth())
        self.filterBox.setSizePolicy(sizePolicy)
        self.filterBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.filterBox.setObjectName("filterBox")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.filterBox)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QtWidgets.QLabel(self.filterBox)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.filter_combobox = QtWidgets.QComboBox(self.filterBox)
        self.filter_combobox.setStyleSheet("")
        self.filter_combobox.setObjectName("filter_combobox")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.horizontalLayout_18.addWidget(self.filter_combobox)
        self.add_filter_button = QtWidgets.QPushButton(self.filterBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_filter_button.setFont(font)
        self.add_filter_button.setStyleSheet("background-color: #00A86B;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.add_filter_button.setObjectName("add_filter_button")
        self.horizontalLayout_18.addWidget(self.add_filter_button)
        self.delete_filter_button = QtWidgets.QPushButton(self.filterBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delete_filter_button.setFont(font)
        self.delete_filter_button.setStyleSheet("background-color: #E0115F;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.delete_filter_button.setObjectName("delete_filter_button")
        self.horizontalLayout_18.addWidget(self.delete_filter_button)
        self.gridLayout_6.addWidget(self.filterBox, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.correction_tab, "")
        self.Results_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Results_tab.setPalette(palette)
        self.Results_tab.setStyleSheet("border:none;")
        self.Results_tab.setObjectName("Results_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Results_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.resultBox = QtWidgets.QGroupBox(self.Results_tab)
        self.resultBox.setStyleSheet("")
        self.resultBox.setObjectName("resultBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.resultBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RealBox = QtWidgets.QGroupBox(self.resultBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RealBox.sizePolicy().hasHeightForWidth())
        self.RealBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RealBox.setFont(font)
        self.RealBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.RealBox.setObjectName("RealBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.RealBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(88, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.real_signal = PlotWidget(self.RealBox)
        self.real_signal.setObjectName("real_signal")
        self.verticalLayout_7.addWidget(self.real_signal)
        self.gridLayout_4.addWidget(self.RealBox, 0, 0, 1, 1)
        self.FilteredBox = QtWidgets.QGroupBox(self.resultBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilteredBox.sizePolicy().hasHeightForWidth())
        self.FilteredBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FilteredBox.setFont(font)
        self.FilteredBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.FilteredBox.setObjectName("FilteredBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FilteredBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filtered_signal = PlotWidget(self.FilteredBox)
        self.filtered_signal.setObjectName("filtered_signal")
        self.gridLayout_3.addWidget(self.filtered_signal, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem9 = QtWidgets.QSpacerItem(88, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.FilteredBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.speed_slider = QtWidgets.QSlider(self.FilteredBox)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.horizontalLayout_14.addWidget(self.speed_slider)
        self.speed_LCD = QtWidgets.QLCDNumber(self.FilteredBox)
        self.speed_LCD.setObjectName("speed_LCD")
        self.horizontalLayout_14.addWidget(self.speed_LCD)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.FilteredBox, 1, 0, 1, 1)
        self.loadingBox = QtWidgets.QGroupBox(self.resultBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.loadingBox.setFont(font)
        self.loadingBox.setStyleSheet("QGroupBox {\n"
"background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"}\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: -5px 0px 0px 0px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.loadingBox.setObjectName("loadingBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.loadingBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(394, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(0, -1, 60, -1)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.load_button = QtWidgets.QRadioButton(self.loadingBox)
        self.load_button.setMaximumSize(QtCore.QSize(156, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load_button.setFont(font)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_15.addWidget(self.load_button)
        self.touch_pad_button = QtWidgets.QRadioButton(self.loadingBox)
        self.touch_pad_button.setMaximumSize(QtCore.QSize(156, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touch_pad_button.setFont(font)
        self.touch_pad_button.setObjectName("touch_pad_button")
        self.horizontalLayout_15.addWidget(self.touch_pad_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        spacerItem11 = QtWidgets.QSpacerItem(394, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_22.addLayout(self.verticalLayout_8)
        self.touch_pad = QtWidgets.QGraphicsView(self.loadingBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.touch_pad.sizePolicy().hasHeightForWidth())
        self.touch_pad.setSizePolicy(sizePolicy)
        self.touch_pad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.touch_pad.setStyleSheet("border: 1px solid white;\n"
"border-radius: 15px;")
        self.touch_pad.setObjectName("touch_pad")
        self.horizontalLayout_22.addWidget(self.touch_pad)
        self.gridLayout_8.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.loadingBox, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.resultBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Results_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        Application.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Application)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        Application.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Application)
        self.statusbar.setObjectName("statusbar")
        Application.setStatusBar(self.statusbar)

        self.retranslateUi(Application)
        self.tabWidget.setCurrentIndex(1)
        self.Clear_combobox.setCurrentIndex(0)
        self.mag_slider.valueChanged['int'].connect(self.mag_LCD.display) # type: ignore
        self.phase_slider.valueChanged['int'].connect(self.phase_LCD.display) # type: ignore
        self.speed_slider.valueChanged['int'].connect(self.speed_LCD.display) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "MainWindow"))
        self.label.setText(_translate("Application", "Realtime Digital Filter"))
        self.label_3.setText(_translate("Application", "Z - Pole"))
        self.label_5.setText(_translate("Application", "Zeros-poles placement:"))
        self.label_6.setText(_translate("Application", "Clear:"))
        self.Clear_combobox.setCurrentText(_translate("Application", "all zeros"))
        self.Clear_combobox.setItemText(0, _translate("Application", "all zeros"))
        self.Clear_combobox.setItemText(1, _translate("Application", "all poles"))
        self.Clear_combobox.setItemText(2, _translate("Application", "clear all"))
        self.Clear_combobox.setItemText(3, _translate("Application", "current"))
        self.confirm_button.setText(_translate("Application", "Confirm"))
        self.zeros_button.setText(_translate("Application", "Zeros"))
        self.phase_button.setText(_translate("Application", "Poles"))
        self.label_7.setText(_translate("Application", "magnitude:"))
        self.label_8.setText(_translate("Application", "Phase:"))
        self.label_9.setText(_translate("Application", "Conjugates:"))
        self.add_conjugates.setText(_translate("Application", "Add"))
        self.label_2.setText(_translate("Application", "Magnitude Response"))
        self.label_4.setText(_translate("Application", "Phase Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.design_tab), _translate("Application", "Design"))
        self.label_14.setText(_translate("Application", "Z - Pole"))
        self.label_13.setText(_translate("Application", "Magnitude Response"))
        self.label_16.setText(_translate("Application", "Corrected Phase"))
        self.lineEdit.setPlaceholderText(_translate("Application", "enter arbitary \'a\'"))
        self.apply_custom_filter.setText(_translate("Application", "Apply"))
        self.label_15.setText(_translate("Application", "Choose Filter:"))
        self.filter_combobox.setItemText(0, _translate("Application", "New Item"))
        self.filter_combobox.setItemText(1, _translate("Application", "New Item"))
        self.filter_combobox.setItemText(2, _translate("Application", "New Item"))
        self.filter_combobox.setItemText(3, _translate("Application", "New Item"))
        self.filter_combobox.setItemText(4, _translate("Application", "New Item"))
        self.filter_combobox.setItemText(5, _translate("Application", "custom"))
        self.add_filter_button.setText(_translate("Application", "Add"))
        self.delete_filter_button.setText(_translate("Application", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.correction_tab), _translate("Application", "Correction"))
        self.RealBox.setTitle(_translate("Application", "Real Signal"))
        self.FilteredBox.setTitle(_translate("Application", "Filtered Signal"))
        self.label_12.setText(_translate("Application", "Speed"))
        self.loadingBox.setTitle(_translate("Application", "Preferences"))
        self.load_button.setText(_translate("Application", "Load Signal"))
        self.touch_pad_button.setText(_translate("Application", "Touch Pad"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results_tab), _translate("Application", "Results"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())