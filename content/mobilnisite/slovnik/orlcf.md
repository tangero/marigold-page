---
slug: "orlcf"
url: "/mobilnisite/slovnik/orlcf/"
type: "slovnik"
title: "ORLCF – Optimal Routeing for Late Call Forwarding"
date: 2025-01-01
abbr: "ORLCF"
fullName: "Optimal Routeing for Late Call Forwarding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/orlcf/"
summary: "Funkce pro zpracování hovorů v sítích GSM/UMTS, která optimalizuje směrování při přesměrování hovoru po zjištění nedosažitelnosti volané strany. Minimalizuje signalizaci a využití zdrojů výběrem nejef"
---

ORLCF je funkce pro zpracování hovorů v sítích GSM/UMTS, která optimalizuje směrování za účelem minimalizace signalizace a využití zdrojů, když je hovor přesměrován poté, co volaná strana není dosažitelná.

## Popis

Optimal Routeing for Late Call Forwarding (ORLCF) je funkce síťové inteligence definovaná ve specifikacích 3GPP pro služby okruhově přepínané telefonie, primárně v sítích GSM a UMTS. Řeší konkrétní scénář, kdy hovor nemůže být dokončen k zamýšlenému příjemci (B-strana) kvůli nedosažitelnosti účastníka (např. vypnutý telefon, mimo dosah sítě), a hovor je následně přesměrován na předdefinované přesměrovací číslo (C-strana). Hlavní funkcí ORLCF je určit a navázat nejefektivnější signalizační a přenosovou cestu pro tuto přesměrovanou větev hovoru, s obejitím nepotřebných síťových uzlů za účelem snížení latence a úspory přenosových zdrojů.

Z architektonického hlediska zahrnuje ORLCF logiku uvnitř Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)), které hovor zpracovávají. Když se pokus o sestavení hovoru nezdaří kvůli nedosažitelnosti účastníka a je aktivní služba Call Forwarding on Not Reachable (CFNRc), obslužné MSC získá přesměrovací číslo z Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Bez ORLCF by mohl být hovor směrován zpět přes původní GMSC nebo přes MSC B-strany, než dosáhne C-strany. ORLCF umožňuje síti provést analýzu optimálního směrování, což často dovolí MSC, které zjistilo stav nedosažitelnosti, přímo směrovat hovor do sítě C-strany nebo se co nejdříve připojit k PSTN.

Implementace spoléhá na signalizační protokoly jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC). Klíčové parametry ve zprávách pro sestavení hovoru, jako je Original Called Party Number a Redirecting Number, se používají k informování následných ústředen o události přesměrování, což jim umožňuje aplikovat politiky optimálního směrování. Tím se předchází "trombónovému" efektu (tromboning), kdy větve hovoru procházejí zpět stejnými mezinárodními nebo mezispolečenskými bránami. ORLCF je základním kamenem provádění služeb v inteligentní síti ([IN](/mobilnisite/slovnik/in/)) nebo založených na Camel, a zajišťuje, že doplňkové služby jako přesměrování hovorů nezhoršují celkový výkon sítě. Jeho role je klíčová pro minimalizaci mezispolečenských tranzitních nákladů a pro zlepšení doby sestavení hovoru pro přesměrované hovory, což je obzvláště důležité v scénářích mezinárodního roamingu.

## K čemu slouží

ORLCF byl vytvořen, aby řešil neefektivitu vlastní základním implementacím přesměrování hovorů v raných digitálních mobilních sítích. Před jeho standardizací mohla přesměrovaná výzva, zejména po pozdní události jako 'účastník nedosažitelný', sledovat neoptimální cestu. Například mezinárodní hovor k roamujícímu účastníkovi mohl být směrován k [MSC](/mobilnisite/slovnik/msc/) v navštívené zemi, jen aby byl přesměrován zpět na číslo v zemi volajícího, čímž vznikla drahá a dlouhá 'trombónová' trasa přes mezinárodní spoje dvakrát. Toto plýtvalo přenosovou kapacitou, zvyšovalo prodlevu při sestavování hovoru a způsobovalo zbytečné mezispolečenské poplatky.

Primární motivací byly provozní a ekonomické důvody: snížit zatížení sítě a minimalizovat náklady na propojení mezi operátory. Umožněním přímějšího směrování pro přesměrované hovory ORLCF snižuje signalizační provoz na spojích jádrové sítě a zkracuje dobu obsazení drahých mezinárodních okruhů. Z pohledu služby také zlepšuje uživatelský komfort snížením doby po vytočení pro volající stranu, když je její hovor přesměrován. Jeho zavedení ve Release 4 bylo součástí širšího úsilí 3GPP o optimalizaci provozu okruhově přepínaného jádra sítě a efektivity signalizace, jak se sítě rozšiřovaly a mezinárodní roaming se stával běžnějším.

## Klíčové vlastnosti

- Optimalizuje směrování pro podmínky služby Call Forwarding on Not Reachable (CFNRc)
- Snižuje signalizační zatížení a využití přenosových zdrojů tím, že se vyhýbá "trombónovému" efektu (tromboning)
- Využívá parametry protokolů ISUP/BICC, jako je Redirecting Number, pro analýzu trasy
- Implementována jako logika v řídicí funkci pro hovory v MSC/GMSC
- Snižuje mezispolečenské tranzitní náklady pro přesměrované hovory
- Zkracuje dobu sestavení hovoru pro volající stranu

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [CFNR – Communication Forwarding No Reply](/mobilnisite/slovnik/cfnr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [ORLCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/orlcf/)
