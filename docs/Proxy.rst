=================================
Associare un vassal ad un dominio
=================================

Una volta avviato un vassal, come descritto nella guida dell'Emperor_ è possibile associarlo ad un dominio. Per questo si può usare uWSGI come proxy per le richieste http.

.. _Emperor: https://unbit.it/docs/Emperor

Configurare un dominio
**********************

Nel pannello di controllo del dominio assicurati di aver spuntato la voce **upstream** e che non sia selezionato alcun wizard. Nel campo **upstream_cmd** inserisci una riga così:

.. parsed-literal::

    uwsgi /proc/unbit/**proxy_file.ini**


Creare un proxy
***************

Il **proxy_file.ini** visto prima è un file di configurazione di uWSGI che inoltra le richieste dal dominio al vassal.

Un esempio di proxy_file può essere:

.. code-block:: ini

    [uwsgi]
    plugins = 0:router_uwsgi
    route-run = uwsgi:/proc/unbit/sockets/uwsgi_php54.sock
    offload-threads = 8
    disable-logging = true

Esistono moltissime possibilità di personalizzazione, per maggiori informazioni vedi la documentazione ufficiale di uWSGI InternalRouting_.

.. _InternalRouting: https://uwsgi-docs.readthedocs.org/en/latest/InternalRouting.html
