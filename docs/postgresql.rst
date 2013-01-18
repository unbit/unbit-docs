-------------------
PostgreSQL dedicato
-------------------

Se hai bisogno del massimo della flessibilità nella configurazione di PostgreSQL per la tua applicazione puoi installare un'istanza dedicata del db server all'interno del tuo account. Avrai sia l'accesso come utente *root* che la possibilità di modificare il file di configurazione del server stesso, arrivando a una flessibilità altrimenti ottenibile soltanto con un VPS.

Di norma l'istanza viene installata nella directory ``~/db.pg`` , ascolterà su un socket unix e, opzionalmente, su una porta dell'interfaccia locale. Il file di configurazione sarà ``~/db.pg/postgresql.conf``.

Per prima cosa dovrai inizializzare l'istanza con questo comando:

.. parsed-literal::
    /opt/unbit/postgresql921/bin/initdb -A md5 -U postgres -W -D db.pg -E UTF-8

**NOTA** In questi esempi viene usata la versione 9.2.1 di postgresql, ma i comandi sono validi per tutte le versioni, sarà sufficiente adattare i path. Per comodità puoi aggiungere questa riga al file ``~/.bashrc``:

.. parsed-literal::
    export PATH=/opt/unbit/postgresql921/bin/:$PATH

Dal prossimo login potrai richiamare semplicemente il comando (*psql* , *pg_dump* ecc...) senza il bisogno di specificare il percorso completo.

Per la tua istanza puoi usare come base questo file di configurazione, da salvare col nome ``~/db.pg/postgresql.conf``:

.. parsed-literal::
    listen_addresses = ''           
    max_connections = 10
    unix_socket_directory = '~/db.pg'
    shared_buffers = 16MB
    work_mem = 8MB
    datestyle = 'iso, dmy'
    lc_messages = 'it_IT.utf8'                      
    lc_monetary = 'it_IT.utf8'                      
    lc_numeric = 'it_IT.utf8'                       
    lc_time = 'it_IT.utf8'                          
    default_text_search_config = 'pg_catalog.italian'

A questo punto contatta il nostro staff per avere indicazioni sul metodo migliore per avviarla.
Una volta avviato il server assicurati di settare la password per l'utente postgres. Per farlo dovrai momentaneamente concedere l'accesso senza password modificando il file ``~/db.pg/pg_hba.conf``. Trova questa linea:

.. parsed-literal::
    local   all             all                                     md5

e sostituisci *md5* con *trust*. Quindi invia questo comando per far prendere al server le nuove impostazioni:

.. parsed-literal::
    pg_ctl -D ~/db.pg/ reload

Potrai quindi collegarti alla tua istanza utilizzando questo comando senza specificare alcuna password:

.. parsed-literal::
    psql -h ~/db.pg/ -U postgres

Imposta la password per l'utente *postgres*:

.. parsed-literal::
    **postgres=#** \\password postgres
    **postgres=#** \\q

Modifica di nuovo le impostazioni del file ``~/db.pg/pg_hba.conf`` e ricaricale come visto sopra. Da questo momento potrai accedere all'istanza con la nuova password appena assegnata.

Il passo successivo sarà creare un primo account da usare per la tua applicazione:

.. parsed-literal::
    **postgres=#** CREATE ROLE *nuovoutente* WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN PASSWORD '*nuovapassword*';

Puoi quindi creare un database il cui proprietario sarà l'utente *nuovoutente*:

.. parsed-literal::
    **postgres=#** CREATE DATABASE *nomedb* WITH OWNER = "*nuovoutente*" ENCODING = 'UTF-8';

Fatto questo sei pronto ad utilizzare il nuovo database usando le credenziali appena scelte. Accedi così:

.. parsed-literal::
    psql -h ~/db.pg *nomedb* *nuovoutente*

Se necessario potrai anche riavviare autonomamente il server, i nostri sistemi si occuperanno di riavviarlo entro un minuto. Per farlo in modo sicuro puoi lanciare questo:

.. parsed-literal::
    pg_ctl stop -D ~/db.pg -m smart -U postgres

