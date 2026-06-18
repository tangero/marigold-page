---
slug: "sip-i"
url: "/mobilnisite/slovnik/sip-i/"
type: "slovnik"
title: "SIP-I – Session Initiation Protocol with encapsulated ISDN User Part"
date: 2025-01-01
abbr: "SIP-I"
fullName: "Session Initiation Protocol with encapsulated ISDN User Part"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sip-i/"
summary: "SIP-I je protokol pro interoperabilitu mezi SIP-IP sítěmi a tradičními telefonními sítěmi ISDN/SS7. Zapouzdřuje zprávy ISUP uvnitř SIP, čímž umožňuje bezproblémové signalizace volání a transparentnost"
---

SIP-I je protokol, který zapouzdřuje zprávy ISUP uvnitř protokolu SIP, aby umožnil bezproblémovou interoperabilitu a transparentnost služeb mezi SIP-IP sítěmi a tradičními telefonními sítěmi ISDN/SS7.

## Popis

SIP-I je klíčový interoperabilní protokol definovaný 3GPP a [ITU-T](/mobilnisite/slovnik/itu-t/) (jako Q.1912.5), který usnadňuje komunikaci mezi sítěmi nové generace ([NGN](/mobilnisite/slovnik/ngn/)) založenými na protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a starší veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)), která používá signalizační protokol [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)). Jeho primární funkcí je zajistit, aby signalizace řízení hovoru a doplňkové služby mohly být převedeny a přeneseny mezi těmito odlišnými síťovými doménami bez ztráty funkčnosti. Protokol toho dosahuje zapouzdřením celých zpráv ISUP včetně jejich parametrů a informačních prvků do těla zpráv SIP, obvykle s použitím [MIME](/mobilnisite/slovnik/mime/) typu `application/isup`. Toto zapouzdření zachovává plný sémantický obsah signalizace ISUP a umožňuje transparentní poskytování služeb od konce ke konci.

Z architektonického hlediska funguje SIP-I na signalizační hranici mezi sítěmi, například v řadiči mediální brány ([MGC](/mobilnisite/slovnik/mgc/)) nebo v řadiči hraniční relace (SBC), který propojuje síť IP Multimedia Subsystem (IMS) se starším okruhově přepínaným jádrem. Když hovor pochází z PSTN a je určen pro uživatele IMS, signalizační bod zdrojové sítě odešle zprávu ISUP Initial Address Message (IAM). Interoperabilní funkce tuto zprávu ISUP přijme, namapuje klíčové informace pro sestavení hovoru (jako číslo volaného/volajícího) do odpovídajících hlavičkových polí SIP (jako To a From) a poté vloží původní binárně kódovanou zprávu ISUP do těla požadavku SIP INVITE. Tento SIP INVITE je pak směrován přes IP síť. Příjemní interoperabilní funkce na druhé straně IP sítě extrahuje zapouzdřenou zprávu ISUP a použije ji ke generování odpovídající signalizace ISUP směrem k cílové větvi PSTN, čímž zajišťuje transparentnost služeb.

Návrh protokolu zahrnuje specifická pravidla pro mapování parametrů ISUP na hlavičky SIP, stejně jako postupy pro zpracování následných zpráv řízení hovoru, jako je Answer (ANM), Release (REL) a různá volání doplňkových služeb. Podporuje jak režim „zapouzdření“, kdy je přenášena celá zpráva ISUP, tak režim „překladu“, kdy se použijí pouze sémanticky ekvivalentní informace SIP, ačkoli zapouzdření je pro maximální kompatibilitu upřednostňováno. Role SIP-I je zásadní pro síťové operátory přecházející na plně IP jádra jako IMS, protože jim umožňuje zachovat stávající služby PSTN/ISDN a mezifiremní dohody při modernizaci své infrastruktury. Zajišťuje, že složité telefonní funkce, jako je identifikace volajícího, přesměrování hovoru nebo služby uzavřené skupiny uživatelů, fungují bezproblémově v hybridním síťovém prostředí.

## K čemu slouží

SIP-I byl vytvořen k řešení kritického problému interoperability mezi vznikajícím paketovým IP Multimedia Subsystem (IMS) a rozsáhlou, zavedenou infrastrukturou starší okruhově přepínané PSTN. Když operátoři začali kolem poloviny roku 2000 nasazovat IMS pro poskytování hlasových a multimediálních služeb přes IP, čelili bezprostřední výzvě propojení těchto nových IP sítí s existující globální telefonní sítí. Jednoduchý překlad protokolů byl nedostatečný, protože ISUP nese bohaté, složité signalizační informace pro řízení hovoru a doplňkové služby, které rané, základní mapování SIP na ISUP nedokázalo plně zachovat, což vedlo ke zhoršení služeb nebo selhání mezisíťových hovorů.

Historický kontext představuje dlouhý, postupný přechod od sítí založených na TDM k plně IP sítím. Předchozí přístupy, jako jednoduchá konverze protokolů SIP na ISUP, často vedly ke ztrátě informačních prvků nad rámec základního hovoru, čímž narušily pokročilé telefonní služby. To vytvořilo hlavní překážku pro přijetí IMS. Vznik SIP-I byl motivován potřebou robustní, standardizované metody, která by garantovala transparentnost služeb, a zajistila tak, že hovor pocházející z PSTN a končící v IMS (nebo naopak) bude mít přístup ke stejné sadě služeb jako hovor, který zůstal zcela v rámci jedné síťové domény. Jeho vytvoření bylo řízeno jak 3GPP, tak ITU-T, aby poskytlo jednotnou, spolehlivou specifikaci, kterou by mohli implementovat výrobci zařízení a síťoví operátoři, a zajistili tak globální interoperabilitu během mnohaleté migrační cesty od starší signalizace SS7 k signalizaci založené na IP.

## Klíčové vlastnosti

- Úplné zapouzdření binárních zpráv ISUP v tělech zpráv SIP (MIME typ application/isup)
- Podpora transparentního přenosu signalizačních informací ISUP pro řízení hovoru a doplňkové služby od konce ke konci
- Definovaná pravidla pro mapování parametrů ISUP (např. kategorie volající strany) na hlavičková pole a parametry SIP
- Postupy pro zpracování sestavení hovoru, odpovědi, uvolnění a chybových scénářů přes hranici interoperability
- Kompatibilita se sítěmi 3GPP IMS i architekturami ITU-T NGN
- Umožňuje transparentnost služeb pro funkce jako přenosnost čísel, identifikace volajícího nebo přesměrování hovoru v hybridních sítích

## Související pojmy

- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [NGN – Next Generation Networks](/mobilnisite/slovnik/ngn/)

## Definující specifikace

- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 48.103** (Rel-19) — A Interface User Plane Transport Protocols

---

📖 **Anglický originál a plná specifikace:** [SIP-I na 3GPP Explorer](https://3gpp-explorer.com/glossary/sip-i/)
