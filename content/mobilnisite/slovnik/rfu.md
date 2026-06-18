---
slug: "rfu"
url: "/mobilnisite/slovnik/rfu/"
type: "slovnik"
title: "RFU – Reserved for Future Use"
date: 2025-01-01
abbr: "RFU"
fullName: "Reserved for Future Use"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/rfu/"
summary: "Reserved for Future Use (RFU) je označení rezervovaného místa používané v technických specifikacích 3GPP pro bity, pole, kódové body nebo prvky zpráv, které nejsou definovány v aktuální verzi standard"
---

RFU je označení rezervovaného místa ve specifikacích 3GPP pro bity nebo pole, která nejsou v současné době definována. Zajišťuje zpětnou kompatibilitu tím, že příjemci je ignorují, a umožňuje jejich budoucí využití.

## Popis

Reserved for Future Use (RFU) je klíčová standardizační technika používaná napříč specifikacemi protokolů a rozhraní 3GPP. Odkazuje na konkrétní části protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), informačního prvku ([IE](/mobilnisite/slovnik/ie/)), pole zprávy nebo bitové mapy, které jsou v aktuální verzi specifikace záměrně ponechány nedefinované. Tyto rezervované prvky nesmějí být v aktuální verzi vysílači použity – musí být nastaveny na předdefinovanou hodnotu, často '0'. Příjemci jsou naopak povinni ignorovat obsah jakéhokoli pole označeného jako RFU. Toto chování typu 'ignorovat a zpracovat zbytek' nebo 'ignorovat a přeposlat' je základním pravidlem pro zajištění robustní dopředné kompatibility.

Z architektonického hlediska se RFU objevuje v abstraktní syntaxi definic protokolů, typicky popsané v Abstract Syntax Notation One (ASN.1) nebo v tabulkových popisech bitových polí. Například 2bitové pole může mít hodnoty '00' pro význam 'povoleno', '01' pro 'zakázáno' a hodnoty '10' a '11' označené jako RFU. Ve schématech toku zpráv a podrobných specifikacích je sémantika a přípustné hodnoty jakéhokoli prvku označeného jako RFU výslovně uvedena jako 'rezervováno' pro budoucí verze. Zacházení s RFU je klíčovou součástí shody s protokolem: kompatibilní UE nebo síťový uzel nesmí vysílat libovolné hodnoty v bitech RFU a nesmí interpretovat přijaté bity RFU jako přenášející jakoukoli smysluplnou informaci.

Fungování RFU je nedílnou součástí vývoje standardů. Když je v pozdější verzi 3GPP (např. Rel-18) potřeba zavést novou funkci, pracovní skupina pro standardy může přehodnotit dříve RFU pole a přiřadit mu nový, konkrétní význam. Například RFU bit v řídicím prvku [MAC](/mobilnisite/slovnik/mac/) z Rel-15 může být v Rel-18 definován jako příznak pro nový signál úspory energie. Protože všechna zařízení Rel-15 a Rel-16 byla povinna tento bit ignorovat, budou i nadále fungovat normálně při příjmu zpráv od vysílače Rel-18, který novou funkci používá. Zařízení Rel-18, které zná svou vlastní schopnost, může bit interpretovat správně. Tento mechanismus umožňuje plynulá, nerušivá vylepšení.

Role RFU se rozprostírá napříč všemi vrstvami a rozhraními, od struktur rámců fyzické vrstvy (jako jsou formáty downlink control information, [DCI](/mobilnisite/slovnik/dci/), v NR) až po signalizaci vyšších vrstev [NAS](/mobilnisite/slovnik/nas/) a [RRC](/mobilnisite/slovnik/rrc/), a dokonce i do managementových rozhraní. Je to proaktivní konstrukční princip, který předjímá budoucí neznámé požadavky. Rezervováním místa předem se tvůrci specifikací vyhýbají potřebě pozdějších, více rušivých změn, jako je zvětšování velikosti zpráv nebo definování zcela nových zpráv pro drobná vylepšení, což by bylo méně efektivní a pravděpodobně by vedlo k problémům s interoperabilitou mezi různými verzemi standardu.

## K čemu slouží

Hlavním účelem mechanismu RFU je zaručit dlouhodobou dopřednou a zpětnou kompatibilitu v ekosystému s více dodavateli a více verzemi standardu. Mobilní sítě jsou nasazovány po desetiletí, přičemž spolu koexistuje zařízení a terminály od mnoha různých dodavatelů podporujících různé verze 3GPP. Bez disciplinovaného přístupu k rezervování polí by každá nová funkce riskovala narušení funkčnosti starších zařízení nebo by vyžadovala neefektivní řešení, jako jsou nové typy zpráv. RFU poskytuje strukturovaný 'únikový ventil' pro budoucí inovace v rámci stávajícího protokolového rámce.

Řeší problém sklerotizace protokolu. V raných telekomunikačních standardech někdy absence takové rezervace vedla k 'vyčerpání bitů', kdy nezbývaly žádné volné kódy pro nové funkce, což nutilo k neohrabaným rozšířením nebo dokonce k úplnému překreslení protokolu. Koncept RFU je poučením z těchto zkušeností. Umožňuje standardu vyvíjet se přírůstkově a udržitelně. Tím, že nařizuje příjemcům ignorovat RFU, zajišťuje, že starší zařízení neporuchuje ani nesprávně neinterpretuje zprávu z novější sítě, která využívá budoucí funkci zakódovanou v dříve RFU poli.

Dále RFU podporuje efektivní využití šířky pásma a výpočetního výkonu. Namísto neustálého přidávání nových volitelných [IE](/mobilnisite/slovnik/ie/) nebo prodlužování zpráv – což zvyšuje režii – lze nové funkce často kompaktně zakódovat do již přidělených a přenášených bitů. To je obzvláště důležité pro řídicí signalizaci, která by měla být minimální. Historický kontext RFU je zakořeněn v robustních principech softwarového a protokolového inženýrství aplikovaných na vysoce omezenou a na interoperabilitě kritickou doménu globálních mobilních standardů. Ztělesňuje princip návrhu pro změnu, který zajišťuje, že se systémy 3GPP mohou během své provozní životnosti přizpůsobit nepředvídaným službám a technologiím.

## Klíčové vlastnosti

- Rezervované místo pro nedefinované bity/pole/kódové body v dané verzi specifikace
- Vysílače musí nastavit RFU na určené výchozí hodnoty (např. nulu)
- Příjemci musí ignorovat hodnotu/obsah jakéhokoli pole RFU
- Umožňuje nerušivé zavedení nových funkcí v budoucích verzích
- Důsledně aplikováno napříč protokoly fyzické, spojové a síťové vrstvy
- Základní prvek pro zajištění dopředné/zpětné kompatibility v nasazeních s více verzemi standardu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [RFU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfu/)
