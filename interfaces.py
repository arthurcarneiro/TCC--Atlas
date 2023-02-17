from PyQt5 import QtGui, QtCore, QtWidgets
import sys, cv2, numpy as np
from netmiko import Netmiko, ConnectHandler, file_transfer
 
class Second(QtWidgets.QMainWindow):
    def __init__(self, Image, parent=None):
        super(Second, self).__init__(parent)
        self.Image = Third(self)
        self.pixmap = QtGui.QPixmap(Image)
        self.resize(self.pixmap.width(),self.pixmap.height())
        self.Image.setGeometry(QtCore.QRect(-1, -1, self.pixmap.width(),self.pixmap.height()))
        self.Image.setPixmap(self.pixmap)
        self.setGeometry(300, 500, self.Image.width(), self.Image.height())
        #self.setMouseTracking(True)
    
    def getXandY (self):
        x, y = self.Image.getXandY()
        return x, y
    
    def refresh_image(self, Image):
        self.pixmap = QtGui.QPixmap(Image)
        self.Image.setPixmap(self.pixmap)

    def get_pixmap (self):
        return self.pixmap

    
    
    
    

class Third(QtWidgets.QLabel):
    def __init__(self, parent=None):
        self.x = 0
        self.y = 0
        super(Third, self).__init__(parent)
        
    
    def mouseDoubleClickEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        
    def getXandY (self):
        return self.x, self.y
    
    
        
    
    

 
 
class First(QtWidgets.QMainWindow):
    def __init__(self, MainWindow, parent=None):
        super(First, self).__init__(parent)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.Image = QtWidgets.QLabel(self.frame)
        self.Image.setMinimumSize(QtCore.QSize(100, 250))
        self.Image.setText("No Image Loaded.")
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        
        self.verticalLayout_2.addWidget(self.Image)
        spacerItem = QtWidgets.QSpacerItem(300, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(2000, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.Run = QtWidgets.QPushButton(self.frame_2)
        self.Run.setMaximumSize(QtCore.QSize(300, 50))
        self.Run.setObjectName("Run")
        self.horizontalLayout_2.addWidget(self.Run)
        


        self.Get_Files = QtWidgets.QPushButton(self.frame_2)
        self.Get_Files.setMaximumSize(QtCore.QSize(300, 50))
        self.Get_Files.setObjectName("Get_Files")
        self.horizontalLayout_2.addWidget(self.Get_Files)
        
        self.verticalLayout_2.addWidget(self.frame_2)
        
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.line)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.LoadImage = QtWidgets.QPushButton(self.centralwidget)
        self.LoadImage.setMaximumSize(QtCore.QSize(400, 40))
        self.LoadImage.setObjectName("LoadImage")
        self.verticalLayout.addWidget(self.LoadImage)
        
        self.CreateMask = QtWidgets.QPushButton(self.centralwidget)
        self.CreateMask.setMaximumSize(QtCore.QSize(400, 40))
        self.CreateMask.setObjectName("CreateMask")
        self.verticalLayout.addWidget(self.CreateMask)

        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.append_value = QtWidgets.QPushButton(self.centralwidget)
        self.append_value.setMaximumSize(QtCore.QSize(400, 40))
        self.append_value.setObjectName("Append Value")
        self.verticalLayout.addWidget(self.append_value)

        self.save_mask = QtWidgets.QPushButton(self.centralwidget)
        self.save_mask.setMaximumSize(QtCore.QSize(400, 40))
        self.save_mask.setObjectName("Append Value")
        self.verticalLayout.addWidget(self.save_mask)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.huawei_logo = QtGui.QPixmap("Screenshot from 2023-02-15 16-16-03.png")
        self.huawei_logo = self.huawei_logo.scaledToWidth(225)
        self.label.setPixmap(self.huawei_logo)

        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.showMaximized()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        self.ImageFile = ""

        self.LoadImage.clicked.connect(self.LoadImageClicked)

        self.CreateMask.clicked.connect(self.on_pushButton_clicked)

        self.append_value.clicked.connect(self.on_append_value_clicked)

        self.save_mask.clicked.connect(self.on_save_mask_clicked)

        self.Run.clicked.connect(self.RunClicked)

        self.Get_Files.clicked.connect(self.GetFilesClicked)

        self.linux_jump_host_ip = '192.168.0.2'
        self.linux_jump_host_user = 'HwHiAiUser'
        self.linux_jump_host_password = '' #Senha padrão do Atlas 200 DK


        self.net_connect = ConnectHandler(
                        device_type='linux',
                        host=self.linux_jump_host_ip,
                        username=self.linux_jump_host_user,
                        password=self.linux_jump_host_password
        )

        self.dialogs = list()

    def on_save_mask_clicked(self):
        imp_img = self.dialog.get_pixmap().toImage()
        imp_img = self.convertQImageToMat(imp_img)

        dummy = cv2.imread(self.ImageFile.split('/')[-1])
        subtracted = cv2.subtract(dummy,imp_img)

        subtracted = cv2.cvtColor(subtracted, cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(subtracted, 10, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.bitwise_not(thresh1)
        self.mask_file_name = 'mask.jpg'
        cv2.imwrite(self.mask_file_name, thresh1)




 
    def on_pushButton_clicked(self):
        print("passei")
        Image = self.ImageFile.split('/')
        self.image_file_name = Image[-1]
        print(self.image_file_name)
        self.dialog = Second(Image[-1], parent=self)
        self.dialogs.append(self.dialog)
        self.dialog.show()

    def on_append_value_clicked(self):
        x,y = self.dialog.getXandY()
        imp_img = self.dialog.get_pixmap().toImage()
        
        imp_img = self.convertQImageToMat(imp_img)
        #img = cv2.imread(imp_img)

        cv2.circle(imp_img,(x,y),50,(0,0,0),-1)

        height, width, channel = imp_img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(imp_img.data, width, height, bytesPerLine, QtGui.QImage.Format_BGR888)
        self.dialog.refresh_image(qImg)

    def convertQImageToMat(self, incomingImage):
        '''  Converts a QImage into an opencv MAT format  '''

        incomingImage = incomingImage.convertToFormat(QtGui.QImage.Format_BGR888)

        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.bits()
        ptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 3)  #  Copies the data
        return arr


    def LoadImageClicked(self):

        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);; Image (*.jpg)")

        if fname:
            self.ImageFile = str(fname[0])
            print(self.ImageFile)
            pixmap = QtGui.QPixmap(self.ImageFile)
            pixmap = pixmap.scaledToWidth(600)
            #self.resize(pixmap.width(),pixmap.height())
            self.Image.setPixmap(pixmap)
    
    def on_CreateMask_Clicked(self):

        image_file = self.ImageFile.split('/')
        mouse_tracker = MouseTracker()
        print("O arquivo é " + str(image_file[-1]))
        
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Get_Files.setText(_translate("MainWindow", "Get Files"))
        self.LoadImage.setText(_translate("MainWindow", "Load Image"))
        self.CreateMask.setText(_translate("MainWindow", "Create Mask"))
        self.append_value.setText(_translate("MainWindow", "Save Values"))
        self.save_mask.setText(_translate("MainWindow", "Save Mask"))


    def GetFilesClicked(self):
        transfer_dict = file_transfer(
        self.net_connect,
        source_file='/home/HwHiAiUser/samples/python/level2_simple_inference/6_other/imageinpainting_hifill/out/outpaint_' + self.image_file_name,
        
        dest_file='/home/arthur/TCC notebooks/out/outpaint_' + self.image_file_name,
        file_system='/',
        direction='get',
        overwrite_file=True,
        )
        print(transfer_dict)
        
    def RunClicked(self):

        

        transfer_dict = file_transfer(
        self.net_connect,
        source_file='/home/arthur/TCC notebooks/' + self.image_file_name,
        dest_file='home/HwHiAiUser/samples/python/level2_simple_inference/6_other/imageinpainting_hifill/data/' + self.image_file_name,
        file_system='/',
        direction='put',
        overwrite_file=True,
        )
        print(transfer_dict)

        transfer_dict = file_transfer(
        self.net_connect,
        source_file='/home/arthur/TCC notebooks/' + self.mask_file_name,
        dest_file='home/HwHiAiUser/samples/python/level2_simple_inference/6_other/imageinpainting_hifill/mask/mask.jpg', #+ self.image_file_name,
        file_system='/',
        direction='put',
        overwrite_file=True,
        )
        print(transfer_dict)

        output1 = self.net_connect.send_command("./run_python_file.sh",expect_string='init',read_timeout=10)
        print(output1)
        output2 = self.net_connect.send_command(self.linux_jump_host_password,expect_string='./ts',read_timeout=10)
        print(output2)



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main = First(MainWindow)
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()