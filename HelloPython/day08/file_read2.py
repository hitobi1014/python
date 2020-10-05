with open("D:/A_TeachingMaterial/8.Python/HelloPython/day08/myfile",'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
# with as문을 걸어주면 구문이 밖을 나오게 될때 자동으로 메모리에서 없어진다