Network Block Device (nbd)
==========================
Network Block Device (nbd), bir ağ üzerindeki disk görüntülerini veya diğer blok cihazlarını uzak bir sistemde kullanmanızı sağlayan bir sistem aracıdır. NBD, istemci-sunucu mimarisi kullanarak çalışır; istemci, NBD sunucusuna bağlanarak uzak bir blok cihazına erişim sağlar. Bu, veri depolama ve yedekleme çözümleri için oldukça faydalıdır.

Sunucu tarafı
+++++++++++++
NBD sunucusu oluşturmak için **qemu-nbd** kullanabilirsiniz. İşlem adımları aşağıdaki gibidir:

Disk İmajı Oluşturma
---------------------
Öncelikle disk imajı oluşturmalısınız:

.. code-block:: shell

    $ qemu-img create -f qcow2 test.img 50G

NBD Sunucusunu Başlatma
-------------------------
Ardından, NBD sunucusunu başlatmak için şu komutu kullanabilirsiniz:

.. code-block:: shell

    # Salt okur yapmak için -r parametresi kullanılır.
    # -b 0.0.0.0 dışa açılacak adres
    # -p port numarası
    # -e en fazla bağlantı sayısı
    $ qemu-nbd -f qcow2 -b 0.0.0.0 -p 10809 -e 10 test.img

Kullanıcı tarafı
++++++++++++++++
Kullanıcı tarafında ise aşağıdaki adımları takip etmelisiniz:

NBD Çekirdek Modülünü Yükleme
-------------------------------
Öncelikle nbd çekirdek modülünü yükleyin:

.. code-block:: shell

    # nbds_max block aygıt sayısı
    $ modprobe nbd nbds_max=1

Bağlantıyı Ayarlama
--------------------
Bağlantıyı ayarlamak için aşağıdaki komutu kullanın:

.. code-block:: shell

    # Buradaki host ve portu kendinize göre değiştirin.
    $ nbd-client 192.168.1.31 /dev/nbd0 -p 10809

Bölüm Listesini Güncelleme
---------------------------
Son olarak, varsa bölümlerin listesini güncelleyin:

.. code-block:: shell

    $ partprobe /dev/nbd0

Artık **/dev/nbd0** blok aygıtını kullanabilirsiniz.

