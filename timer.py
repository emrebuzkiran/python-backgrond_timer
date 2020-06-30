import threading
def finis():
    global timer
    timer = 60

    for x in range(60):
        timer -= 1
        sleep(1)

    print("\ntime end")

finis_thread = threading.Thread(target=finis)
finis_thread.start()

while timer > 0:
  print("hello")
