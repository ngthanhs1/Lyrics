import time
import sys

def animate_text(text, speed=0.1):
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    sys.stdout.write(YELLOW)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET + '\n')

def sing_song():
    lyrics = [
        ("Người đừng lặng im đến thế", 0.11, 0.9),
        ("Vì lặng im sẽ giết chết con tim",  0.135, 3.95),
        ("Dù yêu thương chẳng còn",    0.1, 0.70),
        ("Anh vẫn xin em nói một lời", 0.145, 0.7),
        ("Ngoài kia bao la thế giới", 0.15, 3.7),
        ("Nhưng trong anh thế giới",  0.08, 0.50),
        ("Chỉ là em thôi",     0.13, 0.40),
        ("Mình xa nhau thật rồi",     0.14, 3.7),
        ("Nhưng anh vẫn chờ đợi...",     0.16, 0.8)
    ]

    t0 = time.perf_counter()
    for text, speed, start_at in lyrics:
        now = time.perf_counter() - t0
        wait = start_at - now
        if wait > 0:
            time.sleep(wait)
        animate_text(text, speed)

if __name__ == "__main__":
    sing_song()
