from PyQt5.QtWidgets import QTabWidget
from qtconsole.manager import QtKernelManager
from qtconsole.rich_jupyter_widget import RichJupyterWidget

from glia.utils import get_theme_contents


class TabbedJupyterWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabbedJupyterWidget, self).__init__(parent)

        # Properties
        self.setTabPosition(QTabWidget.South)

        # Default Tab
        self.jupyter_widget = self.start_kernel('python')
        self.addTab(self.jupyter_widget, 'Python')

        # Create a tab creation method that also keeps track of the
        # jupyter objects created.

    def start_kernel(self, kernel: str):
        kernel_manager = QtKernelManager(kernel_name=kernel)
        kernel_manager.start_kernel()

        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        jupyter_widget = RichJupyterWidget()

        jupyter_widget.style_sheet = get_theme_contents(
            "dracula",
            "jupyter.css"
        )
        jupyter_widget.syntax_style = "dracula"
        jupyter_widget.kernel_manager = kernel_manager
        jupyter_widget.kernel_client = kernel_client
        return jupyter_widget  # Binding this to a variable won't work.
