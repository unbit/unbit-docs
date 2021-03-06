---------
Memcached
---------

Memcached è uno dei piu' noti cache server open source.

Configurazione
--------------

Memcached non ha bisogno di un file di configurazione, quindi tutte le opzioni le aggiungeremo alla riga di comando in fase di avvio.

Ricordiamo che il bind può essere effettuato su socket unix o su una delle interfacce locali tre 127.0.0.2 e 255 , sulla porta corrispondente allo uid del tuo account. Se invece vuoi creare un cluster su più account puoi sfruttare una delle interfacce in ascolto sulla rete interna di Unbit: da 192.168.240.x a 192.168.253.x (dove x dipende dal server).

Avvio dell'istanza come demone collegato a un'applicazione
----------------------------------------------------------

Per avviare l'istanza avrai due opzioni. Nella prima memcached rimarrà in esecuzione soltanto fin quando sarà in esecuzione l'istanza di uWSGI che lo ha lanciato, svuotando così la cache ad ogni riavvio dell'applicazione, mentre nella seconda questo continuerà a funzionare anche quando uWSGI verrà fermato.

**NOTA** Per entrambe le soluzioni è necessario usare uWSGI versione 1.4 o superiore.

"Dumb" mode
-----------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    attach-daemon = memcached -m 64 -l 127.0.0.2 -p **UID** -U 0

dove **UID** corrisponde all'uid del tuo account.

"Smart" mode
------------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    smart-attach-daemon = /proc/unbit/pids/memcached.pid memcached -m 64 -l 127.0.0.2 -p **UID** -U 0 -d -P /proc/unbit/pids/memcached.pid

dove **UID** corrisponde all'uid del tuo account.

Unix Socket
-----------
Per utilizzare soltanto i socket unix per comunicare con memcached è sufficiente sostituire, per entrambe le configurazioni viste sopra, ``-l 127.0.0.2`` e ``-U 0`` con ``-s /proc/unbit/sockets/memcached.sock``

A questo punto sei pronto per avviarlo, impostando il campo **upstream_cmd** del pannello di controllo a questo valore:

.. parsed-literal::
    uwsgi14 --ini uwsgi.ini


