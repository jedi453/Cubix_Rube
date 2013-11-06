
import sys, pygame, math, pygame.mixer
from pygame.locals import *

pygame.init()

size = width, height = 720, 540

black = 0, 0, 0

# Make Screen
screen = pygame.display.set_mode(size)

# Load Color Images:
White = pygame.image.load("White.png")		# 0
Yellow = pygame.image.load("Yellow.png")	# 1
Red = pygame.image.load("Red.png")			# 2
Blue = pygame.image.load("Blue.png")		# 3
Green = pygame.image.load("Green.png")		# 4
Orange = pygame.image.load("Orange.png")	# 5

Center = pygame.image.load("Center.png")	# 6

Up = pygame.image.load("Up.png")			# 10
Front = pygame.image.load("Front.png")		# 11
Right = pygame.image.load("Right.png")		# 12
Back = pygame.image.load("Back.png")		# 13
Left = pygame.image.load("Left.png")		# 14
Down = pygame.image.load("Down.png")		# 15

# Create Color Constants
WC = 0
YC = 1
RC = 2
BC = 3
GC = 4
OC = 5
CC = 6
UpC = 10
FrontC = 11
RightC = 12
BackC = 13
LeftC = 14
DownC = 15

# Set Faces
U = [[YC, YC, YC], [YC, YC, YC], [YC, YC, YC]]
F = [[GC, GC, GC], [GC, GC, GC], [GC, GC, GC]]
R = [[OC, OC, OC], [OC, OC, OC], [OC, OC, OC]]
B = [[BC, BC, BC], [BC, BC, BC], [BC, BC, BC]]
L = [[RC, RC, RC], [RC, RC, RC], [RC, RC, RC]]
D = [[WC, WC, WC], [WC, WC, WC], [WC, WC, WC]]
# Buffer Face
Buff = [[YC, YC, YC], [YC, YC, YC], [YC, YC, YC]]

# Set Default Faces
U0 = [[YC, YC, YC], [YC, YC, YC], [YC, YC, YC]]
F0 = [[GC, GC, GC], [GC, GC, GC], [GC, GC, GC]]
R0 = [[OC, OC, OC], [OC, OC, OC], [OC, OC, OC]]
B0 = [[BC, BC, BC], [BC, BC, BC], [BC, BC, BC]]
L0 = [[RC, RC, RC], [RC, RC, RC], [RC, RC, RC]]
D0 = [[WC, WC, WC], [WC, WC, WC], [WC, WC, WC]]
# Buffer Face
Buff0 = [[YC, YC, YC], [YC, YC, YC], [YC, YC, YC]]

def ResetFaces():
	# Set Faces
	for i in range(3):
		for j in range(3):
			U[i][j] = U0[i][j]
			F[i][j] = F0[i][j]
			R[i][j] = R0[i][j]
			B[i][j] = B0[i][j]
			L[i][j] = L0[i][j]
			D[i][j] = D0[i][j]


# Set Sizes and Locations
CubieSize = 50, 50
CubieSpacing = 2
ULoc = 200, 200
FLoc = 200, 360
RLoc = 360, 200
BLoc = 200, 40
LLoc =  40, 200
DLoc = 520, 200
CubieSize2 = 50
CubieFull = CubieSize2 + CubieSpacing

#print U[0][0]	

# Scale Images:
White = pygame.transform.scale( White, CubieSize)		# 0
Yellow = pygame.transform.scale( Yellow, CubieSize)		# 1
Red = pygame.transform.scale( Red, CubieSize)			# 2
Blue = pygame.transform.scale( Blue, CubieSize)			# 3
Green = pygame.transform.scale( Green, CubieSize)		# 4
Orange = pygame.transform.scale( Orange, CubieSize)		# 5
Center = pygame.transform.scale( Center, CubieSize)		# 6

Up = pygame.transform.scale( Up, CubieSize)
Front = pygame.transform.scale( Front, CubieSize)
Right = pygame.transform.scale( Right, CubieSize)
Back = pygame.transform.scale( Back, CubieSize)
Left = pygame.transform.scale( Left, CubieSize)
Down = pygame.transform.scale( Down, CubieSize)

# Set Max FPS
FPS = 40

# Set Clock
clock = pygame.time.Clock()

#print ULoc[0]
#print ULoc[1]

# Function To Place Cubies:
def BlitImage(XLoc, YLoc, XVal, YVal, Color):
	if (Color == WC):
		screen.blit( White, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == YC):
		screen.blit( Yellow, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == RC):
		screen.blit( Red, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == BC):
		screen.blit( Blue, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == GC):
		screen.blit( Green, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == OC):
		screen.blit( Orange, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == CC):
		screen.blit( Center, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == FrontC):
		screen.blit( Front, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == UpC):
		screen.blit( Up, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == RightC):
		screen.blit( Right, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == BackC):
		screen.blit( Back, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == LeftC):
		screen.blit( Left, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))
	elif (Color == DownC):
		screen.blit( Down, ( (XLoc+(XVal*CubieFull)), (YLoc+(YVal*CubieFull))))

# Function to Blit Faces:
def FaceBlit(Face, FaceLoc, FaceName):
	for i in range(3):
		for j in range(3):
			BlitImage(FaceLoc[0], FaceLoc[1], i, j, Face[i][j])
	if FaceName == "Up":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, UpC)
	elif FaceName == "Front":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, FrontC)
	elif FaceName == "Right":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, RightC)
	elif FaceName == "Back":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, BackC)
	elif FaceName == "Left":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, LeftC)
	elif FaceName == "Down":
		BlitImage(FaceLoc[0], FaceLoc[1], 1, 1, DownC)

# Function to Perform transforms:
def RotFace(FaceName, RotCount):
	if FaceName == "R":
		for i in range(3):
			for j in range(3):
				Buff[i][j]=U[i][j]
		for j in range(3):
			U[2][j] = F[2][j]
		for j in range(3):
			F[2][2-j] = D[0][j]
		for j in range(3):
			D[0][j] = B[2][2-j]
		for j in range(3):
			B[2][j] = Buff[2][j]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=R[i][j]
		for i in range(3):
			for j in range(3):
				R[2-j][i]=Buff[i][j]
	elif FaceName == "F":
		for i in range(3):
			for j in range(3):
				Buff[i][j]=U[i][j]
		for j in range(3):
			U[j][2] = L[j][2]
		for j in range(3):
			L[j][2] = D[j][2]
		for j in range(3):
			D[j][2] = R[j][2]
		for j in range(3):
			R[j][2] = Buff[j][2]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=F[i][j]
		for i in range(3):
			for j in range(3):
				F[2-j][i]=Buff[i][j]
	elif FaceName == "U":
		for i in range(3):
			for j in range(3):
				Buff[i][j]=F[i][j]
		for j in range(3):
			F[2-j][0] = R[0][j]
		for j in range(3):
			R[0][j] = B[j][2]
		for j in range(3):
			B[j][2] = L[2][2-j]
		for j in range(3):
			L[2][2-j] = Buff[2-j][0]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=U[i][j]
		for i in range(3):
			for j in range(3):
				U[2-j][i]=Buff[i][j]
		
	elif FaceName == "L":
		for i in range(3):
			for j in range(3):
				Buff[i][j] = U[i][j]
		for j in range(3):
			U[0][j] = B[0][j]
		for j in range(3):
			B[0][j] = D[2][2-j]
		for j in range(3):
			D[2][2-j] = F[0][j]
		for j in range(3):
			F[0][j] = Buff[0][j]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=L[i][j]
		for i in range(3):
			for j in range(3):
				L[2-j][i]=Buff[i][j]
	elif FaceName == "B":
		for i in range(3):
			for j in range(3):
				Buff[i][j] = U[i][j]
		for j in range(3):
			U[j][0] = R[j][0]
		for j in range(3):
			R[j][0] = D[j][0]
		for j in range(3):
			D[j][0] = L[j][0]
		for j in range(3):
			L[j][0] = Buff[j][0]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=B[i][j]
		for i in range(3):
			for j in range(3):
				B[2-j][i]=Buff[i][j]
	elif FaceName == "D":
		# FIX!
		for i in range(3):
			for j in range(3):
				Buff[i][j] = F[i][j]
		for j in range(3):
			F[j][2] = L[0][j]
		for j in range(3):
			L[0][j] = B[2-j][0]
		for j in range(3):
			B[2-j][0] = R[2][2-j]
		for j in range(3):
			R[2][2-j] = Buff[j][2]
		for i in range(3):
			for j in range(3):
				Buff[i][j]=D[i][j]
		for i in range(3):
			for j in range(3):
				D[2-j][i]=Buff[i][j]
	
	# Slices:
	elif FaceName == "M":
		for i in range(3):
			for j in range(3):
				Buff[i][j] = U[i][j]
		for j in range(3):
			U[1][j] = B[1][j]
		for j in range(3):
			B[1][j] = D[1][2-j]
		for j in range(3):
			D[1][2-j] = F[1][j]
		for j in range(3):
			F[1][j] = Buff[1][j]
	elif FaceName == "E":
		for i in range(3):
			for j in range(3):
				Buff[i][j] = F[i][j]
		for j in range(3):
			F[j][1] = L[1][j]
		for j in range(3):
			L[1][j] = B[2-j][1]
		for j in range(3):
			B[2-j][1] = R[1][2-j]
		for j in range(3):
			R[1][2-j] = Buff[j][1]
	elif FaceName == "S":
		for i in range(3):
			for j in range(3):
				Buff[i][j] = U[i][j]
		for j in range(3):
			U[j][1] = L[j][1]
		for j in range(3):
			L[j][1] = D[j][1]
		for j in range(3):
			D[j][1] = R[j][1]
		for j in range(3):
			R[j][1] = Buff[j][1]
	
	# Rotations:
	elif FaceName == "X":
		#print "Not Yet Implemented: X rotation!"
		RotFace("M", 3)
		RotFace("R", 1)
		RotFace("L", 3)
	elif FaceName == "Y":
		RotFace("U", 1)
		RotFace("E", 3)
		RotFace("D", 3)
	elif FaceName == "Z":
		RotFace("F", 1)
		RotFace("S", 1)
		RotFace("B", 3)
	#RotCount = RotCount - 1 # Redundant, comment out
	if RotCount > 1:
		RotFace(FaceName, RotCount - 1)


# Initialize Shift and CTRL as Off
Shift = False
CTRL = False

"""
for i in range(3):
	for j in range(3):
		print U[i][j]
"""

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()
			elif event.key == K_SPACE:
				pygame.image.save(screen, "screenshot.png")
			elif ( event.key == K_LSHIFT ) or ( event.key == K_RSHIFT ):
				Shift = True
			elif ( event.key == K_LCTRL ) or ( event.key == K_RCTRL ):
				CTRL = True
			elif ( event.key == K_BACKSPACE ):
				ResetFaces()
				FaceBlit( U, ULoc, "Up")
				FaceBlit( F, FLoc, "Front")
				FaceBlit( R, RLoc, "Right")
				FaceBlit( L, LLoc, "Left")
				FaceBlit( B, BLoc, "Back")
				FaceBlit( D, DLoc, "Down")
				print "Reset Cube!"
			elif event.key == K_r:
				if Shift:
					# RotFace(FaceName, RotCount)
					Shift = False
					# Do R' Move:
					RotFace("R", 3)
					if CTRL:
						RotFace("M", 1)
						CTRL = False
						print "Did r' Rotation."
					else:
						print "Did R' Rotation."
				else:
					# Do R Move:
					RotFace("R", 1)
					if CTRL:
						RotFace("M", 3)
						CTRL = False
						print "Did r Rotation."
					else:
						print "Did R Rotation."
			
			elif event.key == K_f:
				if Shift:
					Shift = False
					# Do F' Move:
					RotFace("F", 3)
					if CTRL:
						RotFace("S", 3)
						CTRL = False
						print "Did f' Rotation."
					else:
						print "Did F' Rotation."
				else:
					#Do F Move:
					RotFace("F", 1)
					if CTRL:
						RotFace("S", 1)
						CTRL = False
						print "Did f Rotation."
					else:
						print "Did F Rotation."
			
			elif event.key == K_u:
				if Shift:
					Shift = False
					# Do U' Move:
					RotFace("U", 3)
					if CTRL:
						RotFace("E", 1)
						CTRL = False
						print "Did u' Rotation."
					else:
						print "Did U' Rotation."
				else:
					# Do U Move:
					RotFace("U", 1)
					if CTRL:
						RotFace("E", 3)
						CTRL = False
						print "Did u Rotation."
					else:
						print "Did U Rotation."
			
			elif event.key == K_l:
				if Shift:
					Shift = False
					# Do L' Move:
					RotFace("L", 3)
					if CTRL:
						RotFace("M", 3)
						CTRL = False
						print "Did l' Rotation."
					else:
						print "Did L' Rotation."
				else:
					# Do L Move:
					RotFace("L", 1)
					if CTRL:
						RotFace("M", 1)
						CTRL = False
						print "Did l Rotation."
					else:
						print "Did L Rotation."
			
			elif event.key == K_b:
				if Shift:
					Shift = False
					# Do B' Move:
					RotFace("B", 3)
					if CTRL:
						RotFace("S", 1)
						CTRL = False
						print "Did b' Rotation."
					else:
						print "Did B' Rotation."
				else:
					# Do B Move:
					RotFace("B", 1)
					if CTRL:
						RotFace("S", 3)
						CTRL = False
						print "Did b Rotation."
					else:
						print "Did B Rotation."
				
			elif event.key == K_d:
				if Shift:
					print "Did D' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("D", 3)
					if CTRL:
						RotFace("E", 3)
						CTRL = False
				else:
					print "Did D Rotation."
					# Do D Move:
					RotFace("D", 1)
					if CTRL:
						RotFace("E", 1)
						CTRL = False
			
			# Slice Moves:
			elif event.key == K_m:
				CTRL = False
				if Shift:
					print "Did M' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("M", 3)
				else:
					print "Did M Rotation."
					# Do D Move:
					RotFace("M", 1)
			
			elif event.key == K_e:
				CTRL = False
				if Shift:
					print "Did E' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("E", 3)
				else:
					print "Did E Rotation."
					# Do D Move:
					RotFace("E", 1)
					
			elif event.key == K_s:
				CTRL = False
				if Shift:
					print "Did S' Rotation."
					# Do S' Move:
					RotFace("S", 3)
				else:
					print "Did S Rotation."
					# Do S Move:
					RotFace("S", 1)
			
			# Rotations:
			elif event.key == K_x:
				CTRL = False
				if Shift:
					print "Did X' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("X", 3)
				else:
					print "Did X Rotation."
					# Do D Move:
					RotFace("X", 1)
			
			elif event.key == K_y:
				CTRL = False
				if Shift:
					print "Did Y' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("Y", 3)
				else:
					print "Did Y Rotation."
					# Do D Move:
					RotFace("Y", 1)
					
			elif event.key == K_z:
				CTRL = False
				if Shift:
					print "Did Z' Rotation."
					Shift = False
					# Do D' Move:
					RotFace("Z", 3)
				else:
					print "Did Z Rotation."
					# Do D Move:
					RotFace("Z", 1)
	
	
	# Clear Screen:
	screen.fill( black )
	
	# Reference Blit:
	# BlitImage(XLoc, YLoc, XVal, YVal, Color)
	# Reference FaceBlit:
	# FaceBlit(Face, FaceLoc, FaceName)
	
	# Blit All Faces:
	FaceBlit( U, ULoc, "Up")
	FaceBlit( F, FLoc, "Front")
	FaceBlit( R, RLoc, "Right")
	FaceBlit( L, LLoc, "Left")
	FaceBlit( B, BLoc, "Back")
	FaceBlit( D, DLoc, "Down")
	
	# Test Blits:
	#BlitImage( DLoc[0], DLoc[1], 2, 2, YC)
	#BlitImage( FLoc[0], FLoc[1], 2, 2, YC)
	#screen.blit( White, ( 304, 252))
	
	pygame.display.flip()
	clock.tick(FPS) # Wait 1/FPS Seconds
	
