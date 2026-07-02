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
columns = [
    "Query",
    "Subject",
    "Identity",
    "Alignment_Length",
    "Mismatches",
    "Gap_Openings",
    "Query_Start",
    "Query_End",
    "Subject_Start",
    "Subject_End",
    "E-value",
    "Bit_Score"
]

blast_df = pd.read_csv(
    r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\BLAST_hit.csv",
    header=None,
    names=columns
)

print(blast_df.columns)

# %%
import numpy as np

#converting E-value to LogE for better visualization
blast_df["E-value"] = blast_df["E-value"].replace(0, 1e-300)

blast_df["LogE"] = -np.log10(blast_df["E-value"])

#plotting blast hits
plt.figure(figsize=(20,6))
plt.bar(blast_df["Subject"], blast_df["LogE"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Subject")
plt.ylabel("-log10(E-value)")
plt.title("Top Blast Hits for Bacillus subtilis Query")
plt.tight_layout()
plt.savefig(r"C:\Users\Dr.MAAM\Desktop\GC Content Genome Analyser\output\BLAST_hit.png"
)
plt.show()

# %%
print(blast_df.columns.tolist())
print(blast_df.head())
