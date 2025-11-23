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
        ("🎧Anh có nỗi sợ", 0.108, 0.5),
        ("Sợ ta mất nhau", 0.148, 1.2),
        ("Tình yêu bắt đầu", 0.09, 3.0),
        ("Không phải để tìm nỗi đau", 0.12, 3.7),
        ("Sợ giây phút này", 0.12, 4.0),
        ("Chẳng còn", 0.04, 1.0),
        ("thấy em bên anh về sau", 0.176, 8.1),
        ("Nhiều khi nóng giận", 0.1, 16.1),
        ("Nhiều khi cãi nhau       ", 0.13, 8.9),
        ("Để rồi cuối cùng", 0.12, 8.7),
        ("Ta lại trở về với nhau", 0.1, 11.0),
        ("Đôi tay này cần ", 0.114, 11.0),
        ("nâng niu", 0.17, 12.0),
        ("Vì em là người anh yêu...", 0.18, 29.0)
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









