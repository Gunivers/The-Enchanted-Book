# Guide de développement

L’aspect développement, bien que relativement caché pour la plupart des joueurs, fait partie intégrante de la création dans Minecraft. Pour certains, il s’agit là d’une façon d’exploiter le jeu sous des angles nouveaux, et pour d’autre s’agit d’une forme de magie occulte et terrifiante, dont le simple fait de mentionner le mot “commande”  provoque des maux de tête.

Aujourd’hui nous avons décidé, de démystifier cet aspect complexe du jeu et de vous laisser entrevoir les nombreuses possibilités qui vous sont finalement à porté de main.

À tous ceux qui sont lassés des nombreux tutoriels déjà existant : NE FUYEZ PAS ! Cette série n’aura pas pour objectif de vous transmettre une liste indigeste de commandes complexes en vous les expliquant une à une (ça fait beaucoup trop de choses à retenir pour nos petites têtes humaines). Nous allons essayer de vous enseigner les mécaniques et la logique qui se cache derrière. Logique à laquelle, si vous y ajoutez une simple connaissance de base, un esprit curieux – et un peu de patience –  vous permettra de réaliser à peu près tout ce que vous pouvez imaginer !

Ainsi, nous vous proposerons de découvrir les différents éléments majeurs du développement en commandes au rythme d’un article toutes les deux semaines. Le tout sera suivi d’annexes et de bonus pour plus d’informations, sans oublier quelques exercices pratiques permettant de vous aider à mieux saisir les concepts évoqués. Veillez à les faire tranquillement, à tête reposée avec une bonne bière (ou un soda pour les plus jeunes) et une musique d’ambiance : votre apprentissage vous paraîtra plus doux et agréable.

Cet article sera le premier d’une série qui sera publiée à rythme fixe, un jeudi sur deux.

---

## Organisation du guide

Ce guide se verra appliquer une syntaxe particulière aux patterns des commandes, par exemple :

```
/setblock <position> <type>[blockState][NBT] [replace|keep|destroy]
```

:::{note}
Tout ce qui suit le premier mot de la commande (ici “setblock”) est appelé “paramètres”.
:::

Voici une explication de la syntaxe utilisée :
- `<…>` paramètre obligatoire
- `[…]` paramètre optionnel
- `[…|…]` ou `<…|…>` paramètre à choisir parmis les différents éléments précisés, l’élément en gras étant l’élément par défaut si le paramètre est optionnel.

---

## Sommaire

Voici un sommaire des différents articles de cette série. Lors de la parution de l’un d’eux, le lien vers l’article sera ajouté à ce sommaire.

```{toctree}
1-support.md
2-blocs&entités.md
3-execute.md
```