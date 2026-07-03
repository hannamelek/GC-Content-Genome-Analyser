#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
record = SeqIO.read(r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\data\sequence.fasta",
    "fasta")
print(record)

# In[8]:

genome = str(record.seq)
print(len(genome))


# In[11]:


A = genome.count("A")
T = genome.count("T")
G = genome.count("G")
C = genome.count("C")


# In[13]:


print(A)
print(T)
print(G)
print(C)


# In[ ]:
gc = (G + C) / len(genome) * 100
print(gc)

summary = {
    "Statistics": ["Genome Length", "A", "T", "G", "C", "GC%"],
    "Values": [len(genome), A, T, G, C, gc]
}
pd.set_option("display.float_format", "{:.2f}".format)
df = pd.DataFrame(summary)
print(df)

import os
os.makedirs("output", exist_ok=True)  #creates the folder if it doesn't exist

df.to_csv("output/summary.csv", index=False)


#%%
#Calculating Mean, Max, and Min GC Content
mean_gc = gc_df["GC_contents"].mean()
print(mean_gc)

max_gc = gc_df["GC_contents"].max()
print(max_gc)

min_gc = gc_df["GC_contents"].min()
print(min_gc)

std_gc = gc_df["GC_contents"].std()
print(std_gc)

num_windows = len(gc_df)
print(num_windows)

#%%
import matplotlib.pyplot as plt


# Sliding Window GC Analysis


window = 10000      # 10 kb
step = 5000         # 5 kb

positions = []
gc_values = []

for i in range(0, len(genome) - window + 1, step):

    fragment = genome[i:i + window]

    g = fragment.count("G")
    c = fragment.count("C")

    gc = (g + c) / len(fragment) * 100

    positions.append(i)
    gc_values.append(gc)


# Create DataFrame


gc_df = pd.DataFrame({
    "Position": positions,
    "GC_Content": gc_values
})

print(gc_df.head())

# Save CSV
gc_df.to_csv(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\gc_content.csv",
    index=False
)



# Smooth the GC values

gc_df["Smoothed_GC"] = gc_df["GC_Content"].rolling(window=5).mean()

# Average GC
mean_gc = gc_df["GC_Content"].mean()

# Plot


plt.figure(figsize=(16,6))

plt.plot(
    gc_df["Position"] / 1_000_000,
    gc_df["Smoothed_GC"],
    linewidth=2,
    label="Smoothed GC%"
)

plt.axhline(
    mean_gc,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average GC = {mean_gc:.2f}%"
)

plt.xlabel("Genome Position (Mb)", fontsize=12)
plt.ylabel("GC Content (%)", fontsize=12)

plt.title(
    "Sliding Window GC Content Across the Bacillus subtilis Genome",
    fontsize=15
)

plt.grid(alpha=0.3)

plt.legend()

plt.tight_layout()

plt.savefig(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\gc_plot.png",
    dpi=300
)

plt.show()

# %%
print("Summary Statistics:")
print("--------------------")
print("Number of Windows:", num_windows)
print("Average GC%:", round(mean_gc,2))
print("Maximum GC%:", round(max_gc,2))
print("Minimum GC%:", round(min_gc))
print("Standard Deviation:", round(std_gc,2))








