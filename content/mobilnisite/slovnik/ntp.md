---
slug: "ntp"
url: "/mobilnisite/slovnik/ntp/"
type: "slovnik"
title: "NTP – Network Time Protocol"
date: 2026-01-01
abbr: "NTP"
fullName: "Network Time Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ntp/"
summary: "Široce používaný protokol pro synchronizaci hodin počítačových systémů v paketově přepínaných datových sítích s proměnlivou latencí. V systémech 3GPP poskytuje přesné časové reference pro síťové prvky"
---

NTP je široce používaný protokol pro synchronizaci systémových hodin počítačů v datových sítích, který poskytuje přesné časové reference v systémech 3GPP pro koordinované operace.

## Popis

Network Time Protocol (NTP) je síťový protokol navržený pro synchronizaci systémových hodin síťových zařízení na společný časový referenční zdroj s vysokou přesností, typicky v řádu milisekund ve veřejném internetu a potenciálně mikrosekund v řízených lokálních sítích. V rámci architektury 3GPP není NTP protokolem vynalezeným 3GPP, ale je referencován jako standardní metoda pro distribuci přesné časové synchronizace z důvěryhodného časového zdroje (např. přijímače globálního navigačního satelitního systému jako [GPS](/mobilnisite/slovnik/gps/) nebo atomových hodin) k různým síťovým funkcím. Funguje v hierarchii klient-server (stratový model), kde zařízení strat 0 jsou vysoce přesné hardwarové hodiny, servery strat 1 se synchronizují přímo se strat 0 a servery nižších strat se synchronizují se servery vyšších strat, čímž distribuují čas po síti.

Princip fungování spočívá v tom, že NTP klient periodicky odesílá časově označené dotazovací pakety na jeden nebo více nakonfigurovaných NTP serverů. Server odpovídá svými vlastními časovými značkami. Klient následně pomocí těchto časových značek vypočítá dobu zpátečního přenosu (round-trip delay) a časový posun (clock offset) mezi sebou a serverem. K výběru nejlepších časových vzorků, odmítnutí odlehlých hodnot způsobených síťovým jitterem a postupnému seřízení lokálních hodin (obvykle pomocí fázové smyčky) se používají sofistikované algoritmy, včetně algoritmů pro filtraci hodin, výběr, shlukování a kombinování, aby se minimalizovala časová chyba. NTP podporuje autentizační mechanismy, které brání narušení synchronizace ze strany škodlivých časových zdrojů. V síti 3GPP může prvek jako gNB, [MME](/mobilnisite/slovnik/mme/) nebo [UPF](/mobilnisite/slovnik/upf/) fungovat jako NTP klient, synchronizující se s centrálním NTP serverem operátora, který je sám synchronizován s primárním referenčním časovým zdrojem (PRTC).

Jeho role v síti je klíčová pro mnoho časově citlivých operací. Přesná synchronizace je nezbytná pro rádiový přístupový síť (RAN), kde základnové stanice vyžadují těsně sladěné hodiny pro funkce jako Coordinated Multipoint (CoMP), vylepšená koordinace mezibuněčného rušení (eICIC) a přesné časování rádiových rámců, aby se předešlo rušení, zejména v [TDD](/mobilnisite/slovnik/tdd/) systémech. V jádrové síti je synchronizovaný čas nutný pro korelaci záznamů o účtování ([CDR](/mobilnisite/slovnik/cdr/)) z různých uzlů, časové označování událostí pro zákonný odposlech a zajištění toho, aby logy z distribuovaných síťových funkcí mohly být přesně seřazeny pro řešení problémů a bezpečnostní auditování. Zatímco 3GPP definovala také Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)/[IEEE](/mobilnisite/slovnik/ieee/) 1588) pro přísnější požadavky (např. synchronizaci fronthaulu), NTP zůstává zásadní pro širší správu sítě a operace, kde není vyžadována submikrosekundová přesnost.

## K čemu slouží

NTP existuje, aby řešil základní problém časového driftu (clock drift) v distribuovaných výpočetních systémech. Interní oscilátor každého počítače pracuje s mírně odlišnou rychlostí, což způsobuje, že se hodiny v čem rozcházejí. V malé síti by to mohlo způsobit pouze menší nesrovnalosti v logech, ale ve velkém, geograficky distribuovaném systému, jako je telekomunikační síť, mohou nesynchronizované hodiny vést k závažným provozním selháním. Před protokoly jako NTP sítě spoléhaly na ruční nastavování hodin nebo jednodušší časové protokoly jako TIME nebo DAYTIME, které byly nedostatečné z hlediska přesnosti a škálovatelnosti. Vytvoření NTP bylo motivováno potřebou automatizovaného, robustního a škálovatelného mechanismu pro udržování synchronizovaného času v rostoucím internetu a privátních sítích, schopného kompenzovat proměnlivou síťovou latenci.

V kontextu systémů 3GPP bylo přijetí NTP (a odkazů na něj ve specifikacích) motivováno potřebou standardizované, IP-based metody pro distribuci času, která je nezávislá na konkrétním hardwaru. Zatímco dřívější generace mobilních sítí mohly spoléhat na synchronní backhaul (např. linky E1/T1 přenášející hodinové signály) nebo vestavěné [GPS](/mobilnisite/slovnik/gps/) přijímače na každé základnové stanici, jsou tyto přístupy nákladné nebo nepružné. NTP poskytuje nákladově efektivní, softwarové řešení pro synchronizaci prvků jádrové sítě a v některých případech i prvků RAN, kde není vyžadována ultra vysoká přesnost. Řeší problémy jako korelace událostí pro reakci na bezpečnostní incidenty, přesné účtování napříč distribuovanými síťovými uzly a zajištění konzistentního času pro systémy správy sítě. Jeho zařazení do specifikací 3GPP poskytuje operátorům dobře známou, na dodavateli nezávislou možnost protokolu pro vybudování jejich synchronizační infrastruktury.

## Klíčové vlastnosti

- Architektura klient-server s hierarchickým stratovým modelem pro škálovatelnou distribuci času
- Používá UDP pro efektivní komunikaci dotaz/odpověď, typicky na portu 123
- Implementuje sofistikované algoritmy pro filtraci síťového jitteru a výpočet přesného časového posunu
- Podporuje autentizaci (Autokey nebo symetrický klíč) pro zabezpečení proti škodlivým časovým zdrojům
- Dokáže dosáhnout přesnosti synchronizace v řádu milisekund v rozlehlých sítích
- Zahrnuje mechanismy pro řízení hodin (clock discipline), včetně úpravy frekvence a fáze

## Definující specifikace

- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G

---

📖 **Anglický originál a plná specifikace:** [NTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntp/)
