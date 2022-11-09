while True:
    print("\n 1: 새 가사 작성\n 2: 기존 가사에서 단어 수정\n 3: 가사 덧붙임\n 4: 종료")
    try:
        select = int(input("기능을 선택하세요(1~4) :"))

        if select == 1:
            file_name = input("작성한 파일명 입력: ")
            lyrics = input("작성할 가사 입력: ")
            with open(file_name,"w",encoding="utf-8") as f:
                f.write(lyrics)

        elif select ==2:
            modify_file_name = input("수정할 파일명 입력 : ")
            try:
                with open(modify_file_name,"r",encoding="utf-8") as f:
                    data = f.read()
                    print(data)
                    word_1 = input("어떤 단어를 변경하시겠습니까?: ")
                    word_2 = input(f"{word_1}을(를) 어떤 단어로 변경하시겠습니까?: ")
                    data=data.replace(word_1,word_2)
                
                with open(modify_file_name,"w",encoding="utf-8") as f:
                    f.write(data)
                    print(data)

            except:
                print(f"Could not read file {modify_file_name}")

        elif select ==3:
            add_file_name = input("수정할 파일명 입력 : ")
            try:
                with open(add_file_name,"a+",encoding="utf-8") as f:
                    add_lyrics = input("추가 작성할 가사 입력 :")
                    f.write(add_lyrics)
                    lyrics=f.read()
                    print(lyrics)

            except Exception as e:
                print(e)
        elif select ==4:
            break
        else:
            raise Exception("입력 값을 확인하세요.")
    except:
        print("입력 값을 확인하세요.")