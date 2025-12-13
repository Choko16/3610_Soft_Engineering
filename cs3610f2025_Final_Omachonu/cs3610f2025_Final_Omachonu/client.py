from control_button_publisher import ControlButtonPublisher
from control_button import ControlButton
from regular_button import RegularButton

def main() -> None:
    publisher = ControlButtonPublisher()

    up = ControlButton("Up", "UP", publisher)
    down = ControlButton("Down", "DOWN", publisher)
    left = ControlButton("Left", "LEFT", publisher)
    right = ControlButton("Right", "RIGHT", publisher)

    b1 = RegularButton("Button A")
    b2 = RegularButton("Button B")

    
    b1.click(publisher)
    b2.click(publisher)

    up.click()
    right.click()

    
    b1.click(publisher)

    down.click()
    left.click()

if __name__ == "__main__":
    main()
