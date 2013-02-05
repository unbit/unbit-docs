---------------------
Creazione accesso FTP
---------------------

Dal pannello di controllo andare nella sezione **FTP/FTPS/SFTP**

Nella parte destra vi sono gli accessi attualmente presenti per l'account.

Nella colonna di sinistra è possibile creare un nuovo accesso inserendo:

- **id**: username che viene usato per l'accesso

- **password**: password legata allo username

- **home**: la directory a cui si accedera' attraverso l'accesso ftp

**Tale directory deve necessariamente esistere all'interno dello spazio ftp affinche' vi si possa accedere**. E' buona norma alla creazione del primo accesso ftp, lasciare il campo **home** vuoto, in modo di avere un accesso ftp a tutti i propri file e directory.

Un qualsiasi sito ha generalmente come radice **/www/dominio** dove **dominio** è il nome del dominio registrato. Se si vuole quindi creare un accesso al solo spazio di un sito basta impostare il campo **home** a **/www/dominio**.

**Nel caso in cui si voglia accedere a tutti gli spazi relativi ai propri siti basta impostare la home a /www**

Per poter utilizzare l'accesso creato tramite un qualsiasi programma ftp bisogna inserire come host **ftp.dominio**, e la username e password impostate nel pannello di controllo.

**NOTA**: L'uso del protocollo ftp è fortemente sconsigliato perché privo di qualunque forma di crittografia dei dati che transitano nella rete, inclusi username e password.

Selezionando la casella **ftp_ftps** avrai a disposizione non solo il protocollo ftp ma anche ftps, ovvero la versione 'sicura', su protocollo TLS, di ftp.

La casella **sftp** invece abilita, per l'account che stai creando, il protocollo sftp. Questo oltre alla crittografia del canale di trasmissione dati supporta anche l'autenticazione con chiave privata. Sarà sufficiente creare una coppia di chiavi sul proprio computer con il comando:

.. parsed-literal::

    ssh-keygen -f ~/.ssh/unbit

e ricavare la chiave pubblica nel formato RFC4716:

.. parsed-literal::

    ssh-keygen -e -f ~/.ssh/unbit

L'output di questo comando è quello che vorrai inserire nel campo **sftp keys**

