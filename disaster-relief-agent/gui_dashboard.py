import tkinter as tk


class DisasterDashboard:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Disaster Relief Coordination System")
        self.root.geometry("400x300")

        self.title = tk.Label(
            self.root,
            text="Disaster Relief Dashboard",
            font=("Arial", 16, "bold")
        )
        self.title.pack(pady=10)

        self.victims_label = tk.Label(self.root, text="Victims Waiting: 0")
        self.victims_label.pack()

        self.food_label = tk.Label(self.root, text="Food Supplies: 100")
        self.food_label.pack()

        self.shelter_label = tk.Label(self.root, text="Shelter Capacity: 50")
        self.shelter_label.pack()

        self.medical_label = tk.Label(self.root, text="Medical Kits: 30")
        self.medical_label.pack()

        self.event_label = tk.Label(
            self.root,
            text="System Running...",
            fg="blue"
        )
        self.event_label.pack(pady=20)

    def update_dashboard(self, victims, food, shelter, medical, event):

        self.victims_label.config(text=f"Victims Waiting: {victims}")
        self.food_label.config(text=f"Food Supplies: {food}")
        self.shelter_label.config(text=f"Shelter Capacity: {shelter}")
        self.medical_label.config(text=f"Medical Kits: {medical}")

        self.event_label.config(text=f"Event: {event}")

        self.root.update()

    def run(self):
        self.root.mainloop()