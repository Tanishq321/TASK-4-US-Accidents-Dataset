import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import warnings
warnings.filterwarnings("ignore")

# ----------------------------------------------------
# ⚡ FAST DATA LOADING
# ----------------------------------------------------
use_cols = [
    "Start_Time", "Start_Lat", "Start_Lng", "State",
    "Weather_Condition", "Temperature(F)", "Visibility(mi)"
]

print("🔹 Loading a 5% sample of the dataset for faster performance...")
# Read only first 5% of the data (adjust fraction if needed)
df = pd.read_csv(
    "US_Accidents_March23.csv",
    usecols=use_cols,
    low_memory=False
).sample(frac=0.05, random_state=42)

print(f"✅ Sample loaded successfully! Shape: {df.shape}")

# ----------------------------------------------------
# 🧹 DATA CLEANING
# ----------------------------------------------------
print("\n🧹 Cleaning data...")

# Drop rows with missing essential values
df = df.dropna(subset=["Start_Time", "Start_Lat", "Start_Lng"])

# Convert time column
df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")

# Fill missing weather-related columns
for col in ["Weather_Condition", "Temperature(F)", "Visibility(mi)"]:
    if df[col].dtype == "O":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Extract time info
df["Hour"] = df["Start_Time"].dt.hour
df["DayOfWeek"] = df["Start_Time"].dt.day_name()
df["Month"] = df["Start_Time"].dt.month_name()

print("✅ Cleaning complete!")

# ----------------------------------------------------
# 📊 VISUALIZATION
# ----------------------------------------------------
print("\n📊 Generating visualizations...")

# 1️⃣ Accidents by Day
plt.figure(figsize=(8,5))
sns.countplot(
    x="DayOfWeek",
    data=df,
    order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    palette="Spectral"
)
plt.title("Accidents by Day of Week")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("accidents_by_day_fast.png")
plt.close()

# 2️⃣ Accidents by Hour
plt.figure(figsize=(8,5))
sns.histplot(df["Hour"], bins=24, kde=True, color="skyblue")
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("accidents_by_hour_fast.png")
plt.close()

# 3️⃣ Top Weather Conditions
plt.figure(figsize=(10,6))
top_weather = df["Weather_Condition"].value_counts().head(10)
sns.barplot(x=top_weather.values, y=top_weather.index, palette="viridis")
plt.title("Top 10 Weather Conditions During Accidents")
plt.tight_layout()
plt.savefig("top_weather_conditions_fast.png")
plt.close()

# 4️⃣ Top States
plt.figure(figsize=(10,6))
top_states = df["State"].value_counts().head(10)
sns.barplot(x=top_states.values, y=top_states.index, palette="magma")
plt.title("Top 10 States with Most Accidents")
plt.tight_layout()
plt.savefig("top_states_fast.png")
plt.close()

print("✅ Charts saved successfully!")

# ----------------------------------------------------
# 🌎 INTERACTIVE MAP (very small sample)
# ----------------------------------------------------
sample_df = df.sample(10000, random_state=42)  # reduce for speed

m = folium.Map(location=[sample_df["Start_Lat"].mean(), sample_df["Start_Lng"].mean()],
               zoom_start=5, tiles="CartoDB dark_matter")

HeatMap(sample_df[["Start_Lat", "Start_Lng"]].values, radius=7, blur=5).add_to(m)

# Display map directly in browser (no need to open HTML manually)
map_file = "accident_hotspots.html"
m.save(map_file)
import webbrowser
webbrowser.open(map_file)

print("✅ Analysis complete! Map opened in browser.")

# ----------------------------------------------------
# 📈 INSIGHTS
# ----------------------------------------------------
print("\n📈 KEY INSIGHTS")
print(f"🔹 Average Visibility: {df['Visibility(mi)'].mean():.2f} miles")
print(f"🔹 Common Weather: {df['Weather_Condition'].mode()[0]}")
print(f"🔹 Peak Accident Hour: {df['Hour'].mode()[0]}:00")
print(f"🔹 Busiest Day: {df['DayOfWeek'].mode()[0]}")
print(f"🔹 Most Accidents State: {df['State'].mode()[0]}")

print("\n✅ Task 4 completed successfully (FAST MODE). Check your folder for:")
print("   - accidents_by_day_fast.png")
print("   - accidents_by_hour_fast.png")
print("   - top_weather_conditions_fast.png")
print("   - top_states_fast.png")
print("   - accident_hotspots.html")
