Informazioni tecniche di base
=============================

 - La home del tuo account e' mappata sulla directory /accounts/<account>, se il tuo account si chiama topogigio, la home corrispondera' ad /accounts/topogigio
 - Un link simbolico /proc/unbit punta sempre alla tua home
 - Ogni account puo' fare il binding sulla porta corrispondente al suo uid sugli indirizzi da 127.0.0.2 a 127.0.0.255
 - Ogni account puo' fare il binding sulla rete lan Unbit (per il clustering) sulla porta corrispondente al suo uid sugli indirizzi da 192.168.240.x a 192.168.243.x (il valore di x e' dipendente dal webserver)
 - Le informazioni sull'utilizzo di memoria (e gli eventuali errori) di un container sono disponibili nella sezione Container del pannello di controllo
 - Le uniche porte TCP aperte in uscita sono la 80,8080,443,8443,22,5222,3690,9418
 - In entrata le uniche porte aperte sulle interfacce pubbliche sono la 80,8080,443
 - Per inviare email dalle applicazioni si puo' utilizzare 127.0.0.1:25 come servizio (il limite e' di 100 email inviate ogni 5 minuti)
 - Le porte TCP/UDP assegnate a un account non sono accessibili dagli altri account
 - Non ci sono limiti sui socket UNIX
 - Puoi accedere via ssh ad un altro account (ovviamente devi avere chiave/password) usando la rete 192.168.0.x (dove x e' il numero identificativo del server)
 - Non puoi accedere ai database server condivisi direttamente da remoto (usa i tunnel ssh)
 - Se devi effettuare transazioni FTP (ma devi proprio), puoi utilizzare il proxy squid in ascolto sull'indirizzo 192.168.0.19 porta 80
