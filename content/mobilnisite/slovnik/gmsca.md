---
slug: "gmsca"
url: "/mobilnisite/slovnik/gmsca/"
type: "slovnik"
title: "GMSCA – Gateway Mobile Services Switching Centre for the Answering party"
date: 2025-01-01
abbr: "GMSCA"
fullName: "Gateway Mobile Services Switching Centre for the Answering party"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmsca/"
summary: "GMSC umístěný v IPLMN (Interrogating PLMN) volané strany (Answering party) pro hovor s přeneseným číslem (MNP). Provádí počáteční směrovací dotaz a může také vystupovat jako VMSCA, pokud se účastník n"
---

GMSCA je Gateway Mobile Services Switching Centre v síti IPLMN (interrogating PLMN) volaného účastníka, který provádí počáteční směrovací dotaz pro hovor s přeneseným číslem (Mobile Number Portability) a může také fungovat jako navštívená ústředna MSC pro tohoto účastníka.

## Popis

GMSCA je specifická logická role Gateway Mobile Switching Centre ([GMSC](/mobilnisite/slovnik/gmsc/)) definovaná v kontextu přenositelnosti mobilních čísel ([MNP](/mobilnisite/slovnik/mnp/)) a procedur směrování hovorů ve specifikacích 3GPP. Písmeno 'A' znamená 'Answering party', tedy volaný účastník. Tento termín slouží k přesné identifikaci GMSC, který se nachází v Interrogating Public Land Mobile Network ([IPLMN](/mobilnisite/slovnik/iplmn/)). IPLMN je síť, která jako první přijme hovor určený pro přenesené číslo a je odpovědná za dotazování do databáze přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)) nebo za provedení překladu SCCP Global Title ([GT](/mobilnisite/slovnik/gt/)) pro určení správné příjemcovské sítě.

Ve scénáři bez přeneseného čísla je GMSC v domovské síti účastníka ([HPLMN](/mobilnisite/slovnik/hplmn/)) zároveň GMSCA. Avšak s MNP již [MSISDN](/mobilnisite/slovnik/msisdn/) (mobilní číslo) účastníka není pevně svázáno s jeho původní HPLMN. Když je uskutečněn hovor na přenesené číslo, je nejprve směrován na GMSC v síti asociované s původním rozsahem čísla (IPLMN). Tento GMSC, který nyní vystupuje jako GMSCA, musí nejprve provést proces MNP dotazu. Odešle signalizační dotaz (např. zprávu typu SRI-for-SM nebo podobnou [MAP](/mobilnisite/slovnik/map/) zprávu), který spustí překlad SCCP Global Title. Tento překlad, založený na volaném MSISDN, nasměruje dotaz do správné příjemcovské sítě (na HLR donorské sítě nebo centrální NPDB) pro získání směrovacích informací.

Klíčovým architektonickým detailem je, že GMSCA může také sloužit jako Visited MSC pro volanou stranu (VMSCA), pokud se volaný účastník fyzicky nachází v pokrytí stejné sítě, která plní funkci GMSCA. V tomto případě, po dokončení MNP dotazu a potvrzení, že účastník patří do její vlastní sítě (nebo se v ní roamuje), tento uzel plní jak funkci brány, tak funkci obslužné ústředny. Specifikace detailně popisují signalizační toky a rozhodovací logiku pro tyto různé scénáře, aby bylo zajištěno správné směrování hovorů na přenesená čísla bez ohledu na to, zda je účastník ve své donorské síti, příjemcovské síti nebo roamuje jinde.

## K čemu slouží

Koncept GMSCA byl formálně definován, aby řešil složitosti zavedené přenositelností mobilních čísel (MNP). Před MNP bylo směrování hovorů jednodušší: volané MSISDN implicitně definovalo domovskou síť (HPLMN) a hovor byl směrován na GMSC v této síti. MNP toto přímé přiřazení zrušilo a vytvořilo scénář, kdy síť, která hovor jako první přijme (na základě původního rozsahu čísla), nemusí být nutně sítí, která účastníka aktuálně hostí.

Účelem definice role GMSCA je objasnit odpovědnosti a signalizační chování prvního GMSC, který narazí na hovor určený pro potenciálně přenesené číslo. Standardizuje, jak se tento uzel má chovat: musí provést dodatečný krok dotazu na přenositelnost čísla před, nebo jako součást, standardní procedury dotazování HLR. Tím je zajištěna interoperabilita mezi sítěmi různých operátorů v prostředí s přenositelností čísel. Specifikace scénářů, kdy je GMSCA zároveň VMSCA, pomáhá optimalizovat směrování hovorů tím, že se vyhnou zbytečným dalším skokům, když se volaná strana nachází ve stejné síti, která hovor přijala, čímž se zefektivní spojení a sníží signalizační zatížení.

## Klíčové vlastnosti

- Definován jako GMSC v Interrogating PLMN (IPLMN) pro volanou stranu (Answering party)
- Iniciuje proceduru dotazu na přenositelnost mobilních čísel (MNP) pro příchozí hovory
- Může provést překlad SCCP Global Title na základě volaného MSISDN pro směrování dotazů do správné sítě
- Může také převzít roli Visited MSC pro volanou stranu (VMSCA), pokud se účastník nachází v její servisní oblasti
- Integruje logiku MNP se standardním MAP dotazováním HLR pro získání směrovacích informací
- Kritická funkční role pro zajištění správného doručení hovoru v prostředí s přenositelností čísel

## Související pojmy

- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [IPLMN – Interrogating Public Land Mobile Network](/mobilnisite/slovnik/iplmn/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [GMSCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmsca/)
