======
Deployment su Unbit
======

******
Introduzione
******

Ricevute le tue credenziali ed effettuato
l'accesso al pannello di controllo dovrai decidere come suddividere le risorse
tra i tuoi domini (ovviamente se hai un solo dominio la scelta e' abbstanza facile...)

Nel caso di una gestione a processi dovrai scegliete quanti assegnarne (in base al volume
di concorrenza necessario) o, se hai optato per una gestione a container dovrai semplicemente specificare in quale container
far girare le tue applicazioni (quindi i tuoi processi). Di nuovo, se disponi di un solo container la scelta e' molto semplice.


******
Processi e container
******

E' bene ripassare le differenze tra gestione a processi e gestione a container.

Nel primo caso hai un numero limitato di applicativi (processi) che potrai avviare.
Ad esempio ogni richiesta a un'applicazione php tiene impegnato un processo che non potra' gestire nuove richieste
fin quando la richiesta corrente non si sara' conclusa. Avendo un secondo processo si potranno gestire due richieste contemporaneamente
e cosi' via. Quando non ci sono processi a disposizione le richieste rimangono in una coda in attesa di essere processate. La dimensione
di questa coda (ovvero quante richieste possono restare in attesa) e' dipendente dal timeout impostato (vedi spiegazione piu' sotto)

La gestione a Container e' estremamente piu' semplice e piu' vicina alla logica di funzionamento di un normale server. Ogni container
e' un micro-server (con un quantitativo limitato di memoria e spazio disco) in cui potrai far girare tutte le applicazioni (processi) che vorrai finno all'esaurimento della
memoria dedicata.

Se sei in dubbio tra gestione a processi e a container, scegli sempre i container, avrai meno mal di testa (anche se qualche soldo in meno nel portafogli).

In uno stesso account possono convivere piu' container, questo ti permette di isolare le applicazioni facilmente e di tenerle sotto controllo.

******
I Timeout
******

Di default ogni richiesta ad una applicazione deve concludersi entro 10 secondi. Puoi modificare questo timeout fino a un massimo di 300 secondi.
Il timeout incide sul numero di richieste che possono rimanere in attesa in caso di mancanza di risorse. La formula e' (30 - (timeout/10) + 3), il che significa che con l'impostazione di default (10 secondi) potrai gestire fino a 32 richieste in coda. Ricorda sempre che una buona applicazione web deve generare una risposta in meno di un secondo. Tienilo a mente, i tuoi utenti te ne saranno grati.


*******
Avviare le applicazioni: UPSTREAM
*******

UPSTREAM e' il sistema che gestisce l'avvio delle applicazioni sui server Unbit. Ad ogni richiesta il webserver verifica la disponibilita' di un canale (un semplice socket UNIX) con l'applicazione associata al dominio. Se questo canale non e' disponibile, viene avviata una nuova istanza dell'applicazione. Un ulteriore sistema di verifica (basato sull'assegnare una 'firma' ad ogni processo) evita che piu' istanze della stessa applicazione vengano avviate.

******
Configurare UPSTREAM
******

Accedendo alle opzioni del dominio e' possibile configurare UPSTREAM. Il primo passaggio da effettuare e' selezionare il checkbox 'upstream' e successivamente impostare 'upstream_cmd' con il comando (e i suoi argomenti) da avviare. Praticamente si tratta di una shell. Ovviamente ogni utente ha i suoi application server preferiti, ma per semplificare le cose forniamo una serie di 'wizard' che eviteranno agli utenti che fanno un uso piu' "classico" della piattaforma di doversi sposrcare le mani o prendere decisioni alla cieca. Sono disponibili wizard per moltissimi ambienti, se non trovi quello che fa per te e non sai configurare un application server, contatta lo staff o consulta le nostre guide avanzate.
