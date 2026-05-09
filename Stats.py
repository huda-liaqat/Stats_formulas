from collections import Counter
import csv
import re
class StatisticsSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []
        self.weights = []
    # Functional Requirement:
    # System should load CSV data correctly
    def load_data(self):
        try:
            with open(self.file_name, newline='') as file:
                reader = csv.reader(file)
                self.data = list(reader)

            self.data.pop(0)

            for row in self.data:
                weight = float(row[1])
                self.weights.append(weight)

            self.weights.sort()

        except FileNotFoundError:
            print("File not found")

    # Functional Requirement:
    # System should calculate mean
    def get_mean(self):
        """Calculate arithmetic mean of weights"""
        if not self.weights:
            return 0
        return round(sum(self.weights) / len(self.weights), 2)

    # Functional Requirement:
    # System should calculate median
    def get_median(self):
        """Calculate median of weights"""
        if not self.weights:
            return 0
        
        n = len(self.weights)
        if n % 2 == 1:
            return round(self.weights[n // 2], 2)
        else:
            mid1 = self.weights[n // 2 - 1]
            mid2 = self.weights[n // 2]
            return round((mid1 + mid2) / 2, 2)

    # Functional Requirement:
    # System should calculate mode
    def get_mode(self):
        """Calculate mode of weights using weight ranges"""
        data = Counter(self.weights)

        mode_data_for_range = {
            "75-85": 0,
            "85-95": 0,
            "95-105": 0,
            "105-115": 0,
            "115-125": 0,
            "125-135": 0,
            "135-145": 0,
            "145-155": 0,
            "155-165": 0,
            "165-175": 0
        }

        for weight, occurrence in data.items():
            if 75 < weight < 85:
                mode_data_for_range["75-85"] += occurrence
            elif 85 < weight < 95:
                mode_data_for_range["85-95"] += occurrence
            elif 95 < weight < 105:
                mode_data_for_range["95-105"] += occurrence
            elif 105 < weight < 115:
                mode_data_for_range["105-115"] += occurrence
            elif 115 < weight < 125:
                mode_data_for_range["115-125"] += occurrence
            elif 125 < weight < 135:
                mode_data_for_range["125-135"] += occurrence
            elif 135 < weight < 145:
                mode_data_for_range["135-145"] += occurrence
            elif 145 < weight < 155:
                mode_data_for_range["145-155"] += occurrence
            elif 155 < weight < 165:
                mode_data_for_range["155-165"] += occurrence
            elif 165 < weight < 175:
                mode_data_for_range["165-175"] += occurrence

        mode_range = ""
        mode_occurrence = 0
        for value_range, occurrence in mode_data_for_range.items():
            if occurrence > mode_occurrence:
                mode_range = value_range
                mode_occurrence = occurrence

        if not mode_range:
            return 0

        lower, upper = map(int, mode_range.split("-"))
        mode = (lower + upper) / 2

        return round(mode, 2)

    # Non-Functional Requirement:
    # System should validate CSV file names using regex
    def validate_file_name(self):

        pattern = r'^[A-Za-z0-9_]+\.csv$'

        if re.match(pattern, self.file_name):
            return True

        return False


# Main Driver Program
if __name__ == "__main__":

    system = StatisticsSystem("data.csv")

    if system.validate_file_name():

        system.load_data()

        print(f"Mean -> {system.get_mean()}")
        print(f"Median -> {system.get_median()}")
        print(f"Mode -> {system.get_mode()}")

    else:
        print("Invalid File Name")
     