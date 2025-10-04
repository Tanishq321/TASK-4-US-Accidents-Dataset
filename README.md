# 🚦 US Accidents Dataset - Data Cleaning, Visualization & Hotspot Analysis

This project is my **Task 4** submission for the Data Science Internship at SkillCraft Technology.  
It focuses on analyzing and visualizing the **US Accidents Dataset**.

---

## 📂 Dataset
The dataset is available on Kaggle:  
👉 [US Accidents (2016 - 2023) Dataset](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents?resource=download)

### 🔧 Setup Instructions
1. Download the dataset from the Kaggle link above.  
2. Extract the downloaded file **in the same folder where `accident_analysis.py` is located**.  
   - After extraction, you should see:  
     ```
     accident_analysis.py
     US_Accidents_March23.csv
     ```
3. Run the code:  
   ```bash
   python accident_analysis.py

## 📂 Files Generated
- `accidents_by_day_fast.png` → Accidents by day of the week  
- `accidents_by_hour_fast.png` → Accidents by hour of day  
- `top_weather_conditions_fast.png` → Top 10 weather conditions during accidents  
- `top_states_fast.png` → Top 10 states with most accidents  
- `accident_hotspots.html` → Interactive heatmap of accident hotspots  

## 🔧 Key Steps
1. **Data Cleaning**
   - Removed rows with missing essential values
   - Filled missing weather, temperature, and visibility values
   - Extracted `Hour`, `DayOfWeek`, and `Month` from `Start_Time`

2. **Visualization**
   - Accident trends by **day & hour**
   - Impact of **weather conditions**
   - Top accident-prone **states**
   - **Interactive heatmap** with accident hotspots

3. **Insights**
   - Average visibility across accidents
   - Most common weather condition during accidents
   - Peak accident hour and busiest day
   - State with most accidents

## 🚀 Skills Used
- Python  
- Pandas  
- Seaborn  
- Matplotlib  
- Folium (Geospatial Heatmaps)  

## 📌 Internship Details
- Program: **Data Science Internship at SkillCraft Technology**  
- Duration: **September 2025**  

---
✨ This project demonstrates how **data cleaning, visualization, and geospatial analysis** can uncover valuable safety insights.
