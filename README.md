# Dokumentasi Proyek
## Di Susun Oleh : Ulinnuha / L200220265
**web admin**

`username : admin`
`password : admin1234`
## Deskripsi
Tugas ini bertujuan untuk menambah data dinamis ke dalam website personal yang telah dibangun sebelumnya. Kami akan memanfaatkan models, views, urls, dan templates di Django, serta menampilkan data dari database ke halaman web.

## Perubahan yang Dilakukan
Pada tugas ini, saya melakukan beberapa perubahan utama pada website personal:
1. Mengelola profil dan resume ke dalam database.
2. Menampilkan data profil dan resume di halaman web.
3. Mengelola data proyek di dalam database dan menampilkannya di halaman proyek.
4. Menampilkan halaman respons ketika pengunjung mengirimkan pesan melalui form kontak.

## Struktur Folder Aplikasi
Setelah memecah aplikasi `webapp` menjadi aplikasi yang lebih kecil, struktur proyek berubah menjadi seperti berikut:

```
mywebsite/
├── profiles/
│   ├── templates/
│   │   ├── index.html
│   │   └── resume.html     
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── projects/
│   ├── templates/
│   │   ├── projects.html
│   │   └── project_detail.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── contact/
│   ├── templates/
│   │   ├── contact.html
│   │   └── response.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/
│   ├── assets/
│   │   ├── 1.jpeg
│   │   ├── favicon.ico
│   │   └── profile.png
│   ├── css/
│   │   └── styles.css
│   └──js/
│      └── scripts.js
├── templates/
│   └── base.html
└── manage.py
```

## Langkah-Langkah Pengerjaan

### Langkah 1: Memecah Aplikasi Menjadi Modul Terpisah
- Membuat tiga aplikasi baru: `profile`, `projects`, dan `contact`.
- Memindahkan file HTML terkait ke dalam folder `templates` masing-masing aplikasi.
- Menghapus aplikasi `webapp` dan menghapus referensinya dari `settings.py`.


### Langkah 2: Membuat Base Template (`base.html`)
- Mengisolasi bagian HTML yang berulang seperti navbar dan footer ke dalam file `base.html`.
- Menggunakan `{% block %}` dan `{% endblock %}` untuk memisahkan konten dinamis dari setiap halaman.
- Menggunakan `{% extends %}` untuk menghubungkan setiap halaman HTML dengan template dasar `base.html`.


### Langkah 3: Membuat Model untuk Profil, Proyek, dan Kontak
- Menambahkan model `Profile`,
from django.db import models
```python
from django.db import models
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    about = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

class Resume(models.Model):
       title = models.CharField(max_length=100)
       description = models.TextField()
       start_date = models.DateField()
       end_date = models.DateField()
```
- Menambahkan model`Projek`
```python
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

```
- Menambahkan model`kontak`
```python
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
```
- Melakukan migrasi database dengan `python manage.py makemigrations` dan `python manage.py migrate`.
- Menambahkan model ke dalam Django Admin untuk memudahkan manajemen data melalui antarmuka admin.

### Langkah 4: Menampilkan Data Profil
- Menghubungkan view dengan template yang sesuai di dalam aplikasi `profile`.
```python
from django.shortcuts import render
from .models import Profile, Resume

def profiles(request):
    profiles = Profile.objects.first()
    return render(request, 'index.html', {"profiles": profiles})
    

def resume(request):
    resume = Resume.objects.all()
    return render(request, 'resume.html',{"resume": resume})
```


### Langkah 5: Menyusun urls
pada mywebsite, kami mengatur URL seperti berikut:
```python
from django.contrib import admin
from django.urls import path, include
from profiles import views
from projects import views as projek
from contact import views as contact
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('webapp.urls')),
    path('', views.profiles),
    path('resume/', views.resume),
    path('project/', projek.projects),
    path('project/<int:pk>/', projek.project_detail, name='project_detail'),
    path('contact/',contact.contact),
    path('respon/',contact.response, name="respon"),

]
```
### Langkah 5: Mengatur setting
mengkonfigurasi `settings.py` untuk menambahkan aplikasi ke dalam `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'profiles',
    'contact',
]
```
### Langkah 6: Menggunakan template
menggunakan template untuk menyusun struktur halaman. Misalnya, pada `base.html`, kami menyusun menu navigasi dan bagian konten:
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="view   My Websiteport" content="width=device-width, initial-scale=1">
    <title>{% block title %}My Website{% endblock %}</title>
    {% block index_css %}
    
    {% endblock index_css %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body class="container">
    <!--  -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Ulinnuha</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link" href="/">Profiles</a>
              <a class="nav-link" href="/resume/">Resumes</a>
              <a class="nav-link" href="/project/">Project</a>
              <a class="nav-link" href="/contact/">Contact</a>
            </div>
          </div>
        </div>
      </nav>
    <!--  -->
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        &copy; 2021 My Website
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```
### Contoh penggunaan template di profile
```html
{% extends "base.html" %}
{% load static %}
{% block index_css %}
    <link rel="stylesheet" href="{% static '/css/styles.css' %}">
{% endblock index_css %}
{% block title  %} Profiles - Mywebsite {% endblock  %}
{% block content %}
<section class="bg-light py-5">
    <div class="container px-5">
        <div class="row gx-5 justify-content-center">
            <div class="col-xxl-8">
                <div class="text-center my-5">
                    <h2 class="display-5 fw-bolder"><span class="text-gradient d-inline">About Me</span></h2>
                    <p class="lead fw-light mb-4">My name is {{profiles.name}}</p>
                    <p class="text-muted">{{profiles.about}}</p>
                    <a href="respon">Response</a>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock content %}
```
## Hasil Akhir
1. **Halaman Profil**: Menampilkan informasi profil, termasuk nama, email, nomor telepon, alamat, dan lainnya.
2. **Halaman Resume**: Menampilkan daftar resume yang memuat pendidikan dan pengalaman kerja.
3. **Halaman Proyek**: Menampilkan daftar proyek yang pernah dikerjakan, dengan tautan untuk melihat detail proyek.
4. **Halaman Kontak**: Menampilkan form kontak yang memungkinkan pengunjung mengirim pesan, serta halaman respons yang menampilkan pesan terima kasih setelah pengiriman.
