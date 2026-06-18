---
slug: "smil"
url: "/mobilnisite/slovnik/smil/"
type: "slovnik"
title: "SMIL – Synchronized Multimedia Integration Language"
date: 2025-01-01
abbr: "SMIL"
fullName: "Synchronized Multimedia Integration Language"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smil/"
summary: "Značkovací jazyk založený na XML pro vytváření interaktivních multimediálních prezentací, které integrují audio, video, text a grafiku s přesným načasováním a synchronizací. V 3GPP se používá k defini"
---

SMIL je značkovací jazyk založený na XML používaný v 3GPP pro definici multimediálních zpráv a streamovaných prezentací, který umožňuje přesně načasované a synchronizované přehrávání audia, videa, textu a grafiky na mobilních zařízeních.

## Popis

Synchronized Multimedia Integration Language (SMIL) je standard konsorcia World Wide Web Consortium ([W3C](/mobilnisite/slovnik/w3c/)), který poskytuje [XML](/mobilnisite/slovnik/xml/) framework pro tvorbu interaktivních multimediálních prezentací. Umožňuje tvůrcům obsahu kombinovat různé multimediální prvky – jako jsou audio klipy, video streamy, text a obrázky – do jediné synchronizované prezentace. SMIL definuje model založený na časové ose, kde má každý multimediální objekt určený čas začátku a konce, dobu trvání a prostorovou pozici na displeji. To umožňuje přesnou kontrolu nad tím, kdy a kde se multimediální položky objeví, a vytváří tak souvislé zážitky, jako jsou prezentace s audio komentářem, animovaná grafika s video překryvy nebo interaktivní výukové moduly. Jazyk používá značky a atributy k popisu časového chování, rozvržení a propojení médií, což jej činí nezávislým na platformě a snadno parsovatelným přehrávači nebo prohlížeči podporujícím SMIL.

V 3GPP je SMIL přijat primárně pro služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) a streamovací aplikace v mobilních sítích. Pro MMS slouží SMIL jako prezentační vrstva, která definuje, jak jsou multimediální zprávy strukturovány a zobrazovány na přijímacích zařízeních. Typická MMS zpráva obsahuje SMIL dokument, který specifikuje sekvenci multimediálních objektů (např. obrázek následovaný textem a poté audiem) spolu s časovými informacemi a instrukcemi pro rozvržení. To zajišťuje konzistentní zobrazení zprávy na různých typech telefonů a zlepšuje uživatelský zážitek. Specifikace 3GPP, jako je 23.140 pro MMS a 26.234 pro paketově přepínanou streamovací službu, podrobně popisují použití profilů SMIL přizpůsobených pro mobilní prostředí s ohledem na omezení jako velikost obrazovky, šířku pásma a výpočetní výkon. Tyto profily definují podmnožiny funkcí SMIL pro zajištění interoperability a efektivního doručování přes bezdrátové sítě.

Architektura služeb založených na SMIL v 3GPP zahrnuje několik komponent. Tvůrci obsahu používají nástroje pro tvorbu SMIL k vytváření prezentací, které jsou následně zabaleny spolu s multimediálními soubory do jedné entity (např. MMS zprávy nebo streamovacího playlistu). Na straně sítě tyto balíčky doručují do mobilních zařízení centra služby multimediálních zpráv (MMSC) nebo streamovací servery. Klientské zařízení obsahuje přehrávač SMIL – často integrovaný do aplikace pro zasílání zpráv nebo multimediální aplikace – který interpretuje SMIL dokument, načte odkazované multimediální soubory a vykreslí prezentaci podle specifikovaného načasování a rozvržení. Mezi klíčové aspekty patří podpora adaptivního streamování, kde SMIL může popisovat alternativní zdroje médií pro různé podmínky šířky pásma, a integrace s formáty souborů 3GPP jako je [3GP](/mobilnisite/slovnik/3gp/). Role SMIL se rozšiřuje na služby rich communication services ([RCS](/mobilnisite/slovnik/rcs/)) a další multimediální aplikace, poskytuje standardizovaný způsob vytváření poutavého obsahu, který využívá možnosti mobilních sítí.

## K čemu slouží

SMIL byl vyvinut pro řešení potřeby standardizovaného způsobu vytváření synchronizovaných multimediálních prezentací na webu, kde rané přístupy spoléhaly na proprietární technologie nebo komplexní skriptování. Před SMIL vyžadovala integrace více typů médií s přesným načasováním vlastní řešení, která často nebyla interoperabilní napříč různými platformami. [W3C](/mobilnisite/slovnik/w3c/) vytvořilo SMIL jako otevřený jazyk založený na [XML](/mobilnisite/slovnik/xml/), aby umožnilo autorům snadno kombinovat audio, video a grafiku do souvislých prezentací bez hlubokých programátorských znalostí. Tím se demokratizovala tvorba multimediálního obsahu a zajistilo se, že prezentace mohou být konzistentně přehrávány na kompatibilních přehrávačích.

3GPP přijalo SMIL pro vylepšení mobilních multimediálních služeb, zejména se zavedením [MMS](/mobilnisite/slovnik/mms/) v sítích 2G/3G. Jak mobilní zařízení získávala schopnosti pro obrázky, audio a video, objevila se potřeba standardního formátu pro strukturování multimediálních zpráv nad rámec jednoduchých příloh. SMIL poskytlo odlehčený textový formát, který mohl definovat časové a prostorové rozvržení médií, čímž učinilo MMS zprávy interaktivnějšími a vizuálně atraktivnějšími. Vyřešilo problém nekonzistentního vykreslování na různých modelech telefonů tím, že poskytlo společnou prezentační vrstvu. Dále SMIL podporovalo streamovací služby tím, že umožňovalo playlisty a synchronizované doručování obsahu, což bylo klíčové pro aplikace mobilní TV a video na vyžádání. Jeho přijetí umožnilo operátorům nabízet bohaté multimediální zážitky při zajištění interoperability v ekosystému více dodavatelů, což pohánělo úspěch raných mobilních datových služeb.

## Klíčové vlastnosti

- Značkování založené na XML pro definici multimediálních prezentací
- Přesná časová synchronizace audia, videa, textu a obrázků
- Řízení prostorového rozvržení pro pozicování médií na displejích
- Podpora hypertextových odkazů a interaktivních prvků v prezentacích
- Profily přizpůsobené pro mobilní zařízení s omezenými prostředky
- Integrace s formáty souborů a streamovacími protokoly 3GPP

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [3GP – 3GPP File Format](/mobilnisite/slovnik/3gp/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [SMIL na 3GPP Explorer](https://3gpp-explorer.com/glossary/smil/)
