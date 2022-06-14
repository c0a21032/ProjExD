import random

num_let = 8
num_mis = 2
repeat = 3

def main():
    for i in range(repeat):
        seikai = shutsudai()
        result = kaitou(seikai)
        if result == 1:
            print("正解です。おめでとうございます！")
            break



def shutsudai():
    letters = []
    while(len(letters) < num_let):
        letter = chr(random.randint(65, 90))
        if letter not in letters:
            letters.append(letter)
    
    missings = random.sample(letters, 2)

    displayed = []
    for i in letters:
        if i not in missings:
            displayed.append(i)
    
    print("対象文字：")
    print(" ".join(letters))

    print("欠損文字")
    print(" ".join(missings))

    print("表示文字：")
    print(" ".join(displayed))

    return missings




def kaitou(correct):
    ans_num_mis = input("欠損文字はいくつあるでしょうか？：")
    if int(ans_num_mis) == num_mis:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
    else:
        print("不正解です。またチャレンジしてください")
        return 0
    
    for i in range(num_mis):
        answer = input(f"{i+1}個目の文字を入力してください：")
        if answer.upper() not in correct:
            print("不正解ですまたチャレンジしてください。")
            return 0
        else:
            del correct[answer]
    
    return 1



if __name__ == "__main__":
    main()