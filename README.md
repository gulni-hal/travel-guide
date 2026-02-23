#  Travel Guide RAG Chatbot (Roma)
Bu proje gelecek Roma seyahatime hazırlık olarak tasarlanmış bir RAG (Retrieval-Augmented Generation) temelli chatbottur. Chatbot sorulara, seyahatimi planlarken oldukça kullandığım bir blog websitesini scrape edilen gerçek veriler ile cevap verir.
Sistem Ollama aracılığıyla local ortamda çalışmaktadır.

---
## Proje Çalışma Mantığı
Proje 3 aşamadan oluşmaktadır:
1. Web Scraping
   * [Roma içeriğinin çekildiği blog websitesi](https://www.bizevdeyokuz.com/roma).
   * Blogun datalarını scrape edilirken linklerin, reklam içeriklerinin ve TIKLAYIN yazılarının gözükmemesi sağlandı.
   * BeautifulSoup, requests ve regex kütüphaneleri kullanıldı.
2. Embedding ve Vector Database oluşturma
   * Scrape edilen içerik LangChain Document nesnesine dönüştürülür ve chunklara ayrıldı.
   * Ollama embeddings model mxbai-embed-large kullanıldı ve her chunk yüksek boyutlu bir vektöre dönüştürüldü. Vector Database oluşturuldu.
   * Retriever kullanılarak en alakalı 3 chunk ın alınması sağlandı.
3. Retrieval-Augmented Generation (RAG) Chatbot
   * LLM olarak llama3.2 kullanıldı ve hallucination azalması hedeflenerek temperature 0 olarak ayarlandı.
   * Chatbot un sorulara sadece scrape edilen içeriğe dayalı cevap vermesi sağlandı.
  
---
## Sistem Mimarisi
Kullanıcı Sorusu

↓

Embedding (Ollama)

↓

Chroma Vector Database

↓

Retriever (Top-k benzerlik araması)

↓

Prompt Template

↓

LLM (Llama 3.2 - Ollama)

↓

Yanıt

---
## Kurulum
Projenin Templateni ve scrape edilen websitesini değiştirip kendi chatbotunuzu tasarlayabilirsiniz.
### 1. Projeyi Klonlayın

```
git clone <repo-link>
cd travel-guide
```
### 2. Virtual Environment Oluşturun
Proje en iyi Python 3.11 ile çalıştığını göz önünde bulundurunuz. 

```
py -3.11 -m venv venv
venv\Scripts\activate
```
### 3. Gerekli Bağımlılıkları ve Ollama Modellerini Install Edin
### 4. Çalıştırın
```
python main.py
```
---
## Çalışma Örnekleri 
Bazı sorulara verilen cevapların terminal çıktıları:

<img width="1564" height="160" alt="Screenshot 2026-02-17 203504" src="https://github.com/user-attachments/assets/ac1c845d-2448-436b-b3a7-41663459cfb1" />
<img width="1608" height="329" alt="Screenshot 2026-02-17 203621" src="https://github.com/user-attachments/assets/5500bb80-a24b-4fe0-baee-d053c05817d3" />

