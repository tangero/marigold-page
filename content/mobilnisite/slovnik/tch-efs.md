---
slug: "tch-efs"
url: "/mobilnisite/slovnik/tch-efs/"
type: "slovnik"
title: "TCH-EFS – Traffic Channel Enhanced Full rate Speech"
date: 2025-01-01
abbr: "TCH-EFS"
fullName: "Traffic Channel Enhanced Full rate Speech"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-efs/"
summary: "Traffic Channel Enhanced Full rate Speech (TCH-EFS) je varianta hlasového kanálu v GSM definovaná v dokumentu 3GPP TS 46.055. Používá hlasový kodek Enhanced Full Rate (EFR), který poskytuje téměř pevn"
---

TCH-EFS je kanál pro přenos hovorů v síti GSM, který využívá hlasový kodek Enhanced Full Rate pro poskytování kvalitních, okruhově přepínaných hlasových hovorů rychlostí 12,2 kbps, čímž vylepšuje původní kodek Full Rate.

## Popis

Traffic Channel Enhanced Full rate Speech (TCH-EFS) je specifický typ kanálu pro přenos hovorů ([TCH](/mobilnisite/slovnik/tch/)) v systémech GSM určený pro přenos hlasu zakódovaného kodekem Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)). Kodek EFR, standardizovaný jako kodek [ETSI](/mobilnisite/slovnik/etsi/)/3GPP AMR-EFR (Adaptive Multi-Rate - Enhanced Full Rate), pracuje s pevnou rychlostí 12,2 kbps. Jde o kodek založený na [ACELP](/mobilnisite/slovnik/acelp/) (Algebraic Code-Excited Linear Prediction), který poskytuje výrazně lepší kvalitu hlasu ve srovnání s původním kodekem GSM Full Rate ([FR](/mobilnisite/slovnik/fr/)) (13 kbps) a je srovnatelný s kvalitou kodeku Half Rate ([HR](/mobilnisite/slovnik/hr/)), ale při vyšší přenosové rychlosti. Kanál TCH-EFS zahrnuje celý fyzický a logický řetězec pro přenos tohoto zakódovaného hlasu.

Technicky zabírá kanál TCH-EFS na rozhraní rádiového přístupu jeden celý časový slot na [TDMA](/mobilnisite/slovnik/tdma/) rámec, podobně jako [TCH/F](/mobilnisite/slovnik/tch-f/) (Full Rate TCH). Hlasový signál je zpracován kodekem EFR, který vytvoří 244 bitů na 20ms hlasový rámec. Tyto bity jsou klasifikovány do tříd 1a (nejcitlivější, s ochranou CRC), 1b (středně citlivé) a 2 (nejméně citlivé). Kanálové kódování aplikuje na bity třídy 1 konvoluční kód s poměrem 1/2, čímž přidává redundanci pro ochranu proti chybám, zatímco bity třídy 2 jsou přenášeny nekódované. Výsledných 456 bitů na 20ms blok je následně prokládáno přes 8 po sobě jdoucích TDMA rámců pro potlačení úniků a shlukových chyb. Po zašifrování jsou bity modulovány pomocí GMSK a vysílány.

Kanálem TCH-EFS spravuje řídicí jednotka základnových stanic (BSC) a jednotka pro převod kodeku a přizpůsobení rychlosti (TRAU). BSC přiděluje TCH-EFS na základě vyjednání kodeku během sestavování hovoru (pomocí signalizace jako je procedura Codec Negotiation). TRAU, často umístěná mezi BSC a páteřní sítí, provádí kódování/dekódování EFR a přizpůsobuje 64 kbps PCM proud z páteřní sítě rychlosti 12,2 kbps na rozhraní rádiového přístupu. Fungování TCH-EFS je podrobně popsáno v TS 46.055, který specifikuje pravidla pro převod kodeku a kanálové kódování. Zajišťuje interoperabilitu mezi mobilními stanicemi a sítěmi podporujícími EFR a poskytuje konzistentní vysoce kvalitní hlasový zážitek.

## K čemu slouží

TCH-EFS byl vyvinut, aby vyřešil omezení kvality hlasu původního hlasového kodeku GSM Full Rate (FR), který, přestože byl průlomem pro digitální buněčné sítě, vykazoval znatelné artefakty a špatný výkon v hlučném prostředí. Kodek Enhanced Full Rate, původně vyvinutý pro severoamerický standard D-AMPS (IS-136) jako kodek IS-641, byl přijat pro GSM, aby poskytoval kvalitu hlasu 'blízkou pevné lince'. To byla klíčová konkurenční výhoda, jak mobilní sítě dospívaly a uživatelská očekávání ohledně srozumitelnosti hovorů rostla. Kanál TCH-EFS poskytl standardizovanou přenosovou vrstvu pro nasazení tohoto vylepšeného kodeku v GSM sítích po celém světě.

Hlavním řešeným problémem bylo zlepšení vnímané kvality hlasu bez nutnosti dodatečného rádiového spektra nebo změny základní struktury TDMA kanálu. TCH-EFS využívá stejné rádiové zdroje (jeden časový slot na rámec) jako TCH/F, ale používá pokročilejší kodekový algoritmus. To umožnilo operátorům sítí aktualizovat software v telefonech a síťových prvcích (TRAU) pro podporu EFR a nabídnout tak hmatatelné zlepšení kvality účastníkům. Také zlepšil výkon v podmínkách s okolním šumem a snížil únavu posluchače při dlouhých hovorech.

Historicky byl TCH-EFS součástí evoluce směrem k efektivnějšímu a adaptivnímu hlasovému kódování. Předcházel kodeku Adaptive Multi-Rate (AMR), který se stal konečným hlasovým kodekem pro GSM/UMTS. AMR dokázal dynamicky přepínat mezi více rychlostmi (včetně režimu EFR 12,2 kbps) na základě stavu kanálu, optimalizujíc poměr kvality a kapacity. TCH-EFS však zůstal specifikován jako možnost s pevným režimem pro kompatibilitu a scénáře, kde se nepoužívá vyjednávání AMR. Jeho zařazení od Release 8 v 3GPP specifikacích zajišťuje podporu v moderních sítích pro interoperabilitu se staršími systémy a testování, protože mnoho GSM sítí pokračovalo v používání EFR jako vysoce kvalitního záložního nebo preferovaného kodeku.

## Klíčové vlastnosti

- Přenáší hlas zakódovaný kodekem Enhanced Full Rate (EFR) rychlostí 12,2 kbps
- Poskytuje téměř pevnou linkou kvalitu hlasu, lepší než původní GSM Full Rate
- Používá kódování založené na ACELP s propracovanými třídami ochrany proti chybám
- Zabírá jeden celý časový slot na TDMA rámec (stejně jako TCH/F)
- Zahrnuje specifické kanálové kódování a prokládání definované v TS 46.055
- Je aktivován prostřednictvím vyjednání kodeku během sestavování hovoru

## Související pojmy

- [TCH/F – Traffic Channel / Full Rate](/mobilnisite/slovnik/tch-f/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [TRAU – Transcoder and Rate Adaptation Unit (Frame)](/mobilnisite/slovnik/trau/)

## Definující specifikace

- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [TCH-EFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-efs/)
