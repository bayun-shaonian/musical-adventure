import random
suits = ['黑桃', '红桃', '梅花', '方片']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
          'J':10, 'Q':10, 'K':10, 'A':11}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def pai():
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
def fa(hand):
    total=sum(values[rank] for suit, rank in hand)
    aces = sum(1 for suit, rank in hand if rank == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
def show(hand, is_dealer=False):
    if is_dealer:
        print(f"电脑: {hand[1][1]}")
    else:
        print(f"我的手牌: {', '.join([rank for suit, rank in hand])} (点数: {fa(hand)})")
def blackjack():
    print("欢迎来到21点游戏")
    deck = pai()
    hand1=[deck.pop(),deck.pop()]
    hand2=[deck.pop(),deck.pop()]
    show(hand1)
    show(hand2, is_dealer=True)
    while True:
        tools1=fa(hand1)
        if tools1>21:
            return print('你爆牌')
        elif tools1==21:
            return print('你获得游戏胜利')
        else:
            action = input("\n继续抽牌(hit)还是停止抽牌(stand)？(h/s): ").lower()
            if action == 'h':
                hand1.append(deck.pop())
                show(hand1)
            elif action == 's':
                break
            else:
                print("请输入h或s！")
    tools1 = fa(hand1)
    if tools1 <= 21:
        print("\n--- 电脑回合 ---")
        while fa(hand2) < 17:
            hand2.append(deck.pop())
            print(f"电脑要牌: {hand2[-1]}")
        print(
            f"电脑最终手牌: {', '.join([rank for suit, rank in hand2])} (点数: {fa(hand2)})")
    tools2=fa(hand2)
    if tools2 > 21:
        print("电脑爆牌")
    elif tools2 == 21:
        print("电脑获胜")
    elif tools1 > tools2:
        print(f"你以{tools1}大于{tools2}获胜")
    elif tools2 > tools1:
        print(f"电脑以{tools2}大于{tools1}获胜")
    else:
        print("平局")

if __name__ == "__main__":
    blackjack()













