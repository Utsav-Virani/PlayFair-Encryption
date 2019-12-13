import math

key = input("Enter The KEY : ")
plain_txt = input("Enter The Plain Text :  ")
key = key.upper()
plain_txt = plain_txt.upper()

alphas = list()
alp = 'A'
for i in range(0,26):
    alphas.append(alp)
    alp = chr(ord(alp)+1)

key_alp_all_comon = list()
for i in key:
    for j in alphas:
        if i == j:
            key_alp_all_comon.append(i)

key_alp_comon = list()
for k in key_alp_all_comon:
    if k not in key_alp_comon:
        key_alp_comon.append(k)

alphas_alon = list()
for i in alphas:
    if i not in key_alp_comon:
        alphas_alon.append(i)

mat = key_alp_comon + alphas_alon
for k in mat:
    if k == 'J':
        mat.remove(k)

matrix = [[0 for i in range(5)] for j in range(5)]
ind = 0
for i in range(5):
    for j in range(5):
        matrix[i][j] = mat[ind]
        ind+=1

plain_text_list = list()
last = None
for e in plain_txt:
    if e == ' ':
        continue
    else:
        if e == last:
            plain_text_list.append('X')
            plain_text_list.append(e)
            last = e
        else:
            plain_text_list.append(e)
            last = e

if not len(plain_text_list) %2 == 0:
    plain_text_list.append('X')

# print(len(plain_text_list)/2)
mat_txt_pir = [[0 for i in range(2)] for j in range(int(len(plain_text_list) / 2))]
ind = 0
for i in range(int(len(plain_text_list) / 2)):
    for j in range(2):
        mat_txt_pir[i][j] = plain_text_list[ind]
        ind+=1
indx = list()
max_indx_pir = [[0 for i in range(4)] for j in range(int(len(plain_text_list) / 2))]
for ii in range(int(len(plain_text_list) / 2)):
    for jj in range(2):
        for i in range(5):
            for j in range(5):
                if mat_txt_pir[ii][jj] == matrix[i][j]:
                    indx.append(i)
                    indx.append(j)

ind = 0
for i in range(int(len(plain_text_list) / 2)):
    for j in range(4):
        max_indx_pir[i][j] = indx[ind]
        ind+=1

indx_rslt = list()
max_indx_rslt = [[0 for i in range(4)] for j in range(int(len(plain_text_list) / 2))]

for i in range(int(len(plain_text_list) / 2)):
    j=0
    ii = max_indx_pir[i][j]
    j+=1
    jj = max_indx_pir[i][j]
    j+=1
    kk = max_indx_pir[i][j]
    j+=1
    ll = max_indx_pir[i][j]
    if ii == kk:
        if jj == 4:
            jj = -1
        if ll == 4:
            ll = -1
        indx_rslt.append(ii)
        indx_rslt.append(jj+1)
        indx_rslt.append(kk)
        indx_rslt.append(ll+1)

    elif jj == ll:
        if ii == 4:
            ii = -1
        if kk == 4:
            kk = -1
        indx_rslt.append(ii+1)
        indx_rslt.append(jj)
        indx_rslt.append(kk+1)
        indx_rslt.append(ll)

    else:
        indx_rslt.append(ii)
        indx_rslt.append(ll)
        indx_rslt.append(kk)
        indx_rslt.append(jj)

ind = 0
for i in range(int(len(plain_text_list) / 2)):
    for j in range(4):
        max_indx_rslt[i][j] = indx_rslt[ind]
        ind+=1

cip_txt = list()
for i in range(int(len(plain_text_list) / 2)):
    for j in range(0,4,2):
        ii = max_indx_rslt[i][j]
        j+=1
        jj = max_indx_rslt[i][j]
        cip_txt.append(matrix[ii][jj])

print("cipher text : ",str(cip_txt))