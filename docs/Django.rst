Deploy di una applicazione Django
=================================

Django e' uno dei web-framework piu' noti in ambiente python.

Essendo WSGI-compliant puo' essere eseguito sotto uWSGI.


Creare l'ambiente
*****************

Il primo passo sara' istallare i moduli necessari all'applicazione.

Il sistema piu' comodo e' sicuramente quello delle virtualenv.

Creiamo quindi il nostro virtualenv con la versione di python preferita (da scegliere in /opt/unbit).

Se ad esempio opteremo per python 2.7.3:

.. parsed-literal::
   /opt/unbit/python273/bin/virtualenv foobar

dove foobar sara' il path della nostra virtualenv.

A questo punto istalliamo i moduli di cui necessitiamo:

.. parsed-literal::
   ./foobar/bin/pip install django django-mptt requests


istallera' django, django-mptt e requests nella nostra virtualenv

Configurare l'applicazione
**************************

Fate l'upload della vostra applicazione (preferibilmente all'interno di /www per permettervi di passare da un webserver all'altro
senza problemi di permessi) e create il vostro file di configurazione per uWSGI:

.. code-block:: ini

   [uwsgi]
   plugins = python273
   virtualenv = foobar
   chdir = myapp
   module = wsgi

La prima direttiva (**plugins**) indica quale versione di python caricare.

**virtualenv** permette di specificare il path della virtualenv, **chdir** dovrebbe puntare alla directory in cui risiede il
vostro progetto django (la directory che contiene il file wsgi.py). L'ultima direttiva carica il file wsgi.py dal vostro progetto (istallato
di default da django 1.4).


Configurare il dominio (Apache)
*******************************

Sul pannello di controllo assegnate il container al dominio per visualizzare le opzioni UPSTREAM.

Settate la docroot in una directory (all'intrno di /www) che conterra' i vostri file statici. Puo' anche essere una directory vuota, l'importante e' che esista.

Abilitate il checkbox **upstream** e impostate **upstream_cmd** a 

.. parsed-literal::
  uwsgi file.ini

dove file.ini sara' il percorso (relativo alla docroot impostata) del file di configurazione di uWSGI. (per comodita' vi consigliamo
di usare sempre percorsi assoluti)


Tuning
******

La configurazione di base e' estremamente semplice, in base alle risorse acquistate potrete decidere di avviare piu' processi, un master o piu' thread.

Ad esempio una configurazione abbastanza standard e' avere 1 master e 2 worker:

.. code-block:: ini

   [uwsgi]
   plugins = python273
   virtualenv = foobar
   chdir = myapp
   module = wsgi
   master = true
   processes = 2
