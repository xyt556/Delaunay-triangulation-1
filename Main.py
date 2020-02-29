import tkinter as tk
import Functions as f

print("Program is running...")
root = tk.Tk()
canvas = tk.Canvas(root, width=1045, height=554, bg="white")
canvas.pack()

points = []
adjMatrix = []


def add_point(point):
    points.append(point)

    for col in adjMatrix:
        col.append(0)

    tempCol = [0] * len(points)
    adjMatrix.append(tempCol)

    if len(points) > 1:
        adjMatrix[len(points)-2][len(points)-1] = 1

    print(points)
    if len(points) == 3:
        area = f.area(points[0], points[1], points[2])
        print("2A = " + str(area))
        print("left(a,b,c) = " + str(f.left(points[0], points[1], points[2])))
        print("colinear = " + str(f.colinear(points[0], points[1], points[2])))


def left_click(event):
    x = event.x
    y = event.y

    add_point((x,y))
    update()


def enter_press(event):
    global points
    global adjMatrix
    points = []
    adjMatrix = []
    update()


def update():
    for item in canvas.find_all():
        canvas.delete(item)

    r = 4
    for point in points:
        canvas.create_oval(point[0]-r, point[1]-r, point[0]+r, point[1]+r, fill="red")

    for i, col in enumerate(adjMatrix):
        for j, edge in enumerate(col):
            if edge == 1:
                canvas.create_line(points[i][0], points[i][1], points[j][0], points[j][1])
    canvas.pack()


canvas.bind("<Button-1>", left_click)
canvas.bind_all("<Return>", enter_press)

root.mainloop()
