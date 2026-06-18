---
slug: "voip"
url: "/mobilnisite/slovnik/voip/"
type: "slovnik"
title: "VOIP – Voice over IP"
date: 2025-01-01
abbr: "VOIP"
fullName: "Voice over IP"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/voip/"
summary: "Voice over IP (VoIP) je technologie umožňující hlasovou komunikaci a multimediální relace přes sítě Internetového protokolu (IP), jako je internet nebo privátní datové sítě. V 3GPP odkazuje na standar"
---

VOIP je technologie standardizovaná 3GPP pro poskytování hlasové komunikace a multimediálních relací na úrovni veřejné sítě (carrier-grade) přes paketově přepínané IP sítě, jako jsou ty používané pro VoLTE a VoNR.

## Popis

Voice over IP (VoIP) v rámci standardů 3GPP je standardizovaná metodologie pro přenos hlasové komunikace jako datových paketů přes sítě založené na IP, konkrétně přes Evolved Packet Core (EPC) a 5G Core (5GC). Představuje zásadní posun od tradiční okruhově přepínané telefonie (jako hlas 2G/3G [CS](/mobilnisite/slovnik/cs/)) k plně IP, paketově přepínané architektuře. Technologie využívá IP Multimedia Subsystem (IMS) jako základní platformu pro poskytování služeb. IMS poskytuje nezbytné řídicí funkce pro zřizování, správu a ukončování relací pomocí protokolů jako je [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol). Samotná hlasová data jsou kódována pomocí kodeků jako [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate) nebo [EVS](/mobilnisite/slovnik/evs/) (Enhanced Voice Services), zabalena do proudů Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) a přenášena přes podkladovou IP přenosovou síť.

Z architektonického hlediska zahrnuje poskytování služby VoIP několik klíčových síťových funkcí. Uživatelské zařízení (UE) musí podporovat funkcionalitu IMS klienta. Signalizace hovoru prochází přes [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function), [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-CSCF) a další uzly IMS pro směrování a aplikační logiku. Mediální zdroje, pokud jsou potřeba pro konferenční hovory nebo překódování, jsou zpracovávány funkcí Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)). Jádrová síť (EPC/5GC) poskytuje garantované přenosové kanály s podporou QoS (Quality of Service), typicky vyhrazené EPS kanály nebo QoS toky s příslušnými QoS Class Identifiers (QCIs/5QIs) pro konverzační hlas v reálném čase, což zajišťuje nízké zpoždění a ztrátovost paketů.

Provoz VoIP je úzce integrován s řízením politik. Funkce Policy and Charging Rules Function (PCRF) v EPC nebo Policy Control Function (PCF) v 5GC komunikuje s IMS přes rozhraní Rx. Při zahájení relace IMS informuje správce politik o požadovaných parametrech média (kodek, šířka pásma, porty). Správce politik následně zřídí odpovídající pravidla v Packet Gateway (PGW) nebo User Plane Function (UPF) pro vytvoření vyhrazeného přenosového kanálu se správným profilem QoS, což zajišťuje, že hlasové pakety dostanou prioritu v rádiové a přenosové síti. Toto komplexní řízení QoS je klíčové pro dosažení kvality hlasu na úrovni veřejné sítě, která odpovídá nebo překonává kvalitu starších okruhově přepínaných sítí.

## K čemu slouží

VoIP bylo zavedeno, aby řešilo omezení a neefektivitu okruhově přepínaných (CS) hlasových sítí v éře širokopásmových dat. Tradiční hlas CS vyhradil celý 64 kbps časový slot na dobu trvání hovoru, což bylo neefektivní z hlediska zdrojů a nešlo to snadno integrovat s nově vznikajícími službami založenými na IP. Primární motivací byla konvergence sítí – vytvoření jedné, jednotné IP infrastruktury schopné poskytovat všechny služby (hlas, video, data), čímž se zjednodušuje síťová architektura, snižují provozní náklady a umožňuje bezproblémová integrace služeb.

Historicky se sítě 2G (GSM) a 3G (UMTS) spoléhaly na samostatnou okruhově přepínanou jádrovou síť pro hlas. S rozvojem vysokorychlostního paketového přístupu (HSPA) a přechodem k LTE (čistě paketově přepínané rádiové technologii) bylo nutné nové řešení pro hlas. VoIP přes IMS (komerčně označované jako VoLTE) bylo standardizováno, aby poskytlo perspektivní, vysoce kvalitní hlasovou službu nativní pro paketovou síť. Vyřešilo problém 'hlasové mezery' v LTE a umožnilo pokročilé funkce jako simultánní hlas a vysokorychlostní data (SVLTE bylo dočasné řešení, nikoli trvalé), HD hlas a integraci služeb rich communication services (RCS).

Standardizace VoIP dále zajistila interoperabilitu mezi různými operátory a výrobci zařízení a zabránila fragmentaci. Stanovila jasnou evoluční cestu od hlasu CS k IP hlasu, která byla plně realizována v 5G jako Voice over New Radio (VoNR), kde je VoIP jediným nativním hlasovým řešením. Tento přechod podporuje zjednodušení sítě, protože starší CS jádro může být vyřazeno, a umožňuje zacházet s hlasem jako s další datovou aplikací, byť s přísnými požadavky na QoS, v rámci plně softwarově definované a cloud-nativní jádrové sítě.

## Klíčové vlastnosti

- Paketově přepínaný přenos hlasu pomocí protokolů RTP/UDP/IP
- Závislost na IMS pro řízení relací a poskytování služeb
- Povinná podpora komplexního zřizování QoS prostřednictvím řízení politik (PCRF/PCF)
- Využití efektivních hlasových kodeků (např. AMR, AMR-WB, EVS) pro vysokou kvalitu a adaptaci šířky pásma
- Podpora tísňových hovorů (eT911/eT112) a zákonného odposlechu přes IP
- Umožnění inovací služeb jako HD hlas, videohovory a Rich Communication Services (RCS)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [VOIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/voip/)
