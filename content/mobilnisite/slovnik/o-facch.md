---
slug: "o-facch"
url: "/mobilnisite/slovnik/o-facch/"
type: "slovnik"
title: "O-FACCH – Octal FACCH"
date: 2025-01-01
abbr: "O-FACCH"
fullName: "Octal FACCH"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/o-facch/"
summary: "Schéma kódování a modulace kanálu používané v GSM/EDGE Radio Access Network (GERAN) pro přenos zpráv Fast Associated Control Channel (FACCH). Využívá modulaci 8-PSK k zajištění vyšších datových rychlo"
---

O-FACCH je schéma kódování a modulace kanálu v GERAN, které využívá 8-PSK k přenosu zpráv FACCH s vyšší datovou rychlostí než starší schéma GMSK.

## Popis

Octal [FACCH](/mobilnisite/slovnik/facch/) (O-FACCH) je vylepšený přenosový režim pro Fast Associated Control Channel (FACCH) v rámci vývoje GSM/[EDGE](/mobilnisite/slovnik/edge/). FACCH je mechanismus 'krádeže' řídicího kanálu, kdy jsou během hovoru nebo datového přenosu rámy normálně alokované pro Traffic Channel ([TCH](/mobilnisite/slovnik/tch/)) dočasně použity k přenosu naléhavých signalizačních zpráv, jako jsou příkazy k předání spojení. V původním GSM využívá FACCH stejnou modulaci Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) a stejné kódování kanálu jako přidružený TCH. Se zavedením EDGE (Enhanced Data rates for GSM Evolution) byla pro paketová data definována nová schémata modulace a kódování. O-FACCH aplikuje tato vylepšení – konkrétně modulaci [8-PSK](/mobilnisite/slovnik/8-psk/) (Phase Shift Keying) – na FACCH za účelem zvýšení jeho signalizační kapacity a odolnosti.

Fungování O-FACCH je vázáno na modulační a kódovací schéma přidruženého kanálu pro přenos uživatelských dat. Když mobilní stanice a síť podporují EDGE a používají pro paketový datový kanál ([PDTCH](/mobilnisite/slovnik/pdtch/)) modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) založené na 8-PSK, může být přidružená řídicí signalizace na FACCH také vysílána pomocí modulace 8-PSK, odtud označení 'Octal' (osmičková). Zpracování na fyzické vrstvě zahrnuje mapování zakódovaných bitů FACCH na symboly 8-PSK, které nesou tři bity na symbol ve srovnání s jedním bitem na symbol u GMSK. Tím se zhruba ztrojnásobí hrubá rychlost symbolů, ale skutečné navýšení užitečného datového toku je řízeno specifickými schématy kódování kanálu (jako CS-4 pro GMSK nebo MCS-1 až MCS-9 pro 8-PSK), navrženými k vyvážení datové rychlosti a ochrany proti chybám.

Z pohledu sítě se podpora O-FACCH vyjednává při přiřazování rádiového kanálu a je indikována v popisu kanálu. Příjímač musí být schopen demodulovat rámy 8-PSK. Klíčovou výhodou je, že při daném množství 'ukradeného' času na rozhraní vzduch–rádiové rozhraní (jeden rám) může zpráva O-FACCH nést více informací nebo může být odolněji zakódována než zpráva FACCH založená na GMSK. To je zvláště důležité pro efektivní signalizaci v sítích EDGE, kde mohou být řídicí zprávy související s řízením paketového toku, přeřazením kanálu nebo předáním spojení v kontextu vysokorychlostních dat složitější. O-FACCH zajišťuje, že řídicí rovina drží krok se vylepšenými schopnostmi uživatelské roviny ve vyvinutých sítích [GERAN](/mobilnisite/slovnik/geran/).

## K čemu slouží

O-FACCH byl vyvinut k řešení omezení kapacity řídicího kanálu v sítích GSM vylepšených technologií EDGE. EDGE zavedlo modulaci vyššího řádu 8-PSK k výraznému zvýšení datových rychlostí uživatelských dat na kanálech pro přenos uživatelských dat. Avšak přidružený řídicí kanál (FACCH) stále používal starší a pomalejší modulaci GMSK. To vytvořilo nerovnováhu, kdy uživatelská rovina mohla přenášet velké množství dat, ale řídicí rovina zůstávala omezena nižší signalizační kapacitou FACCH založeného na GMSK. To mohlo vést k neefektivitám, jako je potřeba více 'ukradených' rámů k přenosu jedné složité signalizační zprávy, což zvyšovalo latenci a snižovalo čas dostupný pro uživatelská data.

Primárním účelem O-FACCH je sladit výkonnost řídicího kanálu s vylepšenou uživatelskou rovinou. Tím, že umožňuje FACCH používat modulaci 8-PSK, zvyšuje hrubou přenosovou rychlost dostupnou pro signalizaci v rámci jednoho rámu. To umožňuje zabalit více dat do jedné řídicí zprávy nebo aplikovat silnější kódování kanálu ve stejném časovém slotu, čímž se zlepšuje spolehlivost. To je klíčové pro podporu pokročilých funkcí EDGE a udržení efektivního provozu sítě během vysokorychlostních paketových datových relací.

Zavedeno v 3GPP Release 8 jako součást pokračujícího vývoje GERAN, O-FACCH vyřešilo praktický inženýrský problém v nasazených sítích. Umožnilo operátorům maximalizovat využitelnost jejich investic do EDGE tím, že zajistilo, aby řídicí signalizace pro předání spojení, adaptaci spojení a plánování paketů nebyla faktorem omezujícím výkon. Prodlužovalo životnost a konkurenceschopnost sítí GSM/EDGE v éře rostoucí poptávky po mobilních datech a poskytovalo plynulejší uživatelský zážitek z datových služeb bez nutnosti zcela nové technologie rádiového přístupu.

## Klíčové vlastnosti

- Používá modulaci 8-PSK pro přenos FACCH
- Poskytuje vyšší hrubou přenosovou rychlost na rám ve srovnání s FACCH používajícím GMSK
- Používá se ve spojení s paketovými datovými kanály EDGE (PDTCH používající 8-PSK)
- Umožňuje efektivnější nebo odolnější kódování řídicích zpráv
- Vyjednáváno a konfigurováno při přiřazování rádiového kanálu
- Součást vývoje GERAN pro vylepšenou řídicí signalizaci

## Související pojmy

- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [O-FACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-facch/)
