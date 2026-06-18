---
slug: "ce"
url: "/mobilnisite/slovnik/ce/"
type: "slovnik"
title: "CE – Congestion Experienced"
date: 2025-01-01
abbr: "CE"
fullName: "Congestion Experienced"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ce/"
summary: "Congestion Experienced (CE) je signalizační mechanismus v sítích 3GPP, který oznamuje koncovým bodům přetížení sítě. Umožňuje explicitní oznámení o přetížení (ECN) pro IP provoz, což transportním prot"
---

CE je signalizační mechanismus v sítích 3GPP, který oznamuje koncovým bodům přetížení sítě. Umožňuje explicitní oznámení o přetížení (ECN) pro IP provoz za účelem zvýšení účinnosti a snížení latence.

## Popis

Congestion Experienced (CE) je kódový bod uvnitř pole Explicit Congestion Notification ([ECN](/mobilnisite/slovnik/ecn/)) hlavičky IP, standardizovaný v [RFC](/mobilnisite/slovnik/rfc/) 3168 a přijatý specifikacemi 3GPP. V sítích 3GPP funguje CE jako klíčový mechanismus kvality služeb (QoS), který poskytuje včasné varování před přetížením sítě bez nutnosti zahazovat pakety. Když síťové prvky (jako směrovače, brány nebo rádiové uzly) detekují hrozící přetížení na základě délky fronty nebo vytížení vyrovnávací paměti, označí pole ECN v hlavičkách IP paketů kódovým bodem CE místo toho, aby pakety zahazovaly. Toto označení putuje koncově-koncově a informuje jak odesílatele, tak příjemce, že na trase dochází k přetížení.

Mechanismus CE funguje prostřednictvím koordinované interakce mezi síťovými prvky a transportními protokoly koncových hostitelů. Síťové prvky schopné ECN (ECN-Capable Transport, neboli [ECT](/mobilnisite/slovnik/ect/)) monitorují své fronty a podle nastavených prahů aplikují označení CE, typicky za použití algoritmů aktivní správy front (AQM), jako je Random Early Detection (RED). Když paket označený CE dorazí k příjemci, příjemce toto oznámení o přetížení odešle zpět odesílateli pomocí potvrzení na transportní vrstvě (např. TCP ECN-Echo). Po přijetí této zpětné vazby odesílatel sníží svou přenosovou rychlost pomocí algoritmů pro řízení přetížení, čímž zmírní přetížení dříve, než povede ke ztrátě paketů.

V rámci architektury 3GPP může být označení CE aplikováno na více místech: v rádiové přístupové síti (RAN) na eNodeB/gNB při přetížení vzdušného rozhraní, v jádru sítě na branách ([PGW](/mobilnisite/slovnik/pgw/)/[UPF](/mobilnisite/slovnik/upf/)) při přetížení přenosové části a jádra sítě a na vzájemných propojeních mezi operátory. Specifikace 3GPP definují, jak CE interaguje s řízením QoS Flow, službami přenosu a řízením politik. Mechanismus je obzvláště cenný v mobilních sítích, kde jsou rádiové podmínky proměnlivé a přetížení může nastat rychle. Použitím CE namísto zahazování paketů si sítě udržují vyšší propustnost a nižší latenci pro služby v reálném čase, jako je VoIP nebo streamování videa.

Mezi klíčové technické komponenty patří 2bitové pole ECN v hlavičce IP (s hodnotami 00 pro Non-ECT, 01/10 pro ECT a 11 pro CE), transportní protokoly podporující ECN (TCP, [SCTP](/mobilnisite/slovnik/sctp/), [QUIC](/mobilnisite/slovnik/quic/)) a implementace AQM v síťovém vybavení. 3GPP zajišťuje interoperabilitu specifikací zpracování CE napříč rozhraními (S1, N3, N6 atd.) a v protokolových vrstvách ([PDCP](/mobilnisite/slovnik/pdcp/), GTP-U, IP). Účinnost CE závisí na správné konfiguraci prahů pro označování a rozšířené podpoře ECN jak v síťové infrastruktuře, tak v koncových zařízeních.

## K čemu slouží

CE byl vytvořen, aby řešil zásadní problém přetížení sítě v paketově přepínaných sítích, kde tradiční řízení přetížení spoléhá na ztrátu paketů jako na signál přetížení. Tento reaktivní přístup způsobuje výrazné zhoršení výkonu: ztráta paketů spouští retransmise, zvyšuje latenci a snižuje propustnost, což zvláště škodí aplikacím citlivým na zpoždění. V mobilních sítích, kde je přenosová kapacita vzácná a dynamicky sdílená, jsou tyto efekty zesíleny. CE poskytuje explicitní, proaktivní signalizační mechanismus, který umožňuje koncovým bodům snížit přenosovou rychlost dříve, než přetížení povede ke ztrátě paketů, čímž zlepšuje celkovou účinnost sítě a uživatelský zážitek.

Motivace pro CE v rámci 3GPP vychází z potřeby podporovat rozmanité služby s přísnými požadavky na QoS, zejména jak se sítě vyvíjely směrem k plně IP architekturám ve 3G a později. Před ECN/CE řízení přetížení často zahrnovalo fronty s pravidlem zahazování z konce (tail-drop), což vedlo k nafouknutí vyrovnávacích pamětí (bufferbloat), problémům se synchronizací a nespravedlivému rozdělení mezi toky. CE umožňuje jemnější řízení přetížení, snižuje latenci a kolísání zpoždění (jitter), které sužují komunikace v reálném čase, a umožňuje sítím pracovat s vyšším vytížením bez ztráty výkonu. Je v souladu se zaměřením 3GPP na koncově-koncovou QoS napříč heterogenními přístupovými technologiemi.

Historicky integrace CE do norem 3GPP řešila omezení dřívějších metod řízení přetížení, které byly nedostatečné pro případy užití LTE a 5G s nízkou latencí a vysokou spolehlivostí. Přijetím standardu ECN od IETF poskytlo 3GPP standardizovaný způsob, jak se mohou mobilní sítě účastnit celosvětového řízení přetížení na Internetu. To je zvláště kritické pro umožnění efektivní přenosové služby pro aplikace jako VoLTE, streamování videa a IoT aplikace, kde je předvídatelný výkon zásadní. CE řeší problém tichého přetížení – kdy jsou pakety nadměrně zpožďovány ve vyrovnávacích pamětech, aniž by byly zahazovány – tím, že poskytuje explicitní signál, který spouští včasné reakce pro předcházení přetížení.

## Klíčové vlastnosti

- Explicitní signalizace přetížení prostřednictvím pole ECN v hlavičce IP
- Proaktivní předcházení přetížení ještě před ztrátou paketů
- Snížení latence a kolísání zpoždění (jitter) pro služby v reálném čase
- Kompatibilita s algoritmy aktivní správy front (AQM)
- Koncově-koncová funkčnost napříč sítěmi 3GPP i non-3GPP
- Podpora v mnoha transportních protokolech (TCP, SCTP, QUIC)

## Definující specifikace

- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TS 28.880** (Rel-19) — Study on 5G Energy Efficiency & Saving
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1

---

📖 **Anglický originál a plná specifikace:** [CE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ce/)
