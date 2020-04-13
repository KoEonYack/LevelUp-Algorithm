"""
    @ Baek 1620 나는야 포켓몬 마스터 이다솜
    @ Prob. https://www.acmicpc.net/problem/1620
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 13.
    @ End day: 20. 04. 13.
"""

N, M = map(int, input().split())
dict = {}
name = [0]
for i in range(1, N+1):
    S = input()
    dict[S] = i
    name.append(S)

for _ in range(M):
    S = input()
    if S.isdigit():
        print(name[int(S)])
    else:
        print(dict[S])


"""
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
>
Pikachu
26
Venusaur
16
14

"""
