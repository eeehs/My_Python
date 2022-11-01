import multiprocessing as mp

# 프로세스에서 실행할 함수

def sub_process(name):
    print("[sub] start")
    print(name)
    print("[sub] end")


# 메인 프로세스

if __name__ == "__main__":
    print("[main] start")
    p = mp.Process(target=sub_process,args=('startcoding',))
    p.start()
    print("[main] end")