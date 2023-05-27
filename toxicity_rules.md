# Code de la toxicité
L'objectif étant d'avoir les même regles pour labeliser les message

Classement non exaustif du type de message, avec le niveau de toxicité à accorder :

- 0 : message classique / bienveillant *On ne mesure pas la bienveillance, donc tout ce qui n'est pas "malveillant" a un niveau de 0*
- 0.20 : Demande de jouer à un autre jeux / whining
- 0.50 : c'était sur enfait (le  bureau est tapé)
- 0.70 : fils de pute (et ses dérivés)
- 1 : insulte et trashtalk

Ce classement est un guide, le labeliseur est libre d'adapter selon son jugement les points de toxicicté à accorder.

Si vous pensez que le message est ambigüe car issu d'un contexte ou d'une conversation (tag d'un autre viewer etc...), et que cela laisse planer un doute sur l'ironie du message, vous pouvez choisir d'ignorer le message, il ne sera pas pris en compte dans le modèle. Si cependant le message contient une/des insultes, vous devez le juger.