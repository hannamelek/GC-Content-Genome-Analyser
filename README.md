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
│   └── sequence.fasta
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

##  Installation

Clone the repository

```bash
git clone https://github.com/hannamelek/GC_Content_Genome_Analyser.git
```

Move into the project folder

```bash
cd GC_Content_Genome_Analyser
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the GC content analysis

```bash
python gc_content.py
```


Run the BLAST visualization

```bash
python blast_analysis.py
```

## Output Files

The project generates:

| File | Description |
|------|-------------|
| summary.csv | Basic genome statistics |
| summary_statistics.csv | Sliding window summary statistics |
| gc_content.csv | GC percentage for each window |
| gc_plot.png | GC content variation plot |
| query.fasta | Query sequence for BLAST |
| blast_hits.csv | BLAST search results |
| blast_hits.png | BLAST hit visualization |

---
## Example Output

### Summary Table

| Statistic | Value |
|-----------|------:|
| Genome Length | 3,593,163 |
| A | ... |
| T | ... |
| G | ... |
| C | ... |
| GC% | 44.14 |

### Mean, Max, Min, 


<img width="587" height="473" alt="Screenshot 2026-07-04 190729" src="https://github.com/user-attachments/assets/fed8e564-b698-4553-aec7-e19b9ad0a91a" />

---
### GC Content Plot

<img width="4800" height="1800" alt="gc_plot" src="https://github.com/user-attachments/assets/b3c9ac7e-32cc-43fc-84f9-98d539c26a79" />

---

### BLAST Results

<img width="2000" height="600" alt="BLAST_hit" src="https://github.com/user-attachments/assets/07422835-87b8-4b43-8fc2-2192ddc70c32" />

##  Biological Interpretation

The overall GC content provides information about the nucleotide composition of the genome.

The sliding window analysis reveals how GC content changes across different genomic regions.

Regions with unusually high or low GC content may indicate:

- Genomic islands
- Horizontally transferred DNA
- Regulatory regions
- Evolutionary differences

BLAST analysis identifies similar sequences in other organisms and helps determine sequence homology.

---

##  Skills Demonstrated

- Reading FASTA files
- DNA sequence processing
- Biopython
- Pandas DataFrames
- Sliding window algorithms
- Scientific data visualization
- Basic comparative genomics
- BLAST analysis
- GitHub project organization

---

##  References

- NCBI Genome Database
- Biopython Documentation
- Pandas Documentation
- Matplotlib Documentation
- BLAST Documentation

---

##  Author

**Hanna Melek**

This project was completed as part of my bioinformatics learning journey to strengthen my Python programming, sequence analysis, and data visualization skills.


