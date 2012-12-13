Informazioni tecniche di base
=============================

.. parsed-literal::
   La home del tuo account e' mappata sulla directory /accounts/<account>, se il tuo account si chiama topogigio, la home corrispondera' ad
   **/accounts/topogigio**
  
.. parsed-literal::
   Un link simbolico **/proc/unbit** punta sempre alla tua home

.. parsed-literal::
   Ogni account puo' fare il binding sulla porta corrispondente al suo uid sugli indirizzi da **127.0.0.2** a **127.0.0.255**

.. parsed-literal::
   Ogni account puo' fare il binding sulla rete lan Unbit (per il clustering) sulla porta corrispondente al suo uid sugli indirizzi
   da **192.168.240.x** a **192.168.243.x** (il valore di x e' dipendente dal webserver)
 
.. parsed-literal::
   Le informazioni sull'utilizzo di memoria (e gli eventuali errori) di un container sono disponibili nella sezione Container
   del pannello di controllo

.. parsed-literal::
   Le uniche porte TCP aperte in uscita sono la **80,8080,443,8443,22,5222,3690,9418**

.. parsed-literal::
   In entrata le uniche porte aperte sulle interfacce pubbliche sono la **80,8080,443**

.. parsed-literal::
   Per inviare email dalle applicazioni si puo' utilizzare **127.0.0.1:25** come servizio (il limite e' di 100 email inviate ogni 5 minuti)
 
.. parsed-literal::
   Le porte TCP/UDP assegnate a un account non sono accessibili dagli altri account

.. parsed-literal::
   Non ci sono limiti sui socket UNIX

.. parsed-literal::
   Puoi accedere via ssh ad un altro account (ovviamente devi avere chiave/password) usando la rete **192.168.0.x** (dove x e' il numero
   identificativo del server)
 
.. parsed-literal::
   Non puoi accedere ai database server condivisi direttamente da remoto (usa i tunnel ssh)

.. parsed-literal::
   Se devi effettuare transazioni FTP (ma devi proprio), puoi utilizzare il proxy squid in ascolto sull'indirizzo 192.168.0.19 porta 80
 
.. parsed-literal::
   Ogni applicazione gira con i privilegi dell'utente, quindi non modificare i permessi (a meno che tu non abbia un buon motivo) che devono essere **640** per i file e **750** per le directory
 
.. parsed-literal::
   Se utilizzi come webserver Apache (il default) accertati che la docroot sia sotto la directory **/www** e che mantenga la acl POSIX www-data
   (e' il comportamento di default se non si rimuove accidentamente /www)
 
.. parsed-literal::
   Lo spazio occupato dalla directory /logs non viene conteggiato

.. parsed-literal::
   il file **stderr_log** nella home viene usato come file log di default per le applicazioni

.. parsed-literal::
   Prima di chiedere assistenza allo staff controlla SEMPRE i file di log

.. parsed-literal::
   Le macchine sono sistemi Linux con kernel a 64bit e user space a 32 (ma e' possibile far girare processi a 64bit senza problemi)
 
.. parsed-literal::
   Ove possibile cerca sempre di utilizzare i package dentro **/opt/unbit**

.. parsed-literal::
   Prima di inventare qualche soluzione strana di deployment controlla (o chiedi allo staff) se uWSGI non lo fa gia'
 
.. parsed-literal::
   Usare uWSGI come proxy http e' economico (1 MB a istanza) ed estremamente versatile
 
.. parsed-literal::
   Ricordati di usare il comando **quota** per verificare lo spazio disco in tempo reale (il pannello si aggiorna solo ogni 30 minuti)
 
.. parsed-literal::
   Evita di usare il servizio FTP se ci tieni alla sicurezza
 
.. parsed-literal::
   Se possibile utilizza sempre un db dedicato se vuoi il massimo delle performance e della versatilita'

.. parsed-literal::
   Effettuiamo molti backup, ma ti consigliamo di fare sempre una copia dei tuoi file e soprattutto dei tuoi database.
   Se hai dubbi chiedi allo staff quali sono le tecniche di backup migliori.

.. parsed-literal::
   I file .htaccess sono estremamente inefficienti, se puoi evitarli e' meglio (uWSGI include un rewrite engine molto simile a mod_rewrite)

.. parsed-literal::
   Il numero di richieste che apache puo' mantenere in coda e' molto limitato (ed e' direttamente proporzionale ai timeout upstream impostati). Se prevedi di avere un carico elevato e' opportuno utilizzare un altro proxy come nginx o l'http router di uWSGI. Chiedi informazioni allo staff per il setup

.. parsed-literal::
   Fare caching su disco e' inutile (e spesso dannoso), il tuo account Unbit ha molte piu' risorse CPU che I/O. Usa la memoria per il caching.
   Soluzioni come **mecached** o **redis** sono perfette. Fare caching su db e' INUTILE.
