----------------------------
SPF: Sender Policy Framework
----------------------------

Il protocollo SPF è uno dei metodi che hanno i provider di combattere lo spam. Permette infatti all'amministratore di un dominio di specificare da quali indirizzi ip è lecito che provengano le e-mail di quel dominio.

Questo si realizza inserendo le policy nel record TXT della zona DNS del dominio, secondo la sintassi che si può trovare a questo indirizzo:

- http://www.openspf.org/SPF_Record_Syntax

Le impostazioni di default su Unbit sono queste:

.. parsed-literal::
   v=spf1 ip4:81.174.68.0/24 ~all

che danno maggiore priorità alle e-mail provenienti dalla nostra rete.

Inserendo una riga spf nel record TXT di un dominio nella rete di Unbit si può avere il controllo sui criteri di affidabilità di un singolo server o di una rete per quanto riguarda l'invio delle e-mail.

Per maggiori informazioni:

- http://tools.ietf.org/html/rfc4408

- http://www.openspf.org/
