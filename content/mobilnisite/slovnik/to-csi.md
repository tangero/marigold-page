---
slug: "to-csi"
url: "/mobilnisite/slovnik/to-csi/"
type: "slovnik"
title: "TO-CSI – Trunk Originated CAMEL Service Information"
date: 2025-01-01
abbr: "TO-CSI"
fullName: "Trunk Originated CAMEL Service Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/to-csi/"
summary: "Parametr předplatného CAMEL, který označuje, že účastník má nárok na služby inteligentní sítě při přijetí hovoru pocházejícího z trunku (např. z PSTN). Spouští logiku služby CAMEL v síti pro příchozí"
---

TO-CSI je parametr předplatného CAMEL, který spouští logiku služby inteligentní sítě pro příchozí hovory k účastníkovi, pokud hovor pochází z trunku, například z PSTN.

## Popis

Trunk Originated [CAMEL](/mobilnisite/slovnik/camel/) Service Information (TO-CSI) je specifický typ CAMEL Subscription Information ([CSI](/mobilnisite/slovnik/csi/)) uložený v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro mobilního účastníka. CAMEL (Customised Applications for Mobile network Enhanced Logic) je standard inteligentní sítě ([IN](/mobilnisite/slovnik/in/)), který umožňuje operátorům definovat vlastní služby řízení hovorů. Parametr TO-CSI je klíčový pro aplikaci těchto inteligentních služeb na příchozí hovory určené pro účastníka, konkrétně na ty hovory, které pocházejí z mimo mobilní síť, typicky z trunkového rozhraní připojeného k Public Switched Telephone Network ([PSTN](/mobilnisite/slovnik/pstn/)) nebo k jiné síti.

Z architektonického hlediska, když hovor dorazí na Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) z trunku, GMSC dotazuje HLR o směrovací informace (Mobile Station Roaming Number - [MSRN](/mobilnisite/slovnik/msrn/)). Jako součást profilu účastníka může HLR v odpovědi poslat data TO-CSI do GMSC. TO-CSI obsahuje klíčové informace, jako je adresa příslušného CAMEL Service Environment (gsmSCF), který hostuje servisní logiku, Service Key identifikující konkrétní službu a výchozí parametry pro zacházení s hovorem. Po přijetí TO-CSI GMSC, který funguje jako CAMEL Service Switching Function (gsmSSF), zahájí dialog s určeným gsmSCF. Nahlásí událost příchozího hovoru a předá kontrolu, což umožní gsmSCF instruovat GMSC, jak hovor zpracovat na základě přihlášené servisní logiky.

Jak to funguje, zahrnuje interakci v reálném čase mezi síťovými uzly. Například účastník může mít předplacenou službu, která se vztahuje i na příchozí hovory. Když dorazí příchozí hovor z PSTN, GMSC, vybavený TO-CSI, kontaktuje předplacený gsmSCF. gsmSCF pak může zkontrolovat zůstatek na účtu účastníka, aplikovat specifické směrování (např. přesměrovat na hlasovou schránku, pokud je zůstatek nízký) nebo implementovat služby překladu čísel. gsmSCF posílá instrukce zpět do GMSC, aby hovor pokračoval, ukončil nebo upravil. Tento mechanismus zajišťuje, že funkce inteligentní sítě jsou bezproblémově aplikovány na příchozí, z trunku pocházející hovory, a poskytují konzistentní službu bez ohledu na původ hovoru.

## K čemu slouží

TO-CSI byl vytvořen, aby rozšířil výkonné možnosti řízení služeb platformy inteligentní sítě CAMEL na scénáře příchozích hovorů. Rané služby CAMEL se primárně zaměřovaly na řízení hovorů iniciovaných mobilním účastníkem (Mobile Originated - MO). Významná část uživatelského zážitku účastníka – a nabídky služeb operátora – však zahrnuje přijímání hovorů. Bez TO-CSI by inteligentní služby jako blokování příchozích hovorů u předplacených služeb, vlastní přesměrování příchozích hovorů nebo screening příchozích hovorů nemohly být implementovány standardizovaným, síťovým způsobem.

Řeší problém aplikace logiky definované operátorem na hovory přicházející z mimo mobilní síť, konkrétně z trunkových rozhraní připojených k pevným sítím nebo jiným operátorům. Před jeho zavedením bylo zacházení s takovými hovory do značné míry statické, založené na jednoduchých datech z HLR, jako je Call Forwarding Unconditional (CFU). TO-CSI umožnil dynamické řízení v reálném čase serverem servisní logiky. To bylo obzvláště klíčové pro obchodní model předplacených služeb, kde operátoři potřebovali kontrolovat náklady na příchozí hovory (které často nesou) na základě stavu účtu účastníka.

Motivace byla hnána komerční potřebou úplné služební parity mezi příchozími a odchozími hovory v rámci předplacených a dalších přidaných služeb. Jeho zavedení v Release 7 bylo součástí širšího vylepšení CAMEL pro podporu IP Multimedia Subsystem (IMS) a složitějších servisních interakcí, což zajišťovalo, že framework inteligentní sítě zůstal komplexní a použitelný pro všechny části hovoru, čímž chránil příjmy operátorů a umožňoval bohatší funkce služeb.

## Klíčové vlastnosti

- Umožňuje služby inteligentní sítě založené na CAMEL pro příchozí hovory pocházející z trunku/PSTN.
- Uložen jako součást profilu účastníka v Home Location Register (HLR).
- Obsahuje adresu CAMEL Service Environment (gsmSCF) a Service Key.
- Stažen do Gateway MSC (GMSC) během procedury dotazu na směrování hovoru.
- Umožňuje gsmSCF aplikovat servisní logiku v reálném čase (např. kontrolu předplaceného stavu, speciální směrování) na příchozí hovor.
- Nezbytný pro úplnou implementaci předplacené služby, pokrývající jak odchozí, tak příchozí hovory.

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [TO-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/to-csi/)
