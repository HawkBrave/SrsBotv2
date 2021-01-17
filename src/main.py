from bot import Bot
import sys

def main():
    try:
        with open("secret.txt", "r") as f:
            username, password = f.readline().strip(), f.readline().strip()
            b = Bot(username, password)

    except FileNotFoundError as e:
        print("Couldn't detect the necessary file: secret.txt")
        print("If you haven't, please create a file and name it secret.txt. Enter your bilkent ID in the first line and password in the second.")
        sys.exit(1)


    b.run()

if __name__ == "__main__":
    main()
