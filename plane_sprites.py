import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_RATE = 60
# 游戏背景图片相对路径
BACKGROUND_PATH = "./images/background.png"
# 敌机图片相对路径
ENEMY_PATH = "./images/enemy1.png"
# 英雄图片相对路径
HERO_PATH = "./images/me1.png"
# 子弹图片相对路径
BULLET_PATH = "./images/bullet1.png"
# 敌机定时器
ENEMY_EVENT = pygame.USEREVENT


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
    """  背景图片精灵类 """

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


class Enemy(GameSpite):
    """  敌机精灵类 """

    def __init__(self):
        # 调用父类创建敌机
        super().__init__(ENEMY_PATH)
        # 初始化敌机随机速度
        self.speed = random.randint(1, 6)
        # 初始化敌机随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        # 保持敌机垂直飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            # 将精灵从精灵组中删除 同时销毁内存
            self.kill()


class Hero(GameSpite):
    """  英雄精灵类 """

    def __init__(self):
        # 调用父类创建英雄及速度
        super().__init__(HERO_PATH, 0)
        # 初始化英雄位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):
        """  控制英雄移动 """
        self.rect.x += self.speed
        """  自加功能 """
        # 英雄上下移动
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y += -3
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 3
        # 英雄左右边界控制
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        # 英雄上下边界控制
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height


class Bullet(GameSpite):
    """  子弹精灵类 """

    def __init__(self):
        super().__init__()

    def update(self):
        pass