---
slug: "pli"
url: "/mobilnisite/slovnik/pli/"
type: "slovnik"
title: "PLI – Picture Loss Indication"
date: 2025-01-01
abbr: "PLI"
fullName: "Picture Loss Indication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pli/"
summary: "Zpětnovazební mechanismus ve videotelefonii a streamovacích službách, při kterém přijímač informuje odesílatele o ztrátě obrazového snímku videa. To umožňuje odesílateli provést nápravnou akci, jako j"
---

PLI je zpětnovazební mechanismus, při kterém přijímač informuje odesílatele videa o ztrátě obrazového snímku, což umožňuje nápravnou akci pro zachování kvality.

## Popis

Picture Loss Indication (PLI) je řídicí zpráva definovaná v rámci protokolu Real-time Transport Control Protocol ([RTCP](/mobilnisite/slovnik/rtcp/)), konkrétně pro použití s [RTP](/mobilnisite/slovnik/rtp/) video proudy v 3GPP multimediálních službách, jako je IP Multimedia Subsystem (IMS). Funguje jako součást zpětnovazebního mechanismu mezi přijímačem videa (např. UE) a odesílatelem videa (např. media resource function nebo jiné UE). Když video dekodér přijímače zjistí, že chybí nebo je nenávratně poškozen kompletní obraz videa nebo kritický videosnímek (jako I-snímek nebo [IDR](/mobilnisite/slovnik/idr/) snímek), vygeneruje a odešle zpět odesílateli paket PLI. Tento paket je stručná zpětnovazební zpráva, která nespecifikuje, který přesný snímek byl ztracen, ale funguje jako naléhavá žádost.

Po přijetí PLI ji aplikace nebo mediální řadič odesílatele interpretuje jako signál, že predikční stav dekodéru může být poškozen. Protože moderní video kodeky jako H.264 a H.265 používají predikci mezi snímky (kde snímky odkazují na předchozí), ztráta referenčního snímku může způsobit přetrvávající artefakty, dokud není přijat nový nezávislý referenční bod. Proto je typickou a nejúčinnější reakcí odesílatele vygenerování a odeslání nového intra-snímku (I-snímku nebo IDR snímku). Intra-snímek je zakódován bez odkazu na jakýkoli jiný snímek, čímž se resetuje stav dekodéru a zastaví se šíření vizuálních chyb. Tento proces je klíčový pro konverzační služby v reálném čase, kde je retransmise konkrétního ztraceného paketu často neproveditelná kvůli omezením zpoždění.

Implementace a zpracování PLI jsou specifikovány v 3GPP TS 26.114 pro služby založené na IMS a v TS 26.922 pro aspekty specifické pro kodek. Mechanismus je integrován s dalšími typy zpětné vazby [RTCP](/mobilnisite/slovnik/rtpcp/), jako je Full Intra Request ([FIR](/mobilnisite/slovnik/fir/)) a Receiver Reports ([RR](/mobilnisite/slovnik/rr/)). Zatímco FIR je obecnější žádost o intra-snímek, často používaná pro změny scény nebo připojení k relaci, PLI je specificky spouštěna ztrátou paketu. Síťové mechanismy QoS, jako jsou ty ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), pracují na minimalizaci ztrát, ale PLI poskytuje metodu obnovy na aplikační vrstvě pro reziduální chyby, které nastanou, zejména přes bezdrátové spoje. Její role je zásadní pro udržení Quality of Experience ([QoE](/mobilnisite/slovnik/qoe/)) u videohovorů a streamování tím, že zajišťuje rychlé zotavení z přenosových chyb.

## K čemu slouží

PLI byla vytvořena, aby řešila kritický problém šíření chyb v prediktivním video kódování přes paketové sítě, zejména náchylné k chybám bezdrátové kanály v systémech 3G/4G/5G. Před takovými standardizovanými zpětnovazebními mechanismy mohla videotelefonie přes mobilní sítě trpět dlouhotrvajícím vizuálním zhoršením po ztrátě paketu. Jediný ztracený paket obsahující část referenčního snímku mohl poškodit mnoho následných závislých snímků (P-snímků a B-snímků), což vedlo k zamrzlému nebo blokovanému videu, které mohlo přetrvávat až do dalšího přirozeně se vyskytujícího intra-snímku, což mohlo být až za několik sekund. To vážně degradovalo uživatelský zážitek.

Motivace pro PLI vychází z přechodu na plně IP sítě a IMS pro multimediální služby v 3GPP Release 5 a novějších. Jelikož se konverzační video stalo klíčovou službou, byl potřeba standardizovaný, nenáročný způsob, jak může přijímač signalizovat katastrofické selhání stavu dekodéru. PLI to poskytuje vytvořením přímé, rychlé zpětnovazební smyčky v rámci protokolového zásobníku RTP/RTCP, což umožňuje odesílateli proaktivně opravit proud. Řeší omezení čistě síťové retransmise (jako RLC AM), která může zavádět nepřijatelné zpoždění pro video v reálném čase, tím, že přesouvá inteligenci obnovy do aplikační vrstvy, kde je chápán sémantický význam videosnímků.

Historicky byla standardizace PLI spolu s kodeky jako H.264/AVC v Release 8 součástí snahy 3GPP zajistit robustní videotelefonii interoperabilní mezi dodavateli a sítěmi. Řešila nedostatky dřívějších videotelefonních služeb v okruhově přepínaných sítích, které měly odlišné charakteristiky chyb, a poskytla nástroj pro poskytovatele služeb, aby garantovali základní video QoE i za kolísavých rádiových podmínek, což je zásadní pro přijetí a spokojenost uživatelů.

## Klíčové vlastnosti

- Spouští rychlé zotavení ze ztráty video paketu
- Používá RTCP jako transportní protokol pro zpětnou vazbu
- Výsledkem je přenos nového intra-snímku (I-snímku/IDR)
- Minimalizuje šíření chyb v prediktivních video kodecích
- Nezbytná pro udržení QoE u služeb videa v reálném čase
- Standardizována napříč specifikacemi 3GPP IMS pro multimédia

## Související pojmy

- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [PLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pli/)
