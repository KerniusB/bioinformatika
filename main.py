from Bio import SeqIO

START = "ATG"
STOP = ["TAA", "TAG", "TGA"]
ALL_CODONS = ["TTT", "TTC", "TTA", "TTG", "TCT", "TCC", "TCA", "TCG", "TAT", "TAC", "TAA", "TAG", "TGT", "TGC", "TGA",
              "TGG", "CTT", "CTC", "CTA", "CTG", "CCT", "CCC", "CCA", "CCG", "CAT", "CAC", "CAA", "CAG", "CGT", "CGC",
              "CGA", "CGG", "ATT", "ATC", "ATA", "ATG", "ACT", "ACC", "ACA", "ACG", "AAT", "AAC", "AAA", "AAG", "AGT",
              "AGC", "AGA", "AGG", "GTT", "GTC", "GTA", "GTG", "GCT", "GCC", "GCA", "GCG", "GAT", "GAC", "GAA", "GAG",
              "GGT", "GGC", "GGA", "GGG"]


# Funkcija nuskaityti faila
def read_fasta(filename):
    for seq_record in SeqIO.parse(filename, "fasta"):
        return seq_record


# Gražina tripletus
def get_triplets(string):
    return [string[i:i + 3] for i in range(0, len(string), 3)]


def get_frames(sequence):
    a = sequence[0:]
    b = sequence[1:]
    c = sequence[2:]
    d = (sequence[::-1])[0:]
    e = (sequence[::-1])[1:]
    f = (sequence[::-1])[2:]
    return a + b + c + d + e + f


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
                    start_index = j
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


def filter_short(list):
    return_list = []

    for i in list:
        if len(i) >= 100:
            return_list.append(i)
    return return_list


def find_codon_frequency(frames):
    for arr in filtered:
        for codon in arr:
            i = 0
            for triplet in ALL_CODONS:
                if codon == triplet:
                    CODONS_FREQUENCY[i] += 1
                    break
                i += 1


def sum_of_array(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


def findFreq(sum):
    i = 0
    for tripl in CODONS_FREQUENCY:
        CODONS_FREQUENCY[i] = tripl / sum
        i += 1


def findDicFreq(sum):
    i = 0
    for tripl in DICODONS_FREQUENCY:
        DICODONS_FREQUENCY[i] = tripl / sum
        i += 1


def find_dicodons(codons):
    dicodons = []
    for a in ALL_CODONS:
        for b in ALL_CODONS:
            dicodons.append(a + b)
    return dicodons


def find_dicodon_frequency(frames):
    dicodon = ""
    for arr in filtered:
        for codon in arr:
            dicodon += codon
            if len(dicodon) == 6:
                i = 0
                for triplet in ALL_DICODONS:
                    if dicodon == triplet:
                        DICODONS_FREQUENCY[i] += 1
                        break
                    i += 1
                dicodon = ""


def findFreqBetween2Seq(freq1, freq2):
    temp = []
    i = 0
    for j in freq1:
        temp.append(abs(j - freq2[i]))
        i += 1
    return sum_of_array(temp)


# nuskaitom
record = read_fasta('bacterial1.fasta')
record = str(record.seq)
record2 = read_fasta('bacterial2.fasta')
record2 = str(record2.seq)
record3 = read_fasta('bacterial3.fasta')
record3 = str(record3.seq)
record4 = read_fasta('bacterial4.fasta')
record4 = str(record4.seq)
mamalian = read_fasta('mamalian1.fasta')
mamalian = str(mamalian.seq)
mamalian2 = read_fasta('mamalian2.fasta')
mamalian2 = str(mamalian2.seq)
mamalian3 = read_fasta('mamalian3.fasta')
mamalian3 = str(mamalian3.seq)
mamalian4 = read_fasta('mamalian4.fasta')
mamalian4 = str(mamalian4.seq)

records = [record, record2, record3, record4, mamalian, mamalian2, mamalian3, mamalian4]

finalSimilarityNum = []

for record in records:
    # gaynam 6 imanomus variantus
    frames = get_frames(record)

    # gaunam tripletus
    triplets = get_triplets(frames)

    # random kodonus 1
    orf = find_codon(triplets)

    # randam stop start
    stopStart = findStopStart(orf)

    # atfiltruojam trumpus
    filtered = filter_short(orf)

    # ieskome kodonu daznio
    CODONS_FREQUENCY = []
    for i in ALL_CODONS:
        CODONS_FREQUENCY.append(0)
    find_codon_frequency(filtered)
    suma = sum_of_array(CODONS_FREQUENCY)
    findFreq(suma)
    print(CODONS_FREQUENCY)

    # randame dikodonus
    ALL_DICODONS = find_dicodons(ALL_CODONS)
    DICODONS_FREQUENCY = []
    for i in ALL_DICODONS:
        DICODONS_FREQUENCY.append(0)

    # ieskome dikodonu daznio
    find_dicodon_frequency(filtered)
    findDicFreq(sum_of_array(DICODONS_FREQUENCY))
    print(DICODONS_FREQUENCY)

    # randamae panasumo koficienta
    similarity = findFreqBetween2Seq(CODONS_FREQUENCY, CODONS_FREQUENCY)
    print(similarity)
    finalSimilarityNum.append(similarity)

print(finalSimilarityNum)
