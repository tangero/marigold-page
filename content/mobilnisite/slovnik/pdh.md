---
slug: "pdh"
url: "/mobilnisite/slovnik/pdh/"
type: "slovnik"
title: "PDH – Plesiochronous Digital Hierarchy"
date: 2025-01-01
abbr: "PDH"
fullName: "Plesiochronous Digital Hierarchy"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdh/"
summary: "Zastaralá digitální přenosová technologie používaná v telekomunikačních sítích k multiplexování více digitálních kanálů nižší přenosové rychlosti (jako E1/T1) do synchronních datových toků vyšší rychl"
---

PDH je zastaralá digitální přenosová technologie, která multiplexuje kanály nižší přenosové rychlosti do synchronních toků vyšší rychlosti pro páteřní a přístupové sítě. Předcházela technologii SDH/SONET.

## Popis

Plesiochronní digitální hierarchie (PDH) je digitální přenosový systém pro multiplexování více signálů přítokových větví do jediného toku s vyšším datovým tokem pro přenos přes telekomunikační sítě. Termín ‚plesiochronní‘ znamená ‚téměř synchronní‘ a označuje, že jednotlivé vstupní toky jsou nominálně stejné rychlosti, ale mohou mít mírné časové odchylky (v rámci stanovené tolerance). Systém funguje pomocí bitového prokládání přítokových větví. Každý signál přítokové větve (např. tok E1 o rychlosti 2,048 Mbps) má vlastní zdroj hodin. Na multiplexoru se přidávají vyrovnávací (nebo plnící) bity pro kompenzaci malých frekvenčních rozdílů mezi hodinami přítokových větví a interním systémovým hodinovým signálem multiplexoru. Tyto vyrovnávací bity umožňují multiplexoru dočasně zvýšit datový tok pomalejší přítokové větve, aby odpovídal systémovému časování.

Hierarchie PDH je v různých částech světa definována odlišně. Základními úrovněmi jsou: 2,048 Mbps (E1, 32 kanálů po 64 kbps) v Evropě a většině světa a 1,544 Mbps (T1, 24 kanálů po 64 kbps) v Severní Americe a Japonsku. Ty jsou multiplexovány do vyšších úrovní: například čtyři toky E1 jsou multiplexovány do E2 o rychlosti 8,448 Mbps, čtyři toky E2 do E3 o rychlosti 34,368 Mbps a čtyři toky E3 do E4 o rychlosti 139,264 Mbps. Podobná, ale odlišná hierarchie existuje pro T-spany. Multiplexování je na každém stupni synchronní, ale mezi stupni plesiochronní. To znamená, že pro extrakci jediného kanálu nízké rychlosti z toku vysoké rychlosti musí být celý signál demultiplexován krok za krokem zpět na požadovanou úroveň – proces známý jako ‚back-to-back [multiplexing](/mobilnisite/slovnik/multiplexing/)‘.

Ve specifikacích 3GPP je PDH zmíněna primárně v kontextu zastaralých transportních rozhraní pro síťové elementy, zejména v raných verzích pro připojení Node B k řadičům rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo základnových stanic ([BTS](/mobilnisite/slovnik/bts/)) k řadičům základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v GSM. Specifikace jako TS 25.411 (uživatelské rovinné protokoly rozhraní [UTRAN](/mobilnisite/slovnik/utran/) Iu) a TS 29.332 (Media Gateway Control Protocol) zahrnují podporu pro fyzickou vrstvu PDH s rámováním (např. E1, T1). Její role v 3GPP spočívá v podpoře jako transportní technologie pro zastaralá síťová nasazení a propojení, přičemž novější sítě převážně používají transport založený na Ethernetu a IP.

## K čemu slouží

PDH byla vyvinuta pro řešení potřeby efektivního digitálního přenosu a multiplexování ve veřejné telefonní síti ([PSTN](/mobilnisite/slovnik/pstn/)) během 70. a 80. let 20. století. Před PDH se používaly analogové nosné systémy, které byly náchylné k šumu a přeslechu. Přechod na digitální přenos (pulzně kódová modulace – [PCM](/mobilnisite/slovnik/pcm/)) pro hlas vyžadoval metodu pro kombinování více hlasových kanálů o rychlosti 64 kbps pro dálkový přenos přes koaxiální kabel nebo mikrovlnné rádiové spoje.

Účelem PDH bylo vytvořit standardizovanou hierarchii pro agregaci těchto digitálních toků. Řešila praktický problém synchronizace hodin v rozsáhlé síti, kde každá centrála měla vlastní hodiny. ‚Plesiochronní‘ přístup s vyrovnáváním byl pragmatickým řešením, které se vyhnulo nákladům a složitosti vyžadování dokonale synchronního síťového hodinového zdroje. To umožnilo rozsáhlé nasazení digitálních trankových spojů, což dramaticky zlepšilo kvalitu hlasu a umožnilo první digitální datové služby. PDH však měla omezení: složité přidávání/oddělování kanálů (add/drop [multiplexing](/mobilnisite/slovnik/multiplexing/)), omezené možnosti správy a nedostatek standardizace mezi regiony. Tato omezení motivovala vývoj plně synchronních standardů SONET/SDH, které PDH nakonec nahradily v páteřní síťové dopravě, ačkoli PDH zůstává v některých přístupových a zastaralých síťových segmentech stále používána.

## Klíčové vlastnosti

- Multiplexuje více digitálních signálů s nižším datovým tokem do jediného toku s vyšším datovým tokem
- Používá vyrovnávání (bit-stuffing) pro zvládnutí mírných časových rozdílů mezi vstupními signály
- Definuje hierarchické úrovně (např. E1, E2, E3, E4 v Evropě; T1, T2, T3 v Severní Americe)
- Podporuje digitální přenos přes měděné vedení, koaxiální kabel, mikrovlnné spoje a raná optická vlákna
- Vyžaduje postupný demultiplexing krok za krokem pro přístup k jednotlivým kanálům nízké rychlosti uvnitř toku vysoké rychlosti
- Poskytuje základní digitální transportní vrstvu pro zastaralé telekomunikační sítě

## Související pojmy

- [SDH – Synchronous Digital Hierarchy](/mobilnisite/slovnik/sdh/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [PDH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdh/)
