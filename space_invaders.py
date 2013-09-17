#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Modules
import pygame
from pygame.locals import *

#Constant

WIDTH=800
HEIGHT=600

#Classes

class Alien(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=load_image("images/alien.jpg")
		self.rect=self.image.get_rect()
		self.rect.centerx=x
		self.rect.centery=y
		self.speed=[0.2,0.2]
	def update(self,time):
		self.rect.centerx+=self.speed[0]*time
		if self.rect.left<=0:
			self.speed[0]=-self.speed[0]
			self.speed[1]=-self.speed[1]
			self.rect.centerx+=self.speed[0]*time
			self.rect.centery+=self.speed[1]*time
		if self.rect.right>=WIDTH:
			self.speed[0]=-self.speed[0]
			self.speed[1]=-self.speed[1]
			self.rect.centerx+=self.speed[0]*time
			self.rect.centery-=self.speed[1]*time

class Ship(pygame.sprite.Sprite):
	def __init__(self,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=load_image("images/ship.jpg")
		self.rect=self.image.get_rect()
		self.rect.centerx=WIDTH/2
		self.rect.centery=y
		self.speed=0.5
	def move(self,time,keys):
		if self.rect.left>=0:
			if keys[K_LEFT]:
				self.rect.centerx-=self.speed*time
		if self.rect.right<=WIDTH:
			if keys[K_RIGHT]:
				self.rect.centerx+=self.speed*time

#Functions

def load_image(filename,transparent=False):
	try:image=pygame.image.load(filename)
	except pygame.error,message:
		raise SystemExit,message
	image=image.convert()
	if transparent:
		color=image.get_at((0,0))
		image.set_colorkey(color,RLEACCEL)
	return image

def main():
	screen=pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Space Invaders")
	background_image=load_image('images/background.jpg')
	boxes=[]
	for x in range(100,WIDTH-150,100):
		for y in range(10,200,60):
			boxes.append(Alien(x,y))
	ship=Ship(HEIGHT-30)
	clock=pygame.time.Clock()
	while True:
		time=clock.tick(60)
		keys=pygame.key.get_pressed()
		for events in pygame.event.get():
			if events.type==QUIT:
				sys.exit(0)
		ship.move(time,keys)
		screen.blit(background_image,(0,0))
		for i in boxes:
			i.update(time)
			screen.blit(i.image,i.rect)
		screen.blit(ship.image,ship.rect)
		pygame.display.flip()
	return 0

if __name__=='__main__':
	pygame.init()
	main()
