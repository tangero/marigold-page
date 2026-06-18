---
slug: "ole"
url: "/mobilnisite/slovnik/ole/"
type: "slovnik"
title: "OLE – Originating Local Exchange"
date: 2025-01-01
abbr: "OLE"
fullName: "Originating Local Exchange"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ole/"
summary: "Funkční entita v architektuře 3GPP IMS (IP Multimedia Subsystem), konkrétně v rámci frameworku IMS Centralized Services (ICS). Jedná se o MSC (Mobile Switching Centre) rozšířené pro ICS, které zpracov"
---

OLE je MSC rozšířené pro IMS Centralized Services, které zpracovává okruhově přepínanou část hovoru pro uživatelské zařízení, jehož služby jsou řízeny IMS.

## Popis

Originating Local Exchange (OLE) je síťová funkce definovaná v architektuře 3GPP IMS Centralized Services ([ICS](/mobilnisite/slovnik/ics/)), zavedená k zajištění konzistentního uživatelského zážitku bez ohledu na to, zda je uživatel připojen přes okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) rádiovou přístupovou síť (jako [GERAN](/mobilnisite/slovnik/geran/)/[UTRAN](/mobilnisite/slovnik/utran/)) nebo přes paketově přepínaný ([PS](/mobilnisite/slovnik/ps/)) přístup jako LTE. OLE je v podstatě Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo MSC Server, které bylo rozšířeno o schopnosti ICS. Jeho primární role je zpracovat CS přístupovou část pro uživatelské zařízení (UE), které chce využívat služby založené na IMS (jako hlas, video, doplňkové služby), zatímco je připojeno k síti 2G nebo 3G. Když UE zahájí hovor, OLE zachytí CS proceduru sestavení hovoru. Namísto poskytování služeb lokálně z CS domény OLE naváže přenosovou cestu k IMS síti a přepošle signalizaci řízení hovoru (pomocí [SIP](/mobilnisite/slovnik/sip/) přes rozhraní Iq) do IMS jádra uživatele, konkrétně k [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving Call Session Control Function). OLE funguje jako SIP User Agent zastupující UE pro CS přístupovou část, převádějící mezi CS signalizací (např. ISUP, BICC) a SIP. To umožňuje IMS jádru, které obsahuje profil služeb uživatele, plně řídit hovor – aplikovat služby jako překlad čísel, přesměrování hovoru a multimediální funkce. OLE spravuje mediální přenosovou cestu, propojuje CS rádiovou přenosovou cestu s IP přenosovou cestou (např. přes rozhraní Mb), která vede do IMS mediální cesty. Spolupracuje s Terminating Local Exchange (TLE) na straně volaného účastníka. Mezi klíčové protokoly patří SIP (mezi OLE a IMS), ISUP/BICC (pro propojení) a RTP/RTCP pro přenos médií po převodu na IP.

## K čemu slouží

OLE bylo vytvořeno k řešení problému fragmentace služeb během přechodu z okruhově přepínaných sítí na plně IP sítě IMS. Před ICS by uživatel v síti 2G/3G CS dostával služby ze starší CS sítě (MSC/HLR), které byly často odlišné a méně bohaté než služby dostupné v IMS. To vytvářelo nekonzistentní uživatelský zážitek. ICS a OLE jako klíčová komponenta byly motivovány snahou 'centralizovat' řízení služeb v IMS jádře bez ohledu na typ přístupu. Řeší omezení spočívající v duplicitní servisní logice v CS i PS doménách, čímž zjednodušuje síťovou architekturu a nasazení služeb pro operátory. OLE umožňuje operátorům nasadit služby založené na IMS (jako VoLTE/RCS) a zpřístupnit je i účastníkům ve starších CS sítích, čímž chrání investice a zajišťuje plynulou migrační cestu. Řeší konkrétní problém udržení pokročilých doplňkových služeb (jako čekání, přidržení, přesměrování hovoru) konzistentně, když se uživatel pohybuje mezi pokrytím LTE (VoIP) a 2G/3G (okruhově přepínaný hlas).

## Klíčové vlastnosti

- Funguje jako pro ICS rozšířené MSC/MSC Server zpracovávající CS část hovoru na straně volajícího
- Zprostředkovává interworking mezi CS signalizací (ISUP/BICC) a IMS SIP signalizací
- Navazuje mediální přenosovou cestu mezi CS sítí a IMS IP sítí
- Funguje jako SIP User Agent reprezentující UE připojené přes CS vůči IMS jádru
- Umožňuje řízení služeb z IMS (ze S-CSCF) pro hovory pocházející z CS přístupu
- Součást architektury IMS Centralized Services (ICS) pro konzistenci služeb

## Související pojmy

- [ICS – Implementation Conformance Statement](/mobilnisite/slovnik/ics/)
- [TLE – Two Line Elements](/mobilnisite/slovnik/tle/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)

## Definující specifikace

- **TS 29.013** (Rel-19) — MAP-SSAP Interworking for CCBS Service

---

📖 **Anglický originál a plná specifikace:** [OLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ole/)
