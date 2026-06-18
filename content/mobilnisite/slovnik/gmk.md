---
slug: "gmk"
url: "/mobilnisite/slovnik/gmk/"
type: "slovnik"
title: "GMK – Group Management Key"
date: 2026-01-01
abbr: "GMK"
fullName: "Group Management Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmk/"
summary: "Kryptografický klíč používaný k zabezpečení skupinové komunikace a řídicích procedur v sítích 3GPP. Umožňuje autentizaci, ochranu integrity a důvěrnost pro členy skupiny a tvoří základ pro zabezpečené"
---

GMK je kryptografický klíč používaný v sítích 3GPP pro zabezpečení skupinové komunikace a řídicích procedur tím, že členům skupiny poskytuje autentizaci, ochranu integrity a důvěrnost.

## Popis

Skupinový řídicí klíč (Group Management Key, GMK) je základní bezpečnostní přihlašovací údaj v architekturách 3GPP, speciálně navržený pro ochranu služeb založených na skupinách. Jedná se o symetrický kryptografický klíč, který je sdílen mezi všemi legitimními členy skupiny a důvěryhodnými síťovými entitami, jako je Group Management Server ([GMS](/mobilnisite/slovnik/gms/)) nebo [ProSe](/mobilnisite/slovnik/prose/) funkce. GMK slouží jako kořenový klíč pro odvozování dalších bezpečnostních klíčů používaných pro různé ochranné funkce, včetně autentizace mezi členy skupiny a sítí, ochrany integrity signalizace pro řízení skupiny a šifrování provozu skupinové komunikace. Jeho životní cyklus správy – generování, distribuce, uložení a odvolání – je klíčový pro zabezpečení služeb jako Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), Proximity Services (ProSe) přímá komunikace a skupinové zasílání zpráv pro IoT.

Z architektonického hlediska je GMK typicky generován centrální autoritou uvnitř sítě, například GMS v domovské síti nebo specializovaným centrem pro správu klíčů. Pro služby ProSe může klíč GMK generovat ProSe funkce. Klíč je poté bezpečně distribuován do koncového zařízení (UE) každého člena skupiny prostřednictvím chráněných signalizačních kanálů, často za použití individuálních klíčů účastníka pro šifrování přenosu během distribuce. Po uložení do bezpečného prostředí UE (např. v Group Management Clientu) se GMK používá k odvození relace specifických klíčů, jako je Group Traffic Key (GTK) pro šifrování dat v uživatelské rovině nebo Group Integrity Key (GIK) pro ochranu řídicích zpráv. Tato hierarchie klíčů zajišťuje, že kompromitace odvozeného relace specifického klíče neodhalí kořenový klíč GMK.

Provoz klíče GMK zahrnuje několik protokolů a rozhraní. Například v MCPTT, když se UE připojí ke skupině, GMS autentizuje UE a poté zřídí GMK (nebo klíč pro šifrování klíčů pro doručení GMK) do [GMC](/mobilnisite/slovnik/gmc/) v UE. Specifikace popisují funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), které používají GMK spolu s dalšími parametry, jako jsou identifikátory skupiny a pořadová čísla, k vytváření nových klíčů. Síť také pravidelně aktualizuje nebo obnovuje klíč GMK, aby byla zachována dopředná a zpětná důvěrnost, zejména při změnách členství ve skupině. Ve scénářích ProSe může GMK umožnit přímou zabezpečenou komunikaci mezi UE bez síťové infrastruktury tím, že se klíč použije pro vzájemnou autentizaci a šifrování přes referenční bod PC5.

## K čemu slouží

Klíč GMK byl zaveden, aby odstranil nedostatek standardizované, bezpečné správy klíčů pro skupinovou komunikaci v mobilních sítích. Tato mezera se stala kritickou se standardizací služeb Mission Critical Services a [ProSe](/mobilnisite/slovnik/prose/) ve vydání 12. Předtím skupinové služby buď používaly nezabezpečené metody, nebo spoléhaly na zabezpečení na aplikační vrstvě, které nebylo integrováno se síťovou autentizací, což je činilo zranitelnými vůči odposlechu, zosobnění a útokům opakováním. Potřeba zabezpečené skupinové komunikace s nízkou latencí pro veřejnou bezpečnost a kritickou infrastrukturu si vyžádala řešení zabezpečení na síťové úrovni.

Vytvoření klíče GMK poskytuje jednotný kryptografický základ pro skupinové zabezpečení v rámci 3GPP. Řeší problém škálovatelné a efektivní distribuce klíčů pro dynamické skupiny definováním centralizované architektury správy klíčů. To umožňuje síti kryptograficky řídit členství ve skupině; pouze UE disponující platným klíčem GMK se mohou účastnit zabezpečené skupinové komunikace. Řeší omezení párového klíčování, které by vyžadovalo samostatný klíč pro každou dvojici členů a není škálovatelné pro velké skupiny.

Historicky se zabezpečení v mobilních sítích soustředilo primárně na individuální autentizaci účastníka (např. pomocí Ki v [SIM](/mobilnisite/slovnik/sim/) kartách). Klíč GMK rozšiřuje toto paradigma na skupiny a umožňuje nové modely služeb. Jeho návrh byl motivován požadavky organizací veřejné bezpečnosti na zabezpečené push-to-talk služby a komunikaci založenou na blízkosti během nouzových situací. Integrací se stávajícími rámci zabezpečení 3GPP, jako je Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), klíč GMK zajišťuje, že skupinové zabezpečení využívá robustní autentizaci účastníka, která již je zavedena, a přidává nezbytnou správu klíčů orientovanou na skupiny pro podporu scénářů komunikace založených na síti i přímé komunikace mezi zařízeními.

## Klíčové vlastnosti

- Slouží jako kořenový klíč pro odvozování relace specifických klíčů pro skupinový provoz a ochranu integrity
- Centrálně generován a bezpečně distribuován síťovými funkcemi jako GMS nebo ProSe funkce
- Umožňuje autentizaci a zabezpečenou komunikaci mezi členy skupiny
- Podporuje procedury aktualizace a obnovy klíče pro dopřednou/zpětnou důvěrnost
- Integruje se s rámcem 3GPP AKA pro bezpečnou počáteční distribuci
- Používá se k zabezpečení signalizace v řídicí rovině i dat v uživatelské rovině pro skupinové služby

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 23.784** (Rel-16) — Discreet Listening for Mission Critical Services
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [GMK na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmk/)
