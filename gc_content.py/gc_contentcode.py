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
os.makedirs("output", exist_ok=True)  # creates the folder if it doesn't exist

df.to_csv("output/summary.csv", index=False)

# %%


# %%
