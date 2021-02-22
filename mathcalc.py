# centralAngle   ArcLen
# ____________ = ______
#      360         C
import math

pi = float(input('What is your measurement for pi?\n'))
sectorArea = input('Sector Area:\n')

if sectorArea == 'x':
    pass
else:
    sectorArea = float(sectorArea)

centralAngle = input('Central Angle:\n')
if centralAngle == 'x':
    pass
else:
    centralAngle = float(centralAngle)


radius = input('Radius? (If none, type "n")\n')

totalArea = 0
arcLength = 0

if radius == 'n':

    totalArea = input('Area of Circle:\n')
    if totalArea == 'x':
        pass
    else:
        totalArea = float(totalArea)

else:
    radius = float(radius)
    totalArea = (radius **2 * 3.14)
    float(totalArea)

if sectorArea == 'x':
    answer = totalArea*centralAngle/360
    answer = round(answer, 3)
    print(f'\nSector Area: {answer}')
    print(f'Radius: {totalArea/(pi*2)}')
    print(f'Arc Length: {math.sqrt(totalArea/pi)*(centralAngle)/360}')

if centralAngle == 'x':
    answer = 360*sectorArea/totalArea
    answer = round(answer, 3)
    print(f'\nCentral Angle: {answer}')
    print(f'Radius: {totalArea/(pi*2)}')
    print(f'Arc Length: {(math.sqrt((totalArea/pi)*(pi*2)) * answer)/360}')

if totalArea == 'x':
    answer = 360*sectorArea/centralAngle
    answer = round(answer, 3)
    print(f'\nSector Area: {answer}')
    radius = math.sqrt(answer/pi)
    radius = round(radius, 3)
    print(f'Radius: {radius}')
    print(f'Arc Length: {((radius*3.14*2)*centralAngle)/360}')
