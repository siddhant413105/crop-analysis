import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Crop:
    def __init__(self, crop_type, yield_per_hectare, area_hectares):
        self.crop_type = crop_type
        self.yield_per_hectare = yield_per_hectare
        self.area_hectares = area_hectares

    def __str__(self):
        return f"Crop: {self.crop_type}, Yield: {self.yield_per_hectare} tons/ha, Area: {self.area_hectares} ha"

class CropAnalysis:
    def __init__(self):
        self.crops = []

    def add_crop(self, crop_type, yield_per_hectare, area_hectares):
        crop = Crop(crop_type, yield_per_hectare, area_hectares)
        self.crops.append(crop)

    def view_crops(self):
        if not self.crops:
            print("No crop data available.")
            return
        for crop in self.crops:
            print(crop)

    def analyze_crops(self):
        if not self.crops:
            print("No crop data available for analysis.")
            return

        data = {
            "Crop Type": [crop.crop_type for crop in self.crops],
            "Yield per Hectare": [crop.yield_per_hectare for crop in self.crops],
            "Area (Hectares)": [crop.area_hectares for crop in self.crops]
        }
        df = pd.DataFrame(data)

        plt.figure(figsize=(10, 6))
        sns.barplot(x="Crop Type", y="Yield per Hectare", data=df)
        plt.title("Yield per Hectare by Crop Type")
        plt.xlabel("Crop Type")
        plt.ylabel("Yield per Hectare (tons/ha)")
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.barplot(x="Crop Type", y="Area (Hectares)", data=df)
        plt.title("Area by Crop Type")
        plt.xlabel("Crop Type")
        plt.ylabel("Area (Hectares)")
        plt.show()

# Example usage
if __name__ == "__main__":
    crop_analysis = CropAnalysis()
    crop_analysis.add_crop("Wheat", 3.5, 150)
    crop_analysis.add_crop("Corn", 4.2, 200)
    crop_analysis.add_crop("Rice", 2.8, 180)

    print("Current Crop Data:")
    crop_analysis.view_crops()

    print("\nAnalyzing Crops...")
    crop_analysis.analyze_crops()