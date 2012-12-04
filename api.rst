La api (REST) di Unbit
======================

Puoi consultare (e modificare) la configurazione del tuo account e delle risorse usando delle semplici richieste HTTPS.

I formati di output supportati sono XML, JSON e YAML.

Per effettuare accessi alla api e' necessario autenticarsi con le stesse credenziali del pannello di controllo (che in effetti non e' altro che un client per la api)
usando l'HTTP basic auth.

Il metodo GET e' usato per ottenere le informazioni

Il metodo POST e' utilizzato per creare nuove risorse

il metodo PUT per crearne di nuove


account
*******

https://rest.unbit.it/account.xml

https://rest.unbit.it/account.json

https://rest.unbit.it/account.yaml

domini
******

tutti:

https://rest.unbit.it/domains.xml

https://rest.unbit.it/domains.json

https://rest.unbit.it/domains.yaml


singolo (N e' l'id del domnio):

https://rest.unbit.it/domains/N.xml

https://rest.unbit.it/domains/N.json

https://rest.unbit.it/domains/N.yaml
