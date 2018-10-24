from rectangle import Rectangle
import sys

Ax1 = -1
Ay1 = -1
Ax2 = 1
Ay2 = 1
Bx1 = 0
By1 = 0
Bx2 = 2
By2 = 2
rec1 = Rectangle(Ax1,Ay1,Ax2,Ay2)
rec2 = Rectangle(Bx1,By1,Bx2,By2)
rec2.intersects(rec1)

