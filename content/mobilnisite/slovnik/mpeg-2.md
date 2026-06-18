---
slug: "mpeg-2"
url: "/mobilnisite/slovnik/mpeg-2/"
type: "slovnik"
title: "MPEG-2 – Moving Picture Experts Group Transport Stream"
date: 2025-01-01
abbr: "MPEG-2"
fullName: "Moving Picture Experts Group Transport Stream"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpeg-2/"
summary: "Standardizovaný kontejnerový formát pro přenos audio, video a dat. V 3GPP se používá pro služby multimediálního vysílání a skupinového vysílání (MBMS) k efektivní distribuci živého a na vyžádání přehr"
---

MPEG-2 je standardizovaný kontejnerový formát pro digitální data používaný v 3GPP pro služby multimediálního vysílání a skupinového vysílání (MBMS) k distribuci audio, video a datového obsahu přes mobilní sítě.

## Popis

MPEG-2 Transport Stream (MPEG-2 TS) je kontejnerový formát definovaný skupinou [MPEG](/mobilnisite/slovnik/mpeg/), standardizovaný v [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 13818-1. V rámci architektury 3GPP je přijat jako mechanismus pro doručování obsahu služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Transportní proud je navržen pro přenos digitálního audia, videa a dalších dat přes potenciálně ztrátové nebo nespolehlivé přenosové cesty, což jej činí vhodným pro vysílání přes mobilní sítě. Funguje tak, že multiplexuje jeden nebo více elementárních proudů (např. video, audio, titulky) do jediného proudu. Každý elementární proud je paketizován do paketů Packetized Elementary Stream ([PES](/mobilnisite/slovnik/pes/)), které jsou dále rozděleny a zapouzdřeny do paketů Transportního proudu s pevnou délkou 188 bajtů. Tyto TS pakety obsahují hlavičku s identifikátorem paketu ([PID](/mobilnisite/slovnik/pid/)), který jednoznačně identifikuje elementární proud, ke kterému paket patří, což přijímači umožňuje demultiplexovat a rekonstruovat původní proudy.

Architektura pro doručování MPEG-2 TS přes sítě 3GPP zahrnuje několik klíčových komponent definovaných ve specifikacích jako 26.234 a 26.247. Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) funguje jako vstupní bod pro MBMS obsah. Přijímá MPEG-2 TS od poskytovatele obsahu a připravuje jej pro distribuci přes síť 3GPP. BM-SC plní funkce jako oznámení služby, řízení relace a přenosu a důležité je, že může aplikovat Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)) podle protokolu FLUTE (File Delivery over Unidirectional Transport) pro ochranu proudu před ztrátou paketů přes rozhraní rádiového přístupu. Data MPEG-2 TS jsou poté doručována pomocí IP skupinového vysílání do brány MBMS (MBMS-GW) jádra sítě a dále do rádiové přístupové sítě (např. UTRAN nebo E-UTRAN) pro vysílání/skupinové vysílání k uživatelskému zařízení.

Jeho role v síti je klíčová pro efektivní doručování typu point-to-multipoint. Na rozdíl od unicastového streamování, které vyčleňuje zdroje pro každého uživatele, MBMS využívající MPEG-2 TS umožňuje, aby byl stejný obsah odeslán jednou přes sdílené rádiové zdroje k více uživatelům současně, čímž šetří cennou šířku pásma. Použití standardního, dobře známého kontejnerového formátu jako je MPEG-2 TS usnadňuje interoperabilitu s existujícími vysílacími a mediálními ekosystémy a umožňuje poskytovatelům obsahu znovu použít existující pracovní postupy kódování a produkce. Specifikace 3GPP definují profily a omezení pro použití MPEG-2 TS přes MBMS, což zajišťuje, že mobilní zařízení mohou dekódovat proudy s předvídatelnými požadavky na zdroje.

## K čemu slouží

MPEG-2 Transport Stream byl zaveden do standardů 3GPP, aby poskytl robustní a standardizovanou metodu pro doručování multimediálních služeb vysílací kvality přes celulární sítě. Hlavní problém, který řeší, je neefektivní využití síťových zdrojů při doručování populárního živého obsahu (jako sportovní události nebo zprávy) masovému publiku. Použití tradičního unicastového doručování by přetížilo síť, protože každý uživatel by navázal individuální datové spojení. MBMS s MPEG-2 TS jako svým přenašečem umožňuje efektivní vysílání/skupinové vysílání, čímž transformuje síť z komunikačního systému point-to-point na vysílací médium.

Historický kontext vychází z touhy průmyslu nabízet mobilní TV a distribuci obsahu velkého rozsahu jako životaschopnou službu. Před jeho integrací neexistoval standardizovaný, efektivní způsob streamování živé TV do telefonů přes sítě 3G/4G. MPEG-2 TS byl zvolen, protože to byl již zavedený, široce rozšířený standard v digitální televizi (DVB) a satelitním vysílání, jehož schopnost zvládat časovou synchronizaci, asociaci programů a odolnost proti chybám byla ověřena. Jeho přijetí 3GPP umožnilo mobilnímu průmyslu využít existující odborné znalosti a infrastrukturu, čímž urychlilo nasazení služeb MBMS. Řešil omezení používání obecných IP streamovacích protokolů, které nebyly optimalizovány pro specifické výzvy vysílání přes ztrátová bezdrátová spojení a postrádaly nativní podporu pro multiplexování více mediálních komponent do synchronizované prezentace.

## Klíčové vlastnosti

- Struktura paketů s pevnou délkou 188 bajtů pro snadné rámcování a zpracování
- Systém identifikátorů paketů (PID) pro multiplexování a demultiplexování více elementárních proudů
- Tabulky Program Specific Information (PSI), jako PAT a PMT, pro popis obsahu a struktury proudu
- Vestavěné časové reference (PCR) pro synchronizaci dekódování audia a videa
- Podpora podmíněného přístupu a šifrování pro ochranu služby
- Návrh pro přenos přes prostředí náchylná k chybám, vhodný pro bezdrátové vysílání

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP

---

📖 **Anglický originál a plná specifikace:** [MPEG-2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpeg-2/)
