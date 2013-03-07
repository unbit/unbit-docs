===========
Apache Solr
===========

Per utilizzare Solr è sufficiente aggiungere un file vassal con questi contenuti:

.. parsed-literal::

    [uwsgi]
    env = JETTY_HOME=/proc/unbit/solr-4.1.0/example
    chdir = /proc/unbit/solr-4.1.0/example
    attach-daemon = java -Djetty.host= **127.0.0.2** -Djetty.port= **19898** -jar start.jar ./etc/jetty.xml

Nella configurazione riportata si fa partire l'esempio contenuto nella versione 4.1.0 facendo il bind sul socket 127.0.0.2:19898 , ma questi parametri potranno essere diversi nella tua configurazione.

Ricorda che la porta dev'essere uguale all'id del tuo account, mentre l'interfaccia di rete può essere qualunque fra 127.0.0.2 e 127.0.0.254 e fra 192.168.241. **N** e 192.168.253. **N** (dove **N** dipende dal server che ospita il tuo account).

Puoi modificare la massima quantità di memoria che verrà utilizzata con il parametro -Xmx di java. Ad esempio, specificando -Xmx100m l'applicazione non supererà i 100 MB di memoria fisica.
