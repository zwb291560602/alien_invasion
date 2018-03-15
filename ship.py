import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings#获取setting中速度设置
		#加载飞船图像并获取其外接矩形rect
		#加载图像，返回一个表示飞船的surface
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()#获取表示图片的属性
		self.screen_rect = screen.get_rect()#获取表示屏幕的矩形属性
		
		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx#飞船中心的x坐标
		self.rect.bottom = self.screen_rect.bottom#飞船下边缘的y坐标
		
		#在飞船的属性center中存储小数值(rect 的centerx 等属性只能存储整数值)
		self.center = float(self.rect.centerx)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		"""根据移动标志调整飞船的位置"""
		#更新飞船的center值，而不是rect
		if (self.moving_right and 
		self.rect.right < self.screen_rect.right):#小于屏幕右边缘
			self.center += self.ai_settings.ship_speed_factor
		if (self.moving_left and 
		self.rect.left > 0):#大于屏幕左边缘坐标0（左边缘一定是0，右边缘不一定
			self.center -= self.ai_settings.ship_speed_factor
		#根据self.center更新rect对象,从而更新飞船位置
		self.rect.centerx = self.center
	def blitme(self):
		"""在指定位置绘制飞船"""
		#self.rect指定位置绘制self.image
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
