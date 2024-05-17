# Coconut Dev
<img src= "Assets/Design/logo.png" style= width:40%> 

# Balap Kelereng

"Balap Kelereng" adalah game endless runner gratis yang menampilkan karakter yang menggigit sebuah sendok dan berisikan kelereng yang secara otomatis mulai berlari. Pemain dapat mengendalikan karakter ini dengan menekan tombol atas/ space untuk melompat dan bawah untuk menunduk. Tujuannya adalah menghindari rintangan-rintangan seperti pesawat dan drum oli untuk bertahan hidup selama mungkin.

## Modul yang di gunakan
Modul - modul yang di gunakan dalam game ini untuk mempermudah pengembangan game Balap Kelereng:

1. **pygame**: Modul ini digunakan untuk membuat game dan aplikasi multimedia interaktif menggunakan Python. Ini menyediakan akses ke fungsi-fungsi yang memungkinkan Anda mengontrol grafika, suara, dan input pengguna.
   ```bash
   import pygame
   ```
   - Contoh Penggunaan:
      ```bash
      #...
      pygame.init()

      judul = "Balap Kelereng"
      logo_ccb = pygame.image.load(os.path.join("Assets/Design","logo.png"))

      pygame.display.set_caption(judul)
      pygame.display.set_icon(logo_ccb)

      pygame.mixer.music.load("Assets/Music/backsound.mp3")
      pygame.mixer.music.set_volume(0.3)
      pygame.mixer.music.play()
      pygame.mixer.music.play(-1)
      #...
      ```

2. **os**: Modul ini memberikan fungsi-fungsi untuk berinteraksi dengan sistem operasi, seperti mengelola file dan direktori, mengatur variabel lingkungan, dan mengeksekusi perintah shell.
   ```bash
   import os
   ```
   - Contoh Penggunaan:
      ```bash
      #...
      RUN = [pygame.image.load(os.path.join("Assets/Design", "lanang1.png")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Design", "lanang2.png")).convert_alpha()]

      JUMP = pygame.image.load(os.path.join("Assets/Design", "lanang1.png")).convert_alpha()

      DUCK = [pygame.image.load(os.path.join("Assets/Design", "lanang_duck1.png")).convert_alpha(),
            pygame.image.load(os.path.join("Assets/Design", "lanang_duck2.png")).convert_alpha()]
      #...
      ```

3. **random**: Modul ini berisi fungsi-fungsi untuk menghasilkan angka acak atau memanipulasi urutan secara acak. Ini sangat berguna dalam pengembangan game, simulasi, dan aplikasi lainnya yang memerlukan elemen kejutan.
   ```bash
   import random
   ```
   - Contoh Penggunaan:
      ```bash
      #...
      class Drum_Bergerak(Obstacle):
         def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 445
         def update(self):
            self.rect.x -= game_speed * 2  
            if self.rect.x < -self.rect.width:
                  obstacles.pop()


      class Drum_Diam(Obstacle):
         def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 420
      #...
      ```

4. **sys**: Modul ini memberikan akses ke berbagai fungsi dan variabel yang terkait dengan interpretasi Python itu sendiri. Ini sering digunakan untuk mengakses argumen baris perintah, mengatur jalur pencarian, dan mengatur perilaku program saat berinteraksi dengan sistem.
   ```bash
   import sys
   ```
   - Contoh Penggunaan:
      ```bash
      #...
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAINMENU_BACK.checkForInput(MAINMENU_MOUSE_POS):
                    main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                main()
      #...
      ```

5. **json**: Modul ini menyediakan fungsionalitas untuk membaca dan menulis data dalam format JSON (JavaScript Object Notation), yang merupakan format pertukaran data yang umum digunakan dalam aplikasi web dan lainnya. Dengan modul ini, Anda dapat dengan mudah mengonversi struktur data Python ke format JSON dan sebaliknya.
   ```bash
   import json
   ```
   - Contoh Penggunaan:
      ```bash
      #...
      def load_highscore():
         try:
            with open("highscore.json", "r") as file:
                  data = json.load(file)
                  if isinstance(data, dict):
                     return data.get("highscore", 0)
                  else:
                     return 0
         except (FileNotFoundError, json.JSONDecodeError):
            return 0

      def save_highscore(highscore):
         with open("highscore.json", "w") as file:
            json.dump({"highscore": highscore}, file)

      highscore = load_highscore()
      #...
      ```

## Bagaimana cara memainkanya?
1. **Unduh Game:**
   - Download zip clone di terminal linux, mac os, atau git bash melalui link: 
      ```bash
      git clone https://github.com/kevinnaufaldany/Tubes-PBO-Balap-Kelereng.git 
      ```
   - Download zip secara manual melalui link: [Balap-Kelereng.zip](https://github.com/kevinnaufaldany/Tubes-PBO-Balap-Kelereng/archive/refs/heads/main.zip)

2. **Persiapan Lingkungan Pengembangan:**
   - Pastikan Anda telah menginstal Visual Studio Code (VSCode) di komputer Anda. Jika belum, Anda dapat mengunduhnya dari situs resmi [Visual Studio Code](https://code.visualstudio.com/).
   - Selain itu, Anda perlu menginstal Python. Anda dapat mengunduh versi terbaru Python dari situs resmi [Python](https://www.python.org/downloads/).

3. **Instalasi Pygame:**
   - Game ini dibuat menggunakan Pygame, sebuah pustaka Python untuk pengembangan game. Untuk menginstalnya, buka terminal atau command prompt, kemudian jalankan perintah berikut:
      ```bash
      pip install pygame
      ```

4. **Ekstrak File dan Buka di VSCode:**
   - Ekstrak file yang telah diunduh dalam format `zip`.
   - Buka folder game tersebut menggunakan `Visual Studio Code`.

5. **Menjalankan Game:**
   - Untuk menjalankan game, Anda perlu membuka folder program dan anda dapat menjalankan/ runing di file `main.py`.
   - Di terminal VSCode untuk windows, jalankan perintah berikut:
      ```bash
      python main.py
      ```
   - Di terminal VSCode untuk linux atau mac os, jalankan perintah berikut:
     ```bash
     python3 main.py
     ```

6. **Informasi Tambahan:**
   - Pastikan bahwa semua yang di perlukan sudah terinstal dengan benar.
   - Jika terjadi masalah saat menjalankan game, periksa kembali apakah ada kesalahan dalam instalasi atau konfigurasi lingkungan pengembangan Anda.

*Selamat Bermain!*

## Author

| Name                      | NIM       | Role      | link Github                                               | 
| ------------------------- | --------- | --------- | --------------------------------------------------------- |
| Kevin Naufal Dany  | 122140222 | Project Leader & Programer | [@kevinnaufaldany](https://www.github.com/kevinnaufaldany)|
| Khoirul Rijal Wicaksono | 122140234 | Programer | [@kevinnaufaldany](https://www.github.com/kevinnaufaldany)|
| Elkana Jnr Manullang | 122140168 | Programer | [@elkanajnrmanullang](https://www.github.com/elkanajnrmanullang)|
| Rayhan Fadel Irwanto | 122140236 | Programer | [@kevinnaufaldany](https://www.github.com/kevinnaufaldany)|
| Roy Vanzeus Maulana  | 122140238 | Designer | [@kevinnaufaldany](https://www.github.com/kevinnaufaldany)|
| Ferdinand Yehezkiel Hutapea | 122140233 | Designer | [@kevinnaufaldany](https://www.github.com/kevinnaufaldany)|



