#This is my submission for leetcode problem 1768. As a bonus, it works for any amount of words.

def main():
    words=["flesh","wounds"]
    #words=["tis","but","a","flesh","wound"]
    solution=[]

    len_words = len(words)
    exception_counter=0

    idx=0
    while True:
        for word in words:
            try:
                solution.append(word[idx])
            except IndexError:
                exception_counter+=1
                continue
        if exception_counter >= len_words:
            break
        exception_counter = 0
        idx+=1

    print(solution)

if __name__ == "__main__":
    main()
    