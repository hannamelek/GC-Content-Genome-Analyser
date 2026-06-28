#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO

import pandas as pd

import matplotlib.pyplot as plt


# In[6]:


record = SeqIO.read(r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\data\sequence.fasta",
    "fasta")


# In[7]:


print(record)


# In[8]:


genome = str(record.seq)


# In[9]:


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




