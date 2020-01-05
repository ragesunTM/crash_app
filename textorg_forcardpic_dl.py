#ここで一行ずつマージしたかった． paste poti.sh tama.sh > hoge.sh　←これでよかった

with open('./urls.sh') as f:
    lines = f.read().splitlines()

f = open('./poti.sh')
line = f.readline()
i = 0

while line:
    print(line + lines[i])
    line = f.readline()
    i += 1

f.close()