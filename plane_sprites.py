import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_RATE = 60
# 游戏背景图片相对路径
BACKGROUND_PATH = "./images/background.png"


class GameSpite(pygame.sprite.Sprite):
    """ 游戏精灵 """
    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class BackGround(GameSpite):

    def __init__(self, is_alt=False):
        # 调用父类初始化实现背景精灵的创建
        super().__init__(BACKGROUND_PATH)
        # 判断是否交替图像
        if is_alt:
            self.rect.y = - self.rect.height

    """  背景滚动 """
    def update(self):
        # 调用父类的垂直滚动
        super().update()
        # 判断背景图片是否移除屏幕 如果移除屏幕 将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height

