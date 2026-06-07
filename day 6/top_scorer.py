Score=list(map(int,input('Enter the scores : ').split()))
print(f"Ranked : {sorted(Score,reverse=True)} | Top scorer : {max(Score)}")  