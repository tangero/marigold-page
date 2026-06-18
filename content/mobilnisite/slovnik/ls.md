---
slug: "ls"
url: "/mobilnisite/slovnik/ls/"
type: "slovnik"
title: "LS – Local Source"
date: 2025-01-01
abbr: "LS"
fullName: "Local Source"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ls/"
summary: "Termín z protokolu pro řízení mediálních bran H.248/Megaco označující logickou entitu v rámci Media Gateway, která reprezentuje zdroj média (např. zvuku, videa) pocházející lokálně z dané brány. Použí"
---

LS je logická entita v rámci mediální brány (Media Gateway), která reprezentuje zdroj média, například zvuku nebo videa, pocházejícího lokálně z této brány.

## Popis

V rámci architektury 3GPP, zejména ve specifikacích týkajících se funkce řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)) a IP Multimedia Subsystem (IMS), je termín "Local Source" (LS) převzat z konvence pojmenování protokolu [ITU-T](/mobilnisite/slovnik/itu-t/) H.248 (Megaco). H.248 je protokol typu master-slave, který používá řadič mediálních bran ([MGC](/mobilnisite/slovnik/mgc/)), například MGCF, k ovládání zdrojů a zpracování médií v rámci mediální brány ([MGW](/mobilnisite/slovnik/mgw/)). Protokol modeluje mediální bránu jako obsahující sadu ukončení (Terminations) a kontextů (Contexts). Ukončení reprezentují fyzické nebo logické koncové body, které jsou zdrojem nebo cílem mediálních proudů (např. [TDM](/mobilnisite/slovnik/tdm/) timeslot nebo [RTP](/mobilnisite/slovnik/rtp/) port), zatímco kontexty jsou asociace, které mixují, přepínají nebo spojují více ukončení.

"Local Source" je specifická role přiřazená ukončení v rámci kontextu. V typickém kontextu se dvěma ukončeními reprezentujícím hovor typu point-to-point je jedno ukončení označeno jako Local Source (LS) a druhé jako Remote Source ([RS](/mobilnisite/slovnik/rs/)). Ukončení typu Local Source je entita fyzicky umístěná uvnitř řízené mediální brány a je zdrojem mediálního proudu *z pohledu této konkrétní MGW*. Například, pokud MGW převádí TDM okruh ze strany [PSTN](/mobilnisite/slovnik/pstn/) na RTP proud na IP straně, TDM ukončení by bylo nakonfigurováno jako Local Source pro médium proudící z PSTN do brány a RTP ukončení by bylo Remote Source pro tento stejný směr toku média.

Toto rozlišení je zásadní pro řadič mediální brány (MGC), aby mohl správně zadávat operace zpracování média, jako je potlačení ozvěny, transkódování nebo paketizace. Příkazy odesílané přes H.248, jako je Modify, mohou obsahovat deskriptory (např. LocalControl, LocalDescriptor), které obsahují parametry specifické pro ukončení typu Local Source, jako je použitý kodek, perioda paketizace a odesílací IP adresa/port pro RTP proud. Model LS/RS umožňuje MGC jednoznačně definovat topologii a tok média v rámci kontextu, což umožňuje přesnou kontrolu nad složitými scénáři zahrnujícími více mediálních proudů, konferenční hovory nebo hlášení. Ve specifikacích 3GPP, jako je TS 29.230 a TS 29.238, které definují profily H.248 pro IMS a propojení s PSTN/CS, je použití Local Source specifikováno za účelem zajištění interoperabilního řízení mediálních bran napříč zařízeními různých výrobců.

## K čemu slouží

Koncept Local Source (a jeho protějšku, Remote Source) byl v protokolu H.248 zaveden k vyřešení problému jednoznačné kontroly mediálního proudu v dekomponované architektuře brány. Tradiční monolitické ústředny interně zvládaly přepínání a zpracování média. S nástupem architektur softswitch a IMS došlo k oddělení řídicí roviny (MGC/MGCF) od mediální roviny (MGW). To si vyžádalo standardizovaný protokol, H.248, pomocí kterého může řadič instruovat bránu, jak má média zpracovávat. Klíčovou výzvou bylo, aby řadič dokázal popsat obousměrné toky médií a požadavky na jejich zpracování bez znalosti vnitřního fyzického mapování brány.

Terminologie LS/RS poskytuje tento nezbytný referenční rámec. Definováním "lokální" perspektivy (samotná MGW) a "vzdálené" perspektivy (entita na druhé straně mediálního proudu) se příkazy protokolu stávají relativními a přenositelnými. Stejná logická sekvence příkazů může být použita MGC k řízení různých typů MGW (např. jedné s rozhraním DS1 a jiné s rozhraním E1), protože pracuje s abstraktními rolemi LS a RS, nikoli s absolutními fyzickými porty. Tato abstrakce je klíčová pro interoperabilitu mezi více výrobci a pro zjednodušení řídicí logiky v MGC.

V kontextu adopce protokolu H.248 pro řízení IMS mediálních bran v 3GPP bylo specifikování použití Local Source motivováno potřebou přesné kontroly v interworkingových scénářích. Když MGCF sestavuje hovor mezi PSTN a IMS, musí v MGW vytvořit kontexty, které propojí TDM a IP ukončení. Použití označení LS umožňuje MGCF správně nakonfigurovat, které ukončení poskytuje příchozí médium k paketizaci (LS na straně TDM) a které ukončení poskytuje příchozí pakety k převodu na TDM (LS na straně IP). Toto zajišťuje správný tok média, podporuje pokročilé funkce jako vkládání tónů a převod zákona a tvoří základ spolehlivého hlasového a video propojení mezi okruhově přepínanou a paketově přepínanou doménou.

## Klíčové vlastnosti

- Logická role pro ukončení (Termination) v rámci kontextu H.248, označující zdroj média lokální vůči mediální bráně (Media Gateway)
- Poskytuje referenční rámec pro zadávání příkazů pro kontrolu média (např. Modify, Add)
- Používá se společně s deskriptory (LocalDescriptor) k nastavení odesílacích parametrů, jako je kodek a RTP adresa
- Zásadní pro definici směru toku média a topologie v kontextu
- Umožňuje abstraktní, nezávislé na výrobci řízení zpracování média řadičem mediální brány (Media Gateway Controller)
- Kritické pro interworkingové scénáře mezi sítěmi TDM/PSTN a IP/IMS

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 29.230** (Rel-19) — 3GPP Diameter Protocol Codes Specification
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface

---

📖 **Anglický originál a plná specifikace:** [LS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ls/)
