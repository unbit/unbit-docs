=======
MongoDB
=======

MongoDB è uno dei più noti database NoSQL

Configurazione
--------------

Per prima cosa crea la directory dove risiederanno i database:

.. parsed-literal::
    mkdir -p ~/db.mongo/db

Puoi usare come base questo file di configurazione, da salvare col nome ``~/db.mongo/mongod.conf``:

.. code-block:: ini
    
    port = <UID>
    bind_ip = 127.0.0.2
    
    dbpath = /proc/unbit/db.mongo/db
    logpath = /proc/unbit/db.mongo/mongodb.log
    unixSocketPrefix = /proc/unbit/db.mongo
    pidfilepath = /proc/unbit/db.mongo/mongod.pid
    directoryperdb = true
    logappend = true
    noauth = true
    nohttpinterface = true

    journal = true
    smallfiles = true
    journalCommitInterval = 300
    
Ricordiamo che il bind può essere effettuato su socket unix o su una delle interfacce locali tre 127.0.0.2 e 255 , sulla porta corrispondente allo uid del tuo account. Se invece vuoi creare un cluster su più account puoi sfruttare una delle interfacce in ascolto sulla rete interna di Unbit: da 192.168.240.x a 192.168.253.x (dove x dipende dal server).

Le ultime 3 opzioni del file di configurazione sono necessarie soltanto se hai bisogno di un sistema di journaling (rende piu' affidabile l'istanza in caso di crash). Se questa non è importante è raccomandabile non inserirle per avere performance migliori.

Avvio dell'istanza come demone aggiuntivo di un applicazione
------------------------------------------------------------

Per avviare l'istanza avrai due opzioni. Nella prima mongodb rimarrà in esecuzione soltanto fin quando sarà in esecuzione l'istanza di uWSGI che lo ha lanciato, mentre nella seconda questo continuerà a funzionare anche quando uWSGI verrà fermato.

**NOTA** Per entrambe le soluzioni è necessario usare uWSGI versione 1.4 o superiore.

"Dumb" mode
-----------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    attach-daemon = /opt/unbit/mongodb222/bin/mongod -f /proc/unbit/db.mongo/mongod.conf

"Smart" mode
------------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    smart-attach-daemon = /proc/unbit/db.mongo/mongod.pid /opt/unbit/mongodb222/bin/mongod -f ~/db.mongo/mongod.conf

A questo punto sei pronto per avviarlo, impostando il campo **upstream_cmd** del pannello di controllo a questo valore:

.. parsed-literal::
    uwsgi14 --ini uwsgi.ini

