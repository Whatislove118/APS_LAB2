# предположим у нас есть фреймворк для обработки видео

class VideoFramework:
    # тут 1 млн кода и 1 млн методов, но нам нужен только один

    def chop_video(self):
        pass

    # ...........

# Наш фасад
class FacadeChopVideo:

    def chop_video(self):
        # some code
        pass

def main():
    # создаем наш фасад и используем определенную функциональность
    facade = FacadeChopVideo()
    facade.chop_video()


if __name__ == '__main':
    main()