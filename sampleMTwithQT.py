import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sample MT with QT")

        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a canvas object to draw graphs
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        self.plot_graphs()

    def plot_graphs(self):
        ax = self.canvas.axes
        ax.clear()

        # Generate and plot 14 different data graphs
        x = np.linspace(0, 10, 100)
        for i in range(14):
            y = np.sin(x + i) - np.sin(i)  # Adjust each sine wave to start from 0
            ax.plot(x, y, label=f'Graph {i+1}')
            
        ax.legend()
        ax.set_title('14 Different Data Graphs')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
