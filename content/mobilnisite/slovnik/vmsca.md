---
slug: "vmsca"
url: "/mobilnisite/slovnik/vmsca/"
type: "slovnik"
title: "VMSCA – Visited Mobile Switching Center of the A-subscriber"
date: 2025-01-01
abbr: "VMSCA"
fullName: "Visited Mobile Switching Center of the A-subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vmsca/"
summary: "Konkrétně označuje navštívenou ústřednu MSC (Visited MSC), která aktuálně obsluhuje volajícího účastníka (A-subscriber) v mobilně iniciovaném hovoru. Používá se v procedurách směrování hovorů a účtová"
---

VMSCA je navštívený ústřednový uzel mobilní sítě (Visited Mobile Switching Center), který aktuálně obsluhuje volající stranu; používá se k identifikaci síťového prvku zpracovávajícího stranu iniciátora hovoru pro směrování a účtování.

## Popis

Navštívený ústřednový uzel mobilní sítě účastníka A (VMSCA) je specifická instance [VMSC](/mobilnisite/slovnik/vmsc/), identifikovaná v signalizačních protokolech k přesnému určení [MSC](/mobilnisite/slovnik/msc/) obsluhujícího volajícího účastníka. V telekomunikační terminologii je 'A-subscriber' strana iniciující hovor (volající), zatímco 'B-subscriber' je volaná strana (příjemce). VMSCA je tedy VMSC v síti, ve které se A-subscriber aktuálně nachází v roamingu, když uskuteční hovor. Tato přesná identifikace je klíčová pro správné směrování hovorů, provádění služeb a účtování ve scénářích zahrnujících více sítí nebo pokročilé funkce zpracování hovorů.

Z architektonického hlediska se VMSCA neliší jako fyzický uzel od standardního VMSC; jde o roli, kterou VMSC přebírá na základě toku hovoru. Jeho klíčové komponenty jsou shodné s generickým VMSC, včetně ústřednového pole (switch fabric) a přidruženého [VLR](/mobilnisite/slovnik/vlr/). Rozdíl je čistě funkční a kontextový v rámci signalizačních zpráv protokolů, jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)). Když A-subscriber iniciuje hovor, jeho obsluhující VMSC se pro tuto relaci hovoru stává VMSCA. Je zodpovědný za sběr vytočených číslic, provedení počáteční analýzy a zahájení signalizace pro sestavení hovoru směrem k síti účastníka B.

Role VMSCA se stává obzvláště důležitou ve složitých scénářích hovorů, jako je Přesměrování hovoru (Call Forwarding). Pokud má B-subscriber aktivované přesměrování, může být počáteční pokus o sestavení hovoru přesměrován. V takových případech musí záznamy pro účtování (Call Detail Records, [CDR](/mobilnisite/slovnik/cdr/)) přesně odrážet řetězec událostí. Identita VMSCA je zahrnuta v těchto záznamech, aby bylo zajištěno, že síť obsluhující A-subscribera může být správně identifikována pro účely fakturace, zejména při zúčtování mezi operátory. Dále, pro optimální směrování a vyhnutí se neoptimálním směrovacím cestám (tromboning), mohou signalizační zprávy obsahovat adresu VMSCA, aby informovaly následující uzly v cestě hovoru o vstupním bodu iniciátora do sítě.

## K čemu slouží

Koncept VMSCA existuje, aby poskytl granularitu a přesnost v rámci zpracování hovorů a účtování v mobilních sítích s více operátory a podporou roamingu. Jednoduchý identifikátor '[VMSC](/mobilnisite/slovnik/vmsc/)' je nedostatečný, když jedna větev hovoru zahrnuje více MSC (např. ve scénářích s přesměrováním) nebo když je kritické rozlišit mezi sítěmi obsluhujícími volajícího a volaného. Řeší problém nejednoznačného přiřazení v logice účtování a směrování.

Historicky, s tím jak se standardizovaly doplňkové služby jako přesměrování hovoru, se ukázalo, že hovor může procházet několika sítěmi. Například účastník v roamingu v Síti X (VMSCA) volá účastníkovi, jehož telefon je vypnutý a hovor je přesměrován na číslo v Síti Y. Cesta hovoru zahrnuje VMSCA, GMSC/HLR účastníka B a nakonec MSC v Síti Y. Bez explicitního označení VMSCA by mohlo být pro fakturační systémy obtížné určit, která síť hovor iniciovala pro účely rozdělení výnosů mezi operátory.

Účelem definice VMSCA v technických specifikacích je zajistit jednoznačnou signalizaci a záznam dat. Umožňuje správnou aplikaci služeb a tarifů na straně iniciátora pro A-subscribera, i když se nachází v roamingu. Také umožňuje efektivnější rozhodování o směrování dále v řetězci sestavování hovoru, protože uzly, které znají VMSCA, mohou potenciálně volit cesty minimalizující využití mezinárodních nebo mezisíťových tras. Tato úroveň podrobnosti byla motivována potřebou spravedlivého a přesného finančního zúčtování mezi operátory v stále složitějším globálním roamingovém ekosystému.

## Klíčové vlastnosti

- Identifikuje konkrétní VMSC obsluhující volajícího účastníka (A-subscriber)
- Používá se v rámci signalizačních protokolů pro hovory (např. ISUP, MAP) pro informace o směrování
- Kritické pole v záznamech pro účtování (CDR) pro přesné mezifiremní účtování
- Umožňuje správnou aplikaci služeb a omezení hovorů založených na iniciátorovi
- Podporuje optimální směrování ve složitých scénářích hovorů, jako je přesměrování
- Poskytuje kontext pro správu mobility související s iniciátorem hovoru

## Související pojmy

- [VMSC – Visited Mobile Switching Center](/mobilnisite/slovnik/vmsc/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [VMSCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/vmsca/)
