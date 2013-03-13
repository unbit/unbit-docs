--------------
MySQL dedicato
--------------

Se hai bisogno del massimo della flessibilità nella configurazione di MySQL per la tua applicazione puoi installare un'istanza dedicata del db server all'interno del tuo account. Avrai sia l'accesso come utente *root* che la possibilità di modificare il file di configurazione del server stesso, arrivando a una flessibilità altrimenti ottenibile soltanto con un VPS.

Di norma l'istanza viene installata nella directory ``~/db.mysql`` , ascolterà su un socket unix al percorso ``~/db.mysql/mysqld.sock`` e, opzionalmente, su una porta dell'interfaccia locale. Il file di configurazione sarà ``~/my.cnf``.

Per installarla puoi usare come base questo file di configurazione, da salvare col nome ``~/my.cnf``:

.. parsed-literal::
    [client]
    socket          = /proc/unbit/db.mysql/mysqld.sock
    default-character-set=utf8
    
    [mysqld_safe]
    socket          = /proc/unbit/db.mysql/mysqld.sock

    [mysqld]
    skip-networking
    pid-file        = /proc/unbit/db.mysql/mysqld.pid
    socket          = /proc/unbit/db.mysql/mysqld.sock
    datadir         = /proc/unbit/db.mysql

    character-set-server=utf8
    skip-external-locking

    query_cache_size = 8M
    max_connections = 10

    [mysqldump]
    quick
    quote-names
    max_allowed_packet      = 16M

Inizializza quindi l'istanza con:

.. parsed-literal::
    /opt/unbit/mysql5523/scripts/mysql_install_db --basedir=/opt/unbit/mysql5523 --defaults-file=~/my.cnf

A questo punto contatta il nostro staff per avere indicazioni sul metodo migliore per avviarlo.
Una volta avviato il server assicurati di settare la password di root:

.. parsed-literal::
    /opt/unbit/mysql5523/bin/mysqladmin --defaults-file=~/my.cnf -u root password *Nu0vaP4sSWorD*

Potrai quindi collegarti alla tua istanza utilizzando questo comando e specificando la password appena assegnata:

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

**Raccomandato** Esegui un backup periodico dei tuoi database.
Puoi utilizzare lo script incluso qui sotto per farlo:

.. code-block:: perl

    #!/usr/bin/env perl

    use strict;
    use warnings;
    use DBI ;
    use DateTime ;

    ######### Configura il backup
    #
    my %cfg = (
            username  => 'root',                             # Utente amministratore
            password  => '',                                 # Password per l'utente root
            'socket'  => '/proc/unbit/db.mysql/mysqld.sock', # Percorso del socket
            version   => '5523',                             # Versione del server mysql in uso
            mycnf     => '/proc/unbit/my.cnf',               # Percorso del file my.cnf
            backupDir => '/proc/unbit/backup_mysql/',        # Directory dove salvare i backup (slash finale importante)
    );

    ######### Cambia qui sotto solo se sai cosa stai facendo
    #
    my $binDir = "/opt/unbit/mysql" . $cfg{'version'} . "/bin/";
    #
    umask 0027;

    ######### Non cambiare qui sotto

    mkdir $cfg{'backupDir'} unless -d $cfg{'backupDir'};

    my $dbh = DBI->connect( "dbi:mysql:database=mysql;mysql_socket=" . $cfg{'socket'}, $cfg{'username'}, $cfg{'password'} );
    my $sth = $dbh->prepare( "SHOW DATABASES" );

    if ( $sth->execute >=1 ) {
            my $dt = DateTime->now;
            my $day =  $dt->day_of_month;
            while( my $row = $sth->fetchrow_hashref ) {
                    my $db = $row->{Database};
                    next if $db eq 'information_schema';
                    next if $db eq 'performance_schema';
                    mkdir $cfg{'backupDir'} . $db unless -d $cfg{'backupDir'} . $db;
                    my $cmd = $binDir . "mysqldump --defaults-file=" . $cfg{'mycnf'} . " -u " . $cfg{'username'} . " -p". $cfg{'password'} . " " . $db . " | bzip2 -9 > " . $cfg{'backupDir'} . $db . "/" . $day . ".bz2";
                    system ( $cmd );
            }
    }
