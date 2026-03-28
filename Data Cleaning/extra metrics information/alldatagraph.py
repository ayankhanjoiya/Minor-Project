import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

main_folder = r"C:/Users/ayank/OneDrive/Desktop/mini project/Data Collection"

all_data = []

# ========= LOAD ALL CSV FILES =========
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith(".csv"):

            file_path = os.path.join(root, file)
            print("Loading:", file_path)

            try:
                df = pd.read_csv(file_path)

                # ---- Auto detect columns ----
                acc_cols = [c for c in df.columns if 'acc' in c.lower()]
                gyro_cols = [c for c in df.columns if 'gyro' in c.lower()]

                if len(acc_cols) < 3 or len(gyro_cols) < 3:
                    print("❌ Missing sensor columns")
                    continue

                AccX, AccY, AccZ = acc_cols[:3]
                GyroX, GyroY, GyroZ = gyro_cols[:3]

                temp = pd.DataFrame({
                    'AccX': df[AccX],
                    'AccY': df[AccY],
                    'AccZ': df[AccZ],
                    'GyroX': df[GyroX],
                    'GyroY': df[GyroY],
                    'GyroZ': df[GyroZ]
                })

                all_data.append(temp)

            except:
                print("❌ Error reading:", file)

# ========= COMBINE =========
combined = pd.concat(all_data, ignore_index=True)

print("\nTotal samples:", len(combined))

# ========= MAGNITUDE =========
combined['AccMag'] = np.sqrt(combined['AccX']**2 + combined['AccY']**2 + combined['AccZ']**2)
combined['GyroMag'] = np.sqrt(combined['GyroX']**2 + combined['GyroY']**2 + combined['GyroZ']**2)

x_axis = range(len(combined))

# ========= PLOT =========
plt.figure(figsize=(15,10))

# Accelerometer
plt.subplot(2,1,1)
plt.plot(x_axis, combined['AccX'], label="AccX", alpha=0.6)
plt.plot(x_axis, combined['AccY'], label="AccY", alpha=0.6)
plt.plot(x_axis, combined['AccZ'], label="AccZ", alpha=0.6)
plt.plot(x_axis, combined['AccMag'], label="Magnitude", linewidth=2)

plt.title("Combined Accelerometer Data")
plt.legend()
plt.grid(True)

# Gyroscope
plt.subplot(2,1,2)
plt.plot(x_axis, combined['GyroX'], label="GyroX", alpha=0.6)
plt.plot(x_axis, combined['GyroY'], label="GyroY", alpha=0.6)
plt.plot(x_axis, combined['GyroZ'], label="GyroZ", alpha=0.6)
plt.plot(x_axis, combined['GyroMag'], label="Magnitude", linewidth=2)

plt.title("Combined Gyroscope Data")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()