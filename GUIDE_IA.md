# Guide pratique : Codex, ChatGPT, Claude et Copilot

## Bien comprendre les trois objets

1. **Skill AVEVA** : des instructions de méthode pour analyser/générer du QuickScript .NET, des modèles d'objets, de l'OMI et des Industrial Graphics. Source : [SKILL.md](aveva-system-platform/SKILL.md).
2. **Bibliothèque documentaire privée** : des originaux et extraits de missions précédentes. Ils ne sont que des **exemples de structure et de solutions particulières**, jamais les exigences de nouveaux clients.
3. **Documents éditeurs officiels** : autorité pour les **fonctionnalités, limitations, compatibilités et syntaxes documentées d'une version**. Les exigences métier sont définies par le **nouveau client**.

**Le skill n'est pas une connexion à GitHub.** Chaque assistant doit disposer explicitement de l'accès au dossier de skill et, séparément, aux documents privés s'ils sont nécessaires. Ne pas partager de données confidentielles avec un assistant ou un locataire Microsoft non autorisé.

## 1. Codex (CLI / extension IDE)

**Préparation locale :**

```bash
git clone https://github.com/yacine-ibr/AVEVA-Skills.git
cd AVEVA-Skills
python scripts/validate-skill.py
python scripts/install-skill.py --agent codex --scope user
```

Sur Windows, `py` peut remplacer `python`. Pour limiter le skill à un dossier de travail, utiliser `--scope project --project-dir "CHEMIN_DU_PROJET"`.

Le dossier installé contient `SKILL.md`, `examples/` et `references/`. Démarrer une **nouvelle session** Codex dans le projet. L'invocation automatique dépend de la demande et de la description ; vous pouvez demander explicitement : « Utilise le skill `aveva-system-platform` ».

**Demande test :**

> Utilise le skill aveva-system-platform. Je travaille sur AVEVA System Platform 2023 R2 SP1, script Application Server d'un template moteur. Propose un exemple de logique d'arrêt prioritaire, avec attributs supposés, points à vérifier dans la documentation officielle, plan de tests et limites. Ne dis pas que le script est validé en production.

La méthode suit le format Agent Skills documenté : [OpenAI](https://developers.openai.com/api/reference/cli) et [Agent Skills](https://agentskills.io/).

## 2. Claude Code

Depuis le même dépôt cloné :

```bash
python scripts/install-skill.py --agent claude --scope user
```

Pour une installation locale propre au projet : `--scope project --project-dir "CHEMIN_DU_PROJET"`. Démarrer une nouvelle session Claude Code et demander « Utilise `/aveva-system-platform` pour relire ce QuickScript .NET ».

La documentation Claude Code décrit les [skills et leurs emplacements](https://code.claude.com/docs/en/skills).

## 3. GitHub Copilot pour le développement (VS Code, CLI, agents)

Il s'agit de **GitHub Copilot**, distinct de **Microsoft 365 Copilot**.

```bash
python scripts/install-skill.py --agent copilot --scope user
```

Pour les compétences du dépôt projet, utiliser `--scope project` : le script installe dans `.github/skills/aveva-system-platform/`. Relancer/actualiser l'agent et demander « Use the `aveva-system-platform` skill to review this Application Server script ».

Selon l'interface/plan, le support des skills varie. Voir [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## 4. Claude en chat (claude.ai)

Lorsque les **compétences personnalisées** sont disponibles :

1. **Sans Python ni clone :** ouvrir les [exécutions de validation GitHub](https://github.com/yacine-ibr/AVEVA-Skills/actions/workflows/validate-skill.yml), sélectionner la dernière exécution réussie, puis télécharger l'artefact `aveva-system-platform-skill-zip` dans la section **Artifacts**. Extraire le ZIP de l'artefact pour récupérer `aveva-system-platform.zip`. **Alternative locale :** dans ce dépôt cloné, exécuter `python scripts/package-skill.py` pour créer `dist/aveva-system-platform.zip`.
2. Dans Claude, activer l'exécution de code/création de fichiers si nécessaire, puis aller dans **Personnaliser > Compétences**.
3. Ajouter/importer une compétence depuis le ZIP (dossier racine `aveva-system-platform/` avec `SKILL.md`).
4. Activer la compétence et tester : « Applique le skill aveva-system-platform à cette revue de code ».

[Documentation Anthropic](https://support.claude.com/fr/articles/12512180-utiliser-les-competences-dans-claude).

**Autre option :** créer un **Projet Claude**, ajouter le fichier `SKILL.md` ou le texte pertinent comme **instructions de projet** et les exemples comme connaissances. Cela donne du contexte, **sans installer un skill natif**. [Projets Claude](https://support.claude.com/fr/articles/9519177-comment-creer-et-gerer-des-projets).

## 5. ChatGPT en conversation

### Option accessible sans installation de skill : projet ChatGPT

1. Créer un **Projet** dans ChatGPT.
2. Coller les règles pertinentes de `SKILL.md` dans les **instructions du projet**.
3. Ajouter seulement les fichiers nécessaires comme **sources**, par exemple `official-sources.md`, `review-checklist.md` et les extraits techniques autorisés. Ne pas importer tout un corpus client par défaut.
4. Autoriser/utiliser la recherche web lorsque disponible. Demander explicitement de citer la **documentation officielle de la bonne version**.
5. Tester avec une question dont la réponse peut être contrôlée dans le manuel constructeur.

Voir [Projets ChatGPT](https://help.openai.com/fr-fr/articles/10169521-projects-in-chatgpt).

### Skills natifs dans ChatGPT

Les **skills natifs** et leur installation dépendent du produit, de la surface (notamment application de bureau ou plugin) et du forfait / des droits de l'espace de travail. Ne pas confondre l'ajout d'un fichier dans un chat avec l'installation d'un skill. Sur des espaces de travail éligibles, suivre [Compétences dans ChatGPT](https://help.openai.com/fr-fr/articles/20001066-skills-in-chatgpt). Sur d'autres comptes, privilégier les **Projets** et les fichiers de référence.

Un ChatGPT sans connexion GitHub autorisée ne peut pas automatiquement consulter les fichiers d'un dépôt **privé**.

## 6. Microsoft 365 Copilot (Teams, Word, Outlook, etc.)

**Microsoft 365 Copilot n'installe pas automatiquement un Agent Skill GitHub parce qu'un dépôt contient `SKILL.md`.** Les fonctionnalités Agent Builder « skills » peuvent être en version préliminaire et réservées à certains tenants ; l'approche générale disponible dépend de la licence et des politiques Microsoft 365.

Avec un administrateur ou un environnement autorisé :

1. Ouvrir **Microsoft 365 Copilot > Nouvel agent > Configurer** (si cette fonctionnalité est disponible).
2. Coller les règles de comportement pertinentes de `SKILL.md` dans **Instructions** de l'agent, en veillant à respecter la limite du champ.
3. Ajouter comme **Connaissances** des fichiers non confidentiels et pertinents, ou un dossier SharePoint/OneDrive autorisé. Éviter de publier une bibliothèque privée entière vers un espace public.
4. Si un portail AVEVA public est supporté par l'agent comme source web, contrôler l'accès réel et la version du document. Ne pas supposer qu'une URL publique donne accès à toutes les sous-pages.
5. Tester une question précise et les citations fournies ; vérifier que l'agent a réellement eu accès aux fichiers attendus.

Guide officiel [Microsoft 365 Agent Builder, sources](https://learn.microsoft.com/fr-fr/microsoft-365-copilot/extensibility/copilot-studio-lite-knowledge). Pour un usage plus avancé, [Copilot Studio, téléchargement de fichiers](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-file-upload). Les agents Microsoft 365 sont gouvernés par les permissions et les règles de l'organisation.

## 7. Exemple de demande universelle

> Contexte : nouveau projet sur [site], avec [logiciel], [version] et [modules]. Je veux [script / revue / spécification / architecture]. Utilise le skill AVEVA uniquement si le logiciel est réellement AVEVA System Platform. Les anciens documents projets sont des exemples, pas des règles pour ce client. Recherche et cite les sources constructeur officielles adaptées au produit et à sa version. Distingue les besoins client, le fonctionnement produit vérifié, les exemples historiques et les hypothèses. Si la recherche web est inaccessible, indique-le. Fournis un plan de vérification et de tests avant toute mise en production.

## 8. Tests de mise en service

- **Déclenchement :** demande AVEVA Application Server pertinente => le skill est consulté.
- **Non-déclenchement :** demande Ignition ou Siemens => ne pas imposer QuickScript .NET.
- **Version :** si la version manque, l'assistant la demande ou marque ses hypothèses.
- **Preuves :** aucun lien constructeur inventé ; citations vérifiables et datées.
- **Sécurité :** pas de déploiement direct, ni de valeurs de site copiées d'un ancien projet.
- **Accès :** aucune affirmation de lecture d'un dépôt privé sans accès réel.
- **Dégradé :** sans internet, réponse marquée « vérification éditeur non effectuée ».

## 9. Confidentialité et mise à jour

**AVEVA-Skills est public**. Ne jamais y déposer des spécifications, captures, architectures de clients, comptes ou configurations privées. Si des exemples confidentiels doivent être utilisés, ils restent dans un stockage privé autorisé et sont chargés séparément.

Le skill, ses scripts et les pratiques constructeur évoluent : noter les versions des produits, vérifier la documentation AVEVA au moment de la demande et renouveler les tests après les mises à jour.
