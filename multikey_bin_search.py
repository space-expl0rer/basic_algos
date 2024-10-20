#finds indexes (if possible) of q queries in sorted array vec, using bin_search
def bin_search(vec, l, r, el):
    ln = r - l + 1
    if ln == 0:
        return -1
    if ln == 1:
        if vec[l] == el:
            return l
        else:
            return -1
    if vec[ln // 2 + l] == el:
        return l + ln // 2
    elif vec[ln // 2 + l] > el:
        return bin_search(vec, l, ln // 2 + l - 1, el)
    else:
        return bin_search(vec, l + ln // 2 + 1, r, el)
def main():
    n = int(input())
    vec = list(map(int, input().split()))
    q = int(input())
    vec_q = list(map(int, input().split()))
    for i in vec_q:
        print(bin_search(vec, 0, n - 1, i))

main()
