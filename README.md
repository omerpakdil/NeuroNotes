# NeuroNotes  
**AI-Powered Lecture Summarizer & Mind Map Generator for iOS**  

---

## 📌 Proje Açıklaması  
Bu iOS uygulaması, kullanıcıların sesli ders/kayıtlarını yükleyerek **AI destekli özetler** ve **interaktif mind map'ler** oluşturmasını sağlar. PDF/PPT export özelliğiyle notları paylaşılabilir hale getirir.

---

## 🛠️ Teknoloji Stack'i  
| Kategori       | Teknolojiler                          |
|----------------|---------------------------------------|
| **Frontend**   | React Native, React Flow, Expo        |
| **Backend**    | Python (Flask), OpenAI API            |
| **Veritabanı** | Firebase (ücretsiz tier)              |
| **API'ler**    | Whisper (transkripsiyon), GPT-4       |
| **Ödeme**      | RevenueCat (In-App Purchase)          |
| **Deploy**     | App Store, Firebase Hosting           |

---

### **Para Kazanma Modeli (In-App Purchase):**

- **Freemium Model:**

- **Ücretsiz Özellikler:**
  - Haftalık 2 özetleme (max 15dk)
  - Temel mind map düzenleme
  - Watermark ile export

- **Premium Özellikleri ($9.99/ay veya $79.99/yıl):**
  - Sınırsız özet & süre
  - Özel temalar ve şablonlar
  - Watermark'sız export
  - Öncelikli destek

---

### **Rakiplerden Farkı:**

- **Notion/Otter.ai'den Farkı:**
  - Sadece özet değil, **görsel beyin haritası** ile bilgiyi organize etme
  - Öğrenciler ve eğitmenler için "bilgiyi görselleştirme" odaklı
  - iOS native deneyim ve iCloud entegrasyonu
  - AirDrop ile kolay paylaşım

---

### **Pazarlama Stratejisi:**

1. **Hedef Kitle:**
  - iOS kullanan üniversite öğrencileri
  - iPad kullanan eğitmenler
  - Online kurs içerik üreticileri

2. **Taktikler:**
  - App Store Optimization (ASO)
  - Apple Search Ads kampanyaları
  - TikTok/Instagram Reels demo videoları
  - Eğitim influencer'ları ile işbirliği

---

## 📱 iOS Onboarding Akışı

### Ekran 1: Hoş Geldin
- Modern iOS tasarımı
- Uygulama değer önerisi
- "Devam Et" butonu
- Apple ile Giriş seçeneği

### Ekran 2: Özellik Tanıtımı
1. **Kolay Ses Kaydı**
   - Canlı kayıt veya dosya yükleme
   - iOS ses API entegrasyonu
   
2. **Akıllı Mind Map**
   - Otomatik düzenleme
   - iOS gesture desteği
   
3. **Hızlı Paylaşım**
   - AirDrop desteği
   - iCloud entegrasyonu

### Ekran 3: Premium Teklifi
- Ücretsiz 3-gün deneme
- Yıllık plan öne çıkarılmış (%45 indirimli)
- "Restore Purchase" seçeneği
- Gizlilik politikası & Kullanım şartları

---

## 📂 Proje Yapısı  
```bash
NeuroNotes/
├── ios/                     # iOS native kodu
│   ├── Podfile
│   └── NeuroNotes.xcworkspace
├── backend/                 # Python backend
│   ├── app.py              # Flask server
│   ├── modules/
│   │   ├── auth/          # Kimlik doğrulama
│   │   ├── transcription/ # Ses işleme
│   │   ├── mindmap/      # Mind map oluşturma
│   │   └── subscription/ # RevenueCat entegrasyonu
│   └── requirements.txt
├── frontend/               # React Native uygulaması
│   ├── src/
│   │   ├── screens/       # Ekranlar
│   │   │   ├── onboarding/
│   │   │   │   ├── Welcome.tsx
│   │   │   │   ├── Features.tsx
│   │   │   │   └── PremiumOffer.tsx
│   │   │   ├── Home.tsx
│   │   │   └── MindMap.tsx
│   │   ├── components/    # Tekrar kullanılabilir bileşenler
│   │   ├── services/     # API ve RevenueCat servisleri
│   │   └── utils/        # Yardımcı fonksiyonlar
│   └── App.tsx
└── README.md

```

## 🚀 Kurulum Adımları

1. **Gereksinimler**
   - Node.js ≥18.x
   - Python ≥3.9
   - Xcode ≥14
   - CocoaPods
   - OpenAI API Anahtarı
   - RevenueCat Hesabı

2. **Backend Kurulumu**
```bash
# 1. Repoyu klonla
git clone https://github.com/[KULLANICI_ADIN]/NeuroNotes.git
cd NeuroNotes/backend

# 2. Sanal ortam oluştur ve aktifleştir
python -m venv venv
source venv/bin/activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. .env dosyası oluştur
echo "OPENAI_API_KEY=sk-xxx" > .env
echo "REVENUECAT_API_KEY=xxx" >> .env

# 5. Flask server'ı başlat
python app.py
```

3. **iOS Kurulumu**
```bash
cd ../frontend

# 1. Bağımlılıkları yükle
npm install

# 2. iOS bağımlılıklarını yükle
cd ios && pod install && cd ..

# 3. iOS simülatörde başlat
npx react-native run-ios
```

4. **RevenueCat Kurulumu**
   - RevenueCat dashboard'da uygulama oluştur
   - App Store Connect'te ürünleri tanımla
   - API anahtarlarını .env dosyasına ekle
   - Test kullanıcıları tanımla

---

### **Deployment Kontrol Listesi:**

1. **App Store Hazırlık:**
   - App Store Connect hesabı
   - Uygulama ikonu ve ekran görüntüleri
   - App Privacy detayları
   - TestFlight beta testi

2. **Backend Deployment:**
   - Firebase hosting kurulumu
   - SSL sertifikası
   - Environment değişkenleri
   - Monitoring araçları

3. **RevenueCat Kontrolleri:**
   - Ürün ID'leri doğrulama
   - Sandbox testi
   - Webhook kurulumu
   - Analytics takibi
