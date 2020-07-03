from screen.screen import Screen
from utilities.size import Size

def main():
    screen = Screen()

    screen.setWindow(0, 0)
    screen.setFramerate(30)
    screen.setFont('resources/fonts/Courier Prime Code.ttf', 24)

    screen.start()


if __name__ == '__main__':
    main()
