import math
import curses
import time

A, B, C = 0.0, 0.0, 0.0
cubeWidth = 20.0
width, height = 160, 44
zBuffer = [0.0] * (width * height)
buffer = [' '] * (width * height)
backgroundASCIICode = '.'
distanceFromCam = 100
horizontalOffset = 0.0
K1 = 40.0
incrementSpeed = 0.6

def calculateX(i, j, k):
    return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)

def calculateY(i, j, k):
    return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - i * math.cos(B) * math.sin(C)

def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)

def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    global A, B, C
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch

def main(stdscr):
    curses.curs_set(0)
    while True:
        stdscr.clear()
        for i in range(width * height):
            stdscr.addch(i // width, i % width, buffer[i])

        A += 0.05
        B += 0.05
        C += 0.01
        stdscr.refresh()
        time.sleep(0.016)  # Sleep for ~16ms to achieve approximately 60 FPS.

curses.wrapper(main)
