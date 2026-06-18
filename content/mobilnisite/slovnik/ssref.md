---
slug: "ssref"
url: "/mobilnisite/slovnik/ssref/"
type: "slovnik"
title: "SSREF – SS block reference frequency position"
date: 2025-01-01
abbr: "SSREF"
fullName: "SS block reference frequency position"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssref/"
summary: "Definuje absolutní kmitočtovou polohu bloku synchronizačního signálu (SS block) v rámci šířky pásma nosné 5G NR. Jedná se o klíčový parametr pro počáteční vyhledání a přístup k buňce, protože UE použí"
---

SSREF je absolutní kmitočtová pozice bloku synchronizačního signálu (SS block) v rámci nosné 5G NR, kterou uživatelská zařízení (UE) používají k nalezení a synchronizaci s buňkou během počátečního přístupu.

## Popis

Referenční kmitočtová pozice bloku [SS](/mobilnisite/slovnik/ss/) (SSREF) je základní parametr v 5G New Radio (NR), který určuje absolutní číslo rádiového kmitočtového kanálu (např. ve formátu [NR-ARFCN](/mobilnisite/slovnik/nr-arfcn/)) odpovídající prvnímu subnosiči prvního symbolu bloku synchronizačního signálu / fyzického vysílacího kanálu (SS/[PBCH](/mobilnisite/slovnik/pbch/)). Blok SS/PBCH, často označovaný jako SSB, je sled signálů zahrnující primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)) a PBCH. SSREF poskytuje základní referenční bod ve kmitočtové oblasti, který musí uživatelské zařízení (UE) lokalizovat během procedury počátečního vyhledávání buňky. Bez znalosti SSREF by muselo UE slepě prohledávat celou šířku pásma nosné pro SSB, což by bylo velmi neefektivní a energeticky náročné.

Architektura zahrnuje gNodeB (gNB), který konfiguruje a vysílá SSREF jako součást konfigurace buňky. Samotný SSREF není přímo vysílán ve zprávě; je odvozen z jiných systémových informací. Hlavní informační blok ([MIB](/mobilnisite/slovnik/mib/)), přenášený na PBCH uvnitř SSB, poskytuje parametry jako systemFrameNumber a pdcch-ConfigSIB1. UE tyto informace spolu s předdefinovanými mapovacími pravidly a svým měřením pozice SSB vzhledem k nosné používá k určení absolutního kmitočtu. Specifikace jako 3GPP TS 38.101 (vysílání a příjem UE) a TS 38.104 (vysílání a příjem základnové stanice) definují povolené kmitočtové rozsahy a granularitu pro umístění SSREF. Kmitočtová pozice SSB může být konfigurována v rámci flexibilního rastru, odlišného od kanálového rastru používaného pro obecný výběr nosné, což umožňuje efektivnější využití spektra.

Jak to funguje v praxi: Během počátečního přístupu UE skenuje sadu kmitočtů (kanálový rastr). Když detekuje energii, pokusí se najít PSS a SSS korelací známých sekvencí. Jakmile najde SSB, může dekódovat MIB z PBCH. UE kombinuje informace z MIB se znalostí rozestupu subnosičů SSB a předdefinovaného posunu SSB vůči kanálovému rastru, aby vypočítala SSREF a tím i absolutní kmitočet SSB buňky. Tento vypočtený SSREF je pak používán jako reference pro všechna další měření a konfigurace ve kmitočtové oblasti v rámci této buňky, jako je umístění řídicí sady zdrojů ([CORESET](/mobilnisite/slovnik/coreset/)) pro [SIB1](/mobilnisite/slovnik/sib1/) a počátečních částí pásma pro uplink/downlink. V pásmu FR2 (mmWave), kde se používá beamforming, je SSREF konzistentní napříč různými paprsky SSB, což poskytuje stabilní kmitočtovou referenci pro procedury správy paprsků.

## K čemu slouží

SSREF byl zaveden v 5G NR, aby řešil zvýšenou flexibilitu a šířku pásma nosných NR ve srovnání s LTE. V LTE byly primární a sekundární synchronizační signály (PSS/SSS) vždy umístěny ve středu šířky pásma nosné, což poskytovalo pevnou kmitočtovou referenci. 5G NR však podporuje mnohem širší pásma (až 400 MHz) a různé typy spektra (včetně mmWave), což činí pevné centrální umístění neefektivním nebo nepraktickým. Účelem SSREF je oddělit umístění základních synchronizačních signálů od středu nosné, což umožňuje operátorům sítí umístit SSB na optimální kmitočtovou pozici v rámci pásma.

Tato flexibilita řeší několik problémů. Za prvé umožňuje efektivní podporu úzkopásmových UE (např. pro IoT), která mohou být schopna přijímat pouze malou část pásma; SSB může být umístěn do oblasti přístupné takovým zařízením. Za druhé, ve scénářích se sdílením spektra nebo fragmentovaným spektrem může být SSB umístěn tak, aby se vyhnul rušení nebo byl zarovnán s čistými kmitočtovými segmenty. Za třetí, pro mmWave pásma s vysokým útlumem umožňuje umístění SSB do kmitočtového rozsahu, kde může být analogový beamforming gNB nejefektivněji aplikován během počátečního přístupu. Motivací pro jeho vytvoření bylo umožnit širokou škálu nasazovacích scénářů plánovaných pro 5G, od low-band massive IoT po high-band enhanced mobile broadband.

Historicky bylo pevné umístění synchronizačních signálů v LTE omezením pro pokročilé využití spektra. SSREF jako součást návrhu fyzické vrstvy NR od verze Rel-15 poskytuje potřebnou parametrizaci k odemknutí této flexibility. Řeší výzvu počátečního vyhledávání buňky v heterogenním kmitočtovém prostředí a zajišťuje, že UE mohou spolehlivě a rychle najít a synchronizovat se s buňkami bez ohledu na to, kde se operátor rozhodne umístit synchronizační blok v rámci licencovaného spektra, čímž se snižuje přístupová latence a zlepšuje výkon sítě.

## Klíčové vlastnosti

- Definuje absolutní kmitočtový referenční bod pro blok SS/PBCH v rámci nosné NR
- Umožňuje flexibilní umístění SSB nezávislé na středním kmitočtu nosné
- Je odvozován UE z detekovaných signálů SSB a dekódovaných informací MIB
- Používá pro vyhledávání samostatný SSB rastr, odlišný od kanálového rastru pro výběr nosné
- Kritická reference pro určení kmitočtové polohy CORESET#0 a počátečních částí pásma
- Konzistentní napříč všemi paprsky SSB v buňce pro provoz v pásmech FR1 a FR2

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [SSS – Secondary Synchronization Signal](/mobilnisite/slovnik/sss/)
- [PBCH – Physical Broadcast Channel](/mobilnisite/slovnik/pbch/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution

---

📖 **Anglický originál a plná specifikace:** [SSREF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssref/)
