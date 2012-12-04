I Container Unbit
=================

Un Container e' costituito da una quantita' limitata (generalmente tra gli 80MB e i 2GB) di memoria fisica gestita tramite i control groups (cgroups) di Linux e alcuni namespace.

Un namespace e' una risorsa dedicata al Container non ereditata dal sistema principale.

Ogni container ha le seguenti caratteristiche slegate dal sistema:

uts (hostname, machine...)

ipc (shared memory, semafori, code posix...)

Per quanto riguarda la cpu, ogni container ha la stessa quota (generalmente viene garantito l'1% a carico massimo), e non e' possibile modificarla proprio per evitare che un utente ne possa danneggiare un altro.

Lo stessa logica viene applicata all'I/O, anche se (ovviamente) si parla di una risorsa ben piu limitata, quindi cerca di riduddre al minimo gli accessi disco per ottenere le migliori performance (questa in realta'
e' un regola che si applica ad ogni contesto).

Se un Container esaurisce la memoria viene avviato l'OOM killer (Out of Memory Killer) che si occupera' di resettare l'intero container (non preoccuparti e' una operazione che richiede pochi millisecondi) e portarlo allo stato iniziale.

Se la distruzione improvvisa di un processo (ad esempio un database server) potrebbe causare la perdita di dati, ti consigliamo di dedicare un container per questa applicazioni, in modo che processi esterni non
possano scatenarne un riavvio non previsto
