---
slug: "mpls"
url: "/mobilnisite/slovnik/mpls/"
type: "slovnik"
title: "MPLS – Multiprotocol Label Switching Architecture"
date: 2025-01-01
abbr: "MPLS"
fullName: "Multiprotocol Label Switching Architecture"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mpls/"
summary: "Vysoce výkonná technologie přeposílání paketů, která směruje data z jednoho síťového uzlu do dalšího na základě krátkých cestových štítků namísto dlouhých síťových adres. V rámci 3GPP se používá jako"
---

MPLS je vysoce výkonná technologie přeposílání paketů, která směruje data na základě krátkých cestových štítků a používá se v páteřní síti jádra sítě 3GPP k zajištění efektivního, provozně inženýrovaného propojení mezi síťovými prvky.

## Popis

Multiprotocol Label Switching (MPLS) je technika přenosu dat, která funguje mezi tradiční vrstvou [OSI](/mobilnisite/slovnik/osi/) 2 (spojová) a vrstvou 3 (síťová), často označovaná jako vrstva 2,5. V rámci architektury 3GPP se nejedná o protokol vynalezený 3GPP, ale je referencován a využíván jako preferovaná transportní technologie pro IP-based jádro sítě, známé jako Evolved Packet Core (EPC) v LTE a 5G Core (5GC). MPLS funguje tak, že při vstupu paketů do sítě jim přiřadí krátké štítky pevné délky. Tyto štítky se používají pro rozhodování o přeposílání, nahrazují složité IP vyhledávání podle nejdelší shody prefixu jednoduchým přepínáním založeným na štítcích. Síť MPLS se skládá z Label Edge Routerů (LER) na hranici a Label Switch Routerů ([LSR](/mobilnisite/slovnik/lsr/)) v jádře. LER klasifikují příchozí IP pakety, přiřadí vhodný MPLS štítek na základě Forwarding Equivalence Class ([FEC](/mobilnisite/slovnik/fec/)) a vloží štítek do paketu, čímž vytvoří MPLS hlavičku. Jádrové LSR poté nahradí příchozí štítek odchozím štítkem na základě své Label Forwarding Information Base (LFIB) a přepošlou paket podél Label Switched Path ([LSP](/mobilnisite/slovnik/lsp/)).

Klíčové komponenty MPLS v kontextu 3GPP zahrnují samotné LSP, což jsou jednosměrné cesty sítí. Tyto cesty mohou být zřízeny pomocí signalizačních protokolů, jako je Label Distribution Protocol ([LDP](/mobilnisite/slovnik/ldp/)) nebo Resource Reservation Protocol s rozšířeními pro Traffic Engineering (RSVP-TE). Traffic Engineering (MPLS-TE) je klíčovým aspektem, který umožňuje síťovým operátorům explicitně směrovat provoz po specifických cestách, aby se předešlo zahlcení, splnily se požadavky QoS a zajistila se odolnost pomocí mechanismů Fast Reroute (FRR). V jádru 3GPP se tunely MPLS používají k přenosu tunelů [GTP-U](/mobilnisite/slovnik/gtp-u/) (uživatelský provoz) a signalizace [GTP-C](/mobilnisite/slovnik/gtp-c/) mezi síťovými funkcemi přes páteřní síť. Například rozhraní S5/S8 mezi Serving Gateway (SGW) a Packet Data Network Gateway (PGW) nebo rozhraní N9 mezi [UPF](/mobilnisite/slovnik/upf/) v 5G mohou být transportovány přes MPLS LSP.

Jeho role spočívá v poskytnutí škálovatelné, spolehlivé a efektivní transportní vrstvy pro IP provoz mobilního jádra. Použitím štítků MPLS odděluje rozhodování o přeposílání od podkladové technologie spojové vrstvy (Ethernet, PPP atd.) a konečné IP destinace, což umožňuje jednotnou transportní rovinu. To umožňuje vytváření virtuálních privátních sítí (Layer 3 VPNs nebo L3VPNs) pro bezpečné oddělení provozu od různých operátorů nebo služeb. Pro 3GPP to znamená, že stejná fyzická páteř může přenášet provoz pro více mobilních operátorů nebo síťových řezů s přísnou izolací. Schopnosti Traffic Engineeringu MPLS jsou klíčové pro zajištění, že provoz citlivý na latenci (hlas, hry v reálném čase) dostane přednost před best-effort daty, což přímo podporuje diferencované požadavky QoS definované 3GPP.

## K čemu slouží

MPLS byl přijat do architektonických úvah 3GPP, aby řešil omezení tradičního IP směrování pro budování přenosových sítí mobilního backhaulu a jader sítě na úrovni operátora. Jak se mobilní sítě vyvíjely od přepojování okruhů k all-IP architekturám s 3GPP Release 5 a dále, potřeba robustní, škálovatelné a řiditelné transportní technologie se stala prvořadou. Tradiční IP směrování, ač flexibilní, trpí nepředvídatelnými cestami, omezeným Traffic Engineeringem a pomalejšími časy konvergence, což je nepřijatelné pro hlasové služby v reálném čase a kritické mobilní služby.

Historická motivace byla využít osvědčenou, vysoce výkonnou transportní technologii již široce nasazenou v páteřních sítích pevných ISP. MPLS řeší několik klíčových problémů: Za prvé poskytuje rychlejší přeposílání paketů prostřednictvím jednoduchého přepínání štítků, čímž zlepšuje výkon sítě. Za druhé, a to nejdůležitější, zavádí sofistikovaný Traffic Engineering (TE), který umožňuje operátorům kontrolovat přesnou cestu toků provozu pro optimalizaci využití zdrojů a zaručení šířky pásma a latence pro specifické služby – což je přímý enabler pro QoS třídy 3GPP. Za třetí zlepšuje odolnost sítě mechanismy jako MPLS Fast Reroute, který dokáže obnovit konektivitu za méně než 50 ms při výpadku spoje, což je klíčové pro udržení kontinuity hovoru. Nakonec MPLS VPN poskytují přirozený způsob implementace konceptu síťových řezů i na transportní vrstvě a nabízejí bezpečnou multi-tenanci. Referencováním MPLS ve specifikacích jako 23.207 (QoS architektura) a 23.802 (architektonická vylepšení pro end-to-end QoS) poskytlo 3GPP plán pro integraci této výkonné transportní technologie, aby splnilo přísné požadavky na spolehlivost, kvalitu a škálovatelnost moderních mobilních sítí.

## Klíčové vlastnosti

- Přeposílání založené na štítcích pro vysokorychlostní přepínání paketů nezávislé na podkladové spojové vrstvě
- Explicitní Traffic Engineering (MPLS-TE) pro optimální výběr cesty a rezervaci zdrojů
- Fast Reroute (FRR) pro obnovení při výpadku spoje nebo uzlu za méně než 50 ms
- Podpora Layer 3 VPNs (L3VPN) pro vytváření izolovaných virtuálních sítí nad sdílenou infrastrukturou
- Oddělení řídicí roviny (IP směrovací protokoly, LDP, RSVP-TE) a datové roviny (přepínání štítků)
- Schopnost transportovat více protokolů (IPv4, IPv6, Ethernet) přes jednotnou páteř MPLS

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [MPLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpls/)
