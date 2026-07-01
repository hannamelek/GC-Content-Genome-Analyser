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

# %%

# Sliding Window GC Content Analysis
window = 1000
step = 500

positions = []
gc_values = []

for i in range(0, len(genome) - window + 1, step):

    fragment = genome[i:i + window]

    g = fragment.count("G")
    c = fragment.count("C")

    gc = (g + c) / len(fragment) * 100

    positions.append(i)
    gc_values.append(gc)

gc_df = pd.DataFrame({"Position": positions, "GC_contents": gc_values})
print(gc_df.head())

gc_df.to_csv(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\gc_content.csv",
    index=False
)


# %%
#Plotting the Graph
plt.figure(figsize=(12,5))

plt.plot(gc_df["Position"],gc_df["GC_contents"])

plt.xlabel("Genome Position(bp)")
plt.ylabel("GC Content (%)")
plt.title("Sliding Window GC Content of Bacillus subtilis")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\gc_plot.png"
)

plt.show()

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

# %%
print("Summary Statistics:")
print("--------------------")
print("Number of Windows:", num_windows)
print("Average GC%:", round(mean_gc,2))
print("Maximum GC%:", round(max_gc,2))
print("Minimum GC%:", round(min_gc))
print("Standard Deviation:", round(std_gc,2))

#%%
#BLAST Query
query = genome[:1000]
print(query)

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

query_record = SeqRecord(
    Seq(query),
    id="Bsub_query",
    description = "Frst 1000 bp of Bacillus subtilis"
)

SeqIO.write(query_record,
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\query.fasta",
    "fasta")

#%%
#reading blast results
blast_df = pd.read_csv(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\BLAST_hit.csv"
)
print(blast_df.head())
                       
# %%
import numpy as np

blast_df["E-value"] = blast_df["E-value"].replace(0, 1e-300)

blast_df["LogE"] = -np.log10(blast_df["E-value"])

#plotting blast hits
plt.figure(figsize=(10,5))
plt.bar(blast_df["Organism"], blast_df["LogE"])
