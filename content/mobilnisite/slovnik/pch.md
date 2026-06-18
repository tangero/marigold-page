---
slug: "pch"
url: "/mobilnisite/slovnik/pch/"
type: "slovnik"
title: "PCH – Paging Channel"
date: 2025-01-01
abbr: "PCH"
fullName: "Paging Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pch/"
summary: "Přenosový kanál v downlinku používaný k zasílání stránkovacích zpráv a oznámení o změně systémových informací k uživatelským zařízením (UE) v režimu idle nebo inactive. Upozorňuje UE na příchozí hovor"
---

PCH je přenosový kanál v downlinku, který slouží k přenosu stránkovacích zpráv a oznámení o změně systémových informací k uživatelským zařízením (UE) v režimu idle nebo inactive.

## Popis

Stránkovací kanál ([PCH](/mobilnisite/slovnik/pch-text-pch/)) je klíčový přenosový kanál v downlinku používaný v UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a NR (NG-RAN) k oslovení uživatelského zařízení (UE), které není ve stavu aktivního spojení (tj. je v [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE). Jeho hlavní funkcí je doručovat stránkovací zprávy, které slouží k upozornění konkrétního UE nebo skupiny UE na různé události. Tyto události typicky zahrnují příchozí hovor nebo datovou relaci určenou pro mobilní zařízení, potřebu znovu navázat signalizační spojení nebo oznámení o změnách systémových informací (ETWS, [CMAS](/mobilnisite/slovnik/cmas/)).

Z architektonického hlediska je PCH mapován na odpovídající fyzický kanál: Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) v UMTS, Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) v LTE a PDSCH v NR. Stránkovací zprávy nejsou vysílány nepřetržitě. Místo toho jsou přenášeny v konkrétních, předem definovaných časových intervalech určených konceptem stránkovacího rámce ([PF](/mobilnisite/slovnik/pf/)) a stránkovací příležitosti (PO). UE vypočítává svůj konkrétní PF a PO na základě svého jedinečného identifikátoru (jako je IMSI) a parametrů vysílaných v systémových informacích (např. defaultPagingCycle). To umožňuje UE zapnout svůj přijímač pouze během svých určených stránkovacích příležitostí, čímž implementuje přerušovaný příjem (DRX) a výrazně šetří výdrž baterie.

Stránkovací proces je iniciován jádrem sítě. U hovorů určených pro mobilní zařízení přijme funkce pro správu přístupu a mobility (AMF) v 5GC nebo entita pro správu mobility (MME) v EPS požadavek a odešle stránkovací zprávu příslušným základnovým stanicím (gNB nebo eNB) obsluhujícím registrační oblast sledování (tracking area) daného UE. RAN následně naplánuje stránkovací zprávu na PCH ve vypočtené stránkovací příležitosti pro toto UE. Samotná zpráva obsahuje stránkovací identitu UE (5G-S-TMSI, S-TMSI nebo IMSI). Po úspěšném dekódování stránkovací zprávy obsahující její identitu UE zahájí proceduru náhodného přístupu (RACH), aby přešlo do připojeného stavu a odpovědělo síti.

Kromě individuálního stránkování podporuje PCH také skupinové stránkování pro oznámení o změnách systémových informací a veřejné varovné zprávy. V tomto případě je použita vyhrazená stránkovací identita (jako P-RNTI v LTE/NR), která upozorní všechna UE sledující danou stránkovací příležitost, aby si přečetla aktualizovaný blok systémových informací. Koncepce PCH s přerušovaným příjmem (DRX) a mapováním na sdílené fyzické kanály představuje základní kompromis optimalizovaný pro efektivitu sítě a úsporu energie UE, což je klíčové pro mobilní širokopásmové připojení a aplikace hromadného internetu věcí (IoT).

## K čemu slouží

Stránkovací kanál byl vytvořen, aby vyřešil základní problém, jak může síť zahájit komunikaci s mobilním zařízením, které aktivně nevysílá. V raných buněčných systémech by jednoduchý přístup vyžadoval, aby UE neustále naslouchala hovorům, což by bylo nepřijatelně náročné na výdrž baterie. PCH spolu s mechanismem DRX poskytuje elegantní řešení, které umožňuje UE po většinu času spát a probouzet se pouze v konkrétních, předvídatelných intervalech, aby zkontrolovala stránkování.

Tento mechanismus je nezbytný pro zajištění neustálé konektivity z pohledu služeb při zachování několikaleté výdrže baterie některých zařízení IoT. Odděluje dosažitelnost UE od nepřetržité rádiové aktivity. Historický vývoj od stránkování v GSM přes UMTS, LTE až po NR přinesl vylepšení v efektivitě a flexibilitě. Například zavedení více DRX cyklů a mapování PCH na vysoce efektivní sdílený kanál (PDSCH) v LTE/NR, na rozdíl od vyhrazeného fyzického kanálu, zlepšilo spektrální efektivitu a umožnilo pokročilejší strategie stránkování.

Dále PCH podporuje škálovatelnost sítě a správu mobility. Organizací stránkování do oblastí sledování/směrování (tracking/routing areas) může síť stránkovat UE napříč více buňkami bez znalosti jeho přesné polohy, čímž snižuje signalizační režii spojenou s aktualizací polohy. Schopnost stránkovat skupiny UE kvůli systémovým aktualizacím je také klíčová pro provoz sítě a nouzové výstrahy. Stručně řečeno, PCH je základním kamenem architektury mobilních sítí, který umožňuje efektivní, šetrný k baterii a škálovatelný kontakt iniciovaný sítí, což je předpoklad pro prakticky všechny mobilní služby.

## Klíčové vlastnosti

- Doručuje stránkovací zprávy k uživatelským zařízením (UE) ve stavu RRC_IDLE nebo RRC_INACTIVE.
- Umožňuje síti iniciovat navázání signalizačního spojení.
- Využívá přerušovaný příjem (DRX) pro úsporu energie uživatelského zařízení (UE).
- UE sleduje konkrétní stránkovací rámce (PF) a stránkovací příležitosti (PO) vypočítané z jeho identity.
- Podporuje individuální stránkování (pomocí S-TMSI) a skupinové stránkování (pomocí P-RNTI).
- Je mapován na sdílené fyzické kanály (S-CCPCH v UMTS, PDSCH v LTE/NR) pro vyšší efektivitu.

## Související pojmy

- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [S-TMSI – SAE Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/s-tmsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pch/)
