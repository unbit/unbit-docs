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
