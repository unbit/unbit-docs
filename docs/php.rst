===
PHP
===

Per utilizzare questo comunissimo linguaggio è possibile seguire due approcci distinti; il primo si basa su configurazioni pre-confezionate ed è utile soprattutto per gli utenti alle prime armi, mentre il secondo offre maggiore flessibilità e possibilità di tuning illimitate.

Tutte le opzioni citate in questa guida si trovano nel pannello di controllo, nella sezione *domini*.

Per entrambi i metodi di deploy va selezionata l'opzione **upstream** e sarà necessario assegnare al dominio un container o dei processi.
A questo punto i metodi divergono, ecco come:

I wizard
--------

Per ogni versione di php presente sui nostri server sarà disponibile un wizard. Ti basterà selezionare quello dalle opzioni presenti in **upstream_wizard** per la versione di php che ti interessa e salvare le impostazioni. Dopo 30 secondi i nostri sistemi saranno pronti a servire i tuoi script php.

Configurazione manuale
----------------------

In questo metoto avrai il controllo completo sia dell'application server (uWSGI) che delle opzioni del linguaggio.

Per prima cosa dovrai creare un file di configurazione per uWSGI, che chiameremo ``uwsgi.ini``:

.. code-block:: ini

    [uwsgi]
    ; Carico il plugin per php 5.4.7
    plugins = 0:php547
    ; Imposto il nome del dominio
    dominio = sql.mirko.unbit.it
    ; Imposto il numero di processi da avviare...
    processes = 4
    ; ...e il numero minimo di processi da tenere in esecuzione
    cheaper = 2
    ; Abilito il processo master per maggiore affidabilità
    master = true
    ; %p viene automaticamente trasformato nel percorso del file di config
    ; %d corrisponde invece alla directory dove risiede il file di config
    touch-reload = %p
    touch-reload = %d/php.ini
    ; Aggiungo il nome del dominio al nome del processo uWSGI
    auto-procname = true
    procname-prefix-spaced = [%(dominio)]
    ; Controllo se nella docroot ci sono file statici...
    check-static-docroot = true
    ; ...e li servo con il metodo usato da apache
    fileserve-mode = x-sendfile

    ; Specifico una lista di file statici da cercare e da servire quando nessuno è specificato
    for = index.xhtml index.html index.htm
      static-index = %(_)
    endfor =

    ; Imposto opzioni specifiche per i file php
    for = .php .php4 .php5 .php3 .inc
    ;   Salta queste estensioni quando cerchi i file statici
      static-skip-ext = %(_)
    ;   Considerale valide per php
      php-allowed-ext = %(_)
    ;   imposta come pagina indice il file index<.estensione>
      php-index = index%(_)
    endfor =
    ; Il file php.ini nella docroot del dominio verrà passato a php
    php-ini = %d/php.ini

Ti rimando alla documentazione ufficiale di uwsgi [1]_ per la lista completa di opzioni supportate.

A questo punto dovrai creare un file ``php.ini`` nella docroot del tuo dominio. La configurazione di base è:

.. code-block:: ini

    magic_quotes_gpc = Off
    date.timezone = Europe/Rome

Aggiungi poi le estensioni di cui hai bisogno, ad esempio:

.. code-block:: ini

    extension = mysql.so
    extension = curl.so

Puoi trovare la lista di estensioni presenti sul server al percorso ``/opt/unbit/php547/lib/php/extensions/no-debug-non-zts-20100525/`` .

Sei pronto, adesso, per aggiungere questa riga nel campo **upstream_cmd**

.. parsed-literal::
    uwsgi --ini uwsgi.ini

30 secondi dopo l'applicazione partirà con le opzioni che hai scelto.

**NOTA** Ogni volta che effettuerai modifiche al file ``uwsgi.ini`` o al ``php.ini`` il server verrà riavviato per renderle effettive.

PHP da riga di comando
----------------------

Puoi usare php anche da riga di comando, collegandoti al server via ssh. Puoi richiamare il binario usando il percorso completo:

.. parsed-literal::
    /opt/unbit/php547/bin/php-cgi

ma ti consigliamo di personalizzare il tuo ambiente di lavoro inserendolo nel tuo path, aggiungendo al file ``~/.bashrc`` questa riga:

.. parsed-literal::
    export PATH=/opt/unbit/php547/bin:$PATH

e ricorda di specificare sempre il file ``php.ini`` nella docroot del dominio per cui stai effettuando operazioni da command line:

.. parsed-literal::
    php-cgi -c ~/www/example.com/php.ini

PEAR
----

Per utilizzare i moduli PEAR va configurato l'ambiente da riga di comando. Ecco qualche riga per configurare le directory predefinite:

.. parsed-literal::

    pear config-set php_dir /proc/unbit/share/pear
    pear config-set doc_dir /proc/unbit/lib/php/doc
    pear config-set test_dir /proc/unbit/lib/php/test

Fatto questo le estensioni potranno essere installate semplicemente con:

.. parsed-literal::
    
    pear install NomeEstensione

.. [1] https://github.com/unbit/uwsgi-docs
