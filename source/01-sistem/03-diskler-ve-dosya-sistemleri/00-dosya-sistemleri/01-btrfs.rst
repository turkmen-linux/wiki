Btrfs
=====
Btrfs, Linux çekirdeği için geliştirilmiş bir dosya sistemidir. Gelişmiş özellikleri ve esnek yapısıyla, modern depolama ihtiyaçlarını karşılamak üzere tasarlanmıştır.

Disk bağlama
------------
btrfs diskleri bağlamak için öncelikle çekirdek modülünün bulunması gerekmektedir. Bunun için **/sys/fs/btrfs** dizini bulunuyormu diye kontrol edebilirsiniz. Eğer bulunmuyorsa aşağıdaki komut ile etkinleştirebilirsiniz.

.. code-block:: shell

	$ modprobe btrfs

Ardından diski bağlamak için aşağıdaki komutu kullanabilirsiniz.

.. code-block:: shell

	$ mount -t btrfs -o defaults,rf /dev/sda1 /baglama/noktasi


Btrfs biçimlendirme
-------------------
**mkfs.btrfs** komutu btrfs-progs paketi ile sağlanır. Öncelikle btrfs-progs yüklemeliyiz.

.. code-block:: shell

	$ ymp install btrfs-progs

Ardından diski biçimlendirelim.

.. code-block:: shell

	$ mkfs.btrfs /dev/sda1

**Not:** diski biçimlendirmek verilerinize kalıca hasar verebilir.

Rootfs olarak kullanma
----------------------
Btrfs dosya sistemini kök dizin olarak kullanmak için  çekirdek parametrelerine **rootfstype=btrfs** eklenmesi gerekmektedir.
Eğer **grub** kullanıyorsanız **/etc/default/grub** dosyanıza aşağıdaki gibi ekleme yapmalısınız ve yapılandırmanızı güncellemelisiniz.

.. code-block:: shell

	GRUB_CMDLINE_LINUX_DEFAULT="quiet rootfstype=btrfs"

Ardından /etc/fstab içerisine aşağıdaki gibi girdi yazmalısınız.

.. code-block:: shell

	UUID=abcdef-0055-4958-990f-1413ed1186ec    /    btrfs    defaults,rw    0    0

Subvolume kavramı
-----------------
Btrfs dosya sisteminde "subvolume", dosya sisteminin içinde bağımsız bir dosya sistemi gibi davranabilen bir alt bölüm veya mantıksal birimdir. Subvolumelar, Btrfs'nin sunduğu esnekliği ve yönetim kolaylığını artıran önemli bir özelliktir.

Bağlamak
++++++++
Bir btrfs dosya sisteminde subvolume bağlamak için bağlama paraetrelerine **subvol=subvol_adi** şeklinde ekleme yapmalıyız.

.. code-block:: shell

	$ mount -t btrfs -o defaults,rw,subvol=@/yedek /dev/sda1 /yedek

Bununla birlikte bir subvolume varsayılan ayarlanıp seçenek kullanılmadan da bağlanabilir.

.. code-block:: shell

	# subvol-id değerini subvolume listesinden bulabilirsiniz.
	$ btrfs subvol set-default subvol-id /

Oluşturma
+++++++++
Bir subvolume oluşturmak için aşağıdaki komutu kullanabilirsiniz

.. code-block:: shell

	# /bagli/dizin/ dizinine btrfs dosya sistemi bağlı olduğunu düşünebilirsiniz.
	$ btrfs subvol create /bagli/dizin/yeni_subvolume

Listeleme
+++++++++
Btrfs üstündeki subvolume listesi için aşağıdaki komutu kullanabilirsiniz.

.. code-block:: shell

	# /bagli/dizin/ dizinine btrfs dosya sistemi bağlı olduğunu düşünebilirsiniz.
	$ btrfs subvol list -t /bagli/dizin/

Silme
+++++
Btrfs dosya sisteminde subvolume silmek için:

.. code-block:: shell

	# /bagli/dizin/ dizinine btrfs dosya sistemi bağlı olduğunu düşünebilirsiniz.
	$ btrfs subvol delete /bagli/dizin/silinecek_subvolume

Yeniden adlandırma
++++++++++++++++++
Btrfs dosya sisteminde bir subvolume adını değiştirmek için basitçe **mv** komutunu kullanabilirsiniz.

.. code-block:: shell

	$ mv /bagli/dizin/@dosyalar /bagli/dizin/eski-dosyalar


Yedekleme (snapshot)
++++++++++++++++++++
Btrfs dosya sisteminde bir subvolume yedeği alınabilir. Bunun için aşağıdaki komutu kullanabilirsiniz.

.. code-block:: shell

	$ btrfs subvol snapshot /bagli/dizin/@dosyalar /bagli/dizin/@yedek

Bu sayede subvolume yedeğini almış olduk. Yedekten geri dönmek için mevcut subvolume silinip yedeğin yedeği alınabilir.


