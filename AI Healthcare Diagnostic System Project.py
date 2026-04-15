import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

class DataAnalyticsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📊 Smart Data Analytics Tool")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Upload CSV to Analyze 📂", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Upload CSV", command=self.load_csv, width=20).pack(pady=10)

        self.root.mainloop()

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if not path:
            return

        try:
            self.df = pd.read_csv(path)
            messagebox.showinfo("Success", "CSV Loaded Successfully!")

            self.analyze_data()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def analyze_data(self):
        df = self.df

        print("\n📊 DATA OVERVIEW")
        print(df.head())

        print("\n📈 STATISTICS")
        print(df.describe())

        print("\n❗ MISSING VALUES")
        print(df.isnull().sum())

        # ---------------- HISTOGRAM ----------------
        df.hist(figsize=(10, 8))
        plt.suptitle("Histogram")
        plt.show()

        # ---------------- BOXPLOT ----------------
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df)
        plt.title("Boxplot")
        plt.show()

        # ---------------- HEATMAP ----------------
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

        # ---------------- PAIRPLOT ----------------
        sns.pairplot(df.select_dtypes(include='number'))
        plt.show()

        # ---------------- SCATTER PLOTS ----------------
        numeric_cols = df.select_dtypes(include='number').columns

        for i in range(len(numeric_cols)-1):
            plt.figure()
            plt.scatter(df[numeric_cols[i]], df[numeric_cols[i+1]])
            plt.xlabel(numeric_cols[i])
            plt.ylabel(numeric_cols[i+1])
            plt.title("Scatter Plot")
            plt.show()

        # ---------------- LINE CHART ----------------
        df.plot(figsize=(10, 6))
        plt.title("Line Chart")
        plt.show()

        # ---------------- PIE CHART ----------------
        for col in df.select_dtypes(include='object').columns:
            df[col].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title(f"Pie Chart - {col}")
            plt.ylabel("")
            plt.show()


if __name__ == "__main__":
    DataAnalyticsApp()