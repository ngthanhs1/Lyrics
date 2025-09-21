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
        ("🎧 Nói thế thôi chứ", 0.089, 0.5),  
        ("Flop quá thì cứ ghi tên anh vào!", 0.074, 1.24),
        ("Bao lâu bao lâu bao nhiêu lâu rồi...", 0.059, 5.1),
        ("Tên anh nằm trên đỉnh cao bao nhiêu lâu rồi", 0.068, 3.81),
        ("Tham, sân si bao nhiêu lâu rồi", 0.069, 4.5),
        ("Đứng từ xa nhìn ngắm thành công của anh bao nhiêu lâu rồi", 0.044, 6.3),
        ("Đâm sau lưng anh", 0.07, 15.1),
        ("Đúng là lũ trẻ ranh", 0.053, 1.6),
        ("Chẳng có gì hết", 0.057, 0.27),
        ("Chỉ thế là nhanh", 0.058, 0.47),
        ("Bước hết vào đây", 0.074, 5.1),
        ("Tấp hết vào đây ", 0.064, 1.0),
        ("Làm sao cưng ngăn được ý trời đây", 0.069, 4.9),
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









