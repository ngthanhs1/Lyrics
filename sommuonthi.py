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
        ("🎧Baby hỏi khi nào về", 0.4, 0.1),
        ("Anh tung ngay đồng xu", 1.0, 0.1),
        ("Chỉ là 50/50, anh biết thế thoi", 1.4, 0.1),
        ("Nên anh sẽ phải chiến thắng(uh), dù nếm cay đắng(uh)", 0.007, 0.06),
        ("Bay lên cao vút, mang cả nắng về", 0.004, 0.08),
        ("Để thắp sáng trái tim, mặc cho đời nhấn chìm", 0.009, 0.07),
        ("Tình yêu này ngoi lên như vì sao băng trong đêm", 0.001, 0.05),
        ("Sao băng trong đêm...", 0.009, 0.057)
    ]
    t0 = time.perf_counter()
    for text, start_at, speed in lyrics:
        now = time.perf_counter() - t0
        wait = start_at - now
        if wait > 0:
            time.sleep(wait)
        animate_text(text, speed)

if __name__ == "__main__":
    sing_song()









