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
        ("🎧Baby hỏi khi nào về", 0.108, 0.5),
        ("Anh tung ngay đồng xu", 0.148, 1.2),
        ("Chỉ là 50/50, anh biết thế ", 0.09, 3.0),
        ("Nên anh sẽ phải chiến thắng(uh), dù nếm cay đắng(uh)", 0.12, 3.7),
        ("Bay lên cao vút, mang cả nắng về", 0.12, 4.0),
        ("Để thắp sáng trái tim, mặc cho đời nhấn chìm", 0.04, 1.0),
        ("Tình yêu này ngoi lên như vì sao băng trong đêm", 0.176, 8.1),
        ("Sao băng trong đêm...", 0.1, 16.1)
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









