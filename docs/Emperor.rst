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
