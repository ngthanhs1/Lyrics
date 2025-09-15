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
        ("▶ Đường xa lá rơi đón mùa thu", 0.07, 0.5),
        ("♫ Nắng âm áp nhạc ru…", 0.2, 1.2),
        ("  🩶 Nhớ em đếm từng giờ", 0.08, 2.0),
        ("\t\t\t dù trong giấc mơ", 0.2, 2.8),
        ("♪ Vờ như chẳng nhìn thấy một ai", 0.09, 4.3),
        ("𝄫 Chỉ có mỗi mình em", 0.08, 5.0),
        ("𝄞 Rồi dạo bước", 0.08, 5.7),
        ("\t♭ tay nắm thẹn thùng         ", 0.08, 6.3),
        ("\t\t♮ trời mây mỉm cười", 0.2, 7.0),
        ("🎧 Tình yêu tới đôi lúc hằng đêm", 0.08, 11.0),
        ("  ♪ Ánh trăng đến mà xem", 0.2, 12.0),
        ("  ♪ Phải chăng cứ hờn ghen", 0.09, 13.0),
        ("\t\t\t là ta đã yêu💕", 0.2, 13.8),
        ("  Đừng cười với bất cứ 1 ai", 0.09, 15.0),
        ("  Dẫu anh biết là sai", 0.09, 16.0),
        ("♫ Ngại ngùng anh chỉ muốn ", 0.15, 17.0),
        ("  🎼 Thể hiện tình yêu to lớn...", 0.1, 18.0)
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

