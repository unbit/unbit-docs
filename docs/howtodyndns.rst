---------------------------------------------------
Abilitare il servizio di dns dinamico su un dominio
---------------------------------------------------

Il servizio di dns dinamico permette di associare un ip a un nome di dominio in tempo reale. Grazie a questa funzionalita' utenti con indirizzo ip non statico, possono rendere la loro postazione accessibile utilizzando un nome di dominio come se fosse una macchina con ip fisso.

Come funziona ?
***************

Tecnicamente ogni richiesta fatta a un server dns viene mantenuta in cache per un lungo periodo (di norma 8 ore). Questo in caso di server internet non e' un problema poiche' raramente vengono cambiati gli indirizzi ip. Per un sistema con connessione dialup (linee telefoniche,isdn,adsl consumer) invece, il proprio indirizzo tende a cambiare spesso rendendo di fatto il sistema di caching un grosso problema: i server dns manterrebbero in memoria dei dati non piu' congruenti.

Un dns dinamico invece ha un tempo di cache (TTL) molto basso (60 secondi) permettendo all'utente di aggiornare il suo record con un disservizio minimo.

Per abilitare il servizio basta andare sul pannello di controllo nella sezione DNS e spuntare il checkbox **dyndns**

A questo punto con una semplice chiamata XMLRPC/SOAP si potra' assegnare il proprio indirizzo ip:

.. parsed-literal::
   import xmlrpclib

   account = 'xxx'
   password = 'xxx'
   dominio = 'example.com'
   ip = ''

   proxy = xmlrpclib.ServerProxy("https://soap.unbit.it:8192/dom/api")

   domains = proxy.SetDyndnsIp(account,password,dominio,ip)

   print domains

Se il quarto argomento della funzione (l'indirizzo ip) viene lasciato vuoto, il sistema assegnera' al dominio l'indirizzo della macchina che ha fatto la chiamata XMLRPC/SOAP.

**Attenzione**

- Ovviamente il servizio non funziona su reti dietro NAT (fastweb)

- I record MX del dominio non vengono modificati, se si vuole utilizzare la propria macchina come server di posta si puo' configurare un catchalll dalla gestione email sul pannello di controllo 

In Ruby
*******
La medesima procedura utilizzando ruby (1.9.3):

.. parsed-literal::
   require 'xmlrpc/client'
   require 'open-uri'
   
   user = "user"
   password = "password"
   dominio = "dominio"
   ip = open('http://whatismyip.akamai.com').read
   cert_filename = "ca_base64.crt"
   
   server = XMLRPC::Client.new_from_hash({:host =>'soap.unbit.it', 
                               :path => '/dom/api',
                               :port => 8192,
                               :use_ssl => true})
   
   server.instance_variable_get(:@http).verify_mode = OpenSSL::SSL::VERIFY_PEER
   server.instance_variable_get(:@http).ca_file = File.join(File.dirname(__FILE__), cert_filename)
   
   puts server.call("SetDyndnsIp", user, password, dominio, ip)
   
Lo script e' in grado di verificare il certificato presentato tramite SSL. Suppone l'esistenza di un file di nome "ca_base64.crt", nella stessa cartella dello script, contenente il certificato della CA di Unbit salvato con encoding base64.

Per ottenere il certificato aprire con il browser l'indirizzo https://soap.unbit.it:8192/dom/api, richiedere la visualizzazione dello stesso e salvarlo. Per la procedura esatta fare riferimento alla guida del browser prescelto.
