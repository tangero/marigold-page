---
slug: "tmmbr"
url: "/mobilnisite/slovnik/tmmbr/"
type: "slovnik"
title: "TMMBR – Temporary Maximum Media Stream Bit Rate Request"
date: 2025-01-01
abbr: "TMMBR"
fullName: "Temporary Maximum Media Stream Bit Rate Request"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tmmbr/"
summary: "Zpětná vazba protokolu RTCP (Real-Time Transport Control Protocol) používaná v multimediálních relacích k dynamickému požádání protistrany o omezení její maximální vysílací přenosové rychlosti pro kon"
---

TMMBR je zpětná vazba RTCP sloužící k požádání protistrany, aby dočasně omezila svou maximální vysílací přenosovou rychlost pro konkrétní mediální proud, což umožňuje řízení zahlcení v reálných službách, jako je VoIP.

## Popis

TMMBR (Temporary Maximum Media Stream Bit Rate Request) je specifická zpětná vazba definovaná v rámci protokolu [RTCP](/mobilnisite/slovnik/rtcp/) ([RTP](/mobilnisite/slovnik/rtp/) Control Protocol), standardizovaná [IETF](/mobilnisite/slovnik/ietf/) a přijatá 3GPP pro služby IMS (IP Multimedia Subsystem) a [PSS](/mobilnisite/slovnik/pss/) (Packet-Switched Streaming). Funguje jako součást profilu [AVPF](/mobilnisite/slovnik/avpf/) (Audio-Visual Profile with Feedback), který rozšiřuje RTCP o včasnější zpětnou vazbu. Základní mechanismus spočívá v tom, že přijímač analyzuje příchozí mediální proud, detekuje síťové zahlcení nebo omezení vlastních výpočetních kapacit a vygeneruje paket TMMBR. Tento paket je odeslán zdroji (odesílateli média) a obsahuje dva klíčové údaje: jedinečný identifikátor mediálního proudu ([SSRC](/mobilnisite/slovnik/ssrc/)) a požadovaný limit maximální přenosové rychlosti vyjádřený v kilobitech za sekundu.

Po přijetí TMMBR by měl odesílatel upravit své kódovací parametry nebo tvarování provozu tak, aby jeho vysílací přenosová rychlost nepřekročila požadovaný limit. Toto přizpůsobení je 'dočasné', což znamená, že limit lze aktualizovat následnými zprávami TMMBR při změně síťových podmínek. Protokol zahrnuje pravidla pro zpracování více požadavků TMMBR od různých přijímačů pro stejný proud, typicky vyžadující, aby se odesílatel řídil nejrestriktivnějším (nejnižším) limitem přenosové rychlosti mezi aktivními požadavky. Tím je zajištěno, že mediální tok nepřetíží nejvíce omezeného účastníka relace.

Z architektonického hlediska je TMMBR implementován v koncových bodech mediální roviny (např. uživatelské zařízení, mediální servery) a je přenášen přes [UDP](/mobilnisite/slovnik/udp/) spolu s mediálními proudy RTP. Jeho role je nedílnou součástí správy kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) v reálných službách, spolupracuje s dalšími zpětnými vazbami RTCP, jako je TMMBN (Temporary Maximum Media Stream Bit Rate Notification) pro potvrzení limitů a REMB (Receiver Estimated Maximum Bitrate). Poskytuje přímý mechanismus řízení na úrovni relace, který doplňuje protokoly transportní vrstvy, jako je řízení zahlcení v TCP, které není pro média v reálném čase vhodné kvůli zpožděním při opětovném přenosu.

## K čemu slouží

TMMBR byl vytvořen, aby řešil kritickou potřebu dynamické adaptace přenosové rychlosti v multimediální komunikaci v reálném čase přes paketové sítě, které jsou ze své podstaty proměnlivé z hlediska dostupné šířky pásma a latence. Před zavedením takových mechanismů zpětné vazby aplikace často používaly statické přenosové rychlosti nebo jednoduché testování, což mohlo při zhoršení síťových podmínek vést k přetrvávajícímu zahlcení, ztrátě paketů a zhoršené kvalitě zvuku/videa. 'Dočasná' a na požadavku založená povaha TMMBR poskytuje jemnější, přijímačem řízenou kontrolu ve srovnání s odhadem pouze na straně odesílatele nebo samotným označováním kvality služeb (QoS) na síťové vrstvě.

Jeho vývoj byl motivován růstem služeb IMS a mobilního videa ve 3GPP Release 8, kde se efektivní využití rozhraní rádiového přístupu a zdrojů jádra sítě stalo prvořadým. TMMBR umožňuje přijímacímu koncovému bodu, který může být na přetíženém okraji buňky nebo mít omezený výpočetní výkon, proaktivně signalizovat svá omezení vzdálenému odesílateli. Tím řeší problém, kdy mediální zdroj nevědomky vysílá rychlostí, kterou přijímač nebo mezilehlá síťová cesta nedokáže udržet, čímž předchází přetečením vyrovnávací paměti, snižuje chvění a minimalizuje zahazování paketů. Umožňuje plynulejší snížení kvality média při zahlcení.

## Klíčové vlastnosti

- Požadavek na omezení přenosové rychlosti iniciovaný přijímačem pro konkrétní mediální proud RTP
- K přenosu využívá protokol RTCP pro včasné doručení v rámci mediální relace
- Nese specifický identifikátor SSRC a požadovanou hodnotu maximální přenosové rychlosti
- Podporuje dynamické aktualizace při změně síťových podmínek
- Obsahuje mechanismy pro řešení konfliktních požadavků od více přijímačů
- Spolupracuje s TMMBN pro oznámení a potvrzení odesílatelem

## Související pojmy

- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [AVPF – Audio-Video Profile with Feedback](/mobilnisite/slovnik/avpf/)
- [TMMBN – Temporary Maximum Media Stream Bit Rate Notification](/mobilnisite/slovnik/tmmbn/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

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

📖 **Anglický originál a plná specifikace:** [TMMBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmmbr/)
