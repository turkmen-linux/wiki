Zram
^^^^
Linux sistemlerinde bellek yönetimini optimize etmek ve performansı artırmak için kullanılan bir yöntemdir. Zram, sıkıştırılmış bellek blokları oluşturarak, fiziksel RAM üzerinde daha fazla veri depolamaya olanak tanır.

Yapılandırma
++++++++++++
Zram'ı yapılandırmak için, öncelikle zram cihazını oluşturmalısınız. Aşağıdaki adımları izleyerek zram'ı yapılandırabilirsiniz:

1. **Zram Cihazını Oluşturma:**
Aşağıdaki komut ile zram cihazını oluşturabilirsiniz. `num_devices` değeri, oluşturmak istediğiniz zram cihazı sayısını belirtir. Örneğin, 2 zram cihazı oluşturmak için:

.. code-block:: shell

	modprobe zram num_devices=2

2. **Sıkıştırma Algoritmasını Belirleme:**
Zram cihazının sıkıştırma algoritmasını ayarlamak için:

.. code-block:: shell

	echo lz4 > /sys/block/zram0/comp_algorithm

3. **Disk Boyutunu Ayarlama:**
Zram cihazının disk boyutunu belirlemek için:

.. code-block:: shell

	echo 1G > /sys/block/zram0/disksize

**Not:** `disksize` değerini sisteminizin RAM miktarına göre ayarlayabilirsiniz. Örneğin, 1G yerine 2G veya daha fazla bir değer verebilirsiniz.

4. **Swap Alanı Olarak Kullanma:**
Zram cihazını swap alanı olarak kullanmak için:

.. code-block:: shell

	mkswap /dev/zram0
	swapon /dev/zram0

Kullanım
++++++++
Zram, genellikle swap alanı olarak kullanılır. Yukarıdaki adımlarla zram'ı etkinleştirdikten sonra, sisteminizin bellek yönetimi otomatik olarak zram'ı kullanmaya başlayacaktır. Bellek kullanımı arttıkça, zram sıkıştırılmış verileri RAM üzerinde depolayarak sistem performansını artırır.

Zram'ı devre dışı bırakmak için aşağıdaki komutları kullanabilirsiniz:

.. code-block:: shell

	swapoff /dev/zram0
	echo 0 > /sys/block/zram0/disksize

Bu komutlar, zram'ı devre dışı bırakacak ve ilgili kaynakları serbest bırakacaktır.

Zram Durumunu Kontrol Etme
+++++++++++++++++++++++++++
Zram'ın durumunu kontrol etmek için aşağıdaki komutu kullanabilirsiniz:

.. code-block:: shell

	cat /proc/swaps

Bu komut, sistemdeki mevcut swap alanlarını ve zram ile ilgili bilgileri gösterecektir.

