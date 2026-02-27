Türkmen Linux Hardened özellikleri
==================================
Türkmen linuxu diğer dağıtımlardan ayıran en önemli özelliği **hardened** (sıkılaştırılmış) linux dağıtımı olmasıdır. Bu durum bazı farklılıklara sebep olmaktadır.

Komut listesi gizleme:
++++++++++++++++++++++
/usr/bin ve /bin dizinlerinin izinleri yalnızca çalıştırılabilir şekilde ayarlandığında, sistem üzerinde çalışan uygulamalar bu dizinlerdeki komutların varlığını listeleyemez. Bu durum, terminalde Tab tuşu ile komut tamamlama işlemini kısıtlar.

Bu yöntem, kullanıcıların yalnızca belirtilen komutları çalıştırmasına ve diğer komutların görünürlüğünü azaltarak güvenlik sağlar. Özellikle hassas sistemlerde, komutların gizlenmesi, yetkisiz erişim riskini minimize etmenin etkili bir yolu olarak öne çıkar.

Canlı sistem:
+++++++++++++
Türkmen Linux, canlı modda çalıştırıldığında Zram oluşturur ve bu alanı rastgele bir parola ile LUKS (Linux Unified Key Setup) protokolüyle şifreler. Bu sayede canlı sistem üzerinde yapılan değişiklikler şifreli şekilde tutulduğu için fazladan koruma sağlar.

Çekirdek:
+++++++++
Türkmen linux çekirdek yapılandırması varsayılan olarak `hardened<https://archlinux.org/packages/extra/x86_64/linux-hardened/>`_ olarak sağlanır.

Bununla birlikte **sysctl.conf** yapılandırmaları önyüklü olarak gelmektedir.

Varsayılan olarak bazı çekirdek modülleri (uvcvideo gibi) kapalı olarak gelir.

Initramfs:
++++++++++
Türkmen linux initramfs sistemi olarak **mkinitrd** kullanır. Bu initramfs sistemi hook çalıştırmak için cgroup kullanır ve sistemi başlatmadan önce kendisi dışında kalan tüm süreçleri öldürür. Bu sayede initramfs içerisinden kendisi dışında başka bir şeyin çalıştırılmasına engel olur.

Sistem seviyesi önlemler:
+++++++++++++++++++++++++
/tmp dizini **noexec** olarak bağlanır. Bu sayede herhangi bir kullanıcının buraya bir dosya koyup çalıştırmasının önüne geçilir.

Kök dizin **nosuid** olarak bağlanır. Suid ihtiyacı olan dosyalar **/etc/suid.d** dizini altından okunur ve açılışta sadece o dosyalara suid yetkisi verilir.

**/sys/class/dmi** dizine boş dizin bağlanır. Bu sayede çalışan uygulamaların hangi donanımı kullandığınızı görmesi engellenir.

