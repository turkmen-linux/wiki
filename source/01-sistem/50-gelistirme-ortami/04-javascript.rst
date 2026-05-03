Javascript
==========
npm kurulumu
************
Öncelikle yoksa **~/.profile** dosyasını oluşturun. Ardından **git** komutu yoksa yükleyin.

.. code-block:: shell

	$ touch ~/.profile
	$ su
	$ ymp install git

https://nodejs.org/en/download adresinden **nvm** yüklenir.

**~/.profile** dosyasını içeri aktaralım ve **npm** yükleyelim

.. code-block:: shell

	$ source ~/.profile
	nvm install node

Kontrol etmek için `npm --version` komutunu kullanabilirsiniz.

Proje oluşturma
+++++++++++++++
İlk olarak proje dizini oluşturalım.

.. code-block:: shell

	$ mkdir test

`index.js` dosyasını oluşturalım.

.. code-block:: shell

	$ echo 'console.log("Hello World\n");' > index.js


Ardından `package.json` dosyamızı aşağıdaki gibi yazalım.

.. code-block:: json

	{
	  "name": "hello-world",
	  "version": "1.0.0",
	  "description": "Minimal npm project that prints Hello World",
	  "main": "index.js",
	  "scripts": {
	    "start": "node index.js",
	  },
	  "author": "",
	  "license": "MIT"
	}


Projeyi çalıştırmak için `npm run start` komutunu kullanabiliriz.

Bun kurulumu
************
**npm** alternatifi olarak **bun** kullanabilirsiniz.
Öncelikle https://bun.sh/ adresinden bun yüklenir.

.. code-block:: shell

	$ curl https://bun.sh/install | bash

Ardından gerekli çevresel değişkenler eklenir.

.. code-block:: shell

	$ echo 'export BUN_INSTALL="$HOME/.bun"' >> ~/.profile
	$ echo 'export PATH=$BUN_INSTALL/bin:$PATH' >> ~/.profile


Proje oluşturma
+++++++++++++++
İlk olarak proje dizini oluşturulur ve `bun init` komutu çalıştırılır.

.. code-block:: shell

	$ mkdir test
	$ cd test
	$ bun init

Ardından **package.json** dosyasına aşağıdaki gibi ekleme yapın:

.. code-block:: shell

	"scripts": {
	    "start": "bun run ./index.js"
	  },

Projeyi çalıştırmak için `bun run start` komutunu kullanabilirsiniz.
