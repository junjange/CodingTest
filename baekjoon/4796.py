import sys
# ù��° Case
cnt = 1

while True:

    l, p, v = map(int, sys.stdin.readline().split())

    # ������ �ٿ� 0�� 3�� �־����� ������ while���� �����ش�.
    if l == p == v == 0:
        break

    # divmod�� ù��° ���ڸ� �ι�° ���ڷ� ���� ��� �������� tuple �������� ��ȯ�� ���̴�.
    # ���� a �� ��, b �� ������
    a, b = divmod(v, p)
    print(a,b)
    # V��¥�� �ް��� ķ������ �����ϴ� P�Ϸ� �����ԵǸ� ķ������ ��� �� �� �ִ��� ���´�.(��)
    # �������� L�Ϻ��� ������ ��������ŭ �� ķ������ �� �� �ְ� �������� ũ�� L�ϸ�ŭ �� �� �� �ִ�.
    if b <= l:

        print("Case {}: {}".format(cnt, a * l + b))

    else:

        print("Case {}: {}".format(cnt, a * l + l))

    #Case Ƚ�� ī��Ʈ
    cnt += 1