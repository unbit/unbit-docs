--------------
MySQL dedicato
--------------

Se hai bisogno del massimo della flessibilità nella configurazione di MySQL per la tua applicazione puoi richiederci l'installazione di un'istanza dedicata, che verrà installata dal nostro staff all'interno del tuo account. Avrai sia l'accesso come utente *root* che la possibilità di modificare il file di configurazione del server stesso, arrivando a una flessibilità altrimenti ottenibile soltanto con un VPS.

Di norma l'istanza sarà installata nella directory ``~/db.mysql`` , ascolterà su un socket unix al percorso ``~/db.mysql/mysqld.sock`` e, opzionalmente, su una porta dell'interfaccia locale. Il file di configurazione sarà ``~/my.cnf``.

Potrai collegarti alla tua istanza utilizzando questo comando:

.. parsed-literal::
    /opt/unbit/mysql5523/bin/mysql --defaults-file=~/my.cnf -u root -p

**NOTA** In questi esempi viene usata la versione 5.5.23 di mysql, ma i comandi sono validi per tutte le versioni, sarà sufficiente adattare i path. Per comodità puoi aggiungere questa riga al file ``~/.bashrc``:

.. parsed-literal::
    export PATH=/opt/unbit/mysql5523/bin/:$PATH

Dal prossimo login potrai richiamare semplicemente il comando (*mysql* , *mysqldump* ecc...) senza il bisogno di specificare il percorso completo.

Tornando alla gestione dell'istanza, sarà necessario prima di tutto creare un database. Dopo esserti collegato come root puoi dare questa query:

.. parsed-literal::
    mysql> CREATE DATABASE primoDB;

Dai quindi i permessi a un nuovo utente per accedere e modificare il database:

.. parsed-literal::
    mysql> GRANT ALL ON primoDB.* TO 'nuovoUtente'@'%' IDENTIFIED BY 'passwordUtente';

Fatto questo sei pronto ad utilizzare il nuovo database usando le credenziali appena scelte.


Se dovessi avere dubbi sullo stato di salute delle tabelle potrai controllare l'integrità dei database (ed eventualmente ripararli) con questo comando:

.. parsed-literal::
    mysqlcheck -A -r -S ~/db.mysql/mysqld.sock -u root -p

Potrai anche riavviare autonomamente il server, i nostri sistemi si occuperanno di riavviarlo entro un minuto. Per farlo in modo sicuro puoi lanciare questo:

.. parsed-literal::
    mysqladmin -S ~/db.mysql/mysqld.sock -u root -p shutdown

