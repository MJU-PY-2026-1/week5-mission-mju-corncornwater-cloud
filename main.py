
age = input("나이를 입력하세요 :");
exist_coupon = input("할인 쿠폰이 있나요? (Y/N) :");
print("-----------------------------------");
print("결과 :");
if ( exist_coupon == 'Y' and int(age) < 13 ) :
    print("꼬마 VIP 고객님! 팝콘 무료 증정!");
if ( exist_coupon == 'Y' or int(age) >= 65 ) :
    print("티켓 요금 : 무료입니다.");
else :
    print("티켓 요금 : 15,000원입니다.");

