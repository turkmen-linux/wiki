Swap (Takas Alanı)
==================
Swap alanı belleğin yeterli olmadığı durumda adreslemek için kullanılan disk alanıdır.
Bu sayede RAM tamamen dolmaya başladığında bazı veriler swap alanına taşınarak sistemin çakılması önlenmiş olur.

**Not:** Diskin okuma/yazma hızı RAM kadar fazla olmadığı için disk üzerinde swap kullanmak performans sorunlarına sebep olabilir.

Swap alanı oluşturulması
^^^^^^^^^^^^^^^^^^^^^^^^
Swap oluşturmak için bir dosya kullanabilir veya diskin bir bölümünü swap olarak kullanabilirsiniz.

Disk bölümünden swap oluşturulması
++++++++++++++++++++++++++++++++++
Öncelikle disk bölümümüzü formatlayalım.

.. code-block:: shell

	# Burada swap bölümümüzün sda5 olduğunu varsaydık.
	mkswap /dev/sda5

Dosyadan swap oluşturulması
+++++++++++++++++++++++++++
Bir dosya oluşturup formatlayalım.

.. code-block:: shell

	# 4Gb swap dosyası oluşturduk.
	dd if=/dev/zero of=/swapfile bs=4M count=1000
	# gereken iznini ayarladık.
	chmod 0600 /swapfile
	# formatlayalım
	mkswap /swapfile

Bu işlem diske 0 yazarak çalışır. Diskin hızına bağlı olarak uzun sürebilir. Bunun yerine şu şekilde de oluşturabiliriz.

.. code-block:: shell

	# dosya açalım
	truncate -s 4G /swapfile
	# gereken iznini ayarladık.
	chmod 0600 /swapfile
	# loop haline getirelim.
	loop=$(losetup --find --show /swapfile)
	# loop algıtını formatlayalım
	mkswap "$loop"

Swap alanının etkinleştirilmesi
+++++++++++++++++++++++++++++++
Swap alanını **swapon** komutu kullanarak etkinleştirebiliriz.

.. code-block:: shell

	swapon /dev/sda5

Kontrol etmek için **/proc/swaps** dosyasına bakabilirsiniz.

.. code-block:: shell

	cat /proc/swaps
	>> Filenam    Type      Size    Used Priority
	>> /dev/sda5  partition 4194300 0    -2

Swap alanının kapatılması
+++++++++++++++++++++++++
Swap alanını kapatmak için **swapoff** komutu kullanabilirsiniz.

.. code-block:: shell

	swapoff /dev/sda5

