import unittest
from tkinter import Tk
from trafficlightsimulator import TrafficLightSimulator

class TestTrafficLightSimulator(unittest.TestCase):
    def setUp(self):
        # Create a Tkinter root window and a TrafficLightSimulator instance
        self.root = Tk()
        self.app = TrafficLightSimulator(self.root)


    def test_traffic_light_transitions(self):
        # Set custom durations for testing
        self.app.red_duration = 6
        self.app.yellow_duration = 2
        self.app.green_duration = 6

        # Perform traffic light transitions
        self.app.start_simulation()
        
    def tearDown(self):
        # Close the Tkinter window after the test
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
