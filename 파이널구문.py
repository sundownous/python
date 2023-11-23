def write_txt(filename, text):
    try:
        file = open(filename, "w")

        return#중간에 리턴이 되면 파일이 안닫혀

        file.write(text)

    except:
        print("오류")
    finally:
        file.close()#파이널로 닫기
write_txt("테스트파일.txt","이건 실험")
