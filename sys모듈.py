import sys
#명령 매개변수 출력
print(sys.argv)
#컴퓨터의 환경과 관련된 정보를 출력
print("---")
print("getwindowsversion():",sys.getwindowsversion())
print("---")
print("copyright:",sys.copyright)
print("---")
print("version",sys.version)

sys.exit()
#프로그램 강제종료
