Sık karşılaşılabilen problemler             
===============================
Bu başlık altında sıkça karşılaşılabilen hatalar ve olası çözümleri anlatılmaktadır.

docbook-xsl / docbook-xml hataları
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Eğer docbook ile ilgili **add command failed** hatası alıyorsanız. aşağıdaki yolu izleyin.

1- /etc/xml/catalog dosyasını silin

.. code-block:: shell

	rm -f /etc/xml/catalog

2- docbook-xml ve docbook-xsl paketlerinin sysconf yapılandırmasını silin.

.. code-block:: shell

	$ rm -f /var/lib/ymp/sysconf/docbook-xsl/postinstall.done
	$ rm -f /var/lib/ymp/sysconf/docbook-xml/postinstall.done

3- sysconf modellerini sırası ile elle tetikleyin.

.. code-block:: shell

	$ bash -e /etc/sysconf.d/docbook-xml
	$ bash -e /etc/sysconf.d/docbook-xsl

Segmentation fault hatası
^^^^^^^^^^^^^^^^^^^^^^^^^
Bu hata genellikle bir C kütüphanesinin veya kodunun hatasından kaynaklanır.
Hatanın nereden kaynaklandığını bulmak için **gdb** kullanabiliriz.
Bunun için öncelikle hata veren kodun **-g3** parametresi ile derlenmesi gerekir. Örneğin:

.. code-block:: shell

	$ export CFLAGS="-g3" # C için
	$ export CXXFLAGS="-g3" # C++ için
	# Bu kısım değişiklik gösterebilir.
	$ configure --prefix=/usr
	$ make
	$ make install
	# basit bir C kodunu gcc ile derleyeceksek
	$ gcc -g3 main.c -o main

Ardından kodumuzu gdb yardımı ile çalıştıralım.

Örneğin aşağıdaki gibi hatalı yazılmış bir C kodumuz olsun:

.. code-block:: C

	int main(){
	    char* test; // pointer tanımladık.
	    test[1] = 'c'; // mevcut olmayan bir yere yazmaya çalıştık.
	    return 0;
	}

.. code-block:: shell

	$ gdb ./main
	...
	(gdb) run
	...
	Program received signal SIGSEGV, Segmentation fault.
	main () at main.c:3
	3	    test[1] = 'c';

Bu hatanın nereden geldiğini öğrenmek için **backtrace** kullanabiliriz:

.. code-block:: shell

	(gdb) backtrace 
	#0  main () at main.c:3

Hatanın bulunduğu satıra giderek kaynak koddaki sorunu bulup düzeltebilirsiniz.

aclocal-1.x bulunamadı hatası
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Bu hata genellikte eski sürüm automake kullanılarak yapılandırılmış projelerde meydana gelir ve aşağıdakine gibi bir hatadır.

.. code-block:: shell

	build-aux/missing' aclocal-1.17 -I m4
	.../build-aux/missing: line 85: aclocal-1.17: command not found
	WARNING: 'aclocal-1.17' is missing on your system.
	         You should only need it if you modified 'acinclude.m4' or
	         'configure.ac' or m4 files included by 'configure.ac'.
	make: *** [Makefile:2427: aclocal.m4] Error 127

Bu hatayı çözmek için `autoreconf -vfi` komutunu kullanabilirsiniz. Alternatif olarak şu komut ile eski sürüme uyumlu hale getirebilirsiniz.

.. code-block:: shell

	ln -s aclocal /usr/local/bin/aclocal-1.17
	ln -s automake /usr/local/bin/automake-1.17

