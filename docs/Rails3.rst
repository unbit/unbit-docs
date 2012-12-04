Deploy di una applicazione Rails 3.x
====================================

Rails3 e' completamente Rack-compliant, quindi non avrai bisogno di configurazioni particolari per eseguirlo.

Il primo passaggio e' caricare la directory della tua applicazione all'interno di /www nella tua home.

Grazie all'uso di Bundler potrai gestire le gemme (e le loro dipendenze) con estrema facilita'

Ricorda sempre che nel sistema sono disponibili diverse versioni di ruby, fai un giro (via ssh) dentro /opt/unbit
per vedere quale e' la piu' adatta al tuo scopo.

Una volta scelta la versione (ad esempio /opt/unbit/ruby193) potrai aggiungere la sua directory /bin al tuo PATH (per evitare di dover
scrivere lunghe linee di comando ogni volta) oppure potrai usare le scorciatoie messe a disposizione:

ruby193 -> lancia il comando /opt/unbit/ruby193/bin/ruby

gem193 -> lancia il comando /opt/unbit/ruby193/bin/gem

bundle193 -> lancia il comando /opt/unbit/ruby193/bin/bundle

rake193 -> lancia il comando /opt/unbit/ruby193/bin/rake193


Quindi per eseguire il classico bundle install potrai utilizzare

bundle193 install --path vendor/gemme

oppure

/opt/unbit/ruby193/bin/bundle install --path vendor/gemme

L'argomento --path vendor/gemme e' un "trucco" per salvare le gemme necessarie all'applicazione
in una directory specifica. Sebbene ora potrebbe esembrare in utile, diventera' molto comodo per implementare dei set di gem
riutilizzabili.

A questo punto configura il database.yml e lancia la prima migration (se necessario) ricordandoti sempre di specificare RAILS_ENV=production
in caso non stessi utilizzando l'ambiente di sviluppo.

Una volta completato il setup dell'applicazione loggati sul pannello di controllo Unbit e accedi alle opzioni del dominio.

Imposta la docroot (che e' sempre relativa a /www) alla directory /public all'interno della tua applicazione (esempio myapp/public).

Abilita upstream e imposta upstream_cmd a 'uwsgi config.ini'

config.ini e' il file di configurazione di uWSGI (da caricare all'interno di /public). Puoi usare l'esempio qui sotto come base,
ma ti consigliamo di personalizzarlo in base alle tue esigenze. La configurazione sottostante e' molto utile se si usa Heroku come ambiente di test.



.. code-block:: ini

   [uwsgi]
   ; carico il plugin per ruby 1.9.3
   plugins = 0:rack193
   ;impostare il nome del dominio
   dominio = XXX
   ; impostare il numero di processi da avviare
   processi = 2
   ; scrivi i log nel file specificato
   logto = ../%(dominio).log
   ; mi sposto fuori da public
   chdir = ..
   ; decommentarlo per andare in produzione
   env = RAILS_ENV=production
   ; abilito il master che fa tante cose divertenti tra cui controllare se
   ; i worker sono in salute
   master = true
   ; avvio 4 processi
   processes = %(processi)
   ; carico l'applicazione una volta per worker, anziche' all'inizio per poi chiamare
   ; fork(). Consuma piu' memoria ma e' come funziona l'application server di heroku
   lazy-apps = true
   ; quando 'tocco' uno di questi file, riavvia il server
   touch-reload = reload.txt
   ; %p viene automaticamente trasformato nel percorso del file di config
   touch-reload = %p
   ; do' un nome 'decente' ai processi
   auto-procname = true
   procname-prefix-spaced = [%(dominio)]
   ; esporta le statistiche (formato json) del server
   ; sul socket 'statistiche.sock'
   stats = statistiche.sock
   ; riporto il consumo di memoria dopo ogni richiesta
   memory-report = true
   ; carico l'applicazione (usando bundler)
   rbrequire = bundler/setup
   rack = config.ru


