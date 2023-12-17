import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(self.root, bg="white", width=400, height=400)
        self.canvas.pack()

        self.circle_radius = 10
        self.circle_x = 20
        self.circle_y = 20
        self.circle = self.canvas.create_oval(
            self.circle_x - self.circle_radius, self.circle_y - self.circle_radius,
            self.circle_x + self.circle_radius, self.circle_y + self.circle_radius,
            fill="blue"
        )

        self.points = []  # قائمة لتخزين نقاط الرسم

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

        self.root.mainloop()

    def move_left(self, event):
        self.move_circle(-10, 0)

    def move_right(self, event):
        self.move_circle(10, 0)

    def move_up(self, event):
        self.move_circle(0, -10)

    def move_down(self, event):
        self.move_circle(0, 10)

    def move_circle(self, dx, dy):
        # تحريك موقع الدائرة
        self.circle_x += dx
        self.circle_y += dy
        self.canvas.coords(
            self.circle,
            self.circle_x - self.circle_radius, self.circle_y - self.circle_radius,
            self.circle_x + self.circle_radius, self.circle_y + self.circle_radius
        )

        # إضافة نقطة لقائمة الرسم
        self.points.append((self.circle_x, self.circle_y))

        # رسم الخط باستخدام النقاط المخزنة
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                x1, y1 = self.points[i]
                x2, y2 = self.points[i + 1]
                self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
