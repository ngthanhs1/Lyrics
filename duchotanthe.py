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
        ("🎧Anh có nỗi sợ", 0.07, 0.5),
        ("Sợ ta mất nhau", 0.15, 1.2),
        ("Tình yêu bắt đầu", 0.07, 2.0),
        ("Không phải để tìm nỗi đau", 0.07, 2.8),
        ("Sợ giây phút này", 0.07, 4.3),
        ("Chẳng còn", 0.06, 5.0),
        ("thấy em bên anh", 0.08, 5.7),
        ("về sau...", 0.06, 6.3),
        ("Nhiều khi nóng giận", 0.09, 7.0),
        ("Nhiều khi cãi nhau       ", 0.15, 8.0),
        ("Để rồi cuối cùng", 0.05, 9.0),
        ("Ta lại trở về với nhau", 0.09, 10.0),
        ("Đôi tay này cần ", 0.01, 11.0),
        ("nâng niu", 0.15, 12.0),
        ("Vì em là người", 0.07, 13.0),
        (" anh yêu...", 0.07, 14.0)
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









