---
slug: "glr"
url: "/mobilnisite/slovnik/glr/"
type: "slovnik"
title: "GLR – Gateway Location Register"
date: 2025-01-01
abbr: "GLR"
fullName: "Gateway Location Register"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/glr/"
summary: "Gateway Location Register (GLR) je funkční uzel v jádrových sítích GSM a UMTS, který slouží jako dočasný návštěvnický lokální registr pro roamující účastníky. Je nasazen na hranici sítě, aby optimaliz"
---

GLR je funkční uzel v sítích GSM a UMTS, který funguje jako dočasný návštěvnický lokální registr pro roamující účastníky. Je nasazen na hranici sítě za účelem optimalizace signalizace mezi sítěmi a snížení zatížení domovského HLR.

## Popis

Gateway Location Register je specializovaný síťový prvek definovaný ve specifikacích 3GPP pro jádrové sítě GSM a UMTS (okruhově přepínaná doména). Jeho hlavní funkcí je sloužit jako dočasná vyrovnávací paměť pro účastnická data příchozích roamujících uživatelů. Když účastník přicestuje (zaroamuje) do navštívené sítě, namísto aby Navštívená ústředna mobilní komunikace ([VMSC](/mobilnisite/slovnik/vmsc/)) dotazovala domovský lokální registr ([HLR](/mobilnisite/slovnik/hlr/)) účastníka v jeho domovské síti pro každou událost mobility nebo služby, přebírá GLR navštívené sítě pro tohoto účastníka roli HLR. GLR si nejprve během počáteční registrace (aktualizace polohy) stáhne profil účastníka ze skutečného HLR a uloží jej lokálně. Následně VMSC komunikuje s GLR, jako by šlo o HLR, při procedurách jako je doručování hovorů, aktualizace polohy uvnitř navštívené sítě a dotazy na doplňkové služby.

Z architektonického hlediska je GLR typicky nasazen na okraji sítě, často integrován s Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) nebo jako samostatný uzel. Rozhraní k VMSC využívá standardní rozhraní B/C/D (protokoly [MAP](/mobilnisite/slovnik/map/)) a domovské síti a jejímu HLR se jeví jako standardní [VLR](/mobilnisite/slovnik/vlr/). Tato transparentnost je klíčová; HLR si není vědom přítomnosti GLR a jednoduše jej vidí jako VLR, který účastníka právě obsluhuje. GLR spravuje mobilitu účastníka v rámci celé navštívené sítě (která může obsahovat více oblastí VLR). Teprve když účastník opustí pokrytí celé navštívené sítě, GLR o nové poloze informuje HLR, čímž minimalizuje mezinárodní signalizaci MAP.

Pro mobilně ukončené hovory je hovor směrován na GMSC navštívené sítě. GMSC se dotazuje HLR, který má adresu GLR uloženou jako aktuální „VLR“. HLR poskytne roamingové číslo od GLR (nikoli od VMSC). GLR, který zná aktuální adresu VMSC účastníka, si pak sám vyžádá roamingové číslo od tohoto VMSC a předá jej GMSC k dokončení navázání hovoru. Tento dvoukrokový proces udržuje HLR mimo signalizační cestu pro každý hovor uvnitř navštívené sítě. GLR také zpracovává autentizaci, často tím, že z HLR získá sadu autentizačních vektorů a používá je postupně, což dále snižuje signalizaci.

## K čemu slouží

GLR byl vyvinut, aby řešil významné náklady na signalizaci a latenci spojené s mezinárodním roamingem v raných sítích GSM. Bez GLR vyžadovala každá událost mobility (jako přesun mezi oblastmi polohy) a každé navázání mobilně ukončeného hovoru pro roamujícího účastníka signalizační výměny mezi navštívenou [MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/) a domovským HLR přes často drahé a přetížené mezinárodní signalizační spoje (SS7). To vedlo k vysokým provozním nákladům pro operátory, prodloužení doby navazování hovorů a zatížení HLR.

Zavedení GLR to vyřešilo lokalizací signalizace uvnitř navštívené sítě. Ukládáním účastnických dat do mezipaměti mohla navštívená síť většinu procedur zvládnout autonomně. Hlavními motivy byly ekonomické (snížení mezinárodního signalizačního provozu) a výkonnostní (zlepšení odezvy služeb pro roamující uživatele). Bylo to zvláště výhodné pro operátory v regionech s vysokým objemem příchozí turistiky nebo služebních cest. Koncept GLR umožnil operátorům navštívených sítí nabízet roamujícím lepší kvalitu služeb při současné kontrole vlastních nákladů na signalizační infrastrukturu, čímž se roamingové dohody staly efektivnějšími. Představoval optimalizaci v rámci architektury jádrové sítě předtím, než rozšířené přijetí přenosu založeného na IP snížilo některé z cenových rozdílů.

## Klíčové vlastnosti

- Funguje jako dočasná proxy HLR pro příchozí roamující účastníky a ukládá jejich profily lokálně.
- Významně snižuje mezinárodní signalizaci MAP mezi navštívenou a domovskou sítí.
- Zpracovává správu mobility (aktualizace polohy) uvnitř navštívené sítě bez kontaktování HLR.
- Spravuje směrování hovorů pro mobilně ukončené hovory komunikací s VMSC za účelem získání roamingových čísel.
- Může dávkově načítat autentizační vektory z HLR k provádění lokální autentizace.
- Je transparentní pro domovský HLR, který GLR vidí jako standardní Navštívený lokální registr (VLR).

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 23.119** (Rel-19) — Gateway Location Register (GLR) Stage 2 Description
- **TR 23.909** (Rel-5) — Gateway Location Register (GLR) Architecture
- **TS 29.119** (Rel-19) — GTP for GLR in 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [GLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/glr/)
