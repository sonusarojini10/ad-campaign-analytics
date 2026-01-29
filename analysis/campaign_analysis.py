import pandas as pd
import matplotlib.pyplot as plt

print("\n=== Ad Campaign Performance Analyzer ===\n")

# Load dataset
df = pd.read_csv("../data/ad_campaign_data.csv")

print("Dataset Loaded Successfully\n")
print(df.head())

# -------------------------
# Calculate Marketing Metrics
# -------------------------

df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100
df["Conversion Rate (%)"] = (df["Conversions"] / df["Clicks"]) * 100
df["CPC"] = df["Cost"] / df["Clicks"]
df["ROI (%)"] = ((df["Revenue"] - df["Cost"]) / df["Cost"]) * 100

print("\n=== Calculated Metrics ===\n")
print(df[[
    "Campaign",
    "Platform",
    "CTR (%)",
    "Conversion Rate (%)",
    "CPC",
    "ROI (%)"
]])

# -------------------------
# Platform Summary
# -------------------------

platform_summary = df.groupby("Platform")[[
    "CTR (%)",
    "Conversion Rate (%)",
    "CPC",
    "ROI (%)"
]].mean()

print("\n=== Average Performance by Platform ===\n")
print(platform_summary)

# -------------------------
# Save Output Report
# -------------------------

df.to_csv("../outputs/summary_report.csv", index=False)
print("\nSummary report saved to outputs/summary_report.csv")

# -------------------------
# Visualization
# -------------------------

plt.figure()
platform_summary["ROI (%)"].plot(kind="bar")
plt.title("Average ROI by Platform")
plt.ylabel("ROI (%)")
plt.xlabel("Platform")
plt.tight_layout()
plt.show()
