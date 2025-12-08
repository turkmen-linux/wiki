Ymp paket sisteminin kurulumu
=============================
Ymp paket sistemini kaynak koddan derlemek için şu adımlar izlenmelidir.

Kaynak kodun indirilmesi
^^^^^^^^^^^^^^^^^^^^^^^^
Kaynak koda https://gitlab.com/turkmen-linux/devel/sources/ymp adresinden ulaşabilirsiniz.

Öncelikle kaynak kodu `git clone` komutu ile indirelim.

.. code-block:: shell

	$ git clone https://gitlab.com/turkmen-linux/devel/sources/ymp.git

Gerekli paketlerin kurulması
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Debian tabanlı dağıtımlar için aşağıdaki paketler kurulmalıdır. (testing/unstable için)

.. code-block:: shell

	# Derleyiciler
	$ apt install meson gcc valac --no-install-recommends -y
	# Derleme bağımlılıkları
	$ apt install libarchive-dev libreadline-dev libcurl4-openssl-dev \
	    libbrotli-dev --no-install-recommends -y

Yapılandırma
^^^^^^^^^^^^
Kaynak kod `meson` komutu ile yapılandırılır.

.. code-block:: shell

	$ meson setup build --prefix=/usr
	    -Dshared=true
	# Burada -Dshared=true veya -Dstatic=true belirtilmelidir.

İstenilen özellikleri `-Dözellik=durum` şeklinde belirterek ayarlayabilirsiniz. Özelliklerin listesine kaynak kod içerisinde bulunan meson_options.txt dosyasından ulaşabilirsiniz.

Derleme ve sisteme kurulma işlemi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`ninja` komutu kullanılarak derleme işlemi yapılır. Derleme sonrasında `ninja install` komutu ile sisteme kurulur. Son olarak `ldconfig` komutu kullanılarak kütüphanesini sistem kütüphane önbelleğini güncellenir.

.. code-block:: shell

	# Derleme işlemi
	$ ninja -C build
	# Kurulma işlemi
	$ ninja install -C build
	$ ldconfig

