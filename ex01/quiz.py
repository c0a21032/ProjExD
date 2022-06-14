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
    questions = list(qanda.keys())
    mondai = questions[random.randint(0, 2)]

    print("問題：")
    print(mondai)

    return qanda[mondai]

def kaito(correct):
    kotae = input("答えるんだ：")
    if kotae in correct:
        print("正解！！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()

