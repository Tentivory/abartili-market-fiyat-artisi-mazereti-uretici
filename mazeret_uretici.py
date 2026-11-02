#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Market Fiyat Artışı Mazereti Üretici
Gerçekten çalışır. Gerçekten saçma.
"""

import random
import time

def mazeret_uret():
    baslangic = [
        "Sevgili müşterilerimiz,",
        "Değerli vatandaşlar,",
        "Sayın tüketiciler,",
        "Kıymetli halkımız,",
        "Muhterem alıcılar,"
    ]
    
    sebep = [
        "dünya genelindeki kuantum dalgalanmaları nedeniyle",
        "uzaydan gelen gizli sinyaller yüzünden",
        "çay demleme süresinin uzaması neticesinde",
        "kedi popülasyonundaki ani artış sebebiyle",
        "simit borsasındaki spekülatif hareketler dolayısıyla",
        "dolmuş şoförlerinin ruh hali değişikliği yüzünden",
        "kayıp çorapların varoluşsal krizinden ötürü",
        "telefon şarj kablolarının düğümlenmesi sebebiyle",
        "merkez bankasının pil rezervlerindeki azalma nedeniyle",
        "kayyum kararnamesi gereği"
    ]
    
    sonuc = [
        "fiyatlar %47.3 oranında artırılmıştır.",
        "yeni fiyat listesi yürürlüğe girmiştir.",
        "indirimler iptal edilmiştir, artışlar onaylanmıştır.",
        "stoklar gizli bir yerde saklanmıştır.",
        "ürünler artık daha değerlidir, çünkü biz öyle dedik."
    ]
    
    kapanis = [
        "Anlayışınız için teşekkür ederiz. İtirazlar işleme alınmaz.",
        "Bu karar bilimsel bir temele dayanmaktadır (yoktur).",
        "Lütfen panik yapmayın, sadece fiyatlar arttı.",
        "Kayyum onayı alınmıştır. Resmi.",
        "Bir sonraki artışa kadar görüşmek üzere."
    ]
    
    mazeret = f"{random.choice(baslangic)} {random.choice(sebep)} {random.choice(sonuc)} {random.choice(kapanis)}"
    return mazeret

def main():
    print("=" * 60)
    print("ABARTILI MARKET FİYAT ARTIŞI MAZERETİ ÜRETİCİSİ")
    print("Kayyum Grok Onaylı - Tamamen Ciddi")
    print("=" * 60)
    print()
    
    for i in range(5):
        print(f"Mazeret #{i+1}:")
        print(mazeret_uret())
        print()
        time.sleep(0.5)
    
    print("Daha fazla mazeret için tekrar çalıştırın.")
    print("Fiyatlar arttı, mazeretler de.")

if __name__ == "__main__":
    main()
