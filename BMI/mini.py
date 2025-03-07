import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QLabel, QApplication, QPushButton, QLineEdit, QTextEdit


class BMICalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BMI Calculator 🏋️‍♂️")
        self.setGeometry(200, 200, 500, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        font = QtGui.QFont()
        font.setPointSize(12)

        # Height Slider & Input
        self.height_label = QLabel("Height (cm):", self)
        self.height_label.setGeometry(50, 50, 120, 30)
        self.height_label.setFont(font)

        self.height_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.height_slider.setGeometry(180, 50, 200, 30)
        self.height_slider.setRange(100, 250)
        self.height_slider.valueChanged.connect(self.update_height)

        self.height_input = QLineEdit(self)
        self.height_input.setGeometry(400, 50, 50, 30)
        self.height_input.setText("170")
        self.height_input.textChanged.connect(self.slider_height_update)

        # Weight Slider & Input
        self.weight_label = QLabel("Weight (kg):", self)
        self.weight_label.setGeometry(50, 100, 120, 30)
        self.weight_label.setFont(font)

        self.weight_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.weight_slider.setGeometry(180, 100, 200, 30)
        self.weight_slider.setRange(30, 200)
        self.weight_slider.valueChanged.connect(self.update_weight)

        self.weight_input = QLineEdit(self)
        self.weight_input.setGeometry(400, 100, 50, 30)
        self.weight_input.setText("70")
        self.weight_input.textChanged.connect(self.slider_weight_update)

        # Calculate Button
        self.calculate_btn = QPushButton("Calculate BMI", self)
        self.calculate_btn.setGeometry(200, 160, 120, 40)
        self.calculate_btn.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 10px;")
        self.calculate_btn.clicked.connect(self.calculate_bmi)

        # BMI Result Output
        self.result_box = QTextEdit(self)
        self.result_box.setGeometry(100, 220, 300, 100)
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("background-color: white; border: 1px solid #ddd; font-size: 14px;")

    def update_height(self):
        self.height_input.setText(str(self.height_slider.value()))

    def update_weight(self):
        self.weight_input.setText(str(self.weight_slider.value()))

    def slider_height_update(self):
        try:
            value = int(self.height_input.text())
            self.height_slider.setValue(value)
        except ValueError:
            pass  # Ignore invalid input

    def slider_weight_update(self):
        try:
            value = int(self.weight_input.text())
            self.weight_slider.setValue(value)
        except ValueError:
            pass  # Ignore invalid input

    def calculate_bmi(self):
        try:
            height = int(self.height_input.text()) / 100  # Convert cm to meters
            weight = int(self.weight_input.text())
            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)

            self.result_box.setText(f"Your BMI is: {bmi:.2f}\nCategory: {category}")
        except ZeroDivisionError:
            self.result_box.setText("Invalid height input!")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight 😕"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight 😊"
        elif 25 <= bmi < 29.9:
            return "Overweight 😐"
        else:
            return "Obese 😟"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())