# -*- coding: utf-8 -*-
"""Movies/Shows-Recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1et-Y6hmi-w55PN5p2JpYU8eE0PfVRYEw

Nama : Muhammad Thayyib

Dataset dari : https://www.kaggle.com/datasets/ishikajohari/imdb-data-with-descriptions

## Domain Knowledge:

Sistem Rekomendasi (SR) merupakan aplikasi inti dalam bidang kecerdasan buatan yang bertujuan untuk memprediksi preferensi pengguna terhadap item tertentu, seperti film, musik, buku, atau produk lainnya, dan memberikan rekomendasi yang relevan kepada pengguna berdasarkan informasi yang dikumpulkan tentang mereka [1]. Dalam konteks Sistem Rekomendasi untuk film, pengguna seringkali dihadapkan pada pilihan yang luas dari berbagai film yang tersedia, dan SR berperan sebagai asisten yang membantu mereka menavigasi melalui pilihan tersebut dengan menawarkan rekomendasi yang sesuai dengan preferensi mereka.

Dua pendekatan utama yang sering digunakan dalam Sistem Rekomendasi film adalah Content-Based Filtering (CBF) dan Collaborative Filtering (CF).

1. **Content-Based Filtering (CBF)**: Pendekatan ini berfokus pada fitur dan karakteristik intrinsik dari item (film) itu sendiri. CBF menggunakan informasi tentang atribut-atribut film, seperti genre, aktor, sutradara, deskripsi, dan kata kunci lainnya, untuk membuat profil film. Profil ini kemudian dibandingkan dengan preferensi pengguna yang diketahui atau yang diungkapkan untuk menemukan kesamaan antara film yang direkomendasikan dengan film yang disukai pengguna sebelumnya. Misalnya, jika seorang pengguna sering menonton film bergenre drama yang disutradarai oleh sutradara tertentu, CBF dapat merekomendasikan film dengan genre dan sutradara serupa.

2. **Collaborative Filtering (CF)**: Pendekatan ini menggunakan informasi dari perilaku pengguna untuk membuat rekomendasi. CF bergantung pada asumsi bahwa pengguna yang memiliki preferensi serupa dalam masa lalu akan memiliki preferensi serupa juga di masa depan. CF dapat dibagi menjadi dua kategori utama: User-Based Collaborative Filtering dan Item-Based Collaborative Filtering. Dalam User-Based CF, rekomendasi dibuat berdasarkan kesamaan antara profil pengguna, sementara dalam Item-Based CF, rekomendasi dibuat berdasarkan kesamaan antara item (film) itu sendiri. Misalnya, jika pengguna A dan B memiliki preferensi film yang serupa, maka CF dapat merekomendasikan film yang disukai oleh pengguna B kepada pengguna A, dan sebaliknya.

Selain itu, fitur visual juga telah digunakan dalam beberapa penelitian terkait Sistem Rekomendasi film. Fitur visual seperti poster film, cuplikan trailer, atau representasi visual lainnya dapat digunakan untuk memperkaya representasi film dan meningkatkan ketepatan rekomendasi [2]. Pendekatan ini dapat mencakup analisis konten visual secara langsung atau memanfaatkan teknik machine learning untuk mengekstraksi fitur-fitur visual yang relevan dari gambar atau video.

Dengan memahami prinsip-prinsip dasar ini, pengembang dan peneliti dapat merancang dan mengembangkan Sistem Rekomendasi film yang efektif dan relevan untuk kebutuhan pengguna. Dengan demikian, Domain Knowledge ini menjadi dasar yang penting dalam merancang solusi yang komprehensif dan berhasil dalam domain Sistem Rekomendasi film.

## Problem Statements:

1. Dalam era digital saat ini, pengguna seringkali dihadapkan pada pilihan yang luas dari berbagai film yang tersedia di platform streaming. Namun, banyak dari mereka mengalami kesulitan dalam memilih film yang sesuai dengan preferensi dan selera mereka.

2. Pengguna seringkali kesulitan menemukan film baru yang menarik dan relevan dengan minat mereka di tengah banyaknya opsi film yang tersedia di platform streaming.

## Goals:

1. Mengembangkan sistem rekomendasi film yang efektif dan dapat memberikan rekomendasi yang personal dan sesuai dengan preferensi pengguna.

2. Meningkatkan pengalaman pengguna dalam menavigasi melalui berbagai opsi film dengan menyediakan rekomendasi yang akurat dan relevan berdasarkan preferensi dan sejarah penontonannya.

3. Meningkatkan tingkat kepuasan pengguna terhadap platform streaming dengan memberikan rekomendasi film yang dapat memenuhi minat dan preferensi mereka, sehingga meningkatkan retensi pengguna dan penggunaan platform secara keseluruhan.

Anda benar, untuk menjaga konsistensi antara tujuan (goals) dan pendekatan solusi (solution approach), jumlahnya harus sama. Mari saya sesuaikan dengan menambahkan satu poin dalam pendekatan solusi:

## Solution Approach:

#### Content-based Filtering:
1. **Feature Extraction**: Pertama-tama, kami akan melakukan ekstraksi fitur dari setiap film dalam dataset. Fitur-fitur ini akan mencakup informasi seperti genre film, aktor utama, sutradara, tahun rilis, dan deskripsi film. Fitur-fitur ini akan digunakan untuk membangun profil setiap film.

2. **User Profile Creation**: Selanjutnya, kami akan membuat profil pengguna berdasarkan preferensi film yang telah ditontonnya sebelumnya. Profil pengguna akan mencakup preferensi genre, aktor, sutradara favorit, dan atribut lainnya yang relevan.

3. **Similarity Calculation**: Kami akan menghitung kesamaan antara film-film dalam dataset dan profil pengguna. Ini dapat dilakukan dengan menggunakan metode seperti cosine similarity atau TF-IDF untuk deskripsi film. Tujuannya adalah untuk menemukan film yang memiliki kesamaan tinggi dengan preferensi pengguna.

4. **Ranking and Recommendation**: Berdasarkan tingkat kesamaan yang dihitung, kami akan merangkum dan memberikan rekomendasi film yang memiliki kesamaan tinggi dengan profil pengguna kepada pengguna. Film-film ini akan diurutkan berdasarkan tingkat kesamaan yang dihasilkan.

#### Collaborative Filtering:
1. **User-Item Matrix**: Kami akan membangun matriks pengguna-item yang merepresentasikan interaksi antara pengguna dan item (film). Ini bisa berupa matriks penilaian atau matriks penontonan.

2. **Similarity Calculation**: Selanjutnya, kami akan menghitung tingkat kesamaan antara pengguna berdasarkan pola interaksi mereka terhadap film. Hal ini dapat dilakukan menggunakan metode seperti cosine similarity atau Pearson correlation.

3. **Prediction**: Kami akan memprediksi penilaian atau preferensi pengguna terhadap film-film yang belum ditontonnya berdasarkan pola kesamaan dengan pengguna lain.

4. **Ranking and Recommendation**: Film-film yang belum ditonton oleh pengguna akan diurutkan berdasarkan prediksi penilaian atau preferensi yang dihasilkan, dan film-film teratas akan direkomendasikan kepada pengguna.

Dengan pendekatan ini, kami berharap dapat memberikan rekomendasi film yang lebih personal dan relevan kepada pengguna, meningkatkan pengalaman mereka dalam menemukan film baru yang sesuai dengan preferensi mereka.
"""

# Install kaggle package
!pip install -q kaggle

# Upload kaggle.json
from google.colab import files
files.upload()

# Make directory and change permission
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle

# Test kaggle dataset list
!kaggle datasets list

"""### Download dataset from kaggle dataset"""

!kaggle datasets download -d ishikajohari/imdb-data-with-descriptions

"""###Ekstrak File Zip"""

import zipfile
import os

# Lokasi file ZIP yang akan diekstrak
zip_file = "/content/imdb-data-with-descriptions.zip"

# Direktori tujuan untuk mengekstrak file
extract_dir = "/content/imdb_dataset"

# Mengekstrak file ZIP
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Menampilkan daftar file yang diekstrak
extracted_files = os.listdir(extract_dir)
print("Daftar file yang diekstrak:")
for file in extracted_files:
    print(file)

"""## Dataset IMDB Movies/Shows with Descriptions

Dataset ini berisi data IMDb tentang film-film dan acara TV, lengkap dengan deskripsi untuk setiap judul. Data tersebut fokus pada judul-judul yang dirilis dari tahun 1990-an hingga saat ini. Deskripsi untuk setiap judul diambil dari sumber Rotten Tomatoes.

### Fitur Utama Dataset:
- **Title Type**: Jenis judul (film atau acara TV).
- **Primary Title**: Judul utama.
- **Original Title**: Judul asli (jika ada).
- **Is Adult?**: Indikator apakah judul tersebut ditujukan untuk pemirsa dewasa.
- **Year**: Tahun rilis.
- **Run-time Minutes**: Durasi judul dalam menit.
- **Genres (Multiple)**: Genre atau kategori judul (dapat berupa beberapa genre).
- **Average Rating (as on IMDb)**: Rating rata-rata berdasarkan IMDb.
- **Num. of Votes**: Jumlah suara atau rating yang diberikan oleh pengguna IMDb.
- **Region**: Wilayah asal judul (misalnya, Kanada, Britania Raya, India, atau Amerika Serikat).
- **Description**: Deskripsi singkat tentang judul tersebut.

### Konteks Penting Dataset:
Dataset ini disaring berdasarkan beberapa kriteria, termasuk periode waktu, bahasa, dan wilayah, untuk memastikan kualitas dan relevansi judul-judul yang disajikan. Selain itu, hanya judul-judul dengan rating tinggi dan jumlah suara yang cukup yang dipertahankan dalam dataset, menjamin bahwa judul-judul yang disediakan memiliki kualitas yang baik dan telah diterima dengan baik oleh pengguna IMDb.

Dataset ini memiliki potensi besar untuk digunakan dalam berbagai analisis dan proyek rekomendasi, seperti analisis lintas-konten dan pengembangan sistem rekomendasi berbasis konten.

## Exploratory Data Analysis
"""

import pandas as pd

# Baca dataset CSV
df = pd.read_csv('/content/imdb_dataset/IMDB.csv')

print("Lima baris pertama dataset:")
print(df.head())

"""### Informasi dataset"""

print("\nInformasi dataset:")
print(df.info())

"""### Statistik deskriptif untuk kolom numerik"""

print("\nStatistik deskriptif untuk kolom numerik:")
print(df.describe())

"""### Jumlah nilai yang hilang di setiap kolom"""

print("\nJumlah nilai yang hilang di setiap kolom:")
print(df.isnull().sum())

"""Berikut adalah penjelasan untuk hasil EDA pada dataset IMDb Movies/Shows with Descriptions:

1. **Lima baris pertama dataset:**
   - Dataset ini terdiri dari 21 kolom dengan berbagai informasi mengenai film atau acara TV, seperti judul, tahun rilis, rating, jumlah suara, deskripsi, dan lainnya.
   - Lima baris pertama dataset menampilkan beberapa contoh data, termasuk kolom-kolom seperti tconst, titleType, primaryTitle, originalTitle, startYear, runtimeMinutes, genres, averageRating, numVotes, region, language, dan Description.

2. **Informasi dataset:**
   - Dataset terdiri dari 7850 baris dan 21 kolom.
   - Tidak ada nilai yang hilang (null) kecuali pada kolom Description yang memiliki 188 nilai yang hilang.

3. **Statistik deskriptif untuk kolom numerik:**
   - Rata-rata rating adalah 7.37 dengan standar deviasi sebesar 0.61.
   - Jumlah suara (numVotes) memiliki rentang yang sangat besar, mulai dari 6 hingga 2.75 juta dengan rata-rata sekitar 75 ribu suara.
   - Tahun rilis (startYear) berkisar antara 1990 hingga 2023, dengan rata-rata tahun rilis sekitar 2013.

4. **Jumlah nilai yang hilang di setiap kolom:**
   - Hanya kolom Description yang memiliki nilai yang hilang sebanyak 188.

Dari hasil EDA ini, kita dapat melihat bahwa dataset memiliki berbagai informasi yang cukup lengkap tentang film dan acara TV, dengan sedikit nilai yang hilang pada kolom Description. Selanjutnya, analisis lebih lanjut dapat dilakukan untuk memahami lebih dalam tentang distribusi fitur-fitur dalam dataset ini.

### Pembersihan Data
"""

# Menghapus baris dengan nilai yang hilang pada kolom 'Description'
df_cleaned = df.dropna(subset=['Description'])

# Menampilkan jumlah data setelah pembersihan
print("Jumlah data setelah pembersihan: ", df_cleaned.shape[0])

"""### Informasi statistik deskriptif untuk kolom numerik"""

numeric_stats = df_cleaned.describe()
print("Statistik deskriptif untuk kolom numerik:\n", numeric_stats)

"""Statistik deskriptif untuk kolom numerik menunjukkan informasi tentang sejumlah variabel dalam dataset:

- `count`: Jumlah entri non-null dalam kolom.
- `mean`: Rata-rata nilai dalam kolom.
- `std`: Standar deviasi, menunjukkan seberapa tersebar nilai-nilai tersebut.
- `min`: Nilai minimum dalam kolom.
- `25%`, `50%`, `75%`: Kuartil bawah (25%), median (50%), dan kuartil atas (75%) dari distribusi nilai.
- `max`: Nilai maksimum dalam kolom.

Dalam dataset ini, kita dapat melihat bahwa kolom `isAdult` memiliki nilai yang sama untuk seluruh entri (0), sehingga tidak ada variasi dalam kolom tersebut. Kolom lainnya memiliki variasi nilai yang lebih besar.

### Visualisasi distribusi kolom 'startYear' menggunakan histogram
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(df['startYear'], kde=True, color='skyblue', bins=30)
plt.title('Distribusi Tahun Mulai Penayangan', fontsize=16)
plt.xlabel('Tahun Mulai Penayangan', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

"""### Visualisasi distribusi kolom 'averageRating' menggunakan histogram"""

plt.figure(figsize=(10, 6))
sns.histplot(df['averageRating'], kde=True, color='salmon', bins=30)
plt.title('Distribusi Rating Rata-Rata', fontsize=16)
plt.xlabel('Rating Rata-Rata', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

"""# Visualisasi distribusi kolom 'numVotes' menggunakan histogram"""

plt.figure(figsize=(10, 6))
sns.histplot(df['numVotes'], kde=True, color='skyblue', bins=30)
plt.title('Distribusi Jumlah Voting', fontsize=16)
plt.xlabel('Jumlah Voting', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

"""### Visualisasi distribusi kolom 'averageRating' menggunakan histogram"""

plt.figure(figsize=(10, 6))
sns.histplot(df['averageRating'], kde=True, color='salmon', bins=30)
plt.title('Distribusi Nilai Rata-rata Rating', fontsize=16)
plt.xlabel('Nilai Rata-rata Rating', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.show()

"""### Menghitung korelasi antar fitur numerik menggunakan Heatmap"""

correlation_matrix = df[['startYear', 'averageRating', 'numVotes']].corr()

# Visualisasi heatmap korelasi
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Heatmap Korelasi Fitur Numerik', fontsize=16)
plt.show()

"""### Visualisasi distribusi dari beberapa fitur numerik"""

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['startYear'], kde=True, color='blue')
plt.title('Distribusi Tahun Mulai', fontsize=14)

plt.subplot(1, 3, 2)
sns.histplot(df['averageRating'], kde=True, color='green')
plt.title('Distribusi Rating Rata-rata', fontsize=14)

plt.subplot(1, 3, 3)
sns.histplot(df['numVotes'], kde=True, color='orange')
plt.title('Distribusi Jumlah Voting', fontsize=14)

plt.tight_layout()
plt.show()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Inisialisasi objek TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Mengganti nilai-nilai yang hilang dalam kolom 'Description'
df['Description'] = df['Description'].fillna('')

# Membangun matriks TF-IDF
tfidf_matrix = tfidf.fit_transform(df['Description'])

# Menghitung cosine similarity antara dokumen
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim, indices):
    # Mendapatkan index dari judul film yang sesuai
    idx = indices[title]

    # Mendapatkan similarity scores dari semua film
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Mengurutkan film berdasarkan similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Mengambil 10 film teratas
    sim_scores = sim_scores[1:11]

    # Mendapatkan indeks film
    movie_indices = [i[0] for i in sim_scores]

    # Mengembalikan judul film teratas
    return df['primaryTitle'].iloc[movie_indices]

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung similarity matrix menggunakan tf-idf matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Membuat indices series untuk pencocokan judul film dengan indeks dataframe
indices = pd.Series(df.index, index=df['primaryTitle']).drop_duplicates()

get_recommendations('Pulp Fiction', cosine_sim, indices)

# Mencari judul yang mirip dengan "Terminator" dalam dataset
similar_titles = df[df['primaryTitle'].str.contains('Terminator', case=False)]
similar_titles[['primaryTitle']]

!pip install scikit-surprise

from surprise import Reader, Dataset
from surprise.model_selection import cross_validate
from surprise import KNNBasic

# Load data
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_builtin('ml-100k', reader)

# Use user-based collaborative filtering
algo = KNNBasic(sim_options={'user_based': True})

# Perform cross-validation
results = cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=True)

# Print mean RMSE score across all folds
print('Mean RMSE:', results['test_rmse'].mean())

