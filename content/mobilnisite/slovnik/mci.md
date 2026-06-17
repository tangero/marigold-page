---
slug: "mci"
url: "/mobilnisite/slovnik/mci/"
type: "slovnik"
title: "MCI – Malicious Call Identification"
date: 2025-01-01
abbr: "MCI"
fullName: "Malicious Call Identification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mci/"
summary: "Doplňková služba v telefonních sítích s přepojováním okruhů, která účastníkovi umožňuje požádat síť o identifikaci a zaznamenání volajícího čísla u zlovolného, obtěžujícího nebo výhružného hovoru. Jde"
---

MCI je doplňková služba v telefonii s přepojováním okruhů, která účastníkovi umožňuje požádat síť o identifikaci a zaznamenání volajícího čísla u zlovolného nebo obtěžujícího hovoru.

## Popis

Malicious Call Identification (MCI) je klasická doplňková služba definovaná v 3GPP pro telefonní sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), včetně GSM, UMTS a starších částí jádra sítě. Jde o síťovou službu vyvolanou volaným účastníkem během nebo po přijetí hovoru vnímaného jako zlovolný, obscénní, výhružný nebo obtěžující. Po aktivaci služba vyvolá v síti zaznamenání a uložení klíčových informací o problematickém hovoru. Tyto informace obvykle zahrnují číslo volajícího (pokud není potlačeno), číslo volaného, datum a čas hovoru a jeho délku. Tato data jsou uložena v zabezpečeném záznamu, k němuž často mají přístup pouze autorizovaní pracovníci operátora nebo orgány činné v trestním řízení, aby napomohla vyšetřování a případným právním krokům.

Služba funguje prostřednictvím specifických signalizačních procedur. V tradičních sítích GSM/UMTS využívá protokoly jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) v jádru sítě a případně [MAP](/mobilnisite/slovnik/map/) pro interakce s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Když účastník chce službu MCI vyvolat, obvykle provede akci během nebo bezprostředně po zlovolném hovoru. To může být vytočením specifického kódu služby (např. *57 v některých regionech) nebo, v modernějších implementacích, prostřednictvím volby v menu telefonu. Tím se vygeneruje žádost o službu odeslaná k Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). MSC, které již hovor obsluhovalo a vede záznamy o podrobnostech hovoru ([CDR](/mobilnisite/slovnik/cdr/)), pak označí konkrétní CDR spojený s tímto hovorem jako událost "malicious call identification". Může také zahájit další procedury zaznamenávání, aby zajistilo, že jsou příslušná data zachována a spojena se stížností účastníka.

Z architektonického hlediska služba MCI závisí na schopnostech MSC a funkčnosti řízení služeb. Ve starších architekturách inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) může být zapojen Service Control Point (SCP) pro správu logiky služby. Klíčovými komponentami jsou účastnický terminál (pro zahájení žádosti), MSC (pro rozpoznání žádosti a označení záznamu o hovoru) a administrativní systémy operátora, kde jsou zaznamenané informace uloženy a vyhledávány. Služba hovor aktivně neblokuje ani nezachycuje v reálném čase; jde o mechanismus identifikace a zaznamenávání po události. Její účinnost závisí na tom, že je prezentována identita volající linky a není potlačena, a na postupech operátora pro nakládání s zaznamenanými daty.

## K čemu slouží

MCI byla vytvořena, aby řešila základní společenský a bezpečnostní problém v telefonii: obtěžující a výhružné hovory. Před existencí takových služeb měly oběti zlovolných hovorů malou možnost obrany. Mohly problém nahlásit operátorovi, ale bez spolehlivého, sítí ověřeného záznamu o původu hovoru bylo vyšetřování obtížné, zvláště pokud volající použil potlačení čísla. Doplňková služba MCI poskytuje standardizovaný, síťově podporovaný mechanismus pro vytvoření ověřitelné stopy. To slouží dvěma hlavním účelům: působí jako odstrašující prostředek, protože potenciální obtěžovatelé vědí, že jejich identita může být vysledována, a poskytuje konkrétní důkaz pro orgány činné v trestním řízení a soudní řízení.

Služba vznikla v éře pevné telefonie a byla přijata do mobilních standardů (GSM od fáze 2 dále), aby poskytovala konzistentní bezpečnostní funkce napříč sítěmi. Řešila problém zranitelnosti účastníka a posílila uživatele tím, že jim dala jednoduchý nástroj pro reakci na zneužití. Pro síťové operátory poskytla standardizovaný způsob, jak řešit běžnou stížnost zákazníků a splnit regulatorní povinnosti týkající se bezpečnosti a soukromí uživatelů. Omezení přístupu před MCI spočívala v závislosti na manuálním zásahu operátora a v absenci garantovaného, proti manipulaci chráněného záznamu přímo spojeného s žádostí účastníka o vyvolání služby.

V moderním kontextu s úpadkem přepojování okruhů pro hlas a s nástupem IP-based Voice over LTE (VoLTE) a Voice over NR (VoNR) se principy MCI vyvinuly. Podobné funkčnosti pro identifikaci nežádoucí komunikace jsou řešeny různými mechanismy ve službách založených na IP Multimedia Subsystem (IMS), jako je signalizace SIP pro zajištění identity a služby identifikace spamu. Nicméně starší služba MCI zůstává definovanou součástí specifikací domény CS v 3GPP, což zajišťuje zpětnou kompatibilitu a kontinuitu služeb pro sítě a zařízení stále využívající circuit-switched fallback (CSFB) nebo tradiční CS hlas.

## Klíčové vlastnosti

- Umožňuje volanému účastníkovi požádat síť o zaznamenání podrobností zlovolného hovoru.
- Zaznamenává kritická data hovoru: číslo volajícího (pokud je dostupné), číslo volaného, čas, datum a délku.
- Vyvolána účastníkem během nebo po hovoru prostřednictvím kódu služby nebo menu telefonu.
- Spoléhá na Mobile Switching Center (MSC), aby označilo a uložilo příslušný Call Detail Record (CDR).
- Poskytuje ověřitelnou stopu pro vyšetřování síťovými operátory nebo orgány činnými v trestním řízení.
- Standardizovaná doplňková služba pro sítě GSM, UMTS a starší jádrové sítě s přepojováním okruhů.

## Související pojmy

- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [MCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mci/)
