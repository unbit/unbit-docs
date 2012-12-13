---
FAQ
---

Questa sezione riporta le domande piu' frequenti riguardo gli aspetti meno "tecnici" dell'infrastruttura. In particolare
sui servizi secondari come email e registrazioni domini. Per tutte le informazioni tecniche, la sezione di riferimento
e' quella degli `Howto </houto>`_

- **Cos'è Unbit?**

Unbit è una piattaforma per la fornitura di servizi internet basata su software opensource. 
Non rientra nella classica concezione di 'hosting' poiche' garantisce un isolamento molto forte dei singoli utenti, ma
non e' neanche una soluzione 'vps' in quanto il singolo utente non ha privilegi di root. E' molto probabilmente quella
che si definisce PaaS (Platform As A Service), ma il termine potrebbe essere fuorviante in quanto spesso applicato a contesti
di cloud computing. Un elemento di forza che amiamo sottolineare e' che Unbit non lavora in regime di overselling, qualsiasi risorsa
assegnata al cliente e' garantita.

- **In rete si trovano molti riferimenti ai vostri prodotti (tutti opensource), siete una software house o una societa' di servizi ?**

In un mercato fortemente competitivo come quello dei servizi internet, dove spesso si tende a competere sui prezzi ma non sulla componente tecnica,
abbiamo deciso di puntare su quello in cui ci sentiamo piu' bravi: sviluppare soluzioni per gli ambienti di deployment piu' disparati.
Questo implica che potrai costruire la stessa infrastruttura Unbit anche su server esterni, usando i nostri prodotti.

- **Come mai devo inviare un contratto anziche' compilare un semplice form ?**

I servizi di Unbit sono esclusivamente pensati per sviluppatori e aziende ed entrambi i target sanno bene quanto sia importante la tutela di un contratto in ambienti lavorativi.

- **Rappresento una società di servizi su web, vorrei offrire hosting ai miei clienti.**

Preparaci un prospetto delle tue esigenze e proveremo a individuare la migliore soluzione.

- **Non sono molto pratico di internet ma voglio avere un mio sito.**

La nostra stuttura e' molto complessa e difficilmente utilizzabile da un non tecnico. Tuttavia abbiamo un buon numero di rivenditori che potranno fornirti supporto e fare da tramite con il nostro staff.

- **Non ho tempo/voglia di leggere tutta la documentazione sui vari servizi, mi spiegate cosa devo fare ?**

Nulla, molto probabilmente non siamo il fornitore adatto a te.

- **Uso degli strumenti poco diffusi, potete dare supporto anche a me?**

Dipende che intendi per strumenti poco diffusi, se ti riferisci al sistema operativo, non farti scrupoli, ne abbiamo visti di tutti i colori ;)


- **Voglio realizzare un sito o una applicazione, potete aiutarmi**

Unbit prima di fornire servizi, sviluppa software, quindi si', potremo aiutarti, ma non aspettarti prezzi da ortofrutta, non ci svendiamo. MAI.
In alto a destra sul sito trovi il link a unbit.is che e' la nostra divisione 'creativa'

- **Come faccio a diventare vostro cliente?**

Leggi attentamente il contratto in ogni suo punto, compilalo (in modo leggibile) e invialo via fax o in pdf via mail.

- **Che diavolo è un account Unbit?**

Un account Unbit è un identificativo che ti viene assegnato e ti permetterà di gestire tutti i tuoi servizi e di acquistarne di nuovi senza effettuare lunghe procedure.


- **Avrei bisogno del servizio XYZ, ma non lo vedo in listino, cosa posso fare?**

Scrivi una mail a info@unbit.it, il nostro staff ne valuterà un eventuale inserimento nella piattaforma.

- **Ok, mi avete convinto, voglio diventare vostro cliente, come posso pagare?**

Puoi pagare con bonifico bancario, postagiro o il classico paypal.

- **Ho acquistato un' offerta che ora non e' piu' presente in listino, cosa succedera' alla scadenza del servizio ?**

Nulla :) Se si acquista l'offerta XYZ si continuera' a pagare per l'offerta XYZ. Solo in caso vi siano nuove offerte piu' vantaggiose economicamente provvederemo ad avvertire il cliente della possibilita' di un passaggio.

- **Come gestite la priorita' delle richieste per il supporto tecnico ?**

Si da' priorita' a tutte le situazioni che a causa di una configurazione errata, poca chiarezza nella documentazione, malfunzionamenti software generino il down di un sito. Hanno invece bassa priorita' tutte le richieste non pertinenti il nostro servizio (come l'aiuto nella configurazione di applicativi non sviluppati da noi) e richieste le cui risposte sono presenti sul wiki o nelle faq. Preghiamo inoltre tutti i clienti di non richiedere un contatto telefonico se non hanno acquistato tale servizio. Per correttezza nei confronti dei clienti paganti non daremo mai supporto telefonico a chi non lo ha acquistato. Saremo comunque noi a telefonare in caso di necessita'.

- **Come funziona il supporto telefonico ?**

Il supporto telefonico va inteso come 'canale' di emergenza, in tutte le situazioni in cui non sia possibile per il cliente contattarci via mail. Gli operatori che rispondono alle chiamate possono non essere qualificati a risolvere problemi che l'helpdesk standard impiegherebbe pochi minuti a processare. Se un operatore non puo' evadere una richiesta, questa viene passata con la massima priorita' al primo tecnico disponibile che provvedera' a ricontattare (telefonicamente) il cliente il prima possibile.

- **Posso ridistribuire le risorse acquistate tra i domini/sottodomini del mio account ?**

Si,dal pannello di controllo puoi riassegnare container e processi come preferisci.


Mail
****

- **Quale è il server POP3/IMAP per poter scaricare la posta sul mio client mail ?**

L'indirizzo del server POP3/IMAP4 è mail.unbit.it. Ricorda di abilitare sempre l'SSL per usufruire del servizio.

- **Quale è il server SMTP per poter inviare la posta dal mio client mail ?**

L'indirizzo del server SMTP è quello che ti viene indicato dal provider che ti fornisce la connessione a Internet. In alternativa puoi richiederci l'attivazione del servizio SMTP autenticato (se il tuo piano non lo prevede)

- **Ricevo un sacco di mail con Subject ===SPAM=== che succede?**

Puoi stare tranquillo, è solo il nostro servizio antispam (basato su SpamAssassin) che ha riconosciuto una mail come spam e l'ha marchiata.

- **Posso disabilitare l'antispam?**

Dal panello di controllo clicca sul nome della mailbox in questione e accederai alle sue impostazioni.

- **Che differenza c'è tra una mailbox e un indirizzo?**

Ogni indirizzo email deve avere una destinazione che può essere una directory su un disco o un altro indirizzo. Una mailbox non è altro che una directory in cui salvare le proprie mail. Quando si scarica la posta non si fa altro che leggere il contenuto della propria mailbox. Ovviamente diversi indirizzi possono salvare all'interno della stessa mailbox.

- **Posso salvare le mail inviate a un indirizzo in più mailbox?**

Certo, puoi configurare i tuoi indirizzi in decine di modalità diverse dal pannello di controllo unbit.

- **Come posso configurare un autoresponder?**

Se vuoi puoi sviluppare un tuo autorespnder utilizzando il **gateway mail2webapp** ma non forniremo alcun supporto. Purtroppo, sebbene di largo uso, e' una tecnica contraria alla netiquette, pertanto non e' supportata da Unbit.


Registrazione e gestione domini
*******************************

- **Quali domini posso registrare?**

Tutti i principali e tutti quelli geografici per cui non sono richiesti particolari requisiti, scrivi sempre a info@unbit.it per sapere se possiamo registrare una determinata estensione.

- **Cos'è un redirect?**

Attivando un redirect puoi reindirizzare le richieste del tuo dominio a un altro sito. È molto utile in caso tu abbia uno stesso dominio con diverse estensioni ma con gli stessi contenuti.

- **Dove è finito il www davanti al mio sito?**

È la domanda che ci viene fatta più spesso. è tutto normale, le richieste a www.nomedominio vengono reindirizzate direttamente al nome del dominio. Usare il www è una convenzione, lo staff di unbit ha reputato che fosse meglio avere nomi più corti mantenendo comunque la compatibilità con il classico www, tuttavia i gusti non si discutono, se vuoi che il www davanti al nome del dominio non sparisca in automatico puoi abilitare il checkbox **www** sul pannello di controllo nella sezione gestione domini.

Banda e traffico
****************

- **Quanta banda potete garantirmi? E che limiti di traffico ci sono?**

Per ogni dominio e' garantito un minimo di 64kbit/s di banda. Ovviamente questa e' la velocita' minima che puoi aspettarti in caso di sovraccarico della nostra rete.

L'utilizzo di banda e' costantemente monitorato e puoi consultare i grafici di consumo delle tue applicazioni dall'apposita sezione del pannello

- **Ho bisogno di piu' banda garantita, cosa posso fare?**

Puoi richiedere banda minima garantita per un dominio o un sottodominio dal pannello di controllo o contattando l'assistenza.


Backup
******

- **Farete un backup del mio sito?**

Della home directory, dei database condivisi, delle mail (nei limiti consentiti dalla legge), delle configurazioni e di tutto quello che concerne un account. Il backup dei database condivisi viene effettuato ogni notte e ruotato ogni mese (quindi avrai sempre 30 backup a disposizione). Per tutti gli altri servizi il backup e' settimanale e incrementale. Se perdi un file o corrompi il database e' tuo diritto chiederci i dati, ma dovremo valutare di volta in volta se sara' necessaria una spesa per il ripristino o meno. La fornitura dei backup dei database e' invece sempre gratuita e praticamente immediata.

