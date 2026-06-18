---
slug: "xpk"
url: "/mobilnisite/slovnik/xpk/"
type: "slovnik"
title: "XPK – XML Protection Key"
date: 2026-01-01
abbr: "XPK"
fullName: "XML Protection Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xpk/"
summary: "Kryptografický klíč používaný k ochraně zpráv založených na XML v sítích 3GPP, zajišťující důvěrnost a integritu pro služby jako SMS a MMS. Je nezbytný pro zabezpečení protokolů aplikační vrstvy proti"
---

XPK je kryptografický klíč používaný k ochraně zpráv založených na XML v sítích 3GPP, zajišťující důvěrnost a integritu pro služby jako SMS a MMS.

## Popis

Klíč pro ochranu [XML](/mobilnisite/slovnik/xml/) (XPK) je bezpečnostní mechanismus definovaný ve specifikacích 3GPP pro zabezpečení dat ve formátu XML vyměňovaných mezi síťovými entitami a uživatelským zařízením (UE). Působí na aplikační vrstvě, konkrétně pro služby využívající XML jako datový formát, jako je služba multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) a některé aplikace IP multimediální podsystému (IMS). Klíč se používá spolu s kryptografickými algoritmy k provádění šifrování a ochrany integrity, což zajišťuje, že zprávy XML zůstanou během přenosu důvěrné a nezměněné.

Z architektonického hlediska je XPK spravován v rámci bezpečnostního rámce sítě, často zahrnující funkce generování, distribuce a ukládání klíčů. Může být poskytován uživatelskému zařízení prostřednictvím zabezpečených kanálů, například těch navázaných protokolem Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), nebo může být odvozen z existujících hlavních klíčů. Klíč se aplikuje na dokumenty XML pomocí standardů jako XML Encryption a XML Signature, které definují, jak šifrovat konkrétní prvky nebo podepsat dokument pro integritu.

V praxi, když je odeslána zpráva XML, odesílající entita použije XPK k zašifrování citlivých částí datové části XML nebo k vytvoření digitálního podpisu. Přijímající entita, disponující stejným nebo odpovídajícím klíčem, data dešifruje nebo ověří podpis. Tento proces chrání před odposlechem a manipulací, což je klíčové pro služby přenášející osobní nebo finanční informace. Role XPK je nedílnou součástí komplexního zabezpečení aplikací založených na XML a doplňuje ochranu na nižších vrstvách, jako je [IPsec](/mobilnisite/slovnik/ipsec/) nebo [TLS](/mobilnisite/slovnik/tls/).

Specifikace popisující XPK, například 3GPP TS 24.281 a 33.179, stanovují jeho použití v konkrétních protokolech a rozhraních. Může být například využíván v prostředí MMS k ochraně obsahu zprávy mezi mobilním zařízením a serverem MMS. Životní cyklus klíče, včetně jeho aktualizací a odvolání, je spravován tak, aby byla dlouhodobě udržována bezpečnost. Poskytnutím standardizovaného přístupu k ochraně XML zajišťuje XPK interoperabilitu mezi různými výrobci a síťovými nasazeními, čímž zvyšuje celkovou bezpečnost systému.

## K čemu slouží

XPK byl zaveden za účelem řešení bezpečnostních slabin vlastních komunikaci založené na [XML](/mobilnisite/slovnik/xml/) v mobilních sítích. Jak služby jako [MMS](/mobilnisite/slovnik/mms/) a IMS získávaly na popularitě, silně spoléhaly na XML pro strukturování dat, ale rané implementace často postrádaly robustní zabezpečení na aplikační vrstvě. To ponechávalo citlivé informace vystavené odposlechu nebo změně během přenosu, což představovalo rizika pro soukromí uživatelů a integritu dat.

Vytvoření XPK bylo motivováno potřebou standardizovaného kryptografického řešení přizpůsobeného jedinečným charakteristikám XML. Předchozí přístupy mohly spoléhat na obecné zabezpečení přenosu (např. [SSL](/mobilnisite/slovnik/ssl/)/TLS), které chrání spojení, ale ne nutně obsah XML komplexně, zejména pokud zprávy procházejí více uzly. XPK tuto mezeru zaplňuje tím, že umožňuje šifrování a podepisování na úrovni prvků XML, což poskytuje podrobnou kontrolu zabezpečení. Souladí se širšími snahami 3GPP o posílení bezpečnosti aplikací nad rámec protokolů základní sítě.

Historicky, jak se 3GPP vyvíjelo od Release 13 dále, rostoucí složitost služeb vyžadovala sofistikovanější bezpečnostní mechanismy. XPK poskytl způsob, jak zabezpečit datové části XML způsobem nezávislým na základním přenosu, což zajišťuje ochranu i ve scénářích, kde data zpracovávají mezilehlé uzly. Tím byly řešeny limity dřívějších bezpečnostních modelů, které nebyly navrženy pro rozšiřitelnou strukturu XML, a tím byla podpořena bezpečná expanze multimediálních a zprávových služeb v sítích 4G a 5G.

## Klíčové vlastnosti

- Poskytuje důvěrnost pro prvky zpráv XML prostřednictvím šifrování
- Zajišťuje integritu a autenticitu prostřednictvím digitálních podpisů XML
- Integruje se s rámci pro správu klíčů 3GPP pro zabezpečenou distribuci
- Podporuje zabezpečení na aplikační vrstvě pro služby jako MMS a IMS
- Umožňuje podrobnou ochranu konkrétních částí dat XML
- Standardizován napříč více vydáními 3GPP pro zajištění interoperability

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [XPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/xpk/)
