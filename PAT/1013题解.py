#

def find(x, p):
    if x != p[x]:
        p[x] = find(p[x], p)
    return p[x]

def main():
    n, k, m = map(int, input().split())

    edges = []
    for _ in range(k):
        a, b = map(int, input().split())
        edges.append((a, b))

    check=list(map(int, input().split()))

    for i in range(m):
        x = check[i]
        p = list(range(n + 1))
        cnt = n - 1

        for a, b in edges:
            if a != x and b != x:
                if find(a, p) != find(b, p):
                    p[find(a, p)] = find(b, p)
                    cnt -= 1

        # 最终连通块的个数减一就是结果
        print(cnt - 1)

if __name__ == "__main__":
    main()

