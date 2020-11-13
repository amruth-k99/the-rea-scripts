s = "abcdefabcdefabcdefabcdefghiaajabcdefa"
st = []
for x in s:
    if x not in st:
        st.append(x)

print('all:', st)
temp = []
main_count = len(st)
count = 0
for x in s:
    
    if(count > main_count):
        main_count = count

print(main_count)
