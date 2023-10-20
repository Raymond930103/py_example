def calculate_similarity(seq1, seq2):
    
    similarity = 0
    min_len = min(len(seq1), len(seq2))
    for i in range(min_len):
        if seq1[i] == seq2[i]:
            similarity += 1
    
    return similarity

DNA = input("input DNA: ")
comp = input("to comp: ")

max_similarity = 0
best_seg = ""

for i in range(len(DNA)):
    for j in range(len(comp)):
        DNA_seg = DNA[i:]
        comp_seg = comp[j:j + len(DNA_seg)]  
        
        similarity = calculate_similarity(DNA_seg, comp_seg)

        if similarity > max_similarity:
            max_similarity = similarity
            best_seg = DNA_seg
    
            
best_seg = best_seg[:max_similarity]
if max_similarity == 0:
    print("none")
else:
    print("max similarity is: ",best_seg)