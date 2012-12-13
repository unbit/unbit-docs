Deploy di Zope+Plone
====================

Requisiti: container da 300MB, 2 GB spazio disco

Scaricare dal sito ufficiale di Plone lo '''Unified Installer''' e decomprimerlo all'interno dela propria home.

Spostarsi all'interno della directory appena creata e lanciare

.. parsed-literal::

   ./install.sh standalone

Ogni versione di Zope richiede una specifica versione di python. Molto probabilmente la versione richiesta e' gia disponibile sul sistema.
In tal caso per risparmiare tempo, spazio disco (e denaro) si puo' lanciare i lcomando precedente come

.. parsed-literal::

   ./install.sh standalone --with-python=/opt/unbit/python273/bin/python

in questo modo si utilizzera' python 2.7.3 (o la versione che preferite) di sistema anziche' compilarne una nuova.

Al termine dell'istallazione (che dovrebbe richiedere tra i 10 e i 15 minuti), troverete la vostra istanza all'interno della directory
Plone/zinstance della vostra home

Scelta delle porte
******************

Come gia' dovresti sapere, ogni account Unbit puo' fare il binding su una porta ben specifica (corrispondente allo uid dell'account)
di una delle interfacce tra 127.0.0.2 e 127.0.0.255

Il primo passaggio da effetuare quindi e' editare il file Plone/zinstance/buildout.cfg e impostare la direttiva http-address.

Ad esempio se il proprio uid e' 19681, si dovra' inserire:

.. parsed-literal::

   http-address = 127.0.0.17:19681

ovviamente si puo' scegliere l'indirizzo piu' adatto (o per lo meno non ancora utilizzato)

Ora bisogna generare la configurazione di Zope. Per farlo e' sufficiente lanciare lo script:

.. parsed-literal::
   Plone/zinstance/bin/buildout

dopo qualche secondo la nostra istanza sara' pronta all'avvio

Avvio e stop dell'istanza
*************************

Per avviare l'istanza si puo' usare lo script

.. parsed-literal::
   Plone/zinstance/bin/plonectl start

Mentre per fermarla

.. parsed-literal::
   Plone/zinstance/bin/plonectl stop

Associare l'istanza a un dominio
********************************

A differenza del solito non useremo un tunnel ssh per il primo test (sebbene si possa configurare normalmente).
Questo perche' Zope ha un sistema di costruzione delle url abbastanza particolare (per essere gentili).

Come al solito ci viene in aiuto uWSGI, quindi il primo passo e' caricare un file di configurazione all'interno
di una docroot (www/nomedominio) con questo contenuto (dovrebbe andare bene in qualsiasi contesto,bisogna solo adattare
nome dominio e indirizzo dell'istanza zope)

.. code-block:: ini

   [uwsgi]
   nome_dominio = unbit.it
   indirizzo_zope = 127.0.0.17:19681
   
   plugins = router_http
   offload-threads = 8
   route-uri = (.*) http:%(indirizzo_zope),%(nome_dominio),/VirtualHostBase/http/%(nome_dominio)$1

mentre se si vuole utilizzare https

.. code-block:: ini

   [uwsgi]
   nome_dominio = unbit.it
   indirizzo_zope = 127.0.0.17:19681
   
   plugins = router_http
   offload-threads = 8
   route-uri = (.*) http:%(indirizzo_zope),%(nome_dominio),/VirtualHostBase/https/%(nome_dominio)$1

Abilitiamo upstream per il nostro dominio e impostiamo upstream_cmd per lanciare uwsgi (almeno versione 1.4) con il nostro file di configurazione

.. parsed-literal::
   uwsgi14 plone.ini

A questo punto attendete 30 secondi, visitate il dominio e configurate la vostra prima istanza Plone.


