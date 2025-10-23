# Wordle-App

Đây là một bản clone của trò chơi Wordle được viết bằng ngôn ngữ Python, với sự hỗ trọ của thư vện Pygame.

##Introduction
Project này mô phỏng lại trò choi Wordle, người chơi phải đoán đúng từ trong 6 lượt chơi. Mục tiêu của project nhằm nâng cao khả năng lập trình và làm quen với ngôn ngữ Python.

Project được code và run trên VStudio Code

##Implement
###1. Download VSCode
Link hướng dẫn và download tại đây: https://code.visualstudio.com/download 
###2. Implement libraries
- Mở terminal trên VSCode, chạy câu lệnh sau để cài đặt các thư viện cần thiết:
pip install -r requirements.txt
- Sau đó chạy game: python main.py
###3. Usage
- Dùng bàn phím để nhập từ
- Nhấn 'Enter' để kiểm tra từ
- Nếu nhập sai, game sẽ không nhận từ, phải xóa từ đó và nhập lại từ mới
- Màu **xanh lá**: có chữ cái, đúng vị trí
- Màu **vàng**: có chữ cái, sai vị trí
- Màu **xám**: không có trong từ

##Công nghệ sử dụng
- 🐍 Python 3.13
- 🎮 Pygame
- 💾 txt (lưu danh sách từ)

##Cấu trúc thư mục
Wordle 
|
|--CodeSource
|  |--wordle.py
|  |--main.py
|  |--wordList.txt
|--requirements.txt
|--README.md
|--Report.pdf
