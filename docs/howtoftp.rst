---------------------
Creazione accesso FTP
---------------------

Dal pannello di controllo andare nella sezione **Gestione ftp**

Nella parte sinistra vi sono gli accessi ftp attualmente presenti per l'account. 

Nella colonna di destra è possibile creare un nuovo accesso inserendo:

- **id**: username che viene usato per l'accesso

- **password**: password legata allo username

- **home**: la directory a cui si accedera' attraverso l'accesso ftp.

Tale directory deve necessariamente esistere all'interno dello spazio ftp affinche' vi si possa accedere. E' buona norma alla creazione del primo accesso ftp, lasciare il campo home vuoto, in modo di avere un accesso ftp a tutti i propri file e directory.

Un qualsiasi sito ha generalmente come radice **/www/dominio** dove **dominio** è il nome del dominio registrato. Se si vuole quindi creare un accesso al solo spazio di un sito basta impostare il campo **home** a **/www/dominio**.

**'Nel caso in cui si voglia accedere a tutti gli spazi relativi ai propri siti basta impostare la home a /www**

'Per poter utilizzare l'accesso creato tramite un qualsiasi programma ftp bisogna inserire come host **ftp.dominio**, e la username e password impostate nel pannello di controllo. 
