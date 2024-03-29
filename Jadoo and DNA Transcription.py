'''Jadoo, the Space Alien has befriended Koba upon landing on Earth. Since then, he wishes Koba to be more like him. 
In order to do so he decides to slowly transcribe Koba's DNA into RNA. 
But he has to write a very short code in order to do the transcription so as not to make Koba aware of the change.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G --> C
C --> G
T --> A
A --> U
 

Input: The input will always be a string of characters.

Output: The output should always be a string of characters. In the case of invalid input, you should output Invalid Input as a string.
Rules: Your code should not consist of any numerical characters (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 
and the length of your code should be <= 103. If your code consists of numerical characters, 
then your score is zero irrespectuve of your code length or testcases satisfied. 
If your code is devoid of numerical characters and is of length > 103 then you score 50%.'''


dna = input('')
standard_set = {'A', 'T', 'G', 'C'}
test_set = set(dna)
if standard_set.union(test_set) == standard_set:
    rna = [w.replace("A", "U").replace("T", "A").replace("C", "B").replace("G", "C").replace("B","G") for w in dna]
    rna = ''.join(rna)
    print(rna)
else:
    print("Invalid Input")
