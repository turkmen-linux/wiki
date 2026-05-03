Javascript
==========
npm kurulumu
++++++++++++
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
İlk olarak proje dizini oluşturalım. Ardından `npm init` komutu ile package.json dosyasını oluşturalım.

.. code-block:: shell

	$ mkdir test
	$ cd test
	$ npm init

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
