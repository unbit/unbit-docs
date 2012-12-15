-----
Redis
-----

Redis è un avanzato database che utilizza lo schema chiave-valore.

Per installarlo nel tuo account puoi usare come base i file di configurazione ufficiali per `Redis 2.4`_ e `Redis 2.6`_, da copiare in ``~/db.redis/redis.conf``.

Configurazione
--------------

Le direttive da personalizzare saranno quelle sull'utilizzo della memoria, a seconda delle dimensioni del tuo container, e quelle per il bind che può essere effettuato su socket unix o su una delle interfacce locali tre 127.0.0.2 e 255 , sulla porta corrispondente allo uid del tuo account.

Se vuoi creare un cluster su più account puoi sfruttare una delle interfacce in ascolto sulla rete interna di Unbit: da 192.168.240.x a 192.168.253.x (dove x dipende dal server).

Avvio dell'istanza
-----------------

Per avviare l'istanza avrai due opzioni. Nella prima il server di redis rimarrà in esecuzione soltanto fin quando sarà in esecuzione l'istanza di uWSGI che lo ha lanciato, mentre nella seconda questo continuerà a funzionare anche quando uWSGI verrà riavviato.
Per entrambe le soluzioni è necessario usare uWSGI versione 1.4 o superiore.

"Dumb" mode
-----------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    attach-daemon = /opt/unbit/redis2417/bin/redis-server /proc/unbit/db.redis/redis.conf

"Smart" mode
------------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    smart-attach-daemon = /proc/unbit/db.redis/redis.pid /opt/unbit/redis2417/bin/redis-server /proc/unbit/db.redis/redis.conf

e nel file ``redis.conf`` modifica questo per rendere redis un demone indipendente:

.. parsed-literal::
    daemonize yes


A questo punto sei pronto per avviarlo, impostando il campo **upstream_cmd** del pannello di controllo a questo valore:

.. parsed-literal::
    uwsgi14 --ini uwsgi.ini


.. _`Redis 2.4`: https://raw.github.com/antirez/redis/2.4/redis.conf
.. _`Redis 2.6`: https://raw.github.com/antirez/redis/2.6/redis.conf
