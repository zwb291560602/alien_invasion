# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:39:42 2018

@author: zwbb
"""

import pygame#包含开发游戏所需的功能
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	"""初始化pygame、设置和屏幕对象"""
	#初始化背景设置
	pygame.init() 
	#创建Settings实例
	ai_settings = Settings()
	#创建显示窗口
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	#设置窗口名称
	pygame.display.set_caption("Alien Invasion")
	#创建play按钮
	play_button = Button(ai_settings,screen,"Play")
	#创建一个用于存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个外星人编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#开始游戏的主循环

	while True:
		#管理事件代码重构至game_functions.py的check_events()函数中
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
		aliens,bullets)
		if stats.game_active:
			#飞船移动
			ship.update()
			#管理子弹代码重构至game_functions.py的update_bullets()函数中
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,
			bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,
			bullets)
		#将更新屏幕的代码重构到game_functions.py的update_screen()函数中
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
