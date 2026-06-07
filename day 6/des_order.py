list=list(map(int,input('Enter the inputs : ').split()))
print(f'Top three numbers: {sorted(list,reverse=True)[:3]}' )
