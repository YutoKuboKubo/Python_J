import sys
args = sys.argv
#引数を変数に代入
N = int(args[1])
#入力した値までの素数のリストを作成
def prime(N):
  primes = []
  for i in range(2, N + 1):
    primes.append(i)
    for p in range(2, i):
      if i % p == 0:
        primes.remove(i)
        break
  return primes
#素数のリストの長さをlist_lenに代入
primes_list = prime(N)
list_len = len(primes_list)
#素因数分解
ps = []
i = 0
while i <= list_len - 1:
  if N % primes_list[i] == 0: #割り切れるとき割って、リストに代入
    N = N / primes_list[i]
    ps.append(primes_list[i])
  elif N % primes_list[i] != 0: #割り切れないときは次の素数へ
    i = i + 1
#素因数分解の結果を出力
print(ps)




    


