# -*- coding: utf-8 -*-
import random
import math
import copy

atlas = []
class Island(object):

	def __init__(self):
		self.x = int(random.random() * 100) #the x size of the world
		self.y = int(random.random() * 100) #the y size of the world
		self.distanceToBeDiscovered = int(random.random() * 10) #the minimal distance that the island can be discovered
		self.isDiscovered = False

class Ship(object):
	def __init__(self, Island):
		self.travel = 10 #the length that the ship can travel each time
		self.fromIsland = Island
		self.orientation = random.random() * math.pi * 2
		self.nextXPoint = self.fromIsland.x + self.travel * math.cos(self.orientation)
		self.nextYPoint = self.fromIsland.y + self.travel * math.sin(self.orientation)

	def findIsland(self, maps):
		A = math.sin(self.orientation)/math.cos(self.orientation)
		B = -1
		C = self.fromIsland.y - (A * self.fromIsland.x)		
		K = -1/A
		B1 = self.fromIsland.y - self.fromIsland.x * K
		B2 = self.nextYPoint - self.nextXPoint * K
		for idx, island in enumerate(maps):
			minDistance = abs(A * island.x + B * island.y + C)/(math.pow((A*A + B*B),(1/2)))
			if (minDistance <= island.distanceToBeDiscovered and island.y >= (K * island.x + B1) and island.y <= (K * island.x + B2)) or (math.pow((island.x - self.fromIsland.x)**2 + (island.y - self.fromIsland.y)**2,1/2) <= island.distanceToBeDiscovered) or (math.pow((island.x - self.nextXPoint)**2 + (island.y - self.nextYPoint)**2,1/2) <= island.distanceToBeDiscovered):
				atlas[idx].isDiscovered = True

if __name__ == '__main__':
	for i in range(100): #the number of islands
		atlas.append(Island())
	atlas[0].isDiscovered = True

	for i in range(20): #the iterations it passes
		tempAtlas = copy.deepcopy(atlas)
		print(i)
		for j in range(100):
			if tempAtlas[j].isDiscovered:
				ship = Ship(tempAtlas[j])
				ship.findIsland(copy.deepcopy(tempAtlas))

	count = 0
	for i in atlas:
		if i.isDiscovered:
			count += 1
	print(count) #print the number of discovered islandsd


	
	  	
		
