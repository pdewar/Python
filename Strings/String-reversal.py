
def reverse(S):
    answer = ""
    for X in S:
        answer = X + answer

    return answer

if __name__ == "__main__":
    print(reverse("hofstra"))
    print(reverse("RAT"))