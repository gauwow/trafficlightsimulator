import tkinter as tk
from tkinter import simpledialog, messagebox

class TrafficLightSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulator")

        self.red_duration = None
        self.yellow_duration = None
        self.green_duration = None

        self.is_running = False

        self.create_widgets()

    def create_widgets(self):
        # Label for configuring durations
        config_label = tk.Label(self.root, text="Configure Durations (seconds)")
        config_label.pack()

        # Entry widgets for configuring durations
        red_label = tk.Label(self.root, text="Red:")
        red_label.pack()
        self.red_entry = tk.Entry(self.root, state="readonly")
        self.red_entry.pack()

        yellow_label = tk.Label(self.root, text="Yellow:")
        yellow_label.pack()
        self.yellow_entry = tk.Entry(self.root, state="readonly")
        self.yellow_entry.pack()

        green_label = tk.Label(self.root, text="Green:")
        green_label.pack()
        self.green_entry = tk.Entry(self.root, state="readonly")
        self.green_entry.pack()

        # Update timer values button
        timer_button = tk.Button(self.root, text="Set Transition Timers", command=self.set_timers)
        timer_button.pack()

        # Start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_simulation, state=tk.DISABLED)
        self.start_button.pack()

        # Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.confirm_exit)
        exit_button.pack()

        # Canvas to display traffic light
        self.canvas = tk.Canvas(self.root, width=100, height=300)
        self.canvas.pack()

        # Draw the initial traffic light
        self.draw_traffic_light("gray", "gray", "gray")

    def set_timers(self):
        try:
            # Open a dialog box to input transition timers
            self.red_duration = simpledialog.askinteger("Traffic Light Timers", "Red Duration (seconds):")
            self.yellow_duration = simpledialog.askinteger("Traffic Light Timers", "Yellow Duration (seconds):")
            self.green_duration = simpledialog.askinteger("Traffic Light Timers", "Green Duration (seconds):")

            if self.red_duration is None or self.yellow_duration is None or self.green_duration is None:
                messagebox.showwarning("Timer Not Set", "Please set a timer for each duration before running the traffic simulator.")
            else:
                self.red_entry.config(state="normal")
                self.red_entry.delete(0, tk.END)
                self.red_entry.insert(0, str(self.red_duration))
                self.red_entry.config(state="readonly")

                self.yellow_entry.config(state="normal")
                self.yellow_entry.delete(0, tk.END)
                self.yellow_entry.insert(0, str(self.yellow_duration))
                self.yellow_entry.config(state="readonly")

                self.green_entry.config(state="normal")
                self.green_entry.delete(0, tk.END)
                self.green_entry.insert(0, str(self.green_duration))
                self.green_entry.config(state="readonly")

                # Enable the "Start" button when timers are set
                self.start_button.config(state=tk.NORMAL)
        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")

    # ... (the rest of your code remains unchanged)


    def draw_traffic_light(self, red_color, yellow_color, green_color):
        # Clear canvas
        self.canvas.delete("all")

        # Draw the traffic light with circles
        self.canvas.create_oval(40, 50, 60, 70, fill=red_color)      # Red light
        self.canvas.create_oval(40, 90, 60, 110, fill=yellow_color)  # Yellow light
        self.canvas.create_oval(40, 130, 60, 150, fill=green_color)  # Green light

    def start_simulation(self):
        if not self.is_running:
            self.is_running = True
            self.perform_transition()

    def perform_transition(self):
        if self.is_running:
            # Red light
            self.draw_traffic_light("red", "gray", "gray")
            self.root.update()
            self.root.after(self.red_duration * 1000, self.transition_to_yellow)

    def transition_to_yellow(self):
        if self.is_running:
            # Yellow light
            self.draw_traffic_light("gray", "yellow", "gray")
            self.root.update()
            self.root.after(self.yellow_duration * 1000, self.transition_to_green)

    def transition_to_green(self):
        if self.is_running:
            # Green light
            self.draw_traffic_light("gray", "gray", "green")
            self.root.update()
            self.root.after(self.green_duration * 1000, self.transition_to_red)

    def transition_to_red(self):
        if self.is_running:
            # Back to red light
            self.draw_traffic_light("red", "gray", "gray")
            self.root.update()
            self.root.after(self.red_duration * 1000, self.perform_transition)

    def show_error_message(self, message):
        messagebox.showerror("Error", message)
        messagebox.showinfo("Exiting Application", "Exiting Application...")
        self.root.destroy()

    def confirm_exit(self):
        # Ask the user for confirmation before exiting
        user_response = messagebox.askquestion("Exit Confirmation", "Are you sure you want to exit the application?")
        if user_response == "yes":
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightSimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.confirm_exit)  # Handle window close button
    root.mainloop()
