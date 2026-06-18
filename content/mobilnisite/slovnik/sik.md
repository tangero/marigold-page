---
slug: "sik"
url: "/mobilnisite/slovnik/sik/"
type: "slovnik"
title: "SIK – SS7 Security Gateway Integrity Key"
date: 2025-01-01
abbr: "SIK"
fullName: "SS7 Security Gateway Integrity Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sik/"
summary: "Kryptografický klíč používaný v sítích 3GPP k zajištění integrity signalizačních zpráv mezi SS7 Security Gateway (SEG) a dalšími síťovými prvky. Chrání protokoly založené na SS7 (jako MAP a CAP) před"
---

SIK je kryptografický klíč používaný v sítích 3GPP k zajištění integrity signalizačních zpráv mezi SS7 Security Gateway a dalšími síťovými prvky, který chrání protokoly jako MAP a CAP před neoprávněnými změnami a opakovanými útoky.

## Popis

[SS7](/mobilnisite/slovnik/ss7/) Security Gateway Integrity Key (SIK) je symetrický kryptografický klíč používaný v bezpečnostní architektuře 3GPP k zabezpečení protokolů Signalizačního systému č. 7 (SS7) používaných v signalizaci jádra sítě. Konkrétně se používá v kontextu Security Gateway ([SEG](/mobilnisite/slovnik/seg/)), která funguje jako firewall a bezpečnostní prostředník pro signalizační provoz mezi různými síťovými operátory nebo mezi síťovými doménami. SIK slouží k vytváření a ověřování kódů pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)) pro signalizační zprávy, čímž zajišťuje jejich integritu a poskytuje ochranu proti útokům modifikací, vkládání nebo opakování. Klíč je typicky odvozen z dlouhodobého sdíleného tajemství navázaného mezi partnerskými SEG pomocí protokolu pro správu klíčů, jako je Internet Key Exchange ([IKE](/mobilnisite/slovnik/ike/)) v rámci frameworku [IPsec](/mobilnisite/slovnik/ipsec/). Při provozu, když je signalizační zpráva (např. zpráva [MAP](/mobilnisite/slovnik/map/) nebo [CAP](/mobilnisite/slovnik/cap/)) odeslána z jedné SEG na druhou přes IP síť (pomocí SIGTRAN nebo jiného transportu), zdrojová SEG použije SIK k výpočtu MAC nad datovou částí zprávy a kritickými hlavičkami. Tento MAC je připojen ke zprávě. Příjemající SEG, která disponuje stejným SIK, přepočítá MAC a porovná jej s přijatou hodnotou. Pokud se shodují, je zpráva přijata jako autentická a nezměněná; v opačném případě je zahozena. SIK se liší od šifrovacích klíčů (jako je [SEK](/mobilnisite/slovnik/sek/) - SS7 Security Gateway Encryption Key) a je specificky určen pro ochranu integrity. Jeho správa je klíčová pro udržení důvěryhodnosti signalizace mezi operátory, která je základní pro funkce jako roaming, autentizace a účtování.

## K čemu slouží

SIK byl zaveden k řešení bezpečnostních zranitelností v tradičních SS7 sítích, které byly původně navrženy pro důvěryhodná, uzavřená prostředí operátorů. S vývojem mobilních sítí a rozšířením propojení přes IP sítě se SS7 signalizace stala vystavena hrozbám, jako je padělání zpráv a jejich neoprávněná změna, což by mohlo vést k podvodům (např. neoprávněné sledování polohy nebo zachycení hovorů) a narušení služeb. Pracovní skupina pro bezpečnost 3GPP definovala architekturu Security Gateway ve verzi 8, aby chránila tato kritická signalizační rozhraní. SIK jako součást této architektury řeší problém zajištění integrity zpráv při přenosu mezi operátory. Poskytuje kryptografické ujištění, že signalizační příkazy nebyly změněny, což je zásadní pro přesnost účtování, soukromí účastníků a spolehlivost sítě. Vytvoření SIK bylo motivováno potřebou modernizovat bezpečnost SS7 bez nahrazení celé signalizační infrastruktury, což umožňuje operátorům postupně zavádět bezpečnostní opatření založená na IP při zachování interoperability se staršími systémy. Představuje klíčovou součást přechodu k plně zabezpečené signalizaci nové generace (např. v 5G).

## Klíčové vlastnosti

- Symetrický klíč pro vytváření a ověřování kódů pro ověření zprávy (MAC)
- Používán konkrétně SS7 Security Gateways (SEG) pro ochranu integrity
- Chrání SS7 aplikační protokoly jako MAP a CAP přes IP sítě
- Typicky odvozen ze sdílených tajemství navázaných pomocí IKE/IPsec
- Zabraňuje neoprávněným změnám zpráv, vkládání a opakovaným útokům
- Odlišný od šifrovacích klíčů (SEK), aby umožňoval samostatnou kontrolu integrity a důvěrnosti

## Související pojmy

- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [IKE – Internet Key Exchange](/mobilnisite/slovnik/ike/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SIK na 3GPP Explorer](https://3gpp-explorer.com/glossary/sik/)
