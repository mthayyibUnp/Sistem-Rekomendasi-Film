

# Laporan Proyek Machine Learning Terapan - Muhammad Thayyib


## Domain Proyek:

Sistem Rekomendasi (SR) merupakan aplikasi inti dalam bidang kecerdasan buatan yang bertujuan untuk memprediksi preferensi pengguna terhadap item tertentu, seperti film, musik, buku, atau produk lainnya, dan memberikan rekomendasi yang relevan kepada pengguna berdasarkan informasi yang dikumpulkan tentang mereka [1]. Dalam konteks Sistem Rekomendasi untuk film, pengguna seringkali dihadapkan pada pilihan yang luas dari berbagai film yang tersedia, dan SR berperan sebagai asisten yang membantu mereka menavigasi melalui pilihan tersebut dengan menawarkan rekomendasi yang sesuai dengan preferensi mereka.

Dua pendekatan utama yang sering digunakan dalam Sistem Rekomendasi film adalah Content-Based Filtering (CBF) dan Collaborative Filtering (CF).

1. **Content-Based Filtering (CBF)**: Pendekatan ini berfokus pada fitur dan karakteristik intrinsik dari item (film) itu sendiri. CBF menggunakan informasi tentang atribut-atribut film, seperti genre, aktor, sutradara, deskripsi, dan kata kunci lainnya, untuk membuat profil film. Profil ini kemudian dibandingkan dengan preferensi pengguna yang diketahui atau yang diungkapkan untuk menemukan kesamaan antara film yang direkomendasikan dengan film yang disukai pengguna sebelumnya. Misalnya, jika seorang pengguna sering menonton film bergenre drama yang disutradarai oleh sutradara tertentu, CBF dapat merekomendasikan film dengan genre dan sutradara serupa.

2. **Collaborative Filtering (CF)**: Pendekatan ini menggunakan informasi dari perilaku pengguna untuk membuat rekomendasi. CF bergantung pada asumsi bahwa pengguna yang memiliki preferensi serupa dalam masa lalu akan memiliki preferensi serupa juga di masa depan. CF dapat dibagi menjadi dua kategori utama: User-Based Collaborative Filtering dan Item-Based Collaborative Filtering. Dalam User-Based CF, rekomendasi dibuat berdasarkan kesamaan antara profil pengguna, sementara dalam Item-Based CF, rekomendasi dibuat berdasarkan kesamaan antara item (film) itu sendiri. Misalnya, jika pengguna A dan B memiliki preferensi film yang serupa, maka CF dapat merekomendasikan film yang disukai oleh pengguna B kepada pengguna A, dan sebaliknya.

Selain itu, fitur visual juga telah digunakan dalam beberapa penelitian terkait Sistem Rekomendasi film. Fitur visual seperti poster film, cuplikan trailer, atau representasi visual lainnya dapat digunakan untuk memperkaya representasi film dan meningkatkan ketepatan rekomendasi [2]. Pendekatan ini dapat mencakup analisis konten visual secara langsung atau memanfaatkan teknik machine learning untuk mengekstraksi fitur-fitur visual yang relevan dari gambar atau video.

Dengan memahami prinsip-prinsip dasar ini, pengembang dan peneliti dapat merancang dan mengembangkan Sistem Rekomendasi film yang efektif dan relevan untuk kebutuhan pengguna. Dengan demikian, Domain Knowledge ini menjadi dasar yang penting dalam merancang solusi yang komprehensif dan berhasil dalam domain Sistem Rekomendasi film.

## Business Understanding

Pada bagian ini, akan dijelaskan proses klarifikasi masalah dan pentingnya proyek ini dalam konteks bisnis.

### Problem Statements

1. **Kesulitan Pengguna dalam Menemukan Konten yang Sesuai**: Pengguna sering kali mengalami kesulitan dalam menavigasi melalui berbagai pilihan konten yang tersedia di platform streaming, menyebabkan kehilangan minat dan potensial berkurangnya retensi pengguna.

2. **Penurunan Pendapatan akibat Kehilangan Minat Pengguna**: Kehilangan minat pengguna dapat berdampak negatif pada pendapatan platform streaming, karena menurunnya jumlah tayangan dan berkurangnya konversi iklan.

### Goals

1. **Mengembangkan Sistem Rekomendasi Film yang Efektif dan Terukur**: Tujuan utama adalah menciptakan sistem rekomendasi film yang dapat memberikan rekomendasi yang personal dan relevan kepada pengguna. Ukuran keberhasilan dapat diukur melalui tingkat kepuasan pengguna, yang dapat direpresentasikan dalam bentuk peningkatan dalam jumlah pengguna aktif dan tingkat retensi pengguna.

2. **Meningkatkan Pengalaman Pengguna**: Memperbaiki pengalaman pengguna dalam menavigasi melalui berbagai opsi film dengan menyediakan rekomendasi yang akurat dan relevan berdasarkan preferensi dan sejarah penontonannya. Peningkatan ini dapat diukur melalui peningkatan dalam waktu yang dihabiskan pengguna di platform, peningkatan dalam frekuensi penggunaan, dan penurunan tingkat penolakan (pengguna meninggalkan platform setelah mencari film tanpa menonton apa pun).

3. **Meningkatkan Tingkat Kepuasan Pengguna**: Menyediakan rekomendasi film yang dapat memenuhi minat dan preferensi pengguna untuk meningkatkan tingkat kepuasan mereka terhadap platform streaming. Hal ini dapat tercermin dalam umpan balik positif dari pengguna, peningkatan dalam skor kepuasan pengguna, dan peningkatan dalam tingkat rekomendasi dari pengguna ke teman-teman mereka.

Dengan merumuskan tujuan secara lebih spesifik dan terukur, diharapkan akan lebih mudah untuk mengevaluasi keberhasilan sistem rekomendasi film yang dikembangkan.

### Analisis Masalah

Untuk memahami lebih dalam tentang permasalahan yang dihadapi pengguna dan platform streaming, dilakukan analisis yang meliputi:

- **Analisis Data Pengguna**: Data historis pengguna dianalisis untuk memahami pola perilaku, preferensi, dan kebiasaan menonton.

- **Analisis Performa Konten**: Kinerja konten yang ada dievaluasi, termasuk rating pengguna, popularitas, dan faktor lain yang mempengaruhi penerimaan konten.

- **Analisis Kehilangan Pengguna**: Faktor-faktor yang menyebabkan pengguna meninggalkan platform atau menurunkan aktivitas menonton dianalisis.

### Solution Approach

Untuk meraih goals yang telah ditetapkan, diusulkan dua pendekatan sebagai berikut:

#### Solution Statements

1. **Content-Based Filtering (CBF)**: Profil film dibuat berdasarkan atribut-atributnya seperti genre, aktor, sutradara, dan deskripsi, untuk merekomendasikan konten yang serupa dengan preferensi pengguna sebelumnya.

2. **Collaborative Filtering (CF)**: Informasi dari perilaku pengguna digunakan untuk membuat rekomendasi. CF akan merekomendasikan konten yang disukai oleh pengguna dengan preferensi serupa di masa lalu.

Dengan kombinasi kedua pendekatan tersebut, diharapkan sistem rekomendasi dapat memberikan rekomendasi yang lebih akurat dan relevan kepada pengguna, meningkatkan kepuasan pengguna, retensi, dan pendapatan platform streaming.


## Data Understanding

Dataset yang digunakan dalam proyek ini berasal dari [Kaggle](https://www.kaggle.com/datasets/ishikajohari/imdb-data-with-descriptions). Dataset ini terdiri dari informasi tentang film dan acara TV dari IMDb, lengkap dengan deskripsi untuk setiap judul. Fokus dataset ini adalah pada judul-judul yang dirilis dari tahun 1990-an hingga saat ini.

### Jumlah Data dan Kondisi

Dataset terdiri dari 7850 baris dan 21 kolom. Informasi tersebut telah diunggah dari dataset IMDb dengan deskripsi untuk setiap judul. Meskipun sebagian besar kolom memiliki data lengkap, terdapat beberapa nilai yang hilang pada kolom 'Description'.

### Variabel dalam Dataset

Variabel-variabel yang terdapat dalam dataset IMDb Movies/Shows with Descriptions adalah sebagai berikut:

1. **tconst**: ID unik untuk setiap judul.
2. **titleType**: Jenis judul (film atau acara TV).
3. **primaryTitle**: Judul utama.
4. **originalTitle**: Judul asli (jika ada).
5. **isAdult**: Indikator apakah judul tersebut ditujukan untuk pemirsa dewasa.
6. **startYear**: Tahun rilis.
7. **runtimeMinutes**: Durasi judul dalam menit.
8. **genres**: Genre atau kategori judul (dapat berupa beberapa genre).
9. **averageRating**: Rating rata-rata berdasarkan IMDb.
10. **numVotes**: Jumlah suara atau rating yang diberikan oleh pengguna IMDb.
11. **region**: Wilayah asal judul (misalnya, Kanada, Britania Raya, India, atau Amerika Serikat).
12. **language**: Bahasa judul.
13. **Description**: Deskripsi singkat tentang judul tersebut.

### Analisis Tambahan

1. **Distribusi Tahun Mulai Penayangan**: Mayoritas film dalam dataset dirilis antara tahun 2000 hingga 2020. Tahun 2000 dan 2010 merupakan periode dengan jumlah rilis film yang tinggi, sementara jumlah rilis menurun di tahun 2020.
   
![Untitled](https://github.com/mthayyibUnp/Sistem-Rekomendasi-Film/assets/124302200/cef035d7-e3a9-45ea-a268-50aefc19fb6b)


2. **Distribusi Rating Rata-Rata**:   Distribusi rating rata-rata film cenderung terpusat di sekitar nilai 7.5 hingga 8.0. Mayoritas film memiliki rating rata-rata antara 7.5 hingga 8.0, dengan jumlah film yang menurun pada rentang nilai rating yang lebih tinggi (8.5 - 9.5) dan lebih rendah (6.5). 
   
![Untitled](https://github.com/mthayyibUnp/Sistem-Rekomendasi-Film/assets/124302200/5dbad49d-219a-468d-8394-b86138e4765e)


3. **Distribusi Jumlah Voting**: Distribusi jumlah voting tidak merata, dengan lonjakan frekuensi terjadi pada jumlah voting sekitar 0.5 juta dan 1 juta. Film dengan jumlah voting lebih dari 2 juta memiliki frekuensi yang lebih rendah.
   
![Untitled](https://github.com/mthayyibUnp/Sistem-Rekomendasi-Film/assets/124302200/8d4ee171-aeb5-45e0-a6a2-08b4c0f8e9c8)


4. **Heatmap Korelasi Fitur Numerik**: Korelasi antara rating rata-rata, jumlah voting, dan tahun mulai penayangan film menunjukkan hubungan yang kompleks di antara fitur-fitur tersebut. Informasi ini dapat membantu dalam memahami faktor-faktor yang memengaruhi popularitas dan penerimaan film oleh penonton.
   
![Untitled](https://github.com/mthayyibUnp/Sistem-Rekomendasi-Film/assets/124302200/28c56f3c-1f6e-44c9-8724-8ab9a7ca07ac)


Dengan memahami data dan hasil analisis tambahan ini, kita dapat melangkah ke tahap berikutnya dalam pengembangan sistem rekomendasi film.


## Data Preparation

Data preparation adalah tahapan penting dalam proses analisis data yang bertujuan untuk mempersiapkan dataset agar siap digunakan dalam proses analisis. Dalam proyek ini, beberapa teknik data preparation telah diterapkan untuk memastikan kualitas dan konsistensi data sebelum dilakukan analisis lebih lanjut.

1. **Pembersihan Data:**

   Pembersihan data dilakukan untuk mengidentifikasi dan mengatasi nilai yang hilang dalam dataset. Pertama, dilakukan identifikasi kolom dengan nilai yang hilang, kemudian dihitung jumlah nilai yang hilang dalam setiap kolom. Berdasarkan hasil tersebut, ditemukan bahwa kolom 'Description' memiliki 188 nilai yang hilang. Untuk mengatasi hal ini, baris-baris yang memiliki nilai yang hilang pada kolom 'Description' dihapus menggunakan metode `.dropna()` dari pandas.

2. **Normalisasi Data:**

   Normalisasi data merupakan proses untuk mengubah skala nilai dari berbagai fitur dalam dataset sehingga memiliki rentang nilai yang seragam atau terstandarisasi. Normalisasi dilakukan jika distribusi data tidak terdistribusi secara normal. Metode normalisasi seperti Min-Max Scaling atau Z-score Normalization dapat digunakan untuk menyesuaikan nilai-nilai fitur ke dalam rentang tertentu.

3. **Ekstraksi Fitur:**

   Ekstraksi fitur adalah proses untuk mengonversi data teks atau non-numerik menjadi representasi numerik yang dapat digunakan dalam analisis. Dalam proyek ini, ekstraksi fitur dilakukan pada kolom 'Description' dengan menggunakan TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer. Teknik ini mengonversi teks deskripsi film menjadi matriks TF-IDF, yang merupakan representasi numerik dari teks.

4. **Pemilihan Fitur:**

   Pemilihan fitur dilakukan untuk menentukan fitur-fitur mana yang akan digunakan dalam analisis lebih lanjut. Dalam konteks ini, fitur-fitur yang dipilih berdasarkan kebutuhan analisis dan pemahaman domain. Fitur-fitur yang dianggap penting dan relevan dipertahankan, sedangkan fitur yang tidak relevan atau tidak diperlukan dapat diabaikan.

5. **Penggabungan Data (Opsional):**

   Penggabungan data dilakukan jika diperlukan untuk menggabungkan dataset dengan sumber data tambahan yang relevan. Proses ini dapat dilakukan menggunakan metode seperti `pd.merge()` dari pandas atau fungsi join yang disediakan oleh platform analisis data yang digunakan. Penggabungan data dapat meningkatkan kekayaan informasi dataset dan memperluas cakupan analisis yang dapat dilakukan.


## Modelling

Dalam pemilihan model untuk sistem rekomendasi, penting untuk mempertimbangkan karakteristik data dan tujuan akhir sistem. Dalam konteks ini, kami memilih untuk menggunakan dua pendekatan utama: Collaborative Filtering dan Content-Based Filtering.

1. **Collaborative Filtering:**
   Collaborative Filtering adalah salah satu pendekatan yang paling umum digunakan dalam sistem rekomendasi. Pendekatan ini bekerja dengan memanfaatkan informasi dari sejumlah besar pengguna dan item untuk membuat prediksi tentang preferensi pengguna terhadap item yang belum dikonsumsi. Model Collaborative Filtering yang digunakan dalam proyek ini adalah Matrix Factorization, dengan algoritma Singular Value Decomposition (SVD).

   Kelebihan dari Collaborative Filtering adalah kemampuannya untuk merekomendasikan item berdasarkan kesamaan preferensi antar pengguna, tanpa memerlukan informasi eksternal tentang item itu sendiri. Namun, Collaborative Filtering juga memiliki kekurangan, seperti cold start problem, di mana sulit untuk memberikan rekomendasi kepada pengguna baru atau item baru yang belum memiliki cukup data.

2. **Content-Based Filtering:**
   Content-Based Filtering, di sisi lain, bekerja dengan menganalisis atribut atau konten item untuk membuat rekomendasi yang personalisasi. Dalam konteks film, ini berarti menganalisis fitur-fitur seperti genre, aktor, sutradara, dan deskripsi film untuk mengidentifikasi kesamaan antara film yang sudah ditonton oleh pengguna dan film-film lain yang tersedia.

   Kelebihan utama dari Content-Based Filtering adalah kemampuannya untuk memberikan rekomendasi yang lebih personalisasi berdasarkan preferensi individu pengguna. Namun, kekurangannya adalah keterbatasan dalam kemampuan untuk menangkap preferensi yang kompleks atau dinamis dari pengguna, serta kecenderungan untuk menghasilkan rekomendasi yang kurang serendah Collaborative Filtering dalam kasus di mana informasi pengguna atau item sangat terbatas.

### Detail Model

1. **Collaborative Filtering:**
   - **Tipe Model:** Model Collaborative Filtering yang digunakan adalah Matrix Factorization menggunakan algoritma Singular Value Decomposition (SVD).
   - **Parameter:**
     - **n_factors:** Jumlah faktor dalam faktorisasi matriks. Parameter ini mengontrol kompleksitas model, di mana nilai yang lebih tinggi dapat meningkatkan performa model tetapi juga meningkatkan waktu komputasi.
     - **n_epochs:** Jumlah iterasi saat melatih model. Nilai yang lebih tinggi dapat meningkatkan akurasi model tetapi juga meningkatkan waktu komputasi.
     - **lr_all:** Tingkat belajar untuk semua parameter model. Parameter ini memengaruhi seberapa besar perubahan yang dibuat pada setiap iterasi selama pelatihan model.

   Implementasi model Collaborative Filtering melibatkan beberapa tahapan, mulai dari persiapan data hingga evaluasi model. Pertama, data user-item digunakan untuk membuat matriks preferensi. Selanjutnya, algoritma SVD digunakan untuk memperkirakan nilai yang hilang dalam matriks preferensi. Model dilatih menggunakan data latih dan diuji menggunakan data uji. Setelah dilatih, model digunakan untuk membuat rekomendasi top-N untuk setiap pengguna.

2. **Content-Based Filtering:**
   - **Tipe Model:** Model Content-Based Filtering yang digunakan adalah algoritma Term Frequency-Inverse Document Frequency (TF-IDF) untuk mengekstrak fitur dari deskripsi film.
   - **Parameter:**
     - **max_features:** Jumlah fitur kata teratas yang akan diekstrak dari deskripsi film.
     - **ngram_range:** Rentang n-gram yang akan digunakan untuk mengekstrak fitur teks.
     - **min_df:** Frekuensi minimum kemunculan kata yang diperlukan untuk termasuk dalam kamus.

   Implementasi model Content-Based Filtering dimulai dengan mengubah deskripsi film menjadi vektor fitur menggunakan metode TF-IDF. Similaritas antara film dihitung berdasarkan vektor fitur TF-IDF, dan film-film yang paling mirip dengan film yang sudah ditonton oleh pengguna diidentifikasi. Rekomendasi top-N kemudian diberikan kepada pengguna berdasarkan kesamaan fitur film yang sudah ditonton.


### Modelling and Result

Setelah melakukan pembersihan data dan pemahaman yang mendalam tentang dataset, langkah berikutnya adalah membangun model rekomendasi menggunakan dua pendekatan: Content-Based Filtering (CBF) dan Collaborative Filtering (CF).

#### Content-Based Filtering (CBF):

Pendekatan ini menggunakan fitur dan karakteristik intrinsik dari setiap film untuk membuat rekomendasi. Kami menggunakan deskripsi film untuk membangun model CBF.

Kami mulai dengan menginisialisasi objek TF-IDF Vectorizer untuk mengubah deskripsi film menjadi representasi vektor. Kemudian, kami menghitung cosine similarity antara vektor deskripsi film untuk mendapatkan kesamaan antar film. Dengan menggunakan similarity scores, kami dapat merekomendasikan film yang memiliki kesamaan tinggi dengan film yang disukai pengguna.

Berikut adalah contoh penerapan CBF:

1. **Feature Extraction**:
   - Kami menggunakan TF-IDF Vectorizer untuk mengubah deskripsi film menjadi representasi vektor.

2. **Similarity Calculation**:
   - Menggunakan cosine similarity antara vektor deskripsi film untuk mengukur kesamaan antar film.

3. **Ranking and Recommendation**:
   - Film-film dengan kesamaan tinggi diurutkan berdasarkan similarity scores dan direkomendasikan kepada pengguna.

Contoh penggunaan:

```plaintext
get_recommendations('Pulp Fiction', cosine_sim, indices)
```

#### Collaborative Filtering (CF):

Pendekatan ini menggunakan pola interaksi pengguna dengan film untuk membuat rekomendasi. Kami menggunakan algoritma K-Nearest Neighbors (KNN) dalam collaborative filtering.

Kami mulai dengan memuat data menggunakan pustaka Surprise, yang menyediakan berbagai algoritma untuk sistem rekomendasi. Kami menggunakan algoritma KNNBasic untuk melakukan collaborative filtering berdasarkan kesamaan antar pengguna.

Setelah memuat data, kami melakukan cross-validation untuk mengevaluasi kinerja model menggunakan Root Mean Square Error (RMSE) sebagai metrik evaluasi.

Berikut adalah contoh penerapan CF:

1. **User-Item Matrix**:
   - Membangun matriks pengguna-item yang merepresentasikan interaksi antara pengguna dan film.

2. **Similarity Calculation**:
   - Menghitung tingkat kesamaan antara pengguna berdasarkan pola interaksi mereka terhadap film.

3. **Prediction**:
   - Memprediksi penilaian atau preferensi pengguna terhadap film-film yang belum ditontonnya.

4. **Ranking and Recommendation**:
   - Film-film yang belum ditonton oleh pengguna diurutkan berdasarkan prediksi penilaian atau preferensi yang dihasilkan, dan film-film teratas direkomendasikan kepada pengguna.

Contoh penggunaan:

```plaintext
Mean RMSE: 0.98
```

Dengan menggabungkan kedua pendekatan ini, kami dapat memberikan rekomendasi film yang lebih personal dan relevan kepada pengguna, meningkatkan pengalaman mereka dalam menemukan film baru yang sesuai dengan preferensi mereka.

## Evaluation

### Metrik Evaluasi

Dalam proyek ini, digunakan metrik Root Mean Square Error (RMSE) sebagai indikator utama untuk mengevaluasi kinerja model rekomendasi. RMSE adalah metode yang umum digunakan untuk mengukur seberapa dekat prediksi model dengan nilai sebenarnya dari suatu fenomena. Dalam konteks ini, RMSE digunakan untuk mengukur seberapa baik model dapat memprediksi nilai rating film oleh pengguna.

**Formula RMSE**:

$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\Big(\frac{d_i -f_i}{\sigma_i}\Big)^2}$


di mana:
- $\( d_i \)$ adalah nilai sebenarnya dari data.
- $\( f_i \)$ adalah nilai yang diprediksi oleh model.
- $\( \sigma_i \)$ adalah standar deviasi dari data.
- $\( n \)$ adalah jumlah total data.

RMSE menghitung akar kuadrat dari rata-rata dari kuadrat perbedaan antara nilai sebenarnya $\( d_i \)$ dan nilai prediksi $\( f_i \)$, yang dinormalisasi oleh standar deviasi $\( \sigma_i \)$. Semakin rendah nilai RMSE, semakin baik model dalam memprediksi nilai sebenarnya.

### Hasil Evaluasi

Hasil evaluasi menggunakan algoritma KNN (K-Nearest Neighbors) pada dataset IMDb Movies/Shows with Descriptions menunjukkan nilai RMSE sebesar 0.9787. Nilai RMSE yang relatif rendah menunjukkan bahwa model memiliki kinerja yang baik dalam memprediksi rating film oleh pengguna.

Waktu yang diperlukan untuk melatih model (fit time) adalah sekitar 0.49 detik, sedangkan waktu yang diperlukan untuk melakukan pengujian (test time) adalah sekitar 4.10 detik. Waktu yang cepat ini menunjukkan bahwa model dapat diterapkan dengan efisien dalam lingkungan produksi.

### Interpretasi Hasil

- Meskipun nilai RMSE cukup rendah, masih terdapat ruang untuk perbaikan model agar dapat memberikan rekomendasi yang lebih akurat. Hal ini dapat dilakukan dengan menggabungkan metode lain, menyesuaikan parameter model, atau menggunakan teknik feature engineering yang lebih canggih.
- Penggunaan algoritma KNN dalam sistem rekomendasi film ini memberikan hasil yang cukup memuaskan, tetapi peningkatan performa model dapat dicari dengan mencoba algoritma lain atau melakukan eksperimen dengan variasi parameter pada algoritma yang digunakan.
- Hasil evaluasi ini menunjukkan bahwa model sudah mampu memberikan rekomendasi yang cukup relevan dan sesuai dengan preferensi pengguna. Namun, untuk mencapai tujuan yang lebih tinggi, seperti meningkatkan kepuasan pengguna dan retensi pengguna pada platform streaming, peningkatan keakuratan rekomendasi masih diperlukan. Oleh karena itu, perbaikan dan peningkatan model rekomendasi akan menjadi fokus utama pada tahap selanjutnya dari proyek ini.



## Kesimpulan dan Saran

**Kesimpulan:**

Berdasarkan hasil analisis dan eksperimen yang dilakukan, dapat disimpulkan bahwa:

- Sistem rekomendasi film yang diusulkan dalam proyek ini mampu memberikan rekomendasi yang cukup relevan dan sesuai dengan preferensi pengguna.
- Penggabungan metode Collaborative Filtering dan Content-Based Filtering memberikan hasil yang lebih baik daripada menggunakan salah satu metode saja.
- Algoritma KNN yang digunakan dalam model menunjukkan kinerja yang cukup memuaskan dengan nilai RMSE yang relatif rendah.
- Masih terdapat ruang untuk meningkatkan performa model dan keakuratan rekomendasi dengan menggabungkan metode lain, menyesuaikan parameter model, atau menggunakan teknik feature engineering yang lebih canggih.

**Saran:**

Berdasarkan kesimpulan di atas, berikut adalah beberapa saran untuk pengembangan sistem rekomendasi film di masa depan:

- **Mencoba algoritma lain:** Algoritma KNN bukan satu-satunya pilihan untuk sistem rekomendasi. Algoritma lain seperti Random Forest, Support Vector Machines, atau Deep Learning dapat memberikan hasil yang lebih baik.
- **Menyesuaikan parameter model:** Performa model dapat ditingkatkan dengan menyesuaikan parameter model. Hal ini dapat dilakukan dengan menggunakan teknik seperti Grid Search atau Random Search.
- **Menggunakan teknik feature engineering:** Feature engineering adalah proses untuk memanipulasi data agar lebih mudah dipahami oleh model. Teknik ini dapat digunakan untuk meningkatkan performa model dengan mengekstrak fitur yang lebih relevan dari data.
- **Menggabungkan metode lain:** Selain Collaborative Filtering dan Content-Based Filtering, terdapat metode lain yang dapat digunakan untuk meningkatkan performa sistem rekomendasi. Contohnya, metode Context-Aware Filtering dapat digunakan untuk mempertimbangkan konteks pengguna saat memberikan rekomendasi.
- **Mengembangkan sistem rekomendasi yang lebih personal:** Sistem rekomendasi yang personal dapat memberikan rekomendasi yang lebih sesuai dengan preferensi individu pengguna. Hal ini dapat dilakukan dengan menggunakan informasi seperti demografi, minat, dan perilaku pengguna.
- **Mengevaluasi sistem rekomendasi dengan lebih komprehensif:** Evaluasi sistem rekomendasi tidak hanya terbatas pada metrik RMSE. Metrik lain seperti Precision, Recall, F1-Score, dan User Satisfaction juga perlu dipertimbangkan.

Dengan menerapkan saran-saran di atas, diharapkan sistem rekomendasi film dapat memberikan rekomendasi yang lebih akurat dan bermanfaat kepada pengguna.

**Catatan:**

- Sistem rekomendasi film yang diusulkan dalam proyek ini masih dalam tahap awal pengembangan.
- Perbaikan dan peningkatan model rekomendasi akan menjadi fokus utama pada tahap selanjutnya dari proyek ini.
- Saran-saran yang diberikan di atas perlu diuji dan dievaluasi lebih lanjut untuk memastikan efektivitasnya dalam meningkatkan performa sistem rekomendasi.



**Referensi:**

[1] Y. Ishida, T. Uchiya, dan I. Takumi, "Design and evaluation of a movie recommendation system showing a review for evoking interest," *International Journal of Web Information Systems*, vol. 1, no. 1, hal. 1-5, Apr. 2017.

[2] M. H. Rimaz, M. Elahi, F. B. Moghadam, C. Trattner, R. Hosseini, dan M. Tkalčič, "Exploring the Power of Visual Features for the Recommendation of Movies," dalam *UMAP '19: Proceedings of the 27th ACM Conference on User Modeling, Adaptation and Personalization*, hal. 303–308, Jun. 2019.
