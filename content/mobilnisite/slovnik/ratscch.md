---
slug: "ratscch"
url: "/mobilnisite/slovnik/ratscch/"
type: "slovnik"
title: "RATSCCH – Robust Amr Traffic Synchronised Control CHannel"
date: 2025-01-01
abbr: "RATSCCH"
fullName: "Robust Amr Traffic Synchronised Control CHannel"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ratscch/"
summary: "Varianta řídicího kanálu v sítích GSM/EDGE navržená pro použití s adaptivním vícerychlostním (AMR) řečovým kodekem. Zvyšuje odolnost řídicí signalizace v náročných rádiových podmínkách, což zajišťuje"
---

RATSCCH je robustní varianta řídicího kanálu v sítích GSM/EDGE pro služby hlasu s kodekem AMR, která zvyšuje spolehlivost signalizace v nepříznivých rádiových podmínkách, aby zajistila sestavení, předání a udržení hovoru.

## Popis

Robust Amr Traffic Synchronised Control CHannel (RATSCCH) je specializovaný logický a fyzický kanál v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)). Je definován jako varianta pomalého přidruženého řídicího kanálu ([SACCH](/mobilnisite/slovnik/sacch/)), který je synchronizován s [AMR](/mobilnisite/slovnik/amr/) provozními kanály ([TCH](/mobilnisite/slovnik/tch/)). RATSCCH funguje ve spojení s AMR řečovým provozním kanálem a přenáší zásadní řídicí signalizační informace, jako jsou měřicí hlášení (pro rozhodování o předání hovoru), příkazy časového předstihu a informace o řízení výkonu mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). Jeho 'robustní' konstrukce odkazuje na použití zvýšené ochrany kanálovým kódováním a případně odlišného prokládání ve srovnání se standardním SACCH, což jej činí odolnějším vůči bitovým chybám v podmínkách slabého signálu. Funguje tak, že je multiplexován na stejný časový úsek fyzického kanálu jako AMR TCH podle definované struktury multirámce. Synchronizace se strukturou AMR rámců zajišťuje, že řídicí signalizace je těsně provázána s řečovými rámci, což umožňuje včasnou adaptaci na základě rádiových podmínek. Klíčové komponenty zahrnují specifická kódovací schémata (např. CS-1) a mapování na typy fyzických rádiových výbuchů. Jeho role je klíčová pro udržení aktivního AMR hlasového hovoru; bez spolehlivé signalizace SACCH nemůže síť správně spravovat spojení, což vede k přerušeným hovorům. RATSCCH je klíčovým prvkem pro fungování AMR kodeku v celém rozsahu jeho režimů, od vysoce kvalitních až po velmi robustní režimy s nízkou přenosovou rychlostí používané ve scénářích s omezeným pokrytím.

## K čemu slouží

RATSCCH byl zaveden, aby řešil specifickou potřebu vysoce spolehlivé řídicí signalizace při použití adaptivního vícerychlostního ([AMR](/mobilnisite/slovnik/amr/)) řečového kodeku v sítích GSM. AMR, který dynamicky upravuje svůj režim kodeku na základě rádiových podmínek, vyžaduje konzistentní a robustní doručování řídicích zpráv (jako jsou příkazy ke změně režimu a měřicí hlášení), aby mohl efektivně fungovat. Standardní SACCH, ačkoli robustní, mohl být stále limitujícím faktorem ve velmi špatných podmínkách, kdy by AMR přešel do svého nejvíce ochranného řečového režimu. Problém byl ten, že k přerušení hovoru mohlo dojít kvůli selhání řídicího kanálu, i když samotný řečový provozní kanál mohl být udržitelný. RATSCCH to řeší poskytnutím zvýšené ochrany proti chybám pro přidružený řídicí kanál speciálně přizpůsobený provoznímu prostředí AMR. To bylo motivováno snahou zlepšit kvalitu hlasu a pokrytí v sítích GSM, zejména na hranicích buněk a v oblastech náchylných k rušení. Zajišťuje, že schopnost sítě řídit hovor (prostřednictvím předání, řízení výkonu) zůstane zachována, i když je řeč přenášena pomocí nejrobustnějšího AMR režimu kodeku s nejnižší přenosovou rychlostí, čímž se rozšiřuje efektivní oblast pokrytí pro vysoce kvalitní hlasové služby a snižuje se míra přerušených hovorů.

## Klíčové vlastnosti

- Vylepšené kanálové kódování pro zvýšenou robustnost ve srovnání se standardním SACCH
- Synchronizovaný provoz s rámci AMR provozního kanálu
- Přenáší zásadní řídicí informace: měřicí hlášení, časový předstih, řízení výkonu
- Funguje jako přidružený řídicí kanál multiplexovaný s AMR TCH
- Podporuje spolehlivou adaptaci režimu AMR kodeku a provedení předání hovoru
- Definován v rámci specifikací GSM/EDGE pro kontinuitu hlasových služeb

## Související pojmy

- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 45.009** (Rel-19) — GSM AMR Link Adaptation & Control

---

📖 **Anglický originál a plná specifikace:** [RATSCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ratscch/)
