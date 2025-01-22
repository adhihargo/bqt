import logging

logger = logging.getLogger(__name__)

try:
    logger.info("Importing Qt module")
    from qtpy import QtCore
    from qtpy.QtCore import Qt, QEvent, QObject, QRect, QSettings, QTimer, QDir
    from qtpy.QtWidgets import QApplication, QWidget, QMainWindow, QDockWidget, QMessageBox
    from qtpy.QtGui import QCloseEvent, QIcon, QWindow, QImage, QPixmap
except Exception:
    logger.exception("Error importing Qt module:")
