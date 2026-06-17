---
slug: "ifp"
url: "/mobilnisite/slovnik/ifp/"
type: "slovnik"
title: "IFP – Internet Facsimile Protocol"
date: 2025-01-01
abbr: "IFP"
fullName: "Internet Facsimile Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifp/"
summary: "Adaptace protokolu definovaná 3GPP pro přenos faxu skupiny 3 (G3F) přes IP sítě v rámci IP Multimedia Subsystem (IMS). Umožňuje kompatibilitu starších faxových přístrojů s moderními plně IP sítěmi zap"
---

IFP je adaptace protokolu 3GPP pro přenos faxů skupiny 3 přes IP sítě v rámci IMS, která umožňuje kompatibilitu se staršími faxovými systémy zapouzdřením signalizace T.30 a dat T.4/T.6 v paketech RTP.

## Popis

Internet Facsimile Protocol (IFP) je protokol specifikovaný 3GPP, který umožňuje přenos tradičních faxových služeb skupiny 3 (G3F) přes paketově orientované sítě, konkrétně v rámci architektury IP Multimedia Subsystem (IMS). Funguje jako bránový protokol, který překládá mezi starším analogovým/digitálním faxovým světem a světem plně IP. IFP nedefinuje novou faxovou kompresi ani signalizační metodu; místo toho zapouzdřuje stávající procedurální signalizaci [ITU-T](/mobilnisite/slovnik/itu-t/) T.30 a protokoly pro obrazová data T.4/T.6 v rámci paketů Real-time Transport Protocol (RTP) pro přenos přes IP síť.

Z architektonického hlediska je IFP implementován ve funkčních entitách nazývaných Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo konkrétněji v Interworking Functions (IWFs), které jsou součástí Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo samostatných bran. Když je faxové volání uskutečněno ze staršího faxového přístroje ve veřejné telefonní síti (PSTN) nebo v síti [ISDN](/mobilnisite/slovnik/isdn/) k uživateli IMS (nebo naopak), je volání směrováno přes Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a Media Gateway (MGW). MGW obsahuje adaptační funkci IFP. Tato funkce ukončuje signalizaci T.30 z okruhově přepínané strany, interpretuje faxový handshake (např. [CNG](/mobilnisite/slovnik/cng/), CED, DIS/[DCS](/mobilnisite/slovnik/dcs/)) a převádí obrazová data T.4/T.6 na paketový proud.

Protokol pracuje ve dvou hlavních fázích: fázi procedury T.30 a fázi obrazových dat. Během fáze procedury T.30 nejsou klíčové signály jako Called Station Identification (CED), Digital Identification Signal (DIS) a Digital Command Signal (DCS) přenášeny jako zvukové tóny přes hlasovou cestu. Místo toho jsou extrahovány bránou, reprezentovány jako pakety IFP (konkrétně pakety T.30-indicator) a odeslány přes IP přenosovou vrstvu. Tato 'demodulace' zabraňuje zkreslení těchto signálů hlasovými kodeky. Během fáze obrazových dat jsou naskenovaná obrazová data, modulovaná pomocí V.27ter, V.29 nebo V.17, bránou demodulována. Poté jsou surová komprimovaná obrazová data (např. Modified Huffman, Modified READ) zabalena do RTP datových jednotek podle formátu IFP (pakety T.4/T.6 data) a odeslána přes IP. Příjemní brána provádí reverzní proces, moduluje data zpět pro cílový faxový přístroj. Tento proces od konce ke konci zajišťuje spolehlivý a efektivní přenos faxu přes IP sítě.

## K čemu slouží

IFP byl vyvinut k řešení kritického problému vzájemného propojení během přechodu z okruhově přepínaných telefonních sítí (PSTN/[ISDN](/mobilnisite/slovnik/isdn/)) na paketově přepínané, plně IP sítě jako je IMS. Tradiční fax (G3F) je vysoce citlivý na latenci, zkreslení času a ztrátu paketů a spoléhá na přesnou signalizaci v pásmu zvukových frekvencí (T.30) a modulovaná obrazová data. Standardní hlasové kodeky (jako AMR, G.711) používané ve VoLTE nebo VoIP tyto modemové signály výrazně zkreslují, což znemožňuje přenos faxu přes běžný VoIP. Rané pokusy o 'fax přes IP' používající G.711 pass-through (bez komprese) byly neefektivní z hlediska šířky pásma a stále náchylné k selháním kvůli problémům v síti.

Vytvoření IFP bylo motivováno potřebou podpory všudypřítomné a právně významné obchodní služby – faxu – v rámci nové architektury 3GPP IMS. Řešilo omezení předchozích přístupů přesunutím složitého zpracování modemových signálů mimo hlasovou cestu do síťových bran. Demodulací signálů na okraji IP sítě a jejich přenosem jako strukturovaných datových paketů činí IFP přenos faxu odolným vůči zkreslení kodekem a obecným problémům IP sítí. Umožňuje operátorům vyřadit starší okruhově přepínané sítě při zachování zpětné kompatibility pro miliony faxových přístrojů, čímž plní regulatorní a komerční požadavky na pokračující podporu faxových služeb v éře plně IP.

## Klíčové vlastnosti

- Zapouzdření faxové signalizace ITU-T T.30 v rámci paketů RTP jako paketů T.30-indicator
- Přenos demodulovaných komprimovaných obrazových dat T.4/T.6 v rámci RTP jako paketů T.4/T.6 data
- Podpora všech standardních modemových rychlostí faxu skupiny 3 (V.27ter, V.29, V.17)
- Umožňuje spolehlivý fax přes IP (FoIP) prostřednictvím IMS, nezávisle na hlasových kodecích
- Definované postupy vzájemného propojení mezi faxovými terminály PSTN/ISDN a IMS klienty
- Využívá standardní IMS řízení volání (SIP) pro navázání relace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [IFP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifp/)
