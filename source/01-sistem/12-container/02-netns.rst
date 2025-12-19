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



