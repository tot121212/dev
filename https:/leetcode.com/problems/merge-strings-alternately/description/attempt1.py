def main():
    words=["flesh","wound"]
    solution=""
    lengths=[]
    longest_word_length=-1
    for word in words:
        length=len(word)
        lengths.append(length)
        if length > longest_word_length:
            longest_word_length = length
            #iterate through each words n th character, if it exists, appending to solution
            for character in range(longest_word_length):
                for word in words:
                    if lengths[word] < longest_word_length:
                        solution.append(word[character]
    print(str(words))
    print(str(solution))