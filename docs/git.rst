---
GIT
---

È possibile sfruttare il sistema di controllo delle versioni *git* [1]_ controllandolo via ssh [2]_ .
Di seguito presentiamo una breve guida per iniziare con *git*. Il prompt **local$** indica un comando da eseguire sul computer locale, mentre **unbit$** segnala che il comando è da inviare al server unbit via ssh.

Per prima cosa dovrai creare un repository vuoto:

.. parsed-literal::
    **unbit$** mkdir repo && cd repo
    **unbit$** git init --bare

A questo punto avrai un repository 'bare' nel tuo account.
Dovrai quindi creare il repository locale, quello su cui lavorerai, che risiederà sul tuo computer, e configurarlo per inviare i cambiamenti a quello su Unbit:

.. parsed-literal::
    **local$** mkdir repo && cd repo
    **local$** git init
    **local$** git remote add origin ssh://unbit/~/repo

Una volta inizializzato il repository è pronto e puoi iniziare a copiare i tuoi file al suo interno.

.. parsed-literal::
    **local$** cp ../miei_file.* .
    **local$** git add miei_file.*
    **local$** git commit -m "Aggiunti i primi file al repository"

A questo punto non ti resta che inviare i cambiamenti al server:

.. parsed-literal::
    **local$** git push origin master


**TIP**
Se vuoi dare ai tuoi collaboratori l'accesso al tuo repository ma non a tutto il tuo account puoi specificare delle chiavi ssh ristrette al solo uso di git.
Per farlo ti basterà modificare la stringa della chiave relativa nel campo **Chiavi SSH** del pannello di controllo, che diventerà qualcosa di simile:

.. parsed-literal::
    **command="git-shell -c \"$SSH_ORIGINAL_COMMAND\"",no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty** ssh-rsa AAAAB[...]

In questo modo l'utente che tenterà di accedere con quella specifica chiave avrà accesso soltanto ai repository git mentre gli verrà rifiutato l'accesso alla shell di sistema.

.. [1] http://git-scm.com/
.. [2] http://test2.unbit.it/docs/ssh
