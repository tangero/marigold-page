---
slug: "ook"
url: "/mobilnisite/slovnik/ook/"
type: "slovnik"
title: "OOK – On-Off Keying"
date: 2026-01-01
abbr: "OOK"
fullName: "On-Off Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ook/"
summary: "Jednoduchá digitální modulační metoda, při které se pro reprezentaci binární '1' vysílá nosná vlna (zapnuto) a pro reprezentaci binární '0' se nevysílá (vypnuto). V rámci 3GPP se používá pro komunikac"
---

OOK je jednoduchá digitální modulační metoda, při které se pro reprezentaci binární '1' vysílá nosná vlna a pro reprezentaci binární '0' se nevysílá; používá se pro komunikaci IoT s nízkou spotřebou.

## Popis

On-Off Keying (OOK) je základní modulační technika typu amplitudové manipulace (ASK), kde přítomnost nebo nepřítomnost nosného signálu přímo kóduje binární data. V kontextu 3GPP, zejména pro NR-Light (RedCap) a vylepšení IoT, je OOK využíváno pro svou extrémní jednoduchost a energetickou účinnost. Architektura vysílače je přímočará: pro binární '1' je po dobu trvání symbolového intervalu generována a vysílána vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) nosná vlna; pro binární '0' je vysílač efektivně utlumen, čímž spotřebovává minimální výkon. Toto zapínání/vypínání je řízeno digitálním základovým pásmovým signálem.

Na straně přijímače demodulace typicky zahrnuje obálkový detektor nebo jednoduchý obvod pro detekci energie. Přijímač měří sílu nebo výkon přijímaného signálu během symbolového intervalu. Signál s výkonem nad určitou prahovou hodnotou je dekódován jako '1', zatímco výkon pod prahem (často pouze šum) je dekódován jako '0'. Tato nekoherentní detekce nevyžaduje složitou obnovu fáze nosné vlny, což dále zjednodušuje návrh přijímače. Klíčové parametry ovlivňující výkon OOK v systémech 3GPP zahrnují rychlost symbolů, která určuje datovou propustnost, a rozhodovací práh na přijímači, který ovlivňuje míru bitových chyb ([BER](/mobilnisite/slovnik/ber/)) v přítomnosti šumu a interference.

Úloha OOK v moderních sítích 3GPP, zejména od Release 18 dále, spočívá především v umožnění rádiových rozhraní s ultranízkou spotřebou pro probouzení (WUR) a pro jednoduchou komunikaci senzorů. Je specifikováno v rámci NR sidelink a potenciálně pro přímou komunikaci mezi zařízeními v IoT scénářích. Jeho spektrální účinnost je nízká ve srovnání s pokročilejšími modulačními schématy, jako jsou [QPSK](/mobilnisite/slovnik/qpsk/) nebo [16QAM](/mobilnisite/slovnik/16qam/), protože přenáší pouze jeden bit na symbol a využívá relativně širokou šířku pásma kvůli ostrým přechodům mezi stavem zapnuto a vypnuto. Tento kompromis je však přijatelný pro aplikace, kde je minimalizace nákladů na zařízení, jeho složitosti a spotřeby energie prvořadá oproti dosažení vysokých přenosových rychlostí.

## K čemu slouží

OOK bylo zavedeno do standardů 3GPP, aby řešilo potřebu extrémní energetické účinnosti pro specifické případy použití Internetu věcí (IoT) a komunikace mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)). Před jeho formálním zahrnutím se i pro jednoduché hlášení stavu nebo probouzení používala složitější modulační schémata, která spotřebovávala více energie, než bylo pro požadovanou funkci nutné. Historická motivace vychází z rozšíření senzorů a nositelných zařízení napájených bateriemi, které vyžadují roky provozu na jedno nabití baterie.

Omezení předchozích přístupů, jako například použití plné fyzické vrstvy NR založené na [OFDM](/mobilnisite/slovnik/ofdm/) pro občasné přenosy malých objemů dat, představovala nadměrná režie a spotřeba energie. OOK poskytuje minimalistickou alternativu. Jeho vytvoření v rámci 3GPP Rel-18 standardizuje společnou, interoperabilní metodu pro implementaci těchto spojů s ultranízkou spotřebou, což zajišťuje, že mohou efektivně koexistovat se širokopásmovými nosnými 5G NR, aniž by způsobovaly škodlivé interference. Řeší problém udržování rádiového spojení pro řídicí účely (jako je probuzení hlavního rádiového rozhraní) nebo přenos minimálních dat ze senzorů při odebírání nepatrného množství energie z baterie zařízení.

## Klíčové vlastnosti

- Binární modulace prostřednictvím přítomnosti (zapnuto) nebo nepřítomnosti (vypnuto) nosné vlny
- Extrémně jednoduchá architektura vysílače a přijímače
- Nekoherentní detekce, která eliminuje potřebu synchronizace fáze nosné vlny
- Vysoká energetická účinnost ideální pro zařízení s omezenou kapacitou baterie
- Specifikováno pro použití v NR sidelink a scénářích vylepšení IoT
- Lze použít k implementaci funkce rádiového rozhraní pro probouzení (Wake-Up Radio, WUR)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.848** (Rel-18) — Technical Report on Ambient IoT
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [OOK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ook/)
