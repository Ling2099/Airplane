from plane_sprites import *


class PlaneGame(object):
    """ 飞机大战主程序类 """

    def __init__(self):
        """ 初始化类 """
        # 创建游戏窗口 480*700
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        # 创建精灵及精灵组
        self.__create_sprites()
        # 创建敌机
        pygame.time.set_timer(ENEMY_EVENT, 400)

    def start_game(self):
        """ 游戏开始 """
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_RATE)
            # 时间监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵及精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()
            pass

    def __create_sprites(self):
        """ 创建精灵 """
        # 创建背景精灵及精灵组
        back_ground1 = BackGround()
        # 第二张背景图片出现在第一张的正上方
        back_ground2 = BackGround(True)
        self.back_group = pygame.sprite.Group(back_ground1, back_ground2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵及精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        """  事件监听 """
        for event in pygame.event.get():
            # 是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加敌机精灵至精灵组
                self.enemy_group.add(enemy)

        # 监听键盘按键 返回按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """ 碰撞检测 """
        pass

    def __update_sprites(self):
        """  更新精灵及精灵组 """
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """ 终止游戏 """
        pygame.quit()
        exit()


game = PlaneGame()
game.start_game()