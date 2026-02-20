import time
from datetime import datetime

print("this line.")


def main():
    print("Hello World!")
    print(f"Current time: {datetime.now()}")
    time.sleep(1)
    print("Goodbye World!")


if __name__ == "__main__":
    main()
