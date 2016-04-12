# -*- coding: utf-8 -*-
import random
import math
import copy
import matplotlib.pyplot as plt

atlas = []
plot = []
for i in range(8):
	plot.append(plt.subplot(2,4,i+1))



class Island(object):

	def __init__(self):
		self.x = int(random.random() * 100) #the x size of the world
		self.y = int(random.random() * 100) #the y size of the world
		self.distanceToBeDiscovered = random.random() * 10 #the minimal distance that the island can be discovered
		self.isDiscovered = False

class Ship(object):
	def __init__(self, Island):
		self.travel = 10 #the length that the ship can travel each time
		self.fromIsland = Island
		self.orientation = random.random() * math.pi * 2
		self.nextXPoint = self.fromIsland.x + self.travel * math.cos(self.orientation)
		self.nextYPoint = self.fromIsland.y + self.travel * math.sin(self.orientation)

	def findIsland(self, maps):
		print('From Island (%d, %d)'%(self.fromIsland.x, self.fromIsland.y))
		A = math.sin(self.orientation)/math.cos(self.orientation)
		print(self.orientation)
		B = -1
		C = self.fromIsland.y - (A * self.fromIsland.x)		
		K = -1/A
		B1 = self.fromIsland.y - self.fromIsland.x * K
		B2 = self.nextYPoint - self.nextXPoint * K
		for idx, island in enumerate(maps):
			minDistance = abs(A * island.x + B * island.y + C)/(math.pow((A*A + B*B),(1/2)))
			if (minDistance <= island.distanceToBeDiscovered and island.y >= (K * island.x + B1) and island.y <= (K * island.x + B2)) or (math.pow((island.x - self.fromIsland.x)**2 + (island.y - self.fromIsland.y)**2,1/2) <= island.distanceToBeDiscovered) or (math.pow((island.x - self.nextXPoint)**2 + (island.y - self.nextYPoint)**2,1/2) <= island.distanceToBeDiscovered):
				if not atlas[idx].isDiscovered:
					print('    Find Island(%d, %d)'%(atlas[idx].x, atlas[idx].y))
				atlas[idx].isDiscovered = True

def generatePlot(plotidx):
	atlasX = []
	atlasY = []
	for i in range(100):
		if atlas[i].isDiscovered:
			atlasX.append(atlas[i].x)
			atlasY.append(atlas[i].y)
	plt.sca(plot[plotidx+1])
	plt.axis([0, 100, 0, 100])
	plt.plot(atlasX, atlasY, 'ro')

def generateAllPlot():
	atlasX = []
	atlasY = []
	for i in range(100):
		atlasX.append(atlas[i].x)
		atlasY.append(atlas[i].y)
	plt.sca(plot[0])
	plt.axis([0, 100, 0, 100])
	plt.plot(atlasX, atlasY, 'ro')


if __name__ == '__main__':

	for i in range(100): #the number of islands
		atlas.append(Island())		
	atlas[0].isDiscovered = True

	for i in range(60): #the iterations it passes
		if i % 10 == 0:
			generatePlot(i//10)
		print('\nGeneration %d' %i)
		tempAtlas = copy.deepcopy(atlas)
		for j in range(100):
			if tempAtlas[j].isDiscovered:
				ship = Ship(tempAtlas[j])
				ship.findIsland(copy.deepcopy(tempAtlas))
	generatePlot(6)
	generateAllPlot()
	count = 0
	for i in atlas:
		if i.isDiscovered:
			count += 1
	print(count) #print the number of discovered islandsd 

	plt.show()



	
	  	
		
