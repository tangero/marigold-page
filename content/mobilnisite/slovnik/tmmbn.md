---
slug: "tmmbn"
url: "/mobilnisite/slovnik/tmmbn/"
type: "slovnik"
title: "TMMBN – Temporary Maximum Media Stream Bit Rate Notification"
date: 2025-01-01
abbr: "TMMBN"
fullName: "Temporary Maximum Media Stream Bit Rate Notification"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tmmbn/"
summary: "Typ paketu protokolu RTCP (Real-time Transport Control Protocol) používaný v relacích založených na RTP k oznámení odesílateli média o dočasném limitu datového toku, který má použít pro konkrétní medi"
---

TMMBN je typ paketu RTCP, který oznamuje odesílateli média dočasný limit maximálního datového toku pro konkrétní proud a poskytuje zpětnou vazbu pro správu zahlcení a přizpůsobení omezením přijímače nebo sítě.

## Popis

TMMBN (Temporary Maximum Media Stream Bit Rate Notification) je specifický formát paketu [RTCP](/mobilnisite/slovnik/rtcp/), původně definovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 5104 a přijatý a profilovaný 3GPP pro použití ve svých multimediálních službách, jako je Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) a další konverzační služby. Funguje jako součást profilu Audio-Visual Profile with Feedback ([AVPF](/mobilnisite/slovnik/avpf/)), který rozšiřuje RTCP o včasnější zpětnou vazbu. Paket TMMBN je odesílán přijímačem média (nebo mezilehlým prvkem, jako je Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)), který funguje jako přijímač), aby informoval odesílatele média o dočasné horní hranici datového toku, kterou má použít pro konkrétní mediální proud identifikovaný svým synchronizačním zdrojem ([SSRC](/mobilnisite/slovnik/ssrc/)).

Struktura paketu TMMBN [RTCP](/mobilnisite/slovnik/rtpcp/) zahrnuje hlavičku identifikující jej jako TMMBN (Packet Type=205, FMT=4), následovanou SSRC entity vydávající oznámení („notifying source“) a jedním nebo více bloky TMMBN FCI (Feedback Control Information). Každý blok FCI obsahuje SSRC mediálního zdroje, na který se limit vztahuje, a hodnotu maximálního datového toku (MBR) vyjádřenou v kilobitech za sekundu. Tato hodnota MBR představuje dočasné omezení, často způsobené limity na straně přijímače (např. schopnost dekodéru, vytížení procesoru) nebo vynucené síťovým prvkem řešícím zahlcení. Klíčové je, že TMMBN označuje limit, který oznamující zdroj aktuálně vynucuje nebo je schopen zvládnout, nikoli pouhou návrh.

TMMBN funguje ve spojení s dalšími zpětnými zprávami RTCP, nejvýznamněji s TMMBR (Temporary Maximum Media Stream Bit Rate Request). Typický pracovní postup zahrnuje odeslání TMMBR přijímačem, aby požádal odesílatele o omezení datového toku. Odesílatel, který může přijímat takové požadavky od více přijímačů v relaci, je vyhodnotí a určí nejpřísnější limit. Následně odpoví paketem TMMBN, aby všechny účastníky informoval, jakému limitu se aktuálně přizpůsobuje a která entita (identifikovaná SSRC) je „vlastníkem“ tohoto omezujícího pravidla. Tento mechanismus zabraňuje více přijímačům ve vydávání protichůdných požadavků a zajišťuje, že všechny strany jsou si vědomy aktivního omezení datového toku. V systémech 3GPP jsou TMMBN/TMMBR nezbytné pro dynamickou adaptaci datového toku ve službách, jako je videotelefonie, a umožňují plynulý provoz za měnících se rádiových podmínek, při síťovém zahlcení nebo s ohledem na schopnosti terminálu, jak je podrobně popsáno ve specifikacích jako TS 26.114 (zpracování médií založené na IMS) a TS 29.333 (řízení MRFP).

## K čemu slouží

TMMBN byl vyvinut k řešení výzvy efektivního a koordinovaného řízení datového toku v víceúčastnických relacích multimédií v reálném čase, zejména přes sítě s proměnlivou šířkou pásma a potenciálně přetížené, jako jsou mobilní rádiové přístupové sítě. Před standardizovanými mechanismy zpětné vazby, jako je AVPF, byla adaptace datového toku méně dynamická a často spoléhala na jednodušší, méně informované metody, jako je sledování ztráty paketů, což je reaktivní a často destruktivní signál. Potřeba proaktivního, explicitního řídicího mechanismu se stala kritickou s nástupem videotelefonie a dalších adaptivních mediálních služeb v sítích 3G a pozdějších.

Vytvoření TMMBN společně s TMMBR řeší konkrétní problém více omezení v relaci. V konferenčním hovoru nebo scénáři vysílání mohou mít různí přijímači různé schopnosti (např. smartphone vs. desktop) nebo zažívat různé síťové podmínky. Bez mechanismu oznamování by mohl být odesílatel média zaplaven protichůdnými požadavky TMMBR. TMMBN poskytuje nezbytnou koordinaci: umožňuje odesílateli potvrdit a zveřejnit aktuálně aplikovaný limit a informovat všechny účastníky. Tím se zabrání plýtvavým vyjednávacím smyčkám, sníží se řídicí provoz a vytvoří se společná představa o mediálních omezeních relace. Jeho přijetí ve standardech 3GPP bylo motivováno požadavkem na robustní Quality of Service (QoS) a kvalitu uživatelského zážitku (QoE) ve službách založených na IMS, což zajišťuje, že datové toky médií mohou být dynamicky a efektivně přizpůsobeny nejužšímu místu na koncové cestě, ať už je na straně přijímače, v síti nebo v uzlu zpracování médií.

## Klíčové vlastnosti

- Typ paketu RTCP pro oznámení vynuceného dočasného limitu datového toku
- Funguje v tandemu s paketem TMMBR (Request) pro koordinovanou adaptaci datového toku
- Identifikuje omezující entitu (SSRC) a konkrétní hodnotu maximálního datového toku (MBR)
- Součást profilu AVPF pro včasnou zpětnou vazbu v relacích médií v reálném čase
- Kritický pro dynamickou adaptaci v mobilní videotelefonii a konferencích
- Zabraňuje protichůdným požadavkům na datový tok v víceúčastnických relacích oznámením aktivního omezení

## Související pojmy

- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [TMMBR – Temporary Maximum Media Stream Bit Rate Request](/mobilnisite/slovnik/tmmbr/)
- [AVPF – Audio-Video Profile with Feedback](/mobilnisite/slovnik/avpf/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [TMMBN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmmbn/)
