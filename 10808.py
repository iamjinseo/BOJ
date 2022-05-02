# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며
# 알파벳 소문자로만 이루어져 있다.

# 출력
# 단어에 포함되어 있는 
# a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

word = input() #집어넣을 단어
output = [0 for i in range(26)] #26가지 알파벳
for letter in word:
    output[ord(letter)-ord('a')]+=1 #아스키코드로 반환해서 리스트에 넣음
    #예를들어 a가 나왔으면 a값-a값이므로 0번째에 들어갈 것임

for letter in output:
    print(letter, end=' ')