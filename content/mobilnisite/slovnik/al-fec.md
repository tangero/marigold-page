---
slug: "al-fec"
url: "/mobilnisite/slovnik/al-fec/"
type: "slovnik"
title: "AL-FEC – Application Layer Forward Error Correction"
date: 2025-01-01
abbr: "AL-FEC"
fullName: "Application Layer Forward Error Correction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/al-fec/"
summary: "AL-FEC je standardizovaný mechanismus pro opravu chyb podle 3GPP, aplikovaný na aplikační vrstvě, který chrání doručování médií přes nespolehlivé sítě. Umožňuje robustní multimediální streamování reko"
---

AL-FEC je standardizovaný mechanismus pro opravu chyb podle 3GPP, aplikovaný na aplikační vrstvě, který chrání doručování médií přes nespolehlivé sítě rekonstrukcí ztracených paketů bez nutnosti retransmisí.

## Popis

Application Layer Forward Error Correction (AL-FEC) je standardizovaný mechanismus pro obnovu chyb definovaný ve specifikacích 3GPP, který funguje na aplikační vrstvě a chrání doručování mediálního obsahu přes paketové sítě. Na rozdíl od mechanismů [FEC](/mobilnisite/slovnik/fec/) na nižších vrstvách je AL-FEC speciálně navržen pro aplikační datové toky a je obzvláště cenný pro služby multicast/broadcast, kde je obnova založená na retransmisích nepraktická. Technologie vytváří redundantní datové pakety z původních mediálních paketů pomocí matematických kódovacích schémat, což příjemcům umožňuje rekonstruovat chybějící pakety bez nutnosti vyžádat si retransmise od zdroje.

AL-FEC funguje prostřednictvím systematických kódovacích schémat, kde se původní zdrojové symboly přenášejí spolu s paritními symboly generovanými algebraickými operacemi. Specifikace 3GPP definují konkrétní schémata FEC včetně Raptor kódů (specifikovaných v 3GPP TS 26.346) a RaptorQ kódů (specifikovaných v [IETF](/mobilnisite/slovnik/ietf/) RFC 6330 a přijatých 3GPP), což jsou fontánové kódy schopné generovat potenciálně neomezený proud kódovacích symbolů. Tyto kódy jsou obzvláště účinné, protože umožňují příjemcům obnovit původní data z jakékoli podmnožiny kódovacích symbolů, která je jen o něco větší než počet zdrojových symbolů, což poskytuje vynikající ochranu proti vzorcům ztráty paketů typickým pro bezdrátové sítě.

Architektura zahrnuje FEC kódování na straně broadcast/multicast serveru a FEC dekódování na klientských zařízeních. Server rozdělí mediální obsah do zdrojových bloků, použije FEC kódování pro generování opravných symbolů a vysílá jak zdrojové, tak opravné symboly podle specifických plánovacích algoritmů. Na straně příjemce klient ukládá přijaté symboly do vyrovnávací paměti a aplikuje dekódovací algoritmy, když je k dispozici dostatek symbolů pro obnovení chybějících paketů. Specifikace 3GPP definují podrobné postupy pro formáty FEC Payload ID, rozdělování zdrojových bloků a konstrukci kódovacích paketů, aby byla zajištěna interoperabilita mezi různými implementacemi.

AL-FEC hraje klíčovou roli v architektuře služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) podle 3GPP, kde zvyšuje spolehlivost služby pro doručování broadcastového obsahu. Je integrován s protokolem [FLUTE](/mobilnisite/slovnik/flute/) (File Delivery over Unidirectional Transport) pro služby doručování souborů a s RTP/RTCP pro služby streamování v reálném čase. Technologie poskytuje konfigurovatelné úrovně ochrany prostřednictvím nastavitelných kódových poměrů, což provozovatelům služeb umožňuje vyvážit režii vůči síle ochrany na základě síťových podmínek a požadavků služby. Tato flexibilita činí AL-FEC vhodným pro různé scénáře nasazení od celulárního broadcastu po over-the-top streamovací služby.

## K čemu slouží

AL-FEC byl vyvinut, aby řešil základní výzvu spolehlivého doručování médií přes inherentně nespolehlivé bezdrátové sítě, zejména pro broadcastové a multicastové služby, kde jsou tradiční mechanismy [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat Request) neefektivní nebo nemožné. V multicastových scénářích různí příjemci zaznamenávají různé vzorce ztráty paketů, což činí obnovu založenou na retransmisích nepraktickou, protože retransmitované pakety by musely vyhovět příjemci v nejhorším případě. AL-FEC poskytuje proaktivní přístup k obnově chyb, který funguje jednotně pro všechny příjemce bez ohledu na jejich individuální vzorce ztrát.

Technologie byla motivována rostoucí poptávkou po efektivních multimediálních broadcastových službách v sítích 3GPP, zejména pro [MBMS](/mobilnisite/slovnik/mbms/), které umožňují simultánní doručování identického obsahu více uživatelům. Předchozí přístupy spoléhaly na [FEC](/mobilnisite/slovnik/fec/) na nižších vrstvách nebo na retransmise na aplikační vrstvě, které byly buď nedostatečně flexibilní pro aplikační potřeby, nebo vytvářely nadměrnou latenci a signalizační režii. AL-FEC konkrétně řeší požadavky služeb streamování v reálném čase, kde jsou zpoždění způsobená retransmisemi nepřijatelná, a broadcastových služeb, kde je zpětný komunikační kanál nedostupný nebo omezený.

Historický kontext ukazuje, že dřívější systémy pro doručování multimédií trpěly buď nadměrnou režií (při silné ochraně), nebo špatnou kvalitou (při slabé ochraně) v podmínkách s vysokou ztrátovostí. AL-FEC přinesl optimální rovnováhu tím, že poskytuje ochranu uvědomující si aplikaci, kterou lze přizpůsobit konkrétním typům obsahu a síťovým podmínkám. Přijetí fontánových kódů, jako jsou Raptor a RaptorQ, představovalo významný pokrok oproti předchozím blokovým kódům, nabízejíc lepší výkon s nižší složitostí a plynulejší degradaci při měnících se podmínkách ztrátovosti.

## Klíčové vlastnosti

- Provoz na aplikační vrstvě nezávislý na transportních protokolech
- Podpora jak systematických, tak nesystematických fontánových kódů (Raptor/RaptorQ)
- Konfigurovatelné úrovně ochrany prostřednictvím nastavitelných kódových poměrů
- Efektivní obnova od výpadků paketů (burst) i náhodných ztrát
- Integrace s protokolem FLUTE pro služby doručování souborů
- Provoz s nízkou latencí vhodný pro aplikace streamování v reálném čase

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [FEC – Forward Erasure Correction / Forward Error Correction](/mobilnisite/slovnik/fec/)
- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)

## Definující specifikace

- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [AL-FEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/al-fec/)
