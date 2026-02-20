import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ========= CONFIG =========
main_folder = r"C://Users/ayank/OneDrive/Desktop/mini project/Data Collection"
save_root = os.path.join(main_folder, "plots")

os.makedirs(save_root, exist_ok=True)

# ========= WALK THROUGH ALL SUBFOLDERS =========
for root, dirs, files in os.walk(main_folder):

    for file in files:
        if file.endswith(".csv"):

            file_path = os.path.join(root, file)
            print(f"Processing: {file_path}")

            try:
                df = pd.read_csv(file_path)

                # ----- Handle index -----
                if 'SrNo' in df.columns:
                    x_axis = df['SrNo']
                else:
                    x_axis = range(len(df))

                # ----- OPTIONAL smoothing -----
                df[['X_Acc','Y_Acc','Z_Acc']] = df[['X_Acc','Y_Acc','Z_Acc']].rolling(5).mean()
                df[['X_Gyro','Y_Gyro','Z_Gyro']] = df[['X_Gyro','Y_Gyro','Z_Gyro']].rolling(5).mean()

                # ----- Magnitude (useful for risk score later) -----
                df['AccMag'] = np.sqrt(df['X_Acc']**2 + df['Y_Acc']**2 + df['Z_Acc']**2)
                df['GyroMag'] = np.sqrt(df['X_Gyro']**2 + df['Y_Gyro']**2 + df['Z_Gyro']**2)

                # ----- Plot -----
                plt.figure(figsize=(14,10))

                # Accelerometer
                plt.subplot(2,1,1)
                plt.plot(x_axis, df['X_Acc'], label='X Accelerometer')
                plt.plot(x_axis, df['Y_Acc'], label='Y Accelerometer')
                plt.plot(x_axis, df['Z_Acc'], label='Z Accelerometer')
                plt.plot(x_axis, df['AccMag'], label='Magnitude', linestyle='--')

                plt.title("Accelerometer Readings")
                plt.xlabel("Sample")
                plt.ylabel("Acceleration")
                plt.legend()
                plt.grid(True)

                # Gyroscope
                plt.subplot(2,1,2)
                plt.plot(x_axis, df['X_Gyro'], label='X Gyroscope')
                plt.plot(x_axis, df['Y_Gyro'], label='Y Gyroscope')
                plt.plot(x_axis, df['Z_Gyro'], label='Z Gyroscope')
                plt.plot(x_axis, df['GyroMag'], label='Magnitude', linestyle='--')

                plt.title("Gyroscope Readings")
                plt.xlabel("Sample")
                plt.ylabel("Angular Velocity")
                plt.legend()
                plt.grid(True)

                plt.tight_layout()

                # ----- Preserve folder structure for saving -----
                relative_path = os.path.relpath(root, main_folder)
                save_folder = os.path.join(save_root, relative_path)
                os.makedirs(save_folder, exist_ok=True)

                save_path = os.path.join(save_folder, file.replace(".csv", ".png"))
                plt.savefig(save_path, dpi=300)
                plt.close()

            except Exception as e:
                print(f"❌ Error in {file}: {e}")

print("✅ All plots generated across folders!")