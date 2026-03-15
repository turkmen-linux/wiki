Udisks
======
Udisks disk bağlama ve düzenleme özelliklerini sağlayan dbus arayüzü ve **udisksctl** komutunu sağlar. Grafik arayüzlü dosya yöneticileri udisks kullanarak disk bağlama işlemlerini gerçekleştirir.

Kurulum
+++++++
Udisks çalışması için polkit ve dbus gerekmektedir. ymp ile yüklemek için:

.. code-block:: shell

	$ ymp install udisks2


Servisin başlatılması
+++++++++++++++++++++
udisk servis yardımı ile çalışır.

Openrc servisin başlatmak için:

.. code-block:: shell

	# Açılışa eklemek için
	$ rc-update add udisks2 default
	# Başlatmak için
	$ rc-service udisks2 start

Kullanım
++++++++
Udisks servisine udisksctl komutu ile komut yollanır.

.. code-block:: shell

	Usage:
	  udisksctl COMMAND

	Commands:
	  help            Shows this information
	  info            Shows information about an object
	  dump            Shows information about all objects
	  status          Shows high-level status
	  monitor         Monitor changes to objects
	  mount           Mount a filesystem
	  unmount         Unmount a filesystem
	  unlock          Unlock an encrypted device
	  lock            Lock an encrypted device
	  loop-setup      Set-up a loop device
	  loop-delete     Delete a loop device
	  power-off       Safely power off a drive
	  smart-simulate  Set SMART data for a drive

Bir disk bağlamak için aşağıdakine benzer komut kullanılır.

.. code-block:: shell

	$ udisksctl mount -b /dev/sdc1

Bağı sökmek için:

.. code-block:: shell

	$ udisksctl unmount -b /dev/sdc1

Yapılandırma
++++++++++++
Yapılandırma dosyasına **/etc/udisks2/udisks2.conf** içinden ulaşabilirsiniz.
Örneğin fat32 ve exfat dosya sistemlerinin fmask ve dmask değerlerini ayarlamak için:

.. code-block:: shell

	[defaults]
	# tüm dosyaların ve dizinlerin izinlerini 755 olarak görmek için
	vfat_defaults=fmask=022,dmask=022,uid=$UID,gid=$GID
	exfat_defaults=fmask=022,dmask=022,uid=$UID,gid=$GID

Yetlkilendirme
++++++++++++++
Disk bağlayan polkit kuralının adı **org.freedesktop.udisks2.filesystem-mount** olmaktadır.

Örneğin parolasız disk bağlamak için aşağıdaki gibi polkit kuralı yazabilirsiniz:

.. code-block:: javascript

	polkit.addRule(function(action, subject){
	    if (action.id == "org.freedesktop.udisks2.filesystem-mount"){
	        return polkit.Result.YES;
	    }
	});


**Not:** Türkmen linux varsayılan olarak udisks parolasız bağlamaya izin vermez.
Bunun kaldırmak için **/usr/share/polkit-1/rules.d/49-auth-udisks2.rules** dosyasını silebilirsiniz.
