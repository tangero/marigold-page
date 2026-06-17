---
slug: "mac-m"
url: "/mobilnisite/slovnik/mac-m/"
type: "slovnik"
title: "MAC-M – Message Authentication Code for Mobile Application Part"
date: 2025-01-01
abbr: "MAC-M"
fullName: "Message Authentication Code for Mobile Application Part"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mac-m/"
summary: "Kód pro ověření zpráv (MAC) používaný v kontextu protokolu MAP (Mobile Application Part), konkrétně pro zabezpečení uživatelských komponent TCAP (Transaction Capabilities Application Part). Poskytuje"
---

MAC-M je kód pro ověření zpráv (Message Authentication Code) používaný v rámci protokolu MAP k zabezpečení uživatelských komponent TCAP, který poskytuje autentizaci a integritu pro signalizační transakce v zastaralých jádrových sítích GSM a UMTS.

## Popis

MAC-M je bezpečnostní mechanismus definovaný ve specifikacích 3GPP pro autentizaci zpráv v sadě protokolů [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part), která se používá pro signalizaci mezi prvky jádrové sítě v okruhově spínaných a paketově spínaných doménách 2G (GSM) a 3G (UMTS). Jeho primární aplikace je v kontextu TCAP (Transaction Capabilities Application Part), který poskytuje rámec pro strukturované dialogy a transakce mezi síťovými uzly. Zprávy TCAP mohou nést různé aplikační kontexty a MAC-M se používá k autentizaci specifických uživatelských komponent v těchto zprávách TCAP.

Technická operace zahrnuje generování [MAC](/mobilnisite/slovnik/mac/) nad vybranými částmi komponenty zprávy TCAP pomocí sdíleného tajného klíče, který je zaveden mezi zapojenými síťovými entitami, jako je například VLR (Visitor Location Register) a [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register). Algoritmus pro výpočet MAC-M není veřejný, standardizovaný kryptografický algoritmus jako [AES](/mobilnisite/slovnik/aes/), ale typicky jde o algoritmus specifický pro operátora sítě, často založený na variantách COMP128 používaných v zastaralé autentizaci. Specifikace 33.204 podrobně popisuje aspekty protokolu a pole, která mají být zahrnuta do výpočtu MAC, ale samotná kryptografická funkce je definována operátorem.

Z architektonického hlediska je MAC-M aplikován na aplikační vrstvě v rámci protokolového zásobníku MAP. Když síťová entita potřebuje odeslat citlivou MAP operaci (např. související se správou dat účastníka nebo získáním autentizačních informací), může vyvolat službu MAP-SECURITY. Tato služba nařídí generování MAC-M pro příslušnou komponentu TCAP. Přijímající entita následně ověří MAC-M pomocí stejného sdíleného tajemství. Úspěšné ověření přijímači zaručuje původ zprávy a to, že nebyla během přenosu pozměněna.

Jeho role je omezena na zabezpečení signalizace mezi síťovými uzly (Network Domain Security), nikoli na zabezpečení mezi uživatelem a sítí. Pomáhá předcházet podvodům a chybnému směrování při výměnách mezi operátory nebo mezi různými síťovými doménami v rámci sítě operátora. S migrací směrem k plně IP jádrovým sítím používajícím protokoly založené na Diameteru (např. S6a, S6d) v EPS a služby založené na [HTTP](/mobilnisite/slovnik/http/)/2 (např. Nudm) v 5GS však význam MAP a následně i MAC-M poklesl, protože jsou tyto technologie z velké části vytlačeny do oblasti interoperace se zastaralými systémy a roamingových scénářů se staršími generacemi sítí.

## K čemu slouží

MAC-M byl vytvořen, aby řešil potřebu zabezpečit určité transakce s vysokou hodnotou nebo citlivé transakce v rámci protokolu [MAP](/mobilnisite/slovnik/map/), který byl páteří signalizace jádrové sítě v GSM a UMTS. Jak se mobilní sítě vyvíjely, aby podporovaly roaming a propojení mezi operátory, stalo se zřejmým riziko podvodných signalizačních zpráv. Například útočník se mohl vydávat za VLR, aby získal autentizační vektory z [HLR](/mobilnisite/slovnik/hlr/), nebo mohl upravovat zprávy o aktualizaci polohy. MAC-M poskytl mechanismus pro bod-bodovou autentizaci specifických MAP operací mezi důvěryhodnými síťovými entitami.

Problém, který řešil, byl nedostatek inherentní bezpečnosti v protokolovém zásobníku MAP založeném na SS7, který byl navržen v éře uzavřených, důvěryhodných sítí operátorů. Jak se sítě otevřely pro globální roaming, byla potřeba metody, která by zajistila, že citlivá data účastníků a řídicí příkazy vyměňované mezi síťovými uzly (např. mezi [MSC](/mobilnisite/slovnik/msc/)/VLR a HLR) jsou autentické a nezměněné. MAC-M tuto mezeru zaplnil pro vybrané operace a přidal vrstvu zabezpečení bez nutnosti kompletní přestavby široce nasazené MAP infrastruktury.

Jeho motivace byla do značné míry řízena regulatorními požadavky a požadavky na prevenci podvodů. Umožnil operátorům implementovat bezpečnostní opatření pro kritické funkce, jako je přenos autentizačních dat (pomocí MAP_SEND_AUTHENTICATION_INFO) nebo vkládání dat účastníka (MAP_INSERT_SUBSCRIBER_DATA). Jeho implementace však byla často volitelná a specifická pro operátora, což vedlo k nekonzistentnímu nasazení. Vývoj směrem k IP jádrovým sítím s vestavěnými, povinnými bezpečnostními protokoly, jako je IPsec a TLS pro Diameter, a opouštění MAP ve prospěch těchto novějších protokolů, řeší omezení MAC-M tím, že poskytuje silnější, standardizované a koncové zabezpečení pro všechny signalizační transakce.

## Klíčové vlastnosti

- Používá se pro autentizaci uživatelských komponent TCAP v rámci signalizačního protokolu MAP.
- Poskytuje bod-bodovou autentizaci mezi uzly jádrové sítě, jako jsou HLR, VLR a MSC.
- Typicky používá kryptografické algoritmy specifické pro operátora, často založené na COMP128.
- Aplikuje se selektivně na citlivé MAP operace prostřednictvím služby MAP-SECURITY.
- Primárně slouží pro zabezpečení síťové domény (Network Domain Security) v zastaralých okruhově spínaných jádrech a jádrech GPRS.
- Podrobně popsán v 3GPP TS 33.204, přičemž se zaměřuje na aplikaci protokolu spíše než na definici kryptografického algoritmu.

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [MAC-M na 3GPP Explorer](https://3gpp-explorer.com/glossary/mac-m/)
