import random

def main():
    seikai = shutsudai()
    kaito(seikai)

def shutsudai():
    qanda = {
            "サザエの旦那の名前は？":["マスオ", "ますお"],
            "カツオの妹の名前は？":["ワカメ", "わかめ"],
            "タラオはカツオから見てどんな関係？":["甥", "おい", "甥っ子", "おいっこ"]
            }
    quiz = list(qanda.keys())
    question = quiz[random.randint(0, 2)]

    print("問題：")
    print(question)

    return qanda[question]

def kaito(correct):
    answer = input("答えるんだ：")
    if answer in correct:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()

