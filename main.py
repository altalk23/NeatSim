from screen.screen import Screen

def main():
    screen = Screen()

    screen.setWindow(960, 540)
    screen.setFramerate(30)
    screen.setFont('resources/fonts/Courier Prime Code.ttf', 24)

    screen.start()


if __name__ == '__main__':
    main()
