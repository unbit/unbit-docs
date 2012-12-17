=======
CouchDB
=======

CouchDB è un database non relazionale basato su documenti. Si controlla via protocollo HTTP e fornisce una comoda interfaccia web.
E' scritto in Erlang.

Configurazione
--------------

Per prima cosa crea la directory dove risiederanno i database:

.. parsed-literal::
    mkdir -p ~/db.couch/data

Sara' poi necessario creare un file di configurazione.

Puoi usare come base questo file ini, da salvare col nome ``~/db.couch/couch.ini``:

.. code-block:: ini

    [couchdb]
    ; /proc/unbit punta sempre alla propria home
    database_dir = /proc/unbit/db.couch/data
    view_index_dir = /proc/unbit/db.couch/data
    uri_file = /proc/unbit/db.couch/couch.uri

    [httpd]
    port = <UID>
    bind_address = 127.0.0.4

    [log]
    file = /proc/unbit/db.couch/couch.log

    [admins]
    admin = miaPassword

Ricordiamo che il bind può essere effettuato su socket unix o su una delle interfacce locali tre 127.0.0.2 e 255 , sulla porta corrispondente allo uid del tuo account. Se invece vuoi creare un cluster su più account puoi sfruttare una delle interfacce in ascolto sulla rete interna di Unbit: da 192.168.240.x a 192.168.253.x (dove x dipende dal server).

**NOTA** Appena couchdb viene avviato la password specificata nella sezione ``[admins]`` della configurazione viene crittata automaticamente.

Avvio dell'istanza come demone aggiuntivo di un'applicazione
------------------------------------------------------------

Per avviare l'istanza avrai due opzioni. Nella prima couchdb rimarrà in esecuzione soltanto fin quando sarà in esecuzione l'istanza di uWSGI che lo ha lanciato, mentre nella seconda questo continuerà a funzionare anche quando uWSGI verrà fermato.

**NOTA** Per entrambe le soluzioni è necessario usare uWSGI versione 1.4 o superiore.

"Dumb" mode
-----------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    attach-daemon = /opt/unbit/couchdb120/bin/couchdb -a /proc/unbit/db.couch/couch.ini

"Smart" mode
------------

Nel file ``uwsgi.ini`` aggiungi questa riga:

.. code-block:: ini

    smart-attach-daemon = /proc/unbit/db.couch/couch.pid /opt/unbit/couchdb120/bin/couchdb -a ~/db.couch/couch.ini

A questo punto sei pronto per avviarlo, impostando il campo **upstream_cmd** del pannello di controllo a questo valore:

.. parsed-literal::
    uwsgi14 --ini uwsgi.ini

