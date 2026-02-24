USB/IP
======
USB/IP protokolü, USB cihazlarının ağ üzerinden paylaşımına olanak tanır.
Bu sayede usb aygıtlarını ağ üzerinden başka bir cihaz ile kullanmak mümkün hale gelir.

Kurulum
+++++++
**usbip** komutu linux çekirdeğinin kod deposu ile beraber gelmektedir.

Türkmen linux üzerine kurmak için:

.. code-block:: shell

	$ ymp install linux-tools


Kurulumu yaptıktan sonra çekirdek modülünün açılışta yüklenmesi için:

.. code-block:: shell

	$ echo "usbip_host" > /etc/modules-load.d/usbip.conf
	$ echo "vhci_hcd" >> /etc/modules-load.d/usbip.conf
	$ modprobe usbip_host
	$ modprobe vhci_hcd

Sunucu tarafı
+++++++++++++
Öncelikle servisi başlatalım.

.. code-block:: shell

	$ usbipd --ipv4 --debug

**Not:** Varsayılan 3240 portu üzerinde ağ üzerinde paylaşılmaktadır. Herhangi bir doğrulama mekanizması olmadğı için güvenlik açısından sorun oluşturabilir.

Ardından usb listesini bulalım.

.. code-block:: shell

	$ usbip list -l

Son olarak usb paylaşıma açalım:

.. code-block:: shell

	$ usbip bind -b 3-1.5

Paylaşımı sonlandırmak için:

.. code-block:: shell

	$ usbip unbind -b 3-1.5

Kullanıcı tarafı
++++++++++++++++
Öncelikle sunucu tarafındani usb listesini alalım.

.. code-block:: shell

	$ usbip list -r 10.0.3.1

Daha sonra usb bağlantısını sağlayalım.

.. code-block:: shell

	$ usbip attach -r 10.0.3.1 3-1.5

Bağlantıyı sonlandırmak için:

.. code-block:: shell

	$ usbip detach -r 10.0.3.1 3-1.5

