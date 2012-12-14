--------------------
Gateway mail2webapp
--------------------

Il **Gateway** Mail2WebApp ti permette di associare uno script web a una mailbox.

Questo script verra' lanciato alla ricezione di ogni singola mail, passandogli 2 parametri tramite metodo POST:

**mailbox** => contiene il nome della mailbox

**mail** => contiene il corpo della mail comprensivo di header e allegati (formato mime)

Puoi utilizzare questa funzionalita' per sviluppare diverse soluzioni, dai ticketing system al parsing delle risposte inviate via posta elettronica alla semplice archiviazione su database dei messaggi.

Se, per esempio, volessimo archiviare le email in arrivo in un database, è sufficiente creare uno script (per questo esempio utilizziamo PHP4), che contiene le istruzioni necessarie. Mettiamo lo script in una **directory presente in un dominio dell'account**.

Per questo esempio chiamiamo lo script 'insert_mail.php', nella dir 'webapp' sotto il nostro dominio

I nomi sono indicativi, per i vostri file potete utilizzare quelli che preferite.

Lo script contiene queste istruzioni: 

.. parsed-literal:: 
   <?php
   ## inserire istruzioni per connessione al database ##
   $mailbox = $_POST['mailbox'];
   $mail = $_POST['mail'];
   $query = "INSERT INTO mail (mail) VALUES ('$mail')";
   mysql_query($query) or die(mysql_error());
   ?>

All'arrivo di una email lo script verrà lanciato in automatico e l'email verrà quindi archiviata nel db.

Per associare lo script alla mailbox accedi alle impostazioni della mailbox nel pannello di controllo e indica il percorso dello script nel campo 'Gateway mail2webapp'
