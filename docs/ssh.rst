---
SSH
---

Per tutti gli account Unbit è disponibile l'accesso tramite protocollo ssh. Avrai accesso alla shell del tuo utente dalla quale potrai fare di tutto, dalla semplice gestione dei file alla creazione di un ambiente completamente personalizzato per le tue applicazioni web.

Nel **pannello di controllo**, alla pagina sulle **Informazioni account**, puoi trovare il comando da eseguire per la connessione. Il comando sarà qualcosa come:

.. parsed-literal::
    ssh -p *PORTA* *ACCOUNT*@*SERVER*.unbit.it

dove *PORTA*, *ACCOUNT* e *SERVER* dipendono dal tuo account.
In questo modo potrai accedere utilizzando le credenziali che hai impostato dal pannello di controllo.

Se vuoi collegarti utilizzando l'autenticazione con chiave pubblica questo è possibile, oltre che raccomandato, aggiungendo la chiave pubblica al campo **Chiavi SSH** del pannello di controllo.

**NOTA** I nostri sistemi aggiornano i database delle credenziali (sia password che chiavi) ogni 30 minuti, quindi assicurati di aver aspettato almeno questo intervallo di tempo dopo la modifica.

Per creare una chiave privata è sufficiente dare questo comando sul tuo computer:

.. parsed-literal::
    ssh-keygen -f ~/.ssh/unbit

Questo creerà due file: *unbit* e *unbit.pub* nella directory *.ssh* della tua home. Adesso copia il contenuto della chiave pubblica (*unbit.pub*) nel campo **Chiavi SSH** del pannello di controllo e aspetta 30 minuti, dopodiché potrai collegarti usando questo comando:

.. parsed-literal::
    ssh -p *PORTA* -i ~/.ssh/unbit *ACCOUNT*@*SERVER*.unbit.it

Il comando può risultare lungo da scrivere e da ricordare, quindi ti consigliamo di aggiungere queste righe al file *~/.ssh/config* (se non esiste va creato):

.. parsed-literal::
    Host unbit
    HostName *SERVER*.unbit.it
    Port *PORTA*
    User *ACCOUNT*
    IdentityFile ~/.ssh/unbit

in questo modo la connessione sarà più semplice ma ugualmente sicura:

.. parsed-literal::
    ssh unbit

Hai un application server in ascolto su una porta locale su unbit? Puoi gestirlo sfruttando un tunnel crittato. Ti basta aggiungere questa riga al file *~/.ssh/config*:

.. parsed-literal::
    LocalForward *PORTA_LOCALE* 127.0.0.1:*PORTA_APP_SERVER*

Questo farà sì che quando effettuerai la connessione ssh al tuo account la porta *PORTA_APP_SERVER* verrà inoltrata sulla *PORTA_LOCALE* del tuo account.

Per ulteriori possibilità di configurazione ti rimando alla documentazione ufficiale di ssh.
