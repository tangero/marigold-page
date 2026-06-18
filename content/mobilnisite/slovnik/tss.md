---
slug: "tss"
url: "/mobilnisite/slovnik/tss/"
type: "slovnik"
title: "TSS – Timing Synchronization Status"
date: 2026-01-01
abbr: "TSS"
fullName: "Timing Synchronization Status"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tss/"
summary: "Indikátor sdělující úroveň synchronizační přesnosti síťového uzlu, například gNB v 5G NR. Informuje sousední uzly o kvalitě časové reference uzlu, což je klíčové pro koordinované operace, jako je koor"
---

TSS je indikátor, který sděluje úroveň synchronizační přesnosti síťového uzlu sousedním uzlům pro kritické koordinované operace.

## Popis

Timing Synchronization Status (TSS) je parametr používaný v 3GPP radiových přístupových sítích, zejména v NG-RAN (Next Generation RAN) pro 5G, k vyjádření synchronizační přesnosti základnové stanice (gNB) nebo distribuované jednotky (gNB-DU). Reprezentuje kvalitu časového zdroje uzlu, který může být odvozen z globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/), např. [GPS](/mobilnisite/slovnik/gps/)), protokolu [IEEE](/mobilnisite/slovnik/ieee/) 1588 Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)) nebo ze síťové synchronizace od hlavního uzlu. TSS je typicky komunikován mezi síťovými elementy prostřednictvím signalizačních zpráv rozhraní Xn nebo F1, například v proceduře Xn Setup nebo gNB Configuration Update.

Z architektonického hlediska je TSS součástí synchronizační architektury definované pro 5G NR, která podporuje požadavky na chybu časové synchronizace až v řádu mikrosekund pro funkce jako provoz s duplexem s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), agregace nosných a koordinované přenosy. Každý gNB vyhodnocuje svou vlastní synchronizační přesnost, často kategorizovanou do úrovní (např. 'synchronizováno', 'nesynchronizováno' nebo specifické rozsahy přesnosti jako ±1,5 μs). Tento status je následně sdílen se sousedními gNB a potenciálně s jádrem sítě pro účely řízení. Informace TSS se používají v algoritmech pro výběr buňky, koordinaci interference a zejména ve schématech CoMP, kde více přenosových bodů společně obsluhuje UE a vyžaduje přesné časové zarovnání, aby se předešlo degradaci signálu.

Během provozu gNB kontinuálně monitoruje svůj synchronizační zdroj. Pokud ztratí synchronizaci nebo zjistí sníženou přesnost, aktualizuje svůj TSS a upozorní partnerské uzly. Sousední uzly, které přijmou TSS s hodnotou 'nesynchronizováno' nebo nízkou přesností, mohou daný uzel vyloučit z určitých kooperativních funkcí nebo upravit své plánování ke zmírnění interference. Například v dynamických TDD systémech mohou nesynchronizované buňky způsobovat přesazovou interferenci, a proto TSS pomáhá při aplikaci technik řízení interference. TSS je také zásadní pro rozhodování o předání spojení, protože cílová buňka se špatnou synchronizací nemusí spolehlivě podporovat služby kritické na latenci.

## K čemu slouží

TSS byl zaveden, aby řešil přísné požadavky na synchronizaci pokročilých funkcí RAN v LTE-Advanced a 5G NR. Dřívější buněčné systémy (2G/3G) se primárně spoléhaly na frekvenční synchronizaci, ale technologie jako [TDD](/mobilnisite/slovnik/tdd/), CoMP a New Radio (NR) s širokou šířkou pásma vyžadují přesnou fázovou/časovou synchronizaci, aby mohly efektivně fungovat. Bez mechanismu pro komunikaci stavu synchronizace hrozilo sítím zhoršení výkonu z důvodu nezarovnaných přenosů.

Parametr TSS tento problém řeší tím, že poskytuje standardizovaný způsob, jak mohou uzly oznamovat svou časovou kvalitu, a umožňuje tak inteligentní koordinaci. Umožňuje RAN dynamicky přizpůsobovat kooperativní chování na základě aktuálních synchronizačních podmínek, čímž zvyšuje odolnost a efektivitu. To je obzvláště důležité v hustých nasazeních a heterogenních sítích, kde nemají všechny uzly rovný přístup ke kvalitním časovým zdrojům. TSS podporuje spolehlivost sítě tím, že brání kaskádovému šíření poruch souvisejících se synchronizací.

## Klíčové vlastnosti

- Udává úroveň synchronizační přesnosti gNB (např. synchronizováno/nesynchronizováno)
- Vyměňován prostřednictvím signalizačních procedur rozhraní Xn a F1
- Podporuje pokročilé funkce RAN, jako je řízení interference u CoMP a TDD
- Používá se pro optimalizaci předávání spojení a kritéria výběru buňky
- Integruje se se synchronizačními architekturami (GNSS, PTP, síťová synchronizace)
- Umožňuje dynamické přizpůsobení schémat kooperativního vícebodového přenosu

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [TSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tss/)
