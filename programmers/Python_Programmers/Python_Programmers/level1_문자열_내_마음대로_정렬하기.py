def solution(strings, n):
    def nkey(x):
        return x[n] 
    strings.sort(key=nkey)
    return strings

string = ["sun", "bed", "car"]
n = 1
print(solution(string,n))