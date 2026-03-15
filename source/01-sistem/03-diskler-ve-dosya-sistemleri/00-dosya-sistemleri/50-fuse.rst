.. _fuse:
Fuse
====
FUSE (Userspace Dosya Sistemi), kullanıcıların özel izinlere ihtiyaç duymadan dosya sistemlerini bağlamalarını sağlayan bir yöntem sunar.
Linux'ta genellikle yönetici ayrıcalıklarına sahip olanlar tarafından gerçekleştirilen bağlama işlemi, FUSE ile herhangi bir kullanıcı tarafından gerçekleştirilebilir hale gelir.

Kurulumu
^^^^^^^^
Türkmen linuxta fuse yüklemek için aşağıdaki komutu kullanabilirsiniz.

.. code-block:: shell

	$ ymp install fuse
	# Eğer libfuse2 gerektiren bir uygulama çalıştıracaksanız şunu da yüklemelisiniz.
	$ ymp install fuse2

Daha sonra fuse servisini çalıştıralım.

.. code-block:: shell

	# Açılışa ekleyelim
	$ rc-update add fuse
	# Çalıştıralım
	$ rc-service fuse start

Eğer servis yerine elle başlatmak isterseniz aşağıdaki gibi çalıştırabilirsiniz.

.. code-block:: shell

	# Önce modülü yükleyelim.
	$ modprobe fuse
	# Şimdi connections kısmını bağlayalım.
	$ mount -t fusectl none /sys/fs/fuse/connections

Son olarak fusermount komutuna suid biti ayarlayalım.

.. code-block:: shell

	$ chmod u+s /usr/bin/fusermount

Yapılandırma
^^^^^^^^^^^^
FUSE için kullanılabilir yapılandırma dosyaları şunlardır:

.. code-block:: shell

	/etc/fuse.conf

fuse.conf dosyasında iki yapılandırma değişkeni bulunur:

* mount_max: Kök olmayan kullanıcılara izin verilen maksimum FUSE bağlantı sayısını ayarlar (varsayılan olarak ayarlanmamışsa 1000'dir).
* user_allow_other: Kök olmayan kullanıcıların allow_other veya allow_root bağlama seçeneklerini belirtmesine izin verir. Bu, güvenlik nedenleriyle devre dışı bırakılmıştır.

Fuse ile dosya sistemi yazma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**fuse** kullanarak dosya sistemi oluşturabiliriz. Aşağıda örnek bir dosya sistemi kodu bulunmaktadır:

.. code-block:: c

	#define FUSE_USE_VERSION 30
	#include <fuse.h>
	#include <stdio.h>
	#include <string.h>
	#include <errno.h>
	#include <fcntl.h>

	// Dosya ve dizin özniteliklerini döndüren işlev
	static int hello_getattr(const char *path, struct stat *stbuf) {
	    int res = 0;
	
	    memset(stbuf, 0, sizeof(struct stat));
	    if (strcmp(path, "/") == 0) {
	        // Root dizin öznitelikleri
	        stbuf->st_mode = S_IFDIR | 0755;
	        stbuf->st_nlink = 2;
	    } else if (strcmp(path+1, "hello") == 0) {
	        // "hello" dosyasının öznitelikleri
	        stbuf->st_mode = S_IFREG | 0444;
	        stbuf->st_nlink = 1;
	        stbuf->st_size = 12; // "Hello World!\n" uzunluğu
	    } else {
	        // Hata durumu: Dosya veya dizin bulunamadı
	        res = -ENOENT;
	    }
	
	    return res;
	}

	// Dizini okuyan işlev
	static int hello_readdir(const char *path, void *buf, fuse_fill_dir_t filler,
	                         off_t offset, struct fuse_file_info *fi) {
	    (void) offset;
	    (void) fi;

	    if (strcmp(path, "/") != 0)
	        return -ENOENT;

	    // Root dizini içeriğini doldur
	    filler(buf, ".", NULL, 0, 0);
	    filler(buf, "..", NULL, 0, 0);
	    filler(buf, "hello", NULL, 0, 0);

	    return 0;
	}

	// Dosyayı açan işlev
	static int hello_open(const char *path, struct fuse_file_info *fi) {
	    if (strcmp(path+1, "hello") != 0)
	        return -ENOENT;
	
	    // Salt okunur olarak dosyayı aç
	    if ((fi->flags & 3) != O_RDONLY)
	        return -EACCES;

	    return 0;
	}

	// Dosyadan okuma işlevi
	static int hello_read(const char *path, char *buf, size_t size, off_t offset,
	                      struct fuse_file_info *fi) {
	    size_t len;
	    (void) fi;
	    if(strcmp(path+1, "hello") != 0)
	        return -ENOENT;
	
	    // "Hello World!\n" içeriğini dosyadan oku
	    char *hello_str = "Hello World!\n";
	    len = strlen(hello_str);
	    if (offset < len) {
	        if (offset + size > len)
	            size = len - offset;
	        memcpy(buf, hello_str + offset, size);
	    } else
	        size = 0;
	
	    return size;
	}

	// FUSE işlevlerini tanımlayan yapı
	static struct fuse_operations hello_oper = {
	    .getattr = hello_getattr,
	    .readdir = hello_readdir,
	    .open = hello_open,
	    .read = hello_read,
	};

	// Ana fonksiyon
	int main(int argc, char *argv[])
	{
	    return fuse_main(argc, argv, &hello_oper, NULL);
	}

Kodu derlemek için aşağıdaki komut kullanılır.

.. code-block:: shell

	gcc -o hello hello.c `pkg-config --cflags --libs fuse3`

Bu basit örnek, FUSE kullanarak "hello" adında bir dosya oluşturur ve bu dosyanın içeriği "Hello World!" cümlesiyle doldurur.
Dosya sistemine "/hello" yolunu kullanarak erişilebilir.
Bu kod, temel dosya sistemlerinin işlevlerini (getattr, readdir, open, read) uygular.
Örneğin, dosyanın özniteliklerini alma (getattr), dizin içeriğini okuma (readdir), dosyayı açma (open) ve dosyadan okuma (read) işlemleri gerçekleştirilir.

