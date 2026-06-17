---
slug: "csb-id"
url: "/mobilnisite/slovnik/csb-id/"
type: "slovnik"
title: "CSB-ID – Crypto Session Bundle Identifier"
date: 2026-01-01
abbr: "CSB-ID"
fullName: "Crypto Session Bundle Identifier"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/csb-id/"
summary: "Jedinečný identifikátor používaný v misijně-kritických službách (MCS) 3GPP pro správu kryptografických relací pro zabezpečenou skupinovou komunikaci. Umožňuje sdružení více krypto relací pod jedním id"
---

CSB-ID je jedinečný identifikátor používaný v misijně-kritických službách 3GPP pro sdružování více kryptografických relací za účelem efektivního řízení klíčů a zabezpečené distribuce médií ve skupinové komunikaci.

## Popis

Crypto Session Bundle Identifier (CSB-ID) je základním bezpečnostním prvkem v architektuře misijně-kritických služeb ([MCS](/mobilnisite/slovnik/mcs/)) 3GPP, konkrétně definovaným v TS 33.180. Slouží jako jedinečný identifikátor, který sdružuje více kryptografických relací spojených s konkrétní misijně-kritickou komunikační skupinou nebo službou. Tento mechanismus sdružování je klíčový pro správu komplexních bezpečnostních požadavků skupinové komunikace, kde více účastníků potřebuje bezpečně vyměňovat média (hlas, video, data) s jednotnou kryptografickou ochranou.

Architektonicky CSB-ID funguje v rámci bezpečnostního rámce MCS, který zahrnuje několik funkčních entit včetně Mission Critical Serveru (MCS), Key Management Serveru ([KMS](/mobilnisite/slovnik/kms/)) a účastnických zařízení (UE). Při zřízení misijně-kritické skupinové komunikace systém vytvoří svazek krypto relací identifikovaný CSB-ID. Tento svazek obsahuje kryptografický kontext pro skupinu, včetně klíčového materiálu, bezpečnostních algoritmů a parametrů relace. CSB-ID je generován Key Management Serverem během procedury navázání skupinového klíče a je distribuován všem autorizovaným účastníkům prostřednictvím zabezpečených signalizačních kanálů.

CSB-ID umožňuje systému efektivně spravovat více paralelních kryptografických relací. Například v misijně-kritickém skupinovém videohovoru mohou existovat samostatné krypto relace pro audio proudy, video proudy a doplňková data. CSB-ID tyto relace spojuje, čímž zajišťuje, že sdílejí společné bezpečnostní parametry a mohou být spravovány jako souvislá jednotka. To je zvláště důležité pro scénáře vyžadující rychlé aktualizace klíčů nebo změny bezpečnostních parametrů napříč všemi typy médií současně.

Z operační perspektivy CSB-ID usnadňuje několik kritických bezpečnostních funkcí. Umožňuje Key Management Serveru sledovat a spravovat životní cyklus všech krypto relací v rámci svazku, včetně generování, distribuce, obnovy a odvolání klíčů. Když je potřeba aktualizovat bezpečnostní klíče (z důvodu periodického přegenerování nebo bezpečnostních incidentů), může KMS použít CSB-ID k identifikaci všech dotčených relací a konzistentně rozšířit nové klíče. Identifikátor také umožňuje efektivní synchronizaci bezpečnostního kontextu mezi členy skupiny a podporuje auditní logování tím, že poskytuje konzistentní referenční bod pro všechny bezpečnostní události v rámci svazku.

Implementace CSB-ID vyžaduje pečlivou koordinaci mezi aplikační vrstvou MCS a podkladovými bezpečnostními mechanismy 3GPP. Integruje se s existujícími bezpečnostními funkcemi 3GPP, jako je autentizace a dohoda o klíči ([AKA](/mobilnisite/slovnik/aka/)), a přidává vylepšení specifická pro misijně-kritické služby. Formát CSB-ID a postupy jeho zpracování jsou standardizovány, aby byla zajištěna interoperabilita mezi implementacemi MCS různých výrobců, což je klíčové pro bezpečnostní sítě, kde zařízení od více výrobců musí bezproblémově spolupracovat.

## K čemu slouží

CSB-ID byl vytvořen, aby řešil specifické bezpečnostní výzvy misijně-kritické skupinové komunikace v sítích 3GPP. Tradiční bezpečnostní mechanismy mobilních sítí byly navrženy primárně pro bodovou komunikaci a postrádaly efektivní metody pro správu kryptografických relací ve skupinových scénářích. Misijně-kritické služby, jako je komunikace pro veřejnou bezpečnost, vyžadují zabezpečenou skupinovou komunikaci, kde se může více uživatelů účastnit hlasových, video a datových relací se zaručenou důvěrností, integritou a autentizací.

Před zavedením CSB-ID ve verzi 14 čelily misijně-kritické služby významným omezením v bezpečnostní správě skupinové komunikace. Každý mediální proud typicky vyžadoval samostatnou správu kryptografické relace, což vedlo k neefektivní distribuci klíčů, zvýšené signalizační zátěži a potenciálním bezpečnostním nekonzistencím napříč různými typy médií. To bylo zvláště problematické pro scénáře zásahu v nouzových situacích, kde je nezbytná rychlá a koordinovaná skupinová komunikace. Absence jednotného identifikátoru pro související krypto relace ztěžovala provádění synchronizovaných bezpečnostních operací, jako je skupinové přegenerování klíčů nebo aktualizace bezpečnostních parametrů.

CSB-ID tyto problémy řeší tím, že poskytuje mechanismus pro sdružení souvisejících kryptografických relací pod jedním identifikátorem. To umožňuje efektivnější správu zabezpečení, snižuje signalizační zátěž a zajišťuje konzistentní uplatňování bezpečnostních politik napříč všemi typy médií v rámci misijně-kritické skupinové komunikace. Vytvoření CSB-ID bylo motivováno rostoucím přijetím sítí 3GPP pro veřejnou bezpečnost a misijně-kritickou komunikaci po celém světě, kde jsou robustní a škálovatelné bezpečnostní mechanismy klíčové pro ochranu citlivé komunikace během nouzových situací a kritických operací.

## Klíčové vlastnosti

- Jedinečný identifikátor pro svazky krypto relací v misijně-kritické komunikaci
- Umožňuje efektivní správu více kryptografických relací jako jedné entity
- Podporuje synchronizované aktualizace klíčů a změny bezpečnostních parametrů napříč sdruženými relacemi
- Usnadňuje konzistentní vynucování bezpečnostních politik napříč různými typy médií
- Snižuje signalizační zátěž sdružením souvisejících bezpečnostních kontextů
- Umožňuje auditní logování a bezpečnostní monitoring pomocí jediného referenčního identifikátoru

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [CSB-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/csb-id/)
