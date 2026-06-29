def delete_others(st):
    others = ["\'", "\"", '.', ',', '!', '?', '`']
    st2 = ""
    for i in range(0, len(st)):
        if(st[i] in others):
            pass
        else:
            st2 += st[i]
    return st2

word = "Let`s go Mike!"
print(delete_others(word))