---
slug: "sor"
url: "/mobilnisite/slovnik/sor/"
type: "slovnik"
title: "SOR – Support of Optimal Routing"
date: 2025-01-01
abbr: "SOR"
fullName: "Support of Optimal Routing"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sor/"
summary: "SOR je funkce CAMEL (Customized Applications for Mobile network Enhanced Logic), která umožňuje optimální směrování mobilních příchozích hovorů. Umožňuje síti dotazovat se HLR na informace o směrování"
---

SOR je funkce CAMEL, která umožňuje optimální směrování mobilních příchozích hovorů dotazováním HLR na informace o směrování, když je účastník v roamingu, čímž se zabrání neefektivním trombónovým trasám.

## Popis

Support of Optimal Routing (SOR, podpora optimálního směrování) je funkce v rámci protokolu [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile network Enhanced Logic), která optimalizuje směrování mobilních příchozích ([MT](/mobilnisite/slovnik/mt/)) hovorů, zejména pro účastníky v roamingu. Její architektura zahrnuje klíčové uzly jádra sítě: Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)), Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visited MSC ([VMSC](/mobilnisite/slovnik/vmsc/)). Když je uskutečněn hovor na účastníka v roamingu, hovor se typicky nejprve směruje do GMSC v domácí síti účastníka. Bez SOR by se GMSC dotázalo HLR, obdrželo od VMSC v navštívené síti Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)) a poté směrovalo hovor mezinárodně z domácí sítě do navštívené sítě. Pokud se však volající nachází ve stejné navštívené zemi nebo v třetí zemi, vytváří to 'trombónový' efekt, kdy přenos hovoru zbytečně putuje do domácí sítě a zpět, čímž se zvyšuje latence a náklady.

SOR funguje vylepšením procesu CAMEL interrogace. Když hovor dorazí do GMSC, lze GMSC nakonfigurovat tak, aby určilo, zda je možné optimální směrování na základě polohy volajícího. Pokud se zjistí, že se volající nachází v místě, kde existuje přímější trasa do navštívené sítě, GMSC zahájí CAMEL dialog s Service Control Point ([SCP](/mobilnisite/slovnik/scp/)). SCP může pomocí své logiky a případně polohy volajícího instruovat GMSC, aby hovor přeposlalo k jinému síťovému uzlu nebo použilo alternativní postup směrování. Klíčový mechanismus spočívá v tom, že GMSC odešle speciální parametr ve zprávě MAP_SEND_ROUTING_INFORMATION do HLR, což indikuje požadavek na informace pro optimální směrování. HLR a VMSC spolupracují na umožnění přímější směrovací cesty, potenciálně poskytnutím směrovacích čísel, která umožní propojení v jiném, optimalizovanějším bodě sítě.

Hlavní úlohou SOR v síti je ekonomická a výkonnostní optimalizace pro mezinárodní roamingové scénáře. Minimalizuje využití nákladných mezinárodních přenosových okruhů spravovaných operátorem domácí sítě, čímž snižuje Inter-Operator Tariffs (IOT). Technicky zkracuje cestu hovoru, což snižuje prodlevu po vytočení a může zlepšit uživatelský zážitek. SOR je úzce integrována s protokolem MAP (Mobile Application Part) a CAMEL servisní logikou. Její nasazení vyžaduje podporu v GMSC, HLR a potenciálně v signalizační síti (např. konfigurace STP), aby bylo zajištěno správné zpracování dotazů a odpovědí pro optimální směrování napříč sítěmi různých operátorů, což je často upraveno bilaterálními dohodami.

## K čemu slouží

SOR byla vytvořena za účelem řešení konkrétního a nákladného problému suboptimálního směrování hovorů pro mobilní účastníky v roamingu, což byla hlavní bolestivá záležitost v raném mezinárodním GSM roamingu. Před SOR bylo směrování hovorů pro účastníka v roamingu pevné a sledovalo standardní cestu: hovor do GMSC domácí sítě -> dotaz na domácí HLR -> kontaktování navštíveného VMSC pro MSRN -> směrování hovoru z domácí sítě do navštívené sítě. Tento model předpokládal, že se volající nachází v domovské zemi. S rostoucím mezinárodním cestováním se však objevil častý scénář: volající ve stejné cizí zemi jako účastník v roamingu (např. dva turisté ve Španělsku) by měl svůj hovor směrován zpět do domácí sítě účastníka (např. v USA), jen aby byl poslán zpět do Španělska, čímž vznikla neefektivní a nákladná 'trombónová' trasa přes mezinárodní přepravce.

Toto trombónování vedlo k několika problémům: delší době sestavení hovoru kvůli delším signalizačním cestám, zvýšené míře neúspěšnosti hovorů kvůli většímu počtu zapojených síťových segmentů a výrazně vyšším nákladům pro operátory i koncové uživatele, protože hovor zahrnoval poplatky za mezinárodní přenos na dvou dlouhých úsecích. SOR tyto omezení řešila zavedením inteligence a flexibility do rozhodování o směrování hovoru. Umožnila síti dynamicky určit optimalizovanější cestu na základě polohy volajícího a obejít domácí síť, pokud nebyla nejefektivnějším směrovacím bodem. Motivace byla primárně ekonomická – snížit vypořádání Inter-Operator Tariff (IOT) mezi operátory – ale také přinesla hmatatelné zlepšení kvality služby tím, že mezinárodní roamingové hovory byly rychlejší a spolehlivější. SOR se stala klíčovou funkcí pro operátory s velkou základnou odchozích roamingových účastníků, aby mohli kontrolovat náklady a zůstat konkurenceschopní.

## Klíčové vlastnosti

- Dynamické vyhýbání se trombónovým trasám pro mobilní příchozí hovory na účastníky v roamingu
- Integrace s protokolem CAMEL pro inteligentní řízení směrování
- Využití vylepšení MAP signalizace mezi GMSC a HLR
- Snížení nákladů na mezinárodní přenos a Inter-Operator Tariffs (IOT)
- Zkrácení doby sestavení hovoru (prodlevy po vytočení) pro roamingové scénáře
- Vyžaduje podporu v GMSC, HLR a často bilaterální dohody mezi operátory

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [SOR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sor/)
