import time

time_to_run = 800
if __name__ == '__main__':
    for i in range(time_to_run):
        print("Count {}".format(i))
        time.sleep(1)
    print("Ended gracefully")
