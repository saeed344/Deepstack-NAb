#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd
from collections import Counter
from Bio import SeqIO


def AAC(fastas, order='ARNDCQEGHILKMFPSTWYV'):
    encodings = []
    header = ['Name'] + list(order)
    encodings.append(header)

    for record in fastas:
        name, sequence = record.id, str(record.seq).replace('-', '')
        count = Counter(sequence)
        total_len = len(sequence)

        code = [name] + [count[aa] / total_len if total_len > 0 else 0 for aa in order]
        encodings.append(code)

    return encodings


# File paths
fasta_file = "DENV_Dataset.fasta"
csv_output_file = "DENV_Dataset_feat.csv"

# Read FASTA sequences
fastas = list(SeqIO.parse(fasta_file, "fasta"))

# Extract AAC features
features = AAC(fastas)

# Save to CSV
df = pd.DataFrame(features[1:], columns=features[0])
df.to_csv(csv_output_file, index=False)

print(f"Features saved to {csv_output_file}")