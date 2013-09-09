==============================
Configurare l'Emperor di uWSGI
==============================

L'emperor permette di avviare una o più istanze di uWSGI (dette *vassals*) prendendo i file di configurazione da una directory specificata.

La documentazione ufficiale si trova a questo indirizzo: http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html

Abilitare l'Emperor
*******************

Per abilitare la funzione è sufficiente andare nella sezione **Container** del pannello di controllo e alla voce Emperor inserire il nome della directory dove si troveranno i file dei *vassals*.

Dopo aver cliccato sul bottone **modifica** e aspettato 30 secondi l'Emperor sarà pronto a caricare i vassals.

Creare un file vassal
*********************

I file vassal sono normali file di configurazione di uWSGI. Le istanze prodotte gireranno all'interno del container e vengono tenute in esecuzione, ed eventualmente riavviate, dall'Emperor.

Un esempio di file vassal per un'applicazione php può essere:

.. code-block:: ini

    [uwsgi]
    plugins = 0:php5419
    socket = /proc/unbit/sockets/uwsgi_php54.sock
    master = true
    processes = 4
    cheaper = 2
    no-orphans = true
    auto-procname = true
    touch-reload = %p
    php-ini = /proc/unbit/www/php.ini
    static-index = index.html
    check-static-docroot = true
    fileserve-mode = x-sendfile
    php-index = index.php
    for = .php .php4 .php5 .php3 .inc
      static-skip-ext = %(_)
      php-allowed-ext = %(_)
    endfor =

È importante notare che impostiamo il socket unix su cui il vassal resterà in ascolto. Questo sarà necessario per associare il vassal ad un dominio tramite Proxy_.

.. _Proxy: http://unbit.it/docs/Proxy

Demoni
******

È possibile far partire demoni sfruttando le direttive **attach-daemon** o **smart-attach-daemon** di uWSGI. Questo è il metodo raccomandato di avviare programmi esterni all'applicazione come MySQL, PostgreSQL ecc.

Un file vassal per avviare MySQL è semplicemente questo:

.. code-block:: ini

    [uwsgi]
    smart-attach-daemon = /proc/unbit/db.mysql/mysqld.pid /opt/unbit/mysql5523/bin/mysqld --defaults-file=/proc/unbit/my.cnf

La differenza fra **attach-daemon** o **smart-attach-daemon** consiste nel fatto che nel primo caso il demone resta in esecuzione soltanto finché esiste il vassal che lo ha generato, mentre nel caso di smart-attach-daemon il demone continua a girare anche se il vassal viene riavviato o ucciso.

**NOTA**: Soltanto **smart-attach-daemon** richiede il pid file come primo parametro.

