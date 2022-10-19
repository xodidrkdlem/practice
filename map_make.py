a = "나비"
b = list(a)
print(b)

map_str ="""
oxoxxxxoF
oooxxooox
oxoxooxox
xxxxooxxx
ooooxoooo
xoxoooxox
ooooxooox
Sxxooxxox
"""
d = list(map_str)
print(d)
print(d[0] ,d[1] ,d[2] ,d[3] ,d[4] ,d[5] ,d[6] ,d[7] ,d[8], d[9],     d[10],     #d[0],d[10] = 띄어쓰기,줄바꿈도 인덱스 한칸 차지
           d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18],d[19],     d[20],
           d[21],d[22],d[23],d[24],d[25],d[26],d[27],d[28],d[29],     d[30],
           d[31],d[32],d[33],d[34],d[35],d[36],d[37],d[38],d[39],     d[40],
           d[41],d[42],d[43],d[44],d[45],d[46],d[47],d[48],d[49],     d[50],
           d[51],d[52],d[53],d[54],d[55],d[56],d[57],d[58],d[59],     d[60],
           d[61],d[62],d[63],d[64],d[65],d[66],d[67],d[68],d[69],     d[70],
           d[71],d[72],d[73],d[74],d[75],d[76],d[77],d[78],d[79],     d[80],)         #d[9] = F , d[71] = s

# print(id(d[1]))  #id 주소 사용하기: o를 사용하는 인덱스 모두 주소값이 같다. 
# print(id(d[2]))                    x를 사용하는 인덱스 모두 주소값이 같다.
# print(id(d[3]))                    F,S를 사용하는 인덱스는 주소값이 틀리다.
# print(id(d[4]))

#애벌레(플레이어)는 p와 s를 포함한  id가 'o'과 같은 곳으로 움직일수 있다.
#  

#-------------------------------------------------------------------
map_str ="""
o x o x x x x o F
o o o x x o o o x
o x o x o o x o x
x x x x o o x x x
o o o o x o o o o
x o x o o o x o x
o o o o x o o o x
S x x o o x x o x
"""

b = map_str.split()
print(b)                            #맵 만들기 최종본.





