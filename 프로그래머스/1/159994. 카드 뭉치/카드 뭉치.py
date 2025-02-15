def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:  # cards1이 비어있지 않고, 첫 번째 요소가 word와 같으면
            cards1.pop(0)
        elif cards2 and word == cards2[0]:  # cards2가 비어있지 않고, 첫 번째 요소가 word와 같으면
            cards2.pop(0)
        else:  # cards1[0] 또는 cards2[0]과 맞지 않으면 순서대로 만들 수 없음
            return "No"
    return "Yes"
