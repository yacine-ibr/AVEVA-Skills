# AVEVA Skills | Assistant d'ingénierie System Platform

Dépôt public de **skills et d'exemples techniques**, utilisable avec les assistants d'IA compatibles. Il vise surtout **AVEVA System Platform Application Server, QuickScript .NET, OMI et Industrial Graphics**.

> **Important :** ce dépôt n'est **ni une documentation officielle AVEVA, ni une bibliothèque de spécifications universelles, ni un package de scripts validés en production**. Vérifier chaque affirmation technique auprès des documents officiels du bon produit et de la bonne version, puis tester avec un ingénieur dans un environnement autorisé.

## Le skill

**[Ouvrir AVEVA System Platform SKILL.md](aveva-system-platform/SKILL.md)**

Il explique à l'IA :
- quand l'utiliser et quand **ne pas** l'utiliser ;
- comment identifier le produit, la version et le contexte d'exécution du script ;
- comment rechercher les **documents officiels constructeur à jour** ;
- comment rédiger et relire du QuickScript .NET sans supposer que le runtime accepte le C# moderne ;
- comment distinguer un exemple de script, un besoin client et une capacité vérifiée de l'éditeur ;
- comment tester et documenter les risques, sans déployer directement sur une installation industrielle.

## Contenu

```text
README.md
GUIDE_IA.md                           Utilisation avec plusieurs assistants
aveva-system-platform/
  SKILL.md                            Skill principal compatible Agent Skills
  README.md                           Présentation courte du skill
  references/
    official-sources.md               Sources AVEVA et méthode de vérification
    review-checklist.md              Checklist ingénierie et validation
  examples/
    README.md                         Statut des exemples
    motor-start-stop.qsnet             Exemple illustratif
    alarm-evaluation.qsnet             Exemple illustratif
    state-derivation.qsnet             Exemple illustratif
  prompts/
    assistant-system-prompt.md         Ancien prompt conservé comme référence
scripts/
  install-skill.py                    Installation locale Codex/Claude Code/Copilot
  package-skill.py                    ZIP compatible avec l'import Claude
  validate-skill.py                   Vérification de structure et des liens
```

Les trois scripts `.qsnet` sont des **illustrations non certifiées** : aucune compilation, simulation AVEVA ni vérification de sécurité en production n'est attestée par le dépôt.

## Démarrer

| Outil | Méthode |
|---|---|
| **Codex CLI / IDE** | Installer le dossier du skill sous `.agents/skills/aveva-system-platform/` ou dans l'emplacement utilisateur `~/.agents/skills/` |
| **Claude Code** | Installer dans `.claude/skills/aveva-system-platform/` ou `~/.claude/skills/` |
| **GitHub Copilot agent / VS Code** | Utiliser `.github/skills/aveva-system-platform/` ou emplacement personnel pris en charge |
| **Claude en chat** | Générer un ZIP du dossier du skill puis l'importer dans `Personnaliser > Compétences`, si la fonctionnalité est disponible |
| **ChatGPT en chat** | Utiliser un projet avec instructions et fichiers de référence ; l'installation de skills dépend de la surface et du forfait |
| **Microsoft 365 Copilot** | Configurer des instructions d'agent et des fichiers de connaissances autorisés ; un `SKILL.md` GitHub n'est pas chargé automatiquement |

**[Guide détaillé et exemples de questions](GUIDE_IA.md)**.

## Installation locale (Windows, Linux ou macOS)

Avec Python 3 et une copie de ce dépôt :

```bash
python scripts/validate-skill.py
python scripts/install-skill.py --agent codex --scope user
python scripts/install-skill.py --agent claude --scope user
python scripts/install-skill.py --agent copilot --scope user
python scripts/package-skill.py
```

Pour obtenir le ZIP **sans installer Python**, le workflow GitHub [Validate AVEVA skill package](https://github.com/yacine-ibr/AVEVA-Skills/actions/workflows/validate-skill.yml) publie un artefact téléchargeable pendant 30 jours. Ouvrir la dernière exécution réussie, télécharger l'artefact, puis en extraire `aveva-system-platform.zip`.

Les scripts d'installation ne requièrent aucun accès réseau et copient uniquement le dossier public `aveva-system-platform/`. Par défaut, une installation existante n'est **pas écrasée**. Utiliser `--help` pour les options et l'installation par projet.

## Relation avec une bibliothèque documentaire privée

Un skill définit une **méthode de travail et de vérification**. Une bibliothèque documentaire peut contenir des **exemples de spécifications d'anciens projets**, mais ceux-ci ne définissent **jamais** les règles du nouveau client.

Les deux peuvent être utilisés dans une même tâche si l'assistant dispose d'accès autorisés à chacun. **Ce dépôt public ne contient pas et ne doit pas recevoir de documents, prompts ou extraits de clients confidentiels.**

## Sources constructeur

Commencer par [AVEVA Documentation](https://docs.aveva.com/) et vérifier le **manuel exact du produit, la version et les notes de version**. Le [guide de sources officielles](aveva-system-platform/references/official-sources.md) précise les limites. Les liens externes et contraintes produit évoluent : revérifier au moment de l'usage.

## Statut

Skill structuré et prêt pour **installation ou import par un utilisateur autorisé**, sous réserve des capacités de chaque assistant. Les exemples QuickScript n'ont pas été testés dans un vrai environnement AVEVA et ne doivent pas être présentés comme production-ready.

Pour poser une question AVEVA, préciser au minimum **produit, version, composant et résultat attendu**.
