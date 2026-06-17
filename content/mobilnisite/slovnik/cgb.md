---
slug: "cgb"
url: "/mobilnisite/slovnik/cgb/"
type: "slovnik"
title: "CGB – Circuit Group Blocking"
date: 2025-01-01
abbr: "CGB"
fullName: "Circuit Group Blocking"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cgb/"
summary: "Circuit Group Blocking (CGB) je procedura správy sítě používaná v telefonii s přepojováním okruhů pro dočasné blokování skupiny okruhů (např. E1/T1 tras) před přenosem provozu. Umožňuje operátorům pro"
---

CGB je procedura správy sítě používaná v telefonii s přepojováním okruhů pro dočasné blokování skupiny okruhů před přenosem provozu za účelem údržby, testování nebo izolace závady.

## Popis

Circuit Group Blocking (CGB) je standardizovaná procedura pro provoz, správu a údržbu (OAM) definovaná ve specifikacích 3GPP, konkrétně podrobně popsaná v TS 29.163. Funguje v doméně jádra sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), kterou typicky spravují síťové prvky jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)). Procedura cílí na 'skupinu okruhů', což je logický soubor jednotlivých fyzických okruhů (časových slotů) v přenosovém systému, jako je například E1 (32 slotů) nebo T1 (24 slotů) trasa spojující síťové uzly. Blokování se provádí pomocí specifických signalizačních zpráv, tradičně v rámci [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) protokolového zásobníku Signalizačního systému č. 7 (SS7) nebo jeho IP nástupců jako SIGTRAN.

Mechanismus funguje tak, že systém správy sítě nebo autorizovaný síťový uzel vydá požadavek na blokování (např. zprávu Circuit Group Blocking) směrem k uzlu, který spravuje cílovou skupinu okruhů. Tento požadavek obsahuje identifikátory skupiny okruhů a konkrétních okruhů v ní, které mají být blokovány. Po přijetí a ověření přijímající uzel označí specifikované okruhy jako 'blokované' nebo 'nedostupné' pro nová sestavení hovorů. Existující hovory na těchto okruzích mohou být dokončeny (plynulé blokování) nebo mohou být ukončeny, v závislosti na typu blokování (např. indikace hardwarové poruchy versus blokování pro údržbu). Stav blokování je udržován, dokud není přijata explicitní zpráva o odblokování, která okruhy vrátí do služby.

Mezi klíčové součásti patří spravující síťová entita (jako Operations Support System - [OSS](/mobilnisite/slovnik/oss/) nebo Network Management System - [NMS](/mobilnisite/slovnik/nms/)), signalizační protokol přenášející příkazy blokování/odblokování a ústředna nebo brána, která fyzicky hostuje okruhy. CGB hraje klíčovou roli ve spolehlivosti sítě a efektivitě údržby. Poskytuje softwarově řízenou, vzdálenou metodu pro izolaci síťových segmentů, která je mnohem rychlejší a méně náchylná k chybám než ruční, fyzické zásahy na rozvaděčích. Tato schopnost je zásadní pro minimalizaci narušení služeb během plánovaných činností a pro rychlé omezení závad nebo degradace výkonu v konkrétních skupinách tras.

## K čemu slouží

CGB byl vytvořen k řešení provozních výzev při správě rozsáhlých, geograficky rozptýlených telefonních sítí s přepojováním okruhů. Před takovými standardizovanými vzdálenými procedurami vyžadovala síťová údržba nebo izolace závad fyzický přístup k přenosovému zařízení – často ve vzdálených ústřednách – pro ruční propojení nebo odpojení kabelů. To bylo časově náročné, nákladné a zvyšovalo riziko lidské chyby ovlivňující služby. CGB poskytuje softwarový, in-band signalizační mechanismus pro logickou izolaci skupin okruhů, což umožňuje rychlou reakci na problémy a plánované práce bez fyzického zásahu.

Technologie řeší problém kontinuity služeb během scénářů údržby a závad. Umožněním selektivního blokování podmnožiny okruhů v rámci trasy může být provoz automaticky přesměrován alternativními cestami, čímž se zachová celková dostupnost sítě. Také napomáhá diagnostice závad tím, že umožňuje operátorům testovat nebo izolovat konkrétní okruhy bez dopadu na celou trasu. Jeho zavedení bylo motivováno potřebou automatizovanějších, efektivnějších OAM postupů, jak sítě rostly ve složitosti a rozsahu, což znamenalo odklon od čistě ručních operací směrem k vzdáleně řízené, softwarově definované kontrole síťových zdrojů.

## Klíčové vlastnosti

- Vzdálené softwarové blokování/odblokování skupin okruhů
- Drobně odstupňovaná kontrola umožňující blokování konkrétních okruhů v rámci skupiny
- Pro provedení využívá standardizovanou signalizaci SS7 ISUP nebo SIGTRAN
- Podporuje různé typy blokování (např. pro údržbu nebo hardwarovou poruchu)
- Umožňuje šetrné zacházení s existujícími hovory během procedur blokování
- Nedílná součást správy závad sítě a plánovaných údržbových operací

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [CGB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cgb/)
