import numpy as np
from Bio import SeqIO
from Bio.Data.CodonTable import unambiguous_dna_by_name

START = "ATG"
STOP = ["TAA", "TAG", "TGA"]


# Funkcija nuskaityti faila
def read_fasta(filename):
    for seq_record in SeqIO.parse(filename, "fasta"):
        return seq_record


# Gražina tripletus
def get_triplets(string):
    return [string[i:i + 3] for i in range(0, len(string), 3)]


def split_by_triplets(string_seq):
    triplets = [string_seq[i:i + 3] for i in range(0, len(string_seq), 3)]
    if len(triplets[-1]) < 3:
        triplets.pop()
    return triplets


# Funkcija rasti kodonus su ATG pradzia ir TAA arba TAG arba TGA pabaigomis
def find_codon(triplets):
    list = []
    i = 0
    j = 0
    while i < len(triplets):
        if triplets[i] == START:
            j = i + 1
            while j < len(triplets):
                if triplets[j] in STOP:
                    break
                j += 1
            list.append(triplets[i:j + 1])
            i = j + 1
        else:
            i += 1
    return list


# Funkcija rasti kodonus su TAA arba TAG arba TGA ir ATG pabaiga
def findStopStart(triplets):
    list = []
    i = 0
    j = 0
    start_index = 0

    while i < len(triplets):
        if triplets[i] in STOP:
            j = i + 1
            while j < len(triplets):
                if triplets[j] == START:
                    start_index=j
                if triplets[j] in STOP and start_index != 0:
                    break
                elif triplets[j] == STOP and start_index == 0:
                    i = j
                j += 1
            list.append(triplets[i:start_index + 1])
            i = j + 1
            start_index = 0
        else:
            i += 1
    return list


def filterShort(list):
    return_list = []

    for i in list:
        if len(i) >= 100:
            return_list.append(i)
    return return_list


# nuskaitom
record = read_fasta('bacterial1.fasta')
record = str(record.seq)

# gaunam tripletus
triplets = get_triplets(record)
print(triplets)

# random kodonus 1
print(find_codon(triplets))

# randam stop start 2
print(findStopStart(triplets))

# atfiltruojam trumpus 3
print(filterShort(findStopStart(triplets)))

# atrusiuojam didziausius, kurie ilgesni nei 100
