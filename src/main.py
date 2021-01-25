from bot import Bot
import sys

def main():
    try:
        with open("secret.txt", "r") as f:
            srs_info = [s.strip() for s in f.readline().split(" ")]
            mail_info = [s.strip() for s in f.readline().split(" ")]

        b = Bot(srs_info, mail_info)

        b.run()

    except FileNotFoundError as e:
        print("Couldn't detect the necessary file: secret.txt")
        print("If you haven't, please create a file and name it secret.txt. Enter your bilkent ID and SRS password in the first line and your email username and password in the second.")
        sys.exit(1)
    except Exception as e:
        raise e
        sys.exit(1)


if __name__ == "__main__":
    main()
