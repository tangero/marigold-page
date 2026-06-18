---
slug: "rd"
url: "/mobilnisite/slovnik/rd/"
type: "slovnik"
title: "RD – Remote Descriptor"
date: 2025-01-01
abbr: "RD"
fullName: "Remote Descriptor"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rd/"
summary: "Protokolový prvek v řídicím protokolu H.248 (Megaco) pro mediální brány, který slouží k popisu vzdálených síťových entit nebo koncových bodů. Umožňuje mediálním bránám a řadičům vyměňovat si informace"
---

RD je protokolový prvek v řídicím protokolu H.248 pro mediální brány, který slouží k popisu vzdálených síťových entit a umožňuje výměnu informací o možnostech vzdáleného konce pro správu relací.

## Popis

Remote Descriptor (RD, deskriptor vzdáleného konce) je datová struktura definovaná v protokolu H.248 (známém také jako Megaco), která se používá pro řízení mediálních bran v telekomunikačních sítích. V architektuře H.248 používá Media Gateway Controller ([MGC](/mobilnisite/slovnik/mgc/)) tento protokol k vydávání příkazů Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pro zřizování, změnu a ukončování mediálních toků. RD je specifický typ deskriptoru, který přenáší informace o vzdáleném koncovém bodě nebo entitě účastnící se mediální relace. Typicky obsahuje parametry jako IP adresy, čísla portů, typy kodeků a atributy Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)), které charakterizují vzdálený konec spojení.

Operačně, když MGC nařídí MGW vytvořit kontext a přidat terminace (logické koncové body pro mediální toky), může zahrnout Remote Descriptory pro specifikaci vlastností partnerské terminace na vzdálené straně. Například ve VoIP hovoru může RD popisovat detaily [RTP](/mobilnisite/slovnik/rtp/) proudu vzdálené strany. Deskriptor je přenášen v rámci příkazů H.248 jako Add, Modify nebo Move, což umožňuje dynamické aktualizace při vývoji relací. Klíčové součásti RD zahrnují pole pro síťovou adresaci (např. IPv4 nebo IPv6), transportní protokol (např. RTP/[UDP](/mobilnisite/slovnik/udp/)), kódování média (např. [AMR](/mobilnisite/slovnik/amr/), G.711) a parametry související s QoS, jako je šířka pásma. MGW tyto informace používá k odpovídající konfiguraci svých funkcí pro zpracování médií, čímž zajišťuje kompatibilitu se vzdáleným koncovým bodem.

RD hraje klíčovou roli při umožnění interoperability mezi různými síťovými segmenty, například mezi okruhově přepínanou a paketově přepínanou doménou. Umožňuje MGC abstrahovat detaily relace bez nutnosti plného povědomí o médiu, delegováním médii specifických konfigurací na MGW. Ve specifikacích 3GPP je RD odkazováno v kontextu IP Multimedia Subsystem (IMS) a řízení mediálních bran, zejména ve specifikacích jako 29.334 (H.248 profil pro IMS). Podporuje pokročilé funkce jako redundance, zabezpečení (např. prostřednictvím parametrů šifrování) a scénáře s více připojeními. Poskytnutím standardizovaného způsobu popisu vzdálených entit RD usnadňuje efektivní mediální vyjednávání a snižuje signalizační režii v komplexních multimediálních relacích.

## K čemu slouží

Remote Descriptor byl zaveden, aby řešil potřebu flexibilního a standardizovaného řízení mediálních bran v rozvíjejících se telekomunikačních sítích, zejména s nástupem VoIP a multimediálních služeb. Před H.248 a deskriptory jako RD se řízení mediálních bran často opíralo o proprietární nebo méně škálovatelné protokoly, což bránilo interoperabilitě mezi různými dodavateli. RD poskytuje strukturovaný způsob, jak může řadič informovat bránu o parametrech vzdálené relace, což umožňuje dynamickou adaptaci na měnící se síťové podmínky a možnosti koncových bodů.

Řeší to problémy související se zřizováním relací napříč heterogenními sítěmi, jako je integrace starší [PSTN](/mobilnisite/slovnik/pstn/) s IP-based IMS. Umožňuje efektivní alokaci zdrojů a vyjednávání kodeků bez nutnosti, aby se [MGC](/mobilnisite/slovnik/mgc/) zabýval nízkourovňovými detaily médií. Motivace vycházela z přijetí protokolu H.248 pro řízení mediálních bran v 3GPP od Release 6 a dále, což podporuje nasazení IMS a zajišťuje konzistentní zpracování médií v různých provozních prostředích.

## Klíčové vlastnosti

- Zapouzdřuje parametry vzdáleného koncového bodu (IP, port, kodek) v H.248 zprávách
- Podporuje dynamickou změnu relace prostřednictvím příkazů MGC
- Umožňuje interoperabilitu mezi různorodými mediálními branami a řadiči
- Usnadňuje výměnu parametrů QoS a zabezpečení pro mediální toky
- Integruje se s SDP pro sladění popisu relace
- Umožňuje konfiguraci redundance a převzetí služeb při selhání pro spolehlivost

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [RD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rd/)
