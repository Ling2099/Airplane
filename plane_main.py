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
        pygame.time.set_timer(ENEMY_EVENT, 500)

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

    def __check_collide(self):
        """ 碰撞检测 """
        pass

    def __update_sprites(self):
        """  更新精灵及精灵组 """
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """ 终止游戏 """
        pygame.quit()
        exit()


game = PlaneGame()
game.start_game()

"""
pygame.init()
# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))
# 加载背景图片数据
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
# 加载玩家图片数据
player = pygame.image.load("./images/me1.png")
screen.blit(player, (180, 500))
# 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 记录玩家位置
player_rect = pygame.Rect(180, 500, 102, 126)

# 创建敌机精灵
enemy = GameSpite("./images/enemy1.png")
enemy1 = GameSpite("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环
while True:
    # 指定执行频率 60次/1s
    clock.tick(60)

    # 捕获操作事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 玩家图片位置计算
    player_rect.y -= 1
    # 如果玩家到达顶部，重置到屏幕底部
    if player_rect.y + player_rect.height <= 0:
        player_rect.y = 700
    # 重置背景图片 遮挡玩家图片
    screen.blit(background, (0, 0))
    # 重新绘制玩家位置
    screen.blit(player, player_rect)

    # 精灵组更新屏幕显示
    enemy_group.update()
    # 在屏幕绘制所有精灵
    enemy_group.draw(screen)

    # 更新屏幕显示
    pygame.display.update()
    pass

"""

# rect = pygame.Rect(100, 500, 120, 125)
# print("只是测试 %d %d" % (rect.x, rect.y))
# print("测试尺寸 %d %d" % (rect.width, rect.height))
# print("再测试 %d %d" % rect.size)
