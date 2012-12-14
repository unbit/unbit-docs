Primo Contatto
==============

Una volta inviato il contratto e completata la procedura di attivazione riceverai le tue credenziali
per il pannello di controllo.

Il pannello e' un client per la nostra Api, quindi **ricorda sempre che potrai automatizzare le varie operazioni**.


Dopo il login, la prima sezione disponibile sara' quella con le informazioni dell'account.

Da questa area sara' possibile modificare la propria password (**ti consigliamo di farlo subito**) e impostare i riferimenti tecnici.

In questa sezione e' anche possibile impostare le **quote disco** e le **chiavi ssh**.

I Domini
========

Generalmente, per accedere alla tua applicazione avrai bisogno di un **nome di dominio**. Potresti averne acquistato uno direttamente da noi,
o potresti aver semplicemente configurato un puntamento Dns, in ogni caso troverai tutti i domini assegnati all'account nella sezione **'Gestione domini'** del pannello di controllo.

Nella schermata di riepilogo sono riportate varie informazioni (oltre al nome):

**id** -> valore numerico che identifica il dominio nei database Unbit (l'id e' utilizzato per le chiamate alla Api)

**dominio** -> nome del dominio

**map_to** -> puoi mappare le risorse di un dominio su quelle di un altro (il map_to riporta il nome del dominio di riferimento)

**redirect** -> commodity che effettua un redirect (301 o 302) automatico ad un altro dominio

**docroot** -> document root del dominio

**risorse** -> risorse assegnate al dominio


Configurare un dominio per eseguire applicazioni
================================================

Una volta cliccato sul nome di un dominio accederai alle sue opzioni.

La prima operazione e' **assegnare delle risorse** (generalmente un Container) al dominio. Una volta applicata la modifica si rendera' disponibile la sezione **UPSTREAM** sul pannello.

**UPSTREAM** e' lo strato software che si occupa di gestire i processi web (dal semplice script php alla piu' complessa applicazione WSGI).

Le opzioni piu' importanti sono **upstream** (ovviamente) che abilita il motore, **upstream_wizard** e **upstream_cmd** (una esclude l'altra) che istruiscono **UPSTREAM** sul tipo di applicazione da eseguire. Per le configurazioni piu' semplici sono disponibili dei wizard (disponibili sotto la voce **upstream_wizard**), quindi se devi (per esempio) eseguire semplici applicazioni php, **seleziona il wizard che piu' si avvicina alle tue necessita'** (in termini di versione di php) e lascia **upstream_cmd** vuoto.

**Attendi 30 secondi**, e se tutto e' andato come previsto, il sistema eseguira' qualsiasi script php caricato nella docroot. Per caricare file nel tuo account puoi usare `SSH/SSFTP </docs/ssh>`_ ma e' possibile configurare accessi **FTP/FTP-SSL**. Ti ricordiamo che il protocollo FTP (non FTP-SSL) trasferisce le tue credenziali in chiaro, quindi e' altamente insicuro. Se il tuo client FTP non supporta l'SSL evita
almeno di salvare le password (specialmente se usi sistemi Windows)


