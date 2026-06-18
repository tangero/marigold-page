---
slug: "gop"
url: "/mobilnisite/slovnik/gop/"
type: "slovnik"
title: "GOP – Group Of Pictures"
date: 2025-01-01
abbr: "GOP"
fullName: "Group Of Pictures"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gop/"
summary: "GOP je základní sekvenční struktura ve videokompresi (např. MPEG, H.26x), skládající se z I-snímku následovaného P- a B-snímky. Definuje vzor vnitro- a mezisnímkového kódování, vyvažuje kompresní účin"
---

GOP je základní sekvenční struktura ve videokompresi, která definuje vzor vnitro- a mezisnímkového kódování pro vyvážení komprese, náhodného přístupu a odolnosti proti chybám pro multimediální služby 3GPP.

## Popis

Skupina snímků (Group Of Pictures, GOP) je klíčová struktura na vysoké úrovni v normách pro kompresi pohyblivého videa, jako jsou [MPEG-2](/mobilnisite/slovnik/mpeg-2/), MPEG-4, H.264/[AVC](/mobilnisite/slovnik/avc/) a H.265/[HEVC](/mobilnisite/slovnik/hevc/). Představuje sekvenci po sobě jdoucích snímků, která začíná nezávisle dekódovatelným vnitrosnímkově kódovaným snímkem (I-snímek) a je následována uspořádáním prediktivně kódovaných snímků (P-snímky) a obousměrně prediktivně kódovaných snímků (B-snímky). Struktura GOP definuje vzor a vzdálenost mezi těmito různými typy snímků, což je zásadní pro výkonnostní charakteristiky kodeku.

I-snímek je zakódován pouze s využitím prostorové redundance v rámci jediného snímku, podobně jako obrázek [JPEG](/mobilnisite/slovnik/jpeg/), což znamená velkou velikost, ale je nezbytný pro náhodný přístup a obnovu po chybě. P-snímky jsou kódovány predikcí pohybu z předchozího I- nebo P-snímku, ukládají se pouze rozdíly (reziduum) a pohybové vektory, což poskytuje dobrou kompresi. B-snímky pro predikci využívají jak minulé, tak budoucí referenční snímky, dosahují nejvyšší komprese, ale zavádějí zpoždění a složitost při kódování/dekódování. GOP je definována dvěma parametry: N (délka GOP, neboli vzdálenost mezi I-snímky) a M (vzdálenost mezi referenčními snímky, např. interval mezi I/P-snímky). Běžná struktura je IBBPBBP... (N=12, M=3).

V rámci specifikací 3GPP je koncept GOP ústřední pro definování profilů a úrovní videokodeků pro streamování (např. 3GPP [PSS](/mobilnisite/slovnik/pss/)), multimediální vysílání/multicasting ([MBMS](/mobilnisite/slovnik/mbms/)) a konverzační služby s přepojováním paketů. Specifikace jako 26.904 (Transparent end-to-end packet-switched streaming service codec specification) podrobně popisují povolené struktury GOP pro vizuální kodek MPEG-4 a kodeky H.264 za účelem zajištění interoperability. Volba struktury GOP přímo ovlivňuje datový tok, latenci, odolnost proti chybám a dobu přepnutí kanálu u videoslužeb. Například dlouhá GOP (velké N) zvyšuje kompresní účinnost, ale činí proud zranitelnějším vůči chybám a prodlužuje dobu přepnutí kanálu (protože dekodér musí čekat na I-snímek). Specifikace 3GPP často tyto parametry omezují, aby vyhovovaly omezením a případům užití mobilních sítí.

## K čemu slouží

Účelem struktury GOP ve videokódování je dosáhnout optimálního kompromisu mezi třemi protichůdnými cíli: vysoká kompresní účinnost, podpora náhodného přístupu (např. přepínání kanálů, vyhledávání) a odolnost vůči ztrátě dat. Bez mezisnímkové predikce (pouze s I-snímky) by byla komprese velmi slabá, což by činilo video nepraktickým pro mobilní sítě s omezenou šířkou pásma. Pokud by se však používala pouze mezisnímková predikce (např. samé P-snímky), vytvořil by se dlouhý predikční řetězec, který by učinil proud extrémně náchylným k chybám a znemožnil by připojení uprostřed proudu.

GOP to řeší periodickým vkládáním velkého, samostatného I-snímku, který resetuje predikční řetězec. To umožňuje dekodérům začít dekódovat na jakékoli hranici GOP, což umožňuje funkce jako rychlý posun vpřed/vzad a přepínání kanálů ve vysílacích službách. P- a B-snímky mezi I-snímky zajišťují vysokou kompresi. V kontextu standardizace mobilních videoslužeb 3GPP bylo definování povolených struktur GOP zásadní pro zajištění toho, aby video obsah zakódovaný jednou entitou mohl být spolehlivě dekódován jakýmkoli kompatibilním UE.

Historicky čelily rané mobilní videoslužby, jako 3GPP Packet-Switched Streaming ([PSS](/mobilnisite/slovnik/pss/)), závažným omezením šířky pásma. Výběr kodeků jako MPEG-4 Visual a H.264 Baseline Profile se specifickými, omezenými parametry GOP (např. krátké délky GOP) byl motivován potřebou minimalizovat složitost dekódování a využití paměti na raných mobilních zařízeních při současném poskytnutí přijatelné kvality a odolnosti proti chybám přes ztrátové rádiové přenosy. S rostoucími schopnostmi zařízení a šířkou pásma sítě pozdější verze 3GPP podporovaly pokročilejší kodeky s flexibilními strukturami GOP, což umožnilo streamování ve vysokém rozlišení a adaptivní streamování (např. [DASH](/mobilnisite/slovnik/dash/)), kde mohou být nabízeny různé reprezentace stejného obsahu s různými strukturami GOP.

## Klíčové vlastnosti

- Definuje periodický vzor I-, P- a B-snímků v rámci videosledu
- Klíčové parametry: N (délka GOP/vzdálenost mezi I-snímky) a M (vzdálenost mezi referenčními snímky)
- I-snímek poskytuje body pro náhodný přístup a odolnost proti chybám resetováním predikčních závislostí
- P- a B-snímky umožňují vysokou kompresní účinnost prostřednictvím časové predikce
- Struktura GOP přímo ovlivňuje datový tok, latenci, šíření chyb a zpoždění při přepínání kanálů
- Je omezena specifikacemi kodeků 3GPP (např. pro H.264 Baseline Profile) za účelem zajištění interoperability a výkonu UE

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TR 26.999** (Rel-19) — VR Streaming Interoperability Test Material

---

📖 **Anglický originál a plná specifikace:** [GOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gop/)
