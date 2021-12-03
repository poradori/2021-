import time

def burger():  #햄버거
    price = [3000,4500,4000,5900,7900,6900,2000,1500,2000]
    choice = []
    total = 0
    order = []
    more_or_stop = 0
    #메뉴 출력
    print("단품 >> 1.불고기버거(3000) 2.모짜렐라버거(4500) 3.새우버거(4000)")
    print("세트 >> 4.불고기버거세트(5900) 5.모짜렐라버거세트(7900) 6.새우버거세트(6900)")
    print("사이드 >> 7.치즈스틱(2000) 8.양념감자(1500) 9.치킨너겟(2000)")

    while(True):  #메뉴선택
        choice = int(input("어떤 음식을 드시겠습니까? "))

        if(choice == 1):
            total += price[0]
            order.append('불고기버거')

        elif(choice == 2):
            total += price[1]
            order.append('모짜렐라버거')

        elif(choice == 3):
            total += price[2]
            order.append('새우버거')

        elif(choice == 4):
            total += price[3]
            order.append('불고기버거세트')

        elif(choice == 5):
            total += price[4]
            order.append('모짜렐라버거세트')

        elif(choice == 6):
            total += price[5]
            order.append('새우버거세트')

        elif(choice == 7):
            total += price[6]
            order.append('치즈스틱')

        elif(choice == 8):
            total += price[7]
            order.append('양념감자')

        elif(choice == 9):
            total += price[8]
            order.append('치킨너겟')

        else:
            print('잘못된 번호입니다')
            continue

        more_or_stop = input("더 결제하시겠습니까?(y/n)")
        #결제 수단 확인

        if(more_or_stop == 'n' or more_or_stop == 'ㅜ'):
            print("결제 내역입니다.")
            print(order)
            print("총 %d원 나오셨습니다." %total)
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")

        elif(more_or_stop == 'y' or more_or_stop == 'ㅛ'):
            continue

        else:
            print('잘못된 입력입니다.')
            continue
        #카드 일때        
        if(howtopay == '카드'):
            print('카드를 삽입해주세요')
            time.sleep(1)
            print('카드 삽입완료')
            time.sleep(1.5)
            print('결제 중입니다.')
            time.sleep(1)
            print('결제 중입니다..')
            time.sleep(1)
            print('결제 중입니다...')
            time.sleep(1.5)
            print('결제가 완료되었습니다! 영수증을 받으십시오.')
            break
        #현금 일때
        elif(howtopay == '현금'):
            money = int(input("돈을 넣어주세요 "))

            if(money < total):
                notenough = input('돈이 부족합니다.')
                break

            elif(money >= total):
                print('%d원을 받았습니다.'
                      %money)

                if(money == total):
                    print('결제가 완료되었습니다.')
                    break
                time.sleep(1)
                print('거스름돈 반환중.')
                time.sleep(1)
                print('거스름돈 반환중..')
                time.sleep(1.5)
                print('잔돈 %d을(를) 받으십시오.'%(money-total))
                break

        else:
            print('잘못된 입력입니다.')
            continue


                                                                          
def cafe():  #카페
    print("1. 빽다방 2. 스타벅스 3. 투썸플레이스 4. 이디야커피 5. 카페베네")
    #카페 종류 선택
    cafe = int(input())
    if(cafe == 1):
        while True:
            menu1=0
            menu2=0
            menu3=0
            menu4=0
            menu5=0
            menu6=0
            menu7=0
            menu8=0
            menu9=0
            cost=0
        
            print("------------ 메뉴 ------------\n")
            print("1. 원조 빽스치노        3000원\n")
            print("2. 앗!메리카노(HOT)     1500원\n")
            print("3. 앗!메리카노(ICE)     2000원\n")
            print("4. 원조 커피(HOT)       2000원\n")
            print("5. 원조 커피(ICE)       2500원\n")
            print("6. 달달연유라떼(HOT)    2500원\n")
            print("7. 달달연유라떼(ICE)    2500원\n")
            print("8. 빽's 라떼(HOT)       2500원\n")
            print("9. 빽's 라떼(ICE)       3000원\n")
            print("0. 주문종료\n")
            print("------------------------------\n")
            print()
        
            while True:
                menu = int(input("드실 음료는 무엇입니까? ")) #음료 선택
                if menu == 1:
                    menu1 += 1
                elif menu == 2:
                    menu2 += 1
                elif menu == 3:
                    menu3 += 1
                elif menu == 4:
                    menu4 += 1
                elif menu == 5:
                        menu5 += 1
                elif menu == 6:
                    menu6 += 1
                elif menu == 7:
                    menu7 += 1
                elif menu == 8:
                    menu8 += 1
                elif menu == 9:
                    menu9 += 1
                elif menu == 0:
                    break
            #주문 내역 출력
            print("\n---------- 총 주문 내역 ----------\n")
            if menu1>0:
                cost += 3000*menu1
                print("       원조 빽스치노 %d개\n" %menu1)
            if menu2>0:
                cost += 1500*menu2
                print("       앗!메리카노(HOT) %d개\n" %menu2)
            if menu3>0:
                cost += 2000*menu3
                print("       앗!메리카노(ICE) %d개\n" %menu3)
            if menu4>0:
                cost += 2000*menu4
                print("       원조 커피(HOT) %d개\n" %menu4)
            if menu5>0:
                cost += 2500*menu5
                print("       원조 커피(ICE) %d개\n" %menu5)
            if menu6>0:
                cost += 2500*menu6
                print("       달달연유라떼(HOT) %d개\n" %menu6)
            if menu7>0:
                cost += 2500*menu7
                print("       달달연유라떼(ICE) %d개\n" %menu7)
            if menu8>0:
                cost += 2500*menu8
                print("       빽's 라떼(HOT) %d개\n" %menu8)
            if menu9>0:
                cost += 3000*menu9
                print("       빽's 라떼(ICE) %d개\n" %menu9)
            print("----------------------------------\n")
            print("총 %d원 입니다." %cost)
            #결제 수단 확인 
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")
            if(howtopay == '카드'):  #카드 일때
                print('카드를 삽입해주세요')
                time.sleep(1)
                print('카드 삽입완료')
                time.sleep(1.5)
                print('결제 중입니다.')
                time.sleep(1)
                print('결제 중입니다..')
                time.sleep(1)
                print('결제 중입니다...')
                time.sleep(1.5)
                print('결제가 완료되었습니다! 영수증을 받으십시오.')
                break
            elif(howtopay == '현금'): #현금 일때
                cash=int(input("보유하고 계신 현금은 얼마입니까? "))
                if cash>cost:
                    print("잔액: %d원" %(cash-cost))
                    print("결제가 완료되었습니다 감사합니다")
                    break
                else:
                    print("잔액이 부족하여 결제에 실패했습니다")
                    break           
    if(cafe == 2):
        while True:
            menu1=0
            menu2=0
            menu3=0
            menu4=0
            menu5=0
            menu6=0
            menu7=0
            menu8=0
            menu9=0
            cost=0
        
            print("--------------- 메뉴 ---------------\n")
            print("1. 토피 넛 라떼               5800원\n")
            print("2. 스타벅스 돌체 라떼         5600원\n")
            print("3. 카페 모카                  5100원\n")
            print("4. 카페 아메리카노            4100원\n")
            print("5. 카페 라떼                  4600원\n")
            print("6. 카라멜 마키아또            5600원\n")
            print("7. 화이트 초콜릿 모카         5600원\n")
            print("8. 에스프레소                 3600원\n")
            print("9. 헤이즐넛 스타벅스 더블 샷  4800원\n")
            print("0. 주문종료\n")
            print("------------------------------------\n")
            print()

            while True:
                menu = int(input("드실 음료는 무엇입니까? "))
                if menu == 1:
                    menu1 += 1
                elif menu == 2:
                    menu2 += 1
                elif menu == 3:
                    menu3 += 1
                elif menu == 4:
                    menu4 += 1
                elif menu == 5:
                    menu5 += 1
                elif menu == 6:
                    menu6 += 1
                elif menu == 7:
                    menu7 += 1
                elif menu == 8:
                    menu8 += 1
                elif menu == 9:
                    menu9 += 1
                elif menu == 0:
                    break
            print("\n---------- 총 주문 내역 ----------\n")
            if menu1>0:
                cost += 5800*menu1
                print("       토피 넛 라떼 %d개\n" %menu1)
            if menu2>0:
                cost += 5600*menu2
                print("       스타벅스 돌체 라떼 %d개\n" %menu2)
            if menu3>0:
                cost += 5100*menu3
                print("       카페 모카 %d개\n" %menu3)
            if menu4>0:
                cost += 4100*menu4
                print("       카페 아메리카노 %d개\n" %menu4)
            if menu5>0:
                cost += 4600*menu5
                print("       카페 라떼 %d개\n" %menu5)
            if menu6>0:
                cost += 5600*menu6
                print("       카라멜 마키아또 %d개\n" %menu6)
            if menu7>0:
                cost += 5600*menu7
                print("       화이트 초콜릿 모카 %d개\n" %menu7)
            if menu8>0:
                cost += 3600*menu8
                print("       에스프레소 %d개\n" %menu8)
            if menu9>0:
                cost += 4800*menu9
                print("       헤이즐넛 스타벅스 버블 샷 %d개\n" %menu9)
            print("----------------------------------\n")
            print("총 %d원 입니다." %cost)
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")
            if(howtopay == '카드'):
                print('카드를 삽입해주세요')
                time.sleep(1)
                print('카드 삽입완료')
                time.sleep(1.5)
                print('결제 중입니다.')
                time.sleep(1)
                print('결제 중입니다..')
                time.sleep(1)
                print('결제 중입니다...')
                time.sleep(1.5)
                print('결제가 완료되었습니다! 영수증을 받으십시오.')
                break
            elif(howtopay == '현금'):
                cash=int(input("보유하고 계신 현금은 얼마입니까? "))
                if cash>cost:
                    print("잔액: %d원" %(cash-cost))
                    print("결제가 완료되었습니다 감사합니다")
                    break
                else:
                    print("잔액이 부족하여 결제에 실패했습니다")
                    break
    if(cafe == 3):
        while True:
            menu1=0
            menu2=0
            menu3=0
            menu4=0
            menu5=0
            menu6=0
            menu7=0
            menu8=0
            menu9=0
            cost=0
        
            print("--------------- 메뉴 ---------------\n")
            print("1. 아메리카노(R)              4100원\n")
            print("2. 아메리카노(L)              4600원\n")
            print("3. 카페라떼(R)                4600원\n")
            print("4. 카페라떼(L)                5100원\n")
            print("5. 모카칩 커피프라페(L)       5800원\n")
            print("6. 민트초코 프라페(L)         6300원\n")
            print("7. 떠먹는 고구마 밀크생크림   6100원\n")
            print("8. 떠먹는 티라미수            6100원\n")
            print("9. 떠먹는 아이스박스          6100원\n")
            print("0. 주문종료\n")
            print("------------------------------------\n")
            print()

            while True:
                menu = int(input("드실 음료는 무엇입니까? "))
                if menu == 1:
                    menu1 += 1
                elif menu == 2:
                    menu2 += 1
                elif menu == 3:
                    menu3 += 1
                elif menu == 4:
                    menu4 += 1
                elif menu == 5:
                    menu5 += 1
                elif menu == 6:
                    menu6 += 1
                elif menu == 7:
                    menu7 += 1
                elif menu == 8:
                    menu8 += 1
                elif menu == 9:
                    menu9 += 1
                elif menu == 0:
                    break
            print("\n---------- 총 주문 내역 ----------\n")
            if menu1>0:
                cost += 4100*menu1
                print("       아메리카노(R) %d개\n" %menu1)
            if menu2>0:
                cost += 4600*menu2
                print("       아메리카노(L) %d개\n" %menu2)
            if menu3>0:
                cost += 4600*menu3
                print("       카페라떼(R) %d개\n" %menu3)
            if menu4>0:
                cost += 5100*menu4
                print("       카페라떼(L) %d개\n" %menu4)
            if menu5>0:
                cost += 5800*menu5
                print("       모카칩 커피프라페(L) %d개\n" %menu5)
            if menu6>0:
                cost += 6300*menu6
                print("       민트초코 프라페(L) %d개\n" %menu6)
            if menu7>0:
                cost += 6100*menu7
                print("       떠먹는 고구마 밀크생크림 %d개\n" %menu7)
            if menu8>0:
                cost += 6100*menu8
                print("       떠먹는 티라미수 %d개\n" %menu8)
            if menu9>0:
                cost += 6100*menu9
                print("       떠먹는 아이스박스 %d개\n" %menu9)
            print("----------------------------------\n")
            print("총 %d원 입니다." %cost)
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")
            if(howtopay == '카드'):
                print('카드를 삽입해주세요')
                time.sleep(1)
                print('카드 삽입완료')
                time.sleep(1.5)
                print('결제 중입니다.')
                time.sleep(1)
                print('결제 중입니다..')
                time.sleep(1)
                print('결제 중입니다...')
                time.sleep(1.5)
                print('결제가 완료되었습니다! 영수증을 받으십시오.')
                break
            elif(howtopay == '현금'):
                cash=int(input("보유하고 계신 현금은 얼마입니까? "))
                if cash>cost:
                    print("잔액: %d원" %(cash-cost))
                    print("결제가 완료되었습니다 감사합니다")
                    break
                else:
                    print("잔액이 부족하여 결제에 실패했습니다")
                    break
    if(cafe == 4):
        while True:
            menu1=0
            menu2=0
            menu3=0
            menu4=0
            menu5=0
            menu6=0
            menu7=0
            menu8=0
            menu9=0
            cost=0
        
            print("--------------- 메뉴 ---------------\n")
            print("1. HOT 카페 아메리카노        3200원\n")
            print("2. ICED 카페 아메리카노       3200원\n")
            print("3. (EX)ICED 연유 카페 라떼    5000원\n")
            print("4. HOT 카페 모카              3900원\n")
            print("5. ICED 카페 모카             3900원\n")
            print("6. HOT 민트 모카              4200원\n")
            print("7. (EX)ICED 카라멜 마끼아또   5100원\n")
            print("8. 생크림 와플                2500원\n")
            print("9. 프레즐                     2300원\n")
            print("0. 주문종료\n")
            print("------------------------------------\n")
            print()

            while True:
                menu = int(input("드실 음료는 무엇입니까? "))
                if menu == 1:
                    menu1 += 1
                elif menu == 2:
                    menu2 += 1
                elif menu == 3:
                    menu3 += 1
                elif menu == 4:
                    menu4 += 1
                elif menu == 5:
                    menu5 += 1
                elif menu == 6:
                    menu6 += 1
                elif menu == 7:
                    menu7 += 1
                elif menu == 8:
                    menu8 += 1
                elif menu == 9:
                    menu9 += 1
                elif menu == 0:
                    break
            print("\n---------- 총 주문 내역 ----------\n")
            if menu1>0:
                cost += 3200*menu1
                print("       HOT 카페 아메리카노 %d개\n" %menu1)
            if menu2>0:
                cost += 3200*menu2
                print("       ICED 카페 아메리카노 %d개\n" %menu2)
            if menu3>0:
                cost += 5000*menu3
                print("       (EX)ICED 연유 카페 라떼 %d개\n" %menu3)
            if menu4>0:
                cost += 3900*menu4
                print("       HOT 카페 모카 %d개\n" %menu4)
            if menu5>0:
                cost += 3900*menu5
                print("       ICED 카페 모카 %d개\n" %menu5)
            if menu6>0:
                cost += 4200*menu6
                print("       HOT 민트 모카 %d개\n" %menu6)
            if menu7>0:
                cost += 5100*menu7
                print("       (EX)ICED 카라멜 마끼아또 %d개\n" %menu7)
            if menu8>0:
                cost += 2500*menu8
                print("       생크림 와플 %d개\n" %menu8)
            if menu9>0:
                cost += 2300*menu9
                print("       프레즐 %d개\n" %menu9)
            print("----------------------------------\n")
            print("총 %d원 입니다." %cost)
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")
            if(howtopay == '카드'):
                print('카드를 삽입해주세요')
                time.sleep(1)
                print('카드 삽입완료')
                time.sleep(1.5)
                print('결제 중입니다.')
                time.sleep(1)
                print('결제 중입니다..')
                time.sleep(1)
                print('결제 중입니다...')
                time.sleep(1.5)
                print('결제가 완료되었습니다! 영수증을 받으십시오.')
                break
            elif(howtopay == '현금'):
                cash=int(input("보유하고 계신 현금은 얼마입니까? "))
                if cash>cost:
                    print("잔액: %d원" %(cash-cost))
                    print("결제가 완료되었습니다 감사합니다")
                    break
                else:
                    print("잔액이 부족하여 결제에 실패했습니다")
                    break
    if(cafe == 5):
        while True:
            menu1=0
            menu2=0
            menu3=0
            menu4=0
            menu5=0
            menu6=0
            menu7=0
            menu8=0
            menu9=0
            cost=0
        
            print("--------------- 메뉴 ---------------\n")
            print("1. 로즈 뱅쇼 R (HOT)          5800원\n")
            print("2. 치즈크림 숏 라떼(ICE)      4800원\n")
            print("3. 아메리카노(L)              4600원\n")
            print("4. 카페모카 R                 5200원\n")
            print("5. 카라멜마끼아또 R           5400원\n")
            print("6. 콜드브루 L                 5000원\n")
            print("7. 베리딸기빙수               11900원\n")
            print("8. 초코악마 빙수(1인)         6800원\n")
            print("9. 바스크 치즈 케이크         6800원\n")
            print("0. 주문종료\n")
            print("------------------------------------\n")
            print()

            while True:
                menu = int(input("드실 음료는 무엇입니까? "))
                if menu == 1:
                    menu1 += 1
                elif menu == 2:
                    menu2 += 1
                elif menu == 3:
                    menu3 += 1
                elif menu == 4:
                    menu4 += 1
                elif menu == 5:
                    menu5 += 1
                elif menu == 6:
                    menu6 += 1
                elif menu == 7:
                    menu7 += 1
                elif menu == 8:
                    menu8 += 1
                elif menu == 9:
                    menu9 += 1
                elif menu == 0:
                    break
            print("\n---------- 총 주문 내역 ----------\n")
            if menu1>0:
                cost += 5800*menu1
                print("       로즈 뱅쇼 R (HOT) %d개\n" %menu1)
            if menu2>0:
                cost += 4800*menu2
                print("       치즈크림 숏 라떼(ICE) %d개\n" %menu2)
            if menu3>0:
                cost += 4600*menu3
                print("       아메리카노(L) %d개\n" %menu3)
            if menu4>0:
                cost += 5200*menu4
                print("       카페모카 R %d개\n" %menu4)
            if menu5>0:
                cost += 5400*menu5
                print("       카라멜마끼아또 R %d개\n" %menu5)
            if menu6>0:
                cost += 5000*menu6
                print("        콜드브루 L %d개\n" %menu6)
            if menu7>0:
                cost += 11900*menu7
                print("        베리딸기빙수 %d개\n" %menu7)
            if menu8>0:
                cost += 6800*menu8
                print("       초코악마 빙수(1인) %d개\n" %menu8)
            if menu9>0:
                cost += 6800*menu9
                print("       바스크 치즈 케이크 %d개\n" %menu9)
            print("----------------------------------\n")
            print("총 %d원 입니다." %cost)
            howtopay = input("결제수단을 입력해주세요.(카드,현금) ")
            if(howtopay == '카드'):
                print('카드를 삽입해주세요')
                time.sleep(1)
                print('카드 삽입완료')
                time.sleep(1.5)
                print('결제 중입니다.')
                time.sleep(1)
                print('결제 중입니다..')
                time.sleep(1)
                print('결제 중입니다...')
                time.sleep(1.5)
                print('결제가 완료되었습니다! 영수증을 받으십시오.')
                break
            elif(howtopay == '현금'):
                cash=int(input("보유하고 계신 현금은 얼마입니까? "))
                if cash>cost:
                    print("잔액: %d원" %(cash-cost))
                    print("결제가 완료되었습니다 감사합니다")
                    break
                else:
                    print("잔액이 부족하여 결제에 실패했습니다")
                    break



def chicken():  #치킨
    from time import sleep
    #메뉴 상세 출력
    def printmenu(menu, pay):
        for i in range(len(menu)):
            print ('%d. %s %d원'%(i+1 ,menu[i] ,pay[i]))
    #메뉴 상세 입력
    def scanmenu(l):
        while(1):
            choose = int(input('\n어떤 메뉴를 선택하시겠습니까?:'))
            return choose-1
    #숫자 범위 체크   
    def check(choose, l):
        if choose >= 0 and choose < l:
            return 0
    #주문 받은 내역 출력
    def orderprint(menu, pay, cnt):
        print('\n\n------------------------------------------------------------')
        print('주문내역')
        for i in range(cnt):
              print ('%d. %s %d원'%(i+1, menu[i] ,pay[i]))
        print('------------------------------------------------------------\n\n')
    #결제 여부
    def paycheck():
        result = int(input('결제하시겠습니까?(예(0)/아니오(1))'))
        return result
    #주문내역 합계
    def add(orderpaylist, cnt):
        total = 0
        for i in range (cnt):
            total += orderpaylist[i]

        return total
    #포장 배달 출력
    print('포장(1)/배달(2)')
    while(1):
        after = int(input('입력:'))
        if after >0 and after <3:
            break;
    if after == 1:
        print('포장을 선택하셨습니다.')
    else:
        print('배달을 선택하셨습니다.')
    #주문목록, 가격 저장을 위한 리스트선언
    ordermenulist = []
    orderpaylist = []
    cnt= 0

    while(1):
        #메뉴 선택
        print('\n\n---------------------BBQ---------------------\n')
        print('메뉴선택')
        menu= ["대표메뉴","신메뉴","사이드메뉴","음료수"]
        for i in range(4):
            print ('%d. %s' %(i+1, menu[i]))
        while(1):
            selectmenu = int(input('\n입력:'))
            if selectmenu > 0 and selectmenu <5:
                break;
        
        print ('\n%s를 선택하셨습니다.\n\n' %menu[selectmenu-1])
    
        if selectmenu == 1:
            menu1 = ["황금올리브 치킨", "자메이카 통다리구이", "핫황금올리브 블랙페퍼" ]
            pay1 = [18000, 19500, 19000]
            l = len(menu1)
            printmenu(menu1, pay1)
            #입력 값이 올바른지 확인
            while(1):
                choose = scanmenu(l)
                if check(choose, l) == 0:
                    break;
            #주문리스트에 추가(이름하고 가격)
            ordermenulist.insert(cnt, menu1[choose])
            orderpaylist.insert(cnt, pay1[choose])
            cnt += 1
        
        if selectmenu == 2:
            menu2 = ["눈맞은닭", "파더스치킨", "까먹 물치킨" ]
            pay2 = [23000,26000,22000]
            l = len(menu2)
            printmenu(menu2, pay2)
            while(1):
                choose = scanmenu(l)
                if check(choose, l) == 0:
                    break;
 
            ordermenulist.insert(cnt, menu2[choose])
            orderpaylist.insert(cnt, pay2[choose])
            cnt += 1
       
        if selectmenu == 3:
            menu3 = ["오감볼", "케이준감자", "황금알 치즈볼"]
            pay3 = [3000,3000,1000]
            l = len(menu3)
            printmenu(menu3, pay3)
            while(1):
                choose = scanmenu(l)
                if check(choose, l) == 0:
                    break;
                
            ordermenulist.insert(cnt, menu3[choose])
            orderpaylist.insert(cnt, pay3[choose])
            cnt += 1

        if selectmenu == 4:
            menu4 = ["콜라", "스프라이트", "레몬보이" ]
            pay4 = [3000,3000,1000]
            l = len(menu4)
            printmenu(menu4, pay4)
            while(1):
                choose = scanmenu(l)
                if check(choose, l) == 0:
                    break;
        
            ordermenulist.insert(cnt, menu4[choose])
            orderpaylist.insert(cnt, pay4[choose])
            cnt += 1
        #주문내역, 가격 출력
        orderprint(ordermenulist, orderpaylist, cnt)
        selectmenu == 0
        while(1):
            delete = int(input('주문내역을 수정하시겠습니까?(예(0)/아니오(1)):'))
            if check(delete, 2) == 0:
                break;
        if delete == 0:
            while(1):
                orderprint(ordermenulist, orderpaylist, cnt)
                deletenum = int(input('수정하고싶은 주문 번호를 입력해주세요(종료는 100):'))
                if deletenum == 100:
                    break;
                del(ordermenulist[deletenum-1])
                del(orderpaylist[deletenum-1])
                cnt = cnt - 1
        #결제 확인
        while(1):
            last = int(input('결제하시겠습니까?(예(0)/아니오(1)):'))
            if check(last, 2) == 0:
                break;
    
        if last == 0:
           break;
    #주문내역 출력
    print('주문내역')
    orderprint(ordermenulist, orderpaylist, cnt)
    total = add(orderpaylist, cnt)
    print(' %d원입니다.\n' %total)
    #결제 수단 확인
    while(1):
            end = int(input('(신용카드(0)/현금(1)):'))
            if check(end, 2) == 0:
                break;
    #신용카드 일때
    if end == 0:
        print('카드를 삽입해주세요')
        sleep(3)
        print('결제중.')
        sleep(1)
        print('결제중..')
        sleep(1)
        print('결제중...')
        sleep(1)
        print('결제가 완료되었습니다!')
    #현금일때
    if end == 1:
        while(1):
            cash = int(input('현금을 투입해주세요'))
            if cash < total:
                    print('잔액이 부족합니다.')
                    print('다시 입력해주세요.')
            if cash >= total:
                break;
            
        if cash >= total:
            cash = cash - total
            if cash != 0:
                print('거스름돈은 %d원 입니다.'%cash)
            print('결제가 완료되었습니다!')
            print('매장을 방문해 주셔서 감사합니다.')
    


print("1.햄버거집 2.일반카페 3.치킨집")
place = int(input("가고싶은 매장을 선택하세요. "))

if(place==1):
    burger()

elif(place ==2):
    cafe()
    
elif(place==3):
    chicken()
