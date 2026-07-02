# 🧬 GC Content Genome Analyser

A beginner-friendly bioinformatics project that analyzes the **GC content** of a complete bacterial genome using Python. This project uses a real genome downloaded from **NCBI**, calculates overall GC content, performs a **sliding window GC analysis**, and visualizes GC variation across the genome.

This project was developed as part of my bioinformatics learning journey to practice sequence analysis, data processing, and scientific visualization.

---

##  Project Overview

GC content is the percentage of **Guanine (G)** and **Cytosine (C)** nucleotides in a DNA sequence.


GC%={G+C}/{A+T+G+C}*100


Instead of calculating a single GC percentage for the entire genome, this project uses a **sliding window approach** to calculate GC content across different regions of the genome.

The analysis was performed on the genome of **Bacillus subtilis** downloaded from NCBI.

---

##  Objectives

- Download a real bacterial genome from NCBI
- Read FASTA files using Biopython
- Calculate nucleotide composition
- Compute overall GC percentage
- Perform sliding window GC analysis
- Store results using Pandas
- Visualize GC variation using Matplotlib
- Generate publication-style summary tables
- Prepare a sequence for BLAST analysis

---

##  Technologies Used

- Python 3
- Biopython
- Pandas
- Matplotlib
- NumPy

---

## Project Structure

```text
GC_Content_Genome_Analyser/

│
├── data/
│   └── genome.fasta
│
├── output/
│   ├── summary.csv
│   ├── summary_statistics.csv
│   ├── gc_content.csv
│   ├── gc_plot.png
│   ├── query.fasta
│   ├── blast_hits.csv
│   └── blast_hits.png
│
├── gc_content.py
├── blast_analysis.py
├── requirements.txt
└── README.md
```

---

