import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

URL = "https://www.instagram.com/"

def verileri_al():
    kullanici_adi = kullanici_entry.get()
    son_url = URL + kullanici_adi

    request = Request(son_url, headers={"User-Agent": "Mozilla/5.0"})
    html_verisi = urlopen(request).read()

    soup = BeautifulSoup(html_verisi, "html.parser")
    try:
        veri = soup.find("meta", property="og:description").attrs["content"]
        veri = veri.split("-")[0]
        veri = veri.split(",")

        takipci_label.config(text="Takipçi sayısı: " + veri[0].strip())
        takip_edilen_label.config(text="Takip edilen sayısı: " + veri[1].strip())
        gonderi_label.config(text="Gönderi sayısı: " + veri[2].strip())

        # Profil açıklamasını kontrol et
        bio_section = soup.find("meta", property="og:title")
        if bio_section:
            bio_text = bio_section.attrs["content"]
            email_match = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', bio_text)
            if email_match:
                email_label.config(text="E-posta: " + email_match[0])
            else:
                email_label.config(text="E-posta bulunamadı.")
        else:
            email_label.config(text="Profil açıklaması bulunamadı.")

    except Exception as e:
        hata_label.config(text="Hata: " + str(e))

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Instagram Bilgi Çekici")

# Kullanıcı adı giriş alanı
kullanici_label = tk.Label(root, text="Kullanıcı Adı:")
kullanici_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

kullanici_entry = tk.Entry(root)
kullanici_entry.grid(row=0, column=1, padx=10, pady=10)

# Bilgi çek butonu
cek_button = tk.Button(root, text="Bilgileri Çek", command=verileri_al)
cek_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sonuç etiketleri
takipci_label = tk.Label(root, text="")
takipci_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

takip_edilen_label = tk.Label(root, text="")
takip_edilen_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

gonderi_label = tk.Label(root, text="")
gonderi_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

email_label = tk.Label(root, text="")
email_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

hata_label = tk.Label(root, text="")
hata_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()
