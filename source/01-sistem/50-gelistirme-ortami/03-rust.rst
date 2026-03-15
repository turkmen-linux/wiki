Rust
====
Rust llvm tabanlı bir programlama dilidir.

Kurulum
+++++++
**rustup** aracını kullanarak kurulum yapılır.

.. code-block:: shell

	$ ymp install rustup

Ardından rust yüklenir.

.. code-block:: shell

	# kurulum konumu değiştirmek için
	$ export RUSTUP_HOME=$HOME/.local/rust
	$ rustup

Araçları **PATH** değişkenine ekleyelim

.. code-block:: shell

	export PATH=$PATH:$RUST_HOME/toolchains/stable-$(uname -m)-unknown-linux-gnu/bin

Son olarak kontrol etmek için:

.. code-block:: shell

	$ rustc --version

**Not:** rust araçları kullanıcı bazlı olarak kurulur.
Sistem bazlı kurulum için öncelikle root yetkisi alarak kurmanız yeterli olur.

Proje oluşturma ve derleme
++++++++++++++++++++++++++
**cargo** komutu ile proje oluşturmak için:

.. code-block:: shell

	$ cargo new hello_world
	$ cd hello_world

Örnek **hello world** kodu aşağıdaki gibi olsun.

.. code-block:: C

	fn main() {
	    println!("Hello, world!");
	}

Son olarak derleyelim.

.. code-block:: shell

	$ cargo build

Çalıştırmak için:

.. code-block:: shell

	$ cargo run

