---
slug: "ses"
url: "/mobilnisite/slovnik/ses/"
type: "slovnik"
title: "SES – Speech Enabled Services"
date: 2025-01-01
abbr: "SES"
fullName: "Speech Enabled Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ses/"
summary: "Speech Enabled Services (SES) představují soubor funkcí standardizovaných organizací 3GPP, které zlepšují hlasovou a řečovou komunikaci v mobilních sítích. Zahrnuje služby jako Voice over LTE (VoLTE),"
---

SES je soubor funkcí standardizovaných organizací 3GPP, včetně VoLTE a VoNR, které zlepšují hlasovou a řečovou komunikaci v mobilních sítích prostřednictvím vysoce kvalitních, interoperabilních služeb.

## Popis

Speech Enabled Services (SES) je v rámci 3GPP široký termín odkazující na standardizaci paketově přepínaných hlasových a řečových služeb, primárně pro LTE (jako VoLTE) a 5G NR (jako VoNR). Definuje koncové architektury, protokoly a kodeky potřebné pro poskytnutí hlasu přes IP (VoIP) na úrovni operátora v sítích založených na IMS. Jádrem SES je IP Multimedia Subsystem (IMS), který poskytuje řídicí rovinu pro zřizování a správu relací a vyvolávání funkcí (jako čekání hovoru a doplňkové služby). Uživatelská rovina přenáší vlastní hlasové pakety pomocí protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)).

Klíčovou technickou součástí SES je soubor standardizovaných pokročilých řečových a audio kodeků. To zahrnuje kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), představený ve verzi 3GPP 12, který poskytuje kvalitu superširokopásmového a plnopásmového zvuku a je vysoce odolný vůči ztrátě paketů. Specifikace SES pokrývají celý hlasový řetězec: od řečového kodéru/dekodéru terminálu, přes přístupové rádiové sítě a přenosové kanály v jádře sítě s příslušnou kvalitou služeb (QoS) – typicky vyhrazený QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) pro garantovaný přenosový výkon – až po IMS jádro a propojení s jinými sítěmi (jako [PSTN](/mobilnisite/slovnik/pstn/) přes [MGCF](/mobilnisite/slovnik/mgcf/)).

SES také definuje kritické procedury pro kontinuitu služeb, jako je Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)), která umožňuje předání hlasového hovoru z paketově přepínané sítě (LTE/5G) do starší okruhově přepínané sítě (2G/3G), když uživatel opustí pokrytí. Pro 5G SES zajišťuje, že hlasová služba je nativně podporována v 5G Core (5GC) prostřednictvím Voice over NR (VoNR) za využití stejného IMS jádra. Specifikace detailně popisují interakci mezi UE, RAN, 5GC (konkrétně [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/)) a IMS za účelem zřízení IMS hlasového přenosového kanálu s příslušnými QoS toky. SES není jednou službou, ale rámcem zajišťujícím, že řečové služby splňují přísné požadavky na zpoždění, chvění, spolehlivost a kvalitu zvuku ve zcela IP sítích.

## K čemu slouží

SES byl vyvinut k vyřešení základní výzvy poskytování tradičních, vysoce kvalitních hlasových služeb podobných okruhově přepínaným přes nové, zcela paketově přepínané architektury mobilních sítí jako LTE a 5G NR. Raná nasazení LTE byla pouze datová, což vyžadovalo pro hlas návrat k okruhově přepínaným 3G sítím (CSFB), což byla podřadná uživatelská zkušenost. Účelem SES, jehož průkopníkem bylo VoLTE, bylo definovat standardizované, interoperabilní a kvalitnější řešení hlasu přes IP, které by se mohlo stát primární hlasovou službou.

Řešil omezení over-the-top (OTT) VoIP služeb zajištěním těsné integrace s mobilní sítí. Tato integrace poskytuje klíčové výhody kontrolované operátorem: garantovanou QoS s prioritou v rádiové a přenosové síti, bezproblémovou mobilitu a předávání hovorů (včetně přechodu na okruhově přepínané sítě), integraci s operátorskými doplňkovými službami (jako přesměrování hovoru) a podporu služeb tísňového volání (např. reportování polohy pro E911). Dále si SES kladl za cíl zlepšit kvalitu hlasu oproti starším úzkopásmovým hovorům povinnou podporou širokopásmového (HD Voice) a později superširokopásmového/plnopásmového zvuku prostřednictvím kodeku EVS.

Vývoj směrem k 5G vyžadoval pokračování tohoto rámce. Účel se rozšířil o zajištění, že hlasová služba je nedílnou, nikoliv dodatečně přidanou součástí 5G. VoNR v rámci SES zajišťuje, že 5G sítě mohou poskytovat ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro hlas, podporují nové schopnosti 5G jádra jako síťové segmentování pro vyhrazený hlasový segment a zachovávají zpětnou kompatibilitu a kontinuitu služeb s 4G VoLTE a 3G okruhově přepínanými sítěmi. SES tedy poskytuje plán dlouhodobého vývoje telefonie v mobilních sítích.

## Klíčové vlastnosti

- Standardizace hlasu přes LTE (VoLTE) a přes NR (VoNR) založeného na IMS
- Specifikace superširokopásmového kodeku Enhanced Voice Services (EVS)
- Komplexní správa QoS s vyhrazenými přenosovými kanály (QCI 1 pro hlas)
- Mechanismy kontinuity služeb jako SRVCC a PS-PS předání
- Podpora služeb rich communication services (RCS) a doplňkových služeb
- Podpora služeb tísňového volání (např. IMS Emergency) v paketových sítích

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)

## Definující specifikace

- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.235** (Rel-12) — Default Codecs for 3GPP IP Multimedia Subsystem
- **TS 26.236** (Rel-12) — Packet Switched Conversational Multimedia Protocols
- **TR 26.943** (Rel-19) — SES Codec Selection Report

---

📖 **Anglický originál a plná specifikace:** [SES na 3GPP Explorer](https://3gpp-explorer.com/glossary/ses/)
