Pipewire
========
Pipewire çoklu ortam yöneticisidir.

Türkmen linuxta pipewire pulseaudio yerine kullanılır ve pipewire-pulse pakete dahildir.

Kurulumu
^^^^^^^^
**pipewire** paketini yüklemeniz gerekmektedir.
Ardından **wireplumber** yükleyip masaüstü ortamı ile çalışmasını sağlamalısınız.

.. code-block:: shell

	$ ymp install pipewire wireplumber


Türkmen linuxta pipewire sistem servisi olarak çalışmaktadır. Bu sebeple sistem servislerini çaşılışa eklemelisiniz.

.. code-block:: shell

	# başlangıçta çalıştırmak için
	$ rc-update add pipewire default
	$ rc-update add pipewire-pulse default
	$ rc-update add wireplumber default
	# başlatmak için
	$ rc-service pipewire start
	$ rc-service pipewire-pulse start
	$ rc-service pipewire start

Kurulum tamamlandıktan sonra oturumunuzu kapatıp açmanız gerekebilir.

Çalışıp çalışmadığını test etmek için **pactl info** ve **wpctl status** komutlarını kullanarak pipewire ile ilgili bilgi alabilirsiniz.


**Not:** pactl komutu pipewire-pulse ile sağlanır. wpctl komutu wireplumber ile sağlanır.

Uzak makinaya bağlanma
^^^^^^^^^^^^^^^^^^^^^^
Öncelikle gerekli modülü sunucu olarak kullanılacak makinada aşağıdaki komut ile etkinleştirelim.

.. code-block:: shell

	# Bu kısım sesi alacak olan makinada çalıştırılır.
	# auth-ip-acl parametresini yazmazsanız herkes tarafından elişilebilir olur.
	# Sadece bu parametre ile belirtilen ip adresine izin verilir.
	# Birden çok ip belirtmek için aralarına ; işareti koyulmalıdır.
	$ pactl load-module module-native-protocol-tcp auth-ip-acl=192.168.0.18;192.168.0.15

Daha sonra bağlantı kurmak için **PULSE_SERVER** çevresel değişkenini kullanabiliriz.

.. code-block:: shell

	# Bu kısım sesi gönderecek olan makinada çalıştırılır.
	$ export PULSE_SERVER=192.168.0.12
	$ mpv /home/pingu/test.mkv

Ses seviyesi ayarı
^^^^^^^^^^^^^^^^^^
Wireplumber üzerinden ses seviyelerini ayarlayabilirsiniz.

Öncelikle **wpctl status** komutu ile mevcut ses aygıtlarının ve uygulamaların id değerlerini bulalım.

.. code-block:: shell

	PipeWire 'pipewire-0' [0.3.67, root@(none), cookie:2586580591]
	 └─ Clients:
	        31. pipewire-pulse                      [0.3.67, root@(none), pid:4772]
	        33. WirePlumber                         [0.3.67, root@(none), pid:4771]
	        34. WirePlumber [export]                [0.3.67, root@(none), pid:4771]
	        63. Firefox                             [0.3.67, root@(none), pid:4806]
	        69. wpctl                               [0.3.67, root@(none), pid:9322]
	
	Audio
	 ├─ Devices:
	 │      47. Built-in Audio                      [alsa]
	 │      55. Built-in Audio                      [alsa]
	 │      59. Built-in Audio                      [alsa]
	 │  
	 ├─ Sinks:
	 │      32. Built-in Audio Analog Stereo        [vol: 0.39]
	 │      51. Built-in Audio Analog Stereo        [vol: 0.40]
	 │  *   57. Built-in Audio Analog Stereo        [vol: 1.00]
	 │  
	 ├─ Sink endpoints:
	 │  
	 ├─ Sources:
	 │      37. Built-in Audio Analog Stereo        [vol: 1.00]
	 │      38. Built-in Audio Stereo               [vol: 1.00]
	 │  *   52. Built-in Audio Analog Stereo        [vol: 1.00]
	 │  
	 ├─ Source endpoints:
	 │  
	 └─ Streams:
	        64. Firefox                                                     
	             44. output_FL       > Generic Analog:playback_FL	[active]
	             66. output_FR       > Generic Analog:playback_FR	[active]
	
	Video
	 ├─ Devices:
	 │  
	 ├─ Sinks:
	 │  
	 ├─ Sink endpoints:
	 │  
	 ├─ Sources:
	 │  
	 ├─ Source endpoints:
	 │  
	 └─ Streams:
	
	Settings
	 └─ Default Configured Node Names:

Bulduğumuz id değerini kullanarak ses seviyesini ayarlayabiliriz.

.. code-block:: shell

	# Ses seviyesi 0-1 arası değerde olmalıdır.
	# Daha yüksek seviyeler de ayarlanabilir. (tavsiye edilmez)
	$ wpctl set-volume 57 0.8

Sessiz moda alıp geri açmak için aşağıdaki gibi komut kullanılabilir.

.. code-block:: shell

	# 1 sessiz moda alır. 0 sessiz moddan çıkar.
	$ wpctl set-mute 57 0


