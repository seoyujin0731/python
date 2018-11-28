price = int(input("금액을 입력하시오 : "))
amount = int(input("수량을 입력하시오: "))
change = price-amount*200
if(change<0):
    print("돈이 부족합니다.")
else:
    print("거스름돈 : ",change,"원 입니다")