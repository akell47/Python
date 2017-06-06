# DNA DioxyriboNucleic Acid
# A, C, G, T - four nucleotides to construct DNA
# A - adenine
# C - cytosine
# G - guanine
# T - thymine
# DNA -> RNA -> Protein
# one amino acid = nucleotide triplet
# sequence of amino acid = protein - comprised of 20 amino acids
# dictionary of life

inputfile = "dna.txt"
# r for reading
# define it to capture the file
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n","")
seq = seq.replace("\r", "")
# print (seq)


def translate(seq):
    """Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids. Nucleotides are
    translated in triplets using the table dictionary; each amino acids is
    encoded with a string of length 1."""
# Translate process - table lookup - dictionary
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

# find a key that corresponds to a sequence
# check length of sequence is divisible by 3
# modulo operator
    protein = ""
    if (len(seq) % 3) == 0:
        # loop over the sequence
        for i in range(0, len(seq), 3):
            # extract a single codon
            codon = seq[i:i+3]
            # look up the codon and store the result
            protein += table[codon]
    return protein
    # look up each 3- letter string in the table and store result
    # continue lookups until reaching end of sequence
print (translate("ATA"))
print (translate("GAC"))
print (translate("GGA"))
print (translate("GCA"))
print (translate("TTC"))
print (translate("GCC"))
#doc string string literal occurs as the first statement in a module function
# or a class or method definition and becomes part of that object
# can use the help function to learn more about the funciton using the doc string
# doc string summarizes the behavior of the function and document its arguments,
# returned values, and possible side effects
print (help(translate))


print (138 % 13)


# inputfile2 = "seq2.txt"
# f2 = open(inputfile2, "r")
# seq2 = f2.read()
# seq2 = seq2.replace("\n","")
# seq2 = seq2.replace(" ", "")
# print seq2
# print seq2[40:50]
