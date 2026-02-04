netns (Network Namespace)
=========================
netns (network namespace), ağ kaynaklarını izole etmek için kullanılan bir mekanizmadır. Birden fazla ağ yığınını tek bir Linux çekirdek üzerinde çalıştırarak, her bir yığın için ayrı ağ ayarları, araçları ve protokolleri oluşturma imkanı sunar.

netns oluşturma ve kaldırma
+++++++++++++++++++++++++++

Bir netns oluşturmak için aşağıdaki komut kullanılır:

.. code-block:: shell

	$ ip netns add deneme

Silmek için ise şu komut kullanılır:

.. code-block:: shell

	$ ip nets del deneme

Var olanları listelemek için:

.. code-block:: shell

	$ ip nets list

netns içerisinde komut çalıştırma
+++++++++++++++++++++++++++++++++
Bir netns içerisinde komut çalıştırarak o komutun izole bir ağ ortamında çalışması sağlanabilir. Bunun için şu komuttan yararlanılabilir.

.. code-block:: shell

	$ ip nets exec deneme /bin/bash

Bu komut hiçbir ağ arayüzü eklemediğimiz için ağ bağlantısı bulunmayan *deneme* ağında çalıştırılır.

netns içine ağ arayüzü eklenmesi
++++++++++++++++++++++++++++++++
Bir ağ arayüzünü netns içine ekleyebilirsiniz. birden çok ethernet ile çalışmanız gerektiğinde kullanışlı olabilmektedir.

.. code-block:: shell

	# eth1 arayüzünü eklemek için (2. ethernet arayüzü)
	$ ip link set eth1 netns deneme
	# loop arayüzünü açalım (127.0.0.1 için)
	$ ip netns exec deneme ip link set up lo
	# dhcp ile ip almak için
	$ busybox udhcpc -i eth1
	# netns içinde firefox başlatmak için (pingu kullanıcısı ile)
	$ ip netns exec deneme su pingu -c "firefox"

netns arası iletişim sağlanması
+++++++++++++++++++++++++++++++
Öncelikle **veth** arayüzü eklememiz gerekmektedir.

.. code-block:: shell

	$ ip link add veth0 type veth peer name veth1

Burada veth0 ve veth1 adında 2 adet veth arayüzümüz oluşmaktadır.
Arayüzlernden birini netns içine alalım.

.. code-block:: shell

	$ ip link set veth1 netns deneme

Ardından arayüzlere birer ip adresi atayalım.

.. code-block:: shell

	# açık hale getirelim
	$ ip link set up veth0
	$ ip netns exec deneme ip link set up veth1
	# loop arayüzünü açalım (127.0.0.1 için)
	$ ip netns exec deneme ip link set up lo
	# ip atayalım
	$ ip addr add 10.0.3.1/24 dev veth0
	$ ip netns exec deneme ip addr add 10.0.3.2/24 dev veth1
	# varsayılan route verelim
	$ ip netns exec deneme ip route add default via 10.0.3.1 dev veth1
	# yetkilendirme verelim
	$ iptables -t nat -A POSTROUTING -o veth0 -j MASQUERADE
	$ iptables -A FORWARD -i veth0 -j ACCEPT
	$ iptables -A FORWARD -o veth0 -j ACCEPT

Artık deneme adındaki netns içerisinden ana makinamıza **10.0.3.1** adresi ile ulaşabilirsiniz. Ana makinanızdan ise **10.0.3.2** adresi ile netns içerisine ulaşabilirsiniz.

.. code-block:: shell

	# netns içinde 8000 portunda tcp dinlemek için
	$ ip netns exec deneme netcat -l -p 8000
	# netns içindeki 8000 portuna bağlanmak için
	$ netcat 10.0.3.2 8000

Dış ağa bağlantı sağlanması
+++++++++++++++++++++++++++
Dış ağa bağlantı sağlanabilmesi için yönlendirmenin açık olması ve ağ kuralı gerekmektedir. Dışa erişim ayarlayalım.

.. code-block:: shell

	$ sysctl net.ipv4.ip_forward=1
	$ iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

Artık **eth0** üzerinden dış ağa erişim sağlanabilir.
