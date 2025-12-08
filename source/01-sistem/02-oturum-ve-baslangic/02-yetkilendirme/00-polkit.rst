Polkit
======
Polkit yetkisiz uygulamaların yetkili olan uygulamalar ile iletişim kurmasını sağlayan bir araçtır. Örneğin gparted gibi uygulamaları başlatmak için **pkexec** komutu ile root yetkisi sağlanır.

Kurulum
^^^^^^^
ymp ile **polkit** yüklemek için aşağıdaki komut kullanılır:

.. code-block:: shell

	$ ymp install polkit

Ardından polkitin servisi için gereken dosyalara **suid** yetkisi verelim.

.. code-block:: shell

	$ chmod 4755 /usr/bin/pkexec
	$ chmod 4755 /usr/lib/polkit-1/polkit-agent-helper-1

Sonra servisi etkinleştirelim.

.. code-block:: shell

	$ rc-update add polkit # açılışta başlaması için
	$ rc-service polkit start # başlatmak için

Son olarak **/etc/shells** dosyasını kontrol edelim.
**echo $SHELL** komutunu çalıştırınca çıkan değerin bu dosyada bulunması gerekir.

Polkit-agent
^^^^^^^^^^^^
Kullandığınız masaüstüne göre polkit-agent yüklemeniz gereklidir. Aşağıda tablo olarak gerekenler verilmiştir.

.. list-table:: Polkit Agent Listesi
   :widths: 30 30 30
   :header-rows: 1
   
   * - Masaüstü
     - paket
     - sağladığı komut
   * - Kde
     - polkit-kde-agent
     - /usr/lib64/libexec/polkit-kde-authentication-agent-1
   * - lxde
     - lxsession
     - /usr/bin/lxpolkit
   * - cinnamon
     - polkit-gnome
     - /usr/libexec/polkit-gnome-authentication-agent-1
   * - xfce
     - xfce-polkit
     - /usr/libexec/xfce-polkit

Not: polkit agent desdeği olmayan masaüstülerde **polkit-gnome** kullanabilirsiniz.


Kurallar
^^^^^^^^
Polkit kural dosyaları **/usr/share/polkit/rules.d/** ve **/etc/polkit/rules.d** dizinlerinde bulunur. Bu dizinlere kurallar ekleyebilirsiniz. Örneğin test gurubundaki herşeye yetki vermek için :

.. code-block:: shell

	polkit.addRule(function(action, subject) {
	    if (subject.isInGroup("test")) {
	      return polkit.Result.YES;
	  }
	});

**Not:** Yukarıdaki örnek sadece konuyu anlatmak içindir. Güvenlik sorunlarına sebep olabilir.

Eylemler
^^^^^^^^
Kural dosyalarına benzer şekilde eylem dosyaları da bulunur. Bu dosyalar ise **/usr/share/polkit-1/actions** içerisinde bulunur. 

Örneğin:

.. code-block:: xml

	<policyconfig>
	  <vendor>Test Vendor</vendor>
	  <vendor_url>https://example.org</vendor_url>
	  <action id="org.turkmen.test.application">
	    <description>Test application</description>
	    <message>Authentication is required for test application</message>
	    <message xml:lang="tr">Test uygulaması için yetkilendirme gerekiyor</message>
	    <icon_name>preferences-system</icon_name>
	    <defaults>
	      <allow_any>yes</allow_any>
	      <allow_inactive>yes</allow_inactive>
	      <allow_active>yes</allow_active>
	    </defaults>
	    <annotate key="org.freedesktop.policykit.exec.path">/usr/sbin/test</annotate>
	    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
	  </action>
	</policyconfig>

Polkit kullanımı
^^^^^^^^^^^^^^^^
**pkexec** komutunu kullanarak polkit çalıştırabilirsiniz. Örneğin:

.. code-block:: shell

	$ pkexec /bin/bash

Burada dikkat etmemiz gereken polkit eylemi olmayan bir komutu çalıştırdığımızda çevresel değişkenler korunmadığı için gui kullanan uygulamaları çalıştıramazsınız.

