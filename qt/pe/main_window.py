# Created By: Virgil Dupras
# Created On: 2009-05-23
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox, QAction

from base.main_window import MainWindow as MainWindowBase

class MainWindow(MainWindowBase):
    def _setupUi(self):
        MainWindowBase._setupUi(self)
        self.actionClearPictureCache = QAction("Clear Picture Cache", self)
        self.menuFile.insertAction(self.actionClearIgnoreList, self.actionClearPictureCache)
        self.connect(self.actionClearPictureCache, SIGNAL("triggered()"), self.clearPictureCacheTriggered)
    
    def clearPictureCacheTriggered(self):
        title = "Clear Picture Cache"
        msg = "Do you really want to remove all your cached picture analysis?"
        if self._confirm(title, msg, QMessageBox.No):
            self.app.scanner.cached_blocks.clear()
            QMessageBox.information(self, title, "Picture cache cleared.")
    