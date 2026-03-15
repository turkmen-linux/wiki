Cryptsetup
^^^^^^^^^^
Linux dağıtımlarında genellikle disk şifrelemek için tercih edilen yöntemlerden biridir.

Kurulum
+++++++
ymp ile yüklemek için aşağıdaki komutu kullanabilirsiniz:

.. code-block:: shell

	ymp install cryptsetup


Kullanımı
+++++++++
Öncelikle diski şifrelemek için formatlayalım.

.. code-block:: shell

	cryptsetup luksFormat /dev/sda

**Not:** bu işlem tüm diski silecektir. Veri kaybına sebep olabilir. Yedek almayı unutmayın.

Ardından diski etkinleştirelim.

.. code-block:: shell

	cryptsetup luksOpen /dev/sda example

Bu şekilde diski çözdükten sonra **/dev/mapper/example** adında bir block aygıt oluşturulur.
Bu block aygıtı bölümlendirip kullanabilirsiniz.

Çözülmüş diskinizi tekrar kapatmak için öncelikle diskin tüm bölümlerinin bağlantısını kesmelisiniz.

.. code-block:: shell

	umount /dev/mapper/example*

Ardından diski kapatabiliriz.

.. code-block:: shell

	cryptsetup luksClose example

Parola değiştirme
+++++++++++++++++
Öncelikle parola eklemiz gerekmektedir. Bunun için aşağıdaki gibi bir yol kullanmalıyız.

.. code-block:: shell

	cryptsetup luksAddKey /dev/sda

Daha sonra eski parolamızı kaldıralım.

.. code-block:: shell

	cryptsetup luksRemoveKey /dev/sda

