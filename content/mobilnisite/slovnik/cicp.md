---
slug: "cicp"
url: "/mobilnisite/slovnik/cicp/"
type: "slovnik"
title: "CICP – Coding-Independent Code Points"
date: 2025-01-01
abbr: "CICP"
fullName: "Coding-Independent Code Points"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cicp/"
summary: "Coding-Independent Code Points (CICP) jsou standardizované identifikátory pro audio a video kodeky a jejich konfigurace, definované v 3GPP. Umožňují jednoznačné signalizování mediálních schopností a p"
---

CICP je sada standardizovaných identifikátorů pro audio a video kodeky, která umožňuje jednoznačné signalizování mediálních schopností mezi koncovými body za účelem zajištění interoperability v systémech jako je IMS.

## Popis

Coding-Independent Code Points (CICP) jsou sada standardizovaných číselných identifikátorů definovaných 3GPP pro jednoznačné reprezentování audio a video kodeků spolu s jejich specifickými konfiguračními parametry, a to způsobem nezávislým na protokolu. Jsou specifikovány primárně v řadách 3GPP TS 26.114 (IMS Multimedia Telephony) a TS 26.226 (Media Handling and Interaction), s příbuznými definicemi ve specifikacích jako TS 26.253, 26.258, 26.918 a 26.949. Základní koncept spočívá v oddělení identifikace mediálního kodeku od konkrétní syntaxe protokolu pro popis relace (např. [SDP](/mobilnisite/slovnik/sdp/)) používaného k jeho vyjednání. Hodnota CICP funguje jako univerzální klíč, který se mapuje na přesný typ kodeku (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/), H.264, H.265) a definovanou sadu jeho atributů, jako je vzorkovací frekvence, profil, úroveň nebo omezení přenosové rychlosti.

Architektonicky CICP funguje v rámci signalizace mediální a řídicí roviny multimediálních služeb, zejména v IP Multimedia Subsystem (IMS). Když uživatelské zařízení (UE) nebo aplikační server oznamuje své podporované mediální schopnosti během nastavování relace (např. prostřednictvím [SIP](/mobilnisite/slovnik/sip/)/SDP), může použít hodnoty CICP v rámci modelu nabídky/odpovědi SDP nebo jiných signalizačních metod. Například v řádku SDP 'm=' pro audio může atribut 'rtpmap' odkazovat na dynamické číslo typu přenášených dat, které je pak asociováno s konkrétní hodnotou CICP definovanou v samostatné deklaraci schopností nebo uvnitř parametru kodeku. Síťové prvky, včetně [P-CSCF](/mobilnisite/slovnik/p-cscf/), [S-CSCF](/mobilnisite/slovnik/s-cscf/) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), mohou tyto hodnoty CICP interpretovat, aby pochopily přesný mediální kodek, který je navrhován, bez nutnosti parsovat kodek-specifické privátní parametry.

Systém funguje tak, že udržuje standardizovaný registr v rámci specifikací 3GPP, který přiřazuje jedinečné celočíselné hodnoty CICP konkrétním konfiguracím kodeků. Například hodnota CICP 1 může být přiřazena kodeku [AMR-NB](/mobilnisite/slovnik/amr-nb/) s konkrétním režimem šetřícím šířku pásma, zatímco hodnota 40 může reprezentovat kodek EVS s plnopásmovou konfigurací. Tento registr je rozšiřitelný, což umožňuje přiřazení nových hodnot CICP novým kodekům a konfiguracím zavedeným v pozdějších vydáních 3GPP. Během vyjednávání relace si koncové body tyto hodnoty vyměňují a síť může na základě jednoznačné identifikace kodeku provádět kontrolu politik, rozhodnutí o překódování nebo rezervace kvality služeb (QoS). To je klíčové pro služby jako Multimedia Telephony Service for IMS (MTSI), konverzační video a služby vysílání/multicastu, kde je vyžadováno konzistentní zpracování médií napříč různými implementacemi od dodavatelů.

Klíčové komponenty v rámci CICP zahrnují definiční tabulky CICP ve specifikacích, signalizační procedury, které přenášejí hodnoty CICP (např. v atributech SDP, hlavičkách SIP nebo vyhrazených XML tělech v IMS), a síťové funkce, které je zpracovávají. Jejich úlohou je sloužit jako společný jazyk pro mediální kodeky, což snižuje selhání interoperability způsobená nejednoznačnými nebo proprietárními popisy kodeků. Poskytnutím stabilního, verzovaného identifikátoru umožňuje CICP efektivněji spravovat zpětnou a dopřednou kompatibilitu, protože koncové body mohou rozpoznat podporu hodnoty CICP, i když se vnitřní detaily kodeku vyvinuly. Tato abstraktní vrstva je zásadní pro flexibilní nasazení pokročilých audio a video kodeků v sítích 3GPP.

## K čemu slouží

CICP byl vytvořen k vyřešení problému nejednoznačné a nekonzistentní signalizace kodeků v multimediálních komunikačních systémech, zejména v rámci 3GPP IMS. Před jeho zavedením bylo vyjednávání kodeků silně závislé na parametrech SDP, které mohly být specifické pro dodavatele, náchylné k chybnému výkladu nebo úzce svázané s mapováním typů RTP přenášených dat. To vedlo k problémům s interoperabilitou, kdy se koncové body mohly shodnout na kodeku podle názvu (např. 'H.264'), ale nepodařilo se jim navázat mediální relaci kvůli neshodám v nedefinovaných parametrech, jako je profil, úroveň nebo režim paketizace. Motivací bylo vytvořit standardizovanou, budoucím vývoji odolnou metodu pro jednoznačnou identifikaci každé možné konfigurace kodeku, která zajistí, že to, co je signalizováno, je přesně tím, čemu všichni účastníci komunikačního řetězce rozumějí.

Historicky, když 3GPP zavádělo pokročilé kodeky jako Enhanced Voice Services (EVS) pro vysoce kvalitní hlas a nové video kodeky pro streamování 4K, složitost možností kodeků dramaticky vzrostla. Tradiční vyjednávání založené na SDP se stalo nedostatečným pro předání nuance schopností bez dlouhých a náchylných k chybám seznamů parametrů. CICP to řeší tím, že poskytuje jednoduchý celočíselný bod, který zapouzdřuje kompletní definici kodeku včetně všech podstatných atributů. Tato abstrakce zjednodušuje signalizaci, snižuje velikost zpráv a zvyšuje efektivitu zpracování v síťových uzlech, které musí činit rychlá rozhodnutí o mediálních politikách, jako je například povolení kodeku na základě síťových politik nebo profilů účastníka.

Dále CICP podporuje vývoj mediálních služeb oddělením identifikace kodeku od transportního protokolu. To umožňuje používat stejnou hodnotu CICP napříč různými relakovými protokoly (např. WebRTC, MSRP) a síťovými architekturami, což usnadňuje konvergenci mezi ekosystémy 3GPP a ne-3GPP. Také umožňuje pokročilé funkce jako dynamická adaptace, kde síť může během relace nařídit změnu konfigurace kodeku odkazem na jinou hodnotu CICP, čímž zajišťuje konzistentní kvalitu za měnících se síťových podmínek. Řešením těchto základních signalizačních výzev CICP podporuje spolehlivost a škálovatelnost bohatých komunikačních služeb v moderních mobilních sítích.

## Klíčové vlastnosti

- Standardizované celočíselné identifikátory pro jednoznačnou signalizaci kodeku a konfigurace
- Nezávislý návrh na protokolu použitelný napříč SDP, SIP a dalšími signalizačními metodami
- Komplexní registr pokrývající audio kodeky (např. AMR, EVS) a video kodeky (např. H.264, H.265)
- Podpora detailních parametrů kodeku včetně profilů, úrovní a omezení přenosové rychlosti
- Umožňuje efektivní vynucování síťových politik a alokaci mediálních prostředků
- Usnadňuje interoperabilitu a snižuje selhání při navazování relací způsobená neshodami kodeků

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [CICP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cicp/)
