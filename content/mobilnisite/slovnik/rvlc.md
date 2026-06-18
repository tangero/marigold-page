---
slug: "rvlc"
url: "/mobilnisite/slovnik/rvlc/"
type: "slovnik"
title: "RVLC – Reverse Variable Length Code"
date: 2025-01-01
abbr: "RVLC"
fullName: "Reverse Variable Length Code"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rvlc/"
summary: "Reverse Variable Length Code (RVLC) je technika kódování kanálu používaná v multimediálních vysílacích službách 3GPP. Zvyšuje odolnost proti chybám tím, že umožňuje dekódování v obou směrech, což zlep"
---

RVLC je technika kódování kanálu používaná v multimediálních vysílacích službách 3GPP, která zvyšuje odolnost proti chybám tím, že umožňuje dekódování v obou směrech (dopředném i zpětném) a tím zlepšuje příjem.

## Popis

Reverse Variable Length Code (RVLC) je schéma kódování pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) specifikované v 3GPP TS 26.111 pro multimediální vysílací/vícestaniční služby ([MBMS](/mobilnisite/slovnik/mbms/)), zejména v kontextu 3GPP Packet Switched Streaming ([PSS](/mobilnisite/slovnik/pss/)) a Multimedia Broadcast Multicast Service (MBMS). Tato kódovací technika je aplikována na data kódovaná proměnnou délkou, jako jsou například Huffmanem kódované symboly, pro zvýšení odolnosti proti chybám. Na rozdíl od konvenčních kódů s proměnnou délkou ([VLC](/mobilnisite/slovnik/vlc/)), které jsou dekódovatelné pouze v jednom směru, je RVLC navržen tak, aby byl jednoznačně dekódovatelný dopředu i dozadu. Tato obousměrná dekódovatelnost je dosažena konstrukcí kódových slov, která splňují symetrické vlastnosti, což umožňuje dekodéru začít s dekódováním z libovolného konce přijatého bitového toku, pokud chyby poškodí část dat.

Z architektonického hlediska RVLC funguje na aplikační vrstvě zásobníku pro doručování multimédií. V systému MBMS je multimediální obsah kódován pomocí audio a video kodeků, které často produkují kódy proměnné délky po entropickém kódování (např. Huffmanovo kódování v Advanced Audio Coding - [AAC](/mobilnisite/slovnik/aac/)). Tyto bitové toky VLC jsou následně chráněny RVLC před zabalením do paketů a přenosem přes vysílací kanál. Klíčové komponenty zahrnují RVLC kodér ve vysílacím zdroji, který mapuje zdrojové symboly na reverzibilní kódová slova, a RVLC dekodér v přijímači, který využívá reverzibility k obnově dat, i když je bitový tok poškozen. Dekodér obvykle využívá synchronizační značky a mechanismy detekce chyb k identifikaci hranic chyb a pokusí se o dekódování z obou směrů, aby maximalizoval obnovu dat.

Jak RVLC funguje, zahrnuje konstrukci kódové knihy, kde každé kódové slovo je palindrom nebo splňuje specifická omezení zajišťující reverzibilitu. Při přenosu kodér zpracovává zdrojové symboly a vytváří RVLC kódová slova. Během příjmu, pokud dojde k chybám, dekodér může ztratit synchronizaci, což znemožňuje dopředné dekódování za bodem chyby. Protože je však kód reverzibilní, může dekodér začít od konce bitového toku a dekódovat dozadu, dokud nenarazí na chybu z druhé strany. To efektivně umožňuje obnovu dat, která by jinak byla ztracena. Tato technika je obzvláště účinná proti shlukovým chybám běžným v bezdrátových kanálech, protože zvyšuje pravděpodobnost dekódování segmentů mezi shluky chyb.

Úloha RVLC v síti spočívá ve zlepšení uživatelského komfortu u vysílacích služeb zvýšením odolnosti proti chybám bez výrazného nárůstu režie. Je klíčovým prvkem pro spolehlivou mobilní [TV](/mobilnisite/slovnik/tv/) a streamování přes vysílací sítě, kde se podmínky na kanále mohou u jednotlivých uživatelů výrazně lišit. Integrací s dalšími mechanismy FEC, jako jsou Reed-Solomonovy kódy na transportní vrstvě, poskytuje RVLC vrstvený přístup k ochraně, který zajišťuje robustní doručování multimediálního obsahu i v náročných rádiových prostředích, čímž podporuje komerční životaschopnost vysílacích služeb v systémech 3GPP.

## K čemu slouží

RVLC byl vyvinut, aby řešil problém šíření chyb v multimediálních datech kódovaných proměnnou délkou přenášených přes náchylné vysílací bezdrátové kanály. V tradičních schématech [VLC](/mobilnisite/slovnik/vlc/), jako je Huffmanovo kódování používané v audio a video kompresi, může jediná bitová chyba způsobit ztrátu synchronizace, což vede ke katastrofálnímu selhání dekódování, protože dekodér špatně interpretuje následující bity. To je obzvláště problematické u vysílacích služeb jako [MBMS](/mobilnisite/slovnik/mbms/), kde jsou retransmise neefektivní nebo nemožné a uživatelé zažívají různou kvalitu signálu. RVLC to řeší umožněním obousměrného dekódování, což přijímačům umožňuje obnovit více dat z poškozených proudů.

Motivace pro RVLC vychází z potřeby efektivní odolnosti proti chybám při multimediálním vysílání bez nadměrné redundance. Předchozí přístupy se výrazně spoléhaly na FEC na nižších vrstvách nebo na retransmise, což mohlo zavést vysokou latenci nebo režii na šířce pásma. RVLC představuje řešení na aplikační vrstvě, které doplňuje ochrany fyzické vrstvy. Bylo představeno v 3GPP Release 8 spolu s vylepšeními pro MBMS jako součást snahy umožnit služby mobilní TV a skupinové komunikace přes mobilní sítě. Tato technika umožňuje vysílatelům doručovat přijatelnou kvalitu většímu publiku, včetně uživatelů na okraji buňky nebo v oblastech se špatným pokrytím.

Historicky zahrnovala odolnost proti chybám u dat VLC techniky jako reverzibilní kódování s proměnnou délkou (RVLC) převzaté ze standardů jako MPEG-4. 3GPP standardizovalo RVLC, aby zajistilo interoperabilitu a optimální výkon ve svých multimediálních frameworkech. Řeší omezení předchozích metod tím, že nabízí standardizovanou konstrukci kódu, která vyvažuje efektivitu komprese se schopností obnovy po chybách. To umožňuje poskytovatelům služeb nasadit vysílací služby spolehlivěji, zlepšit uživatelský komfort a podporovat obchodní modely pro hromadné šíření médií přes mobilní sítě.

## Klíčové vlastnosti

- Obousměrná dekódovatelnost umožňující dopředné i zpětné dekódování kódů s proměnnou délkou
- Zvýšená odolnost proti shlukovým chybám v bezdrátových vysílacích kanálech
- Dopředná korekce chyb na aplikační vrstvě, která doplňuje FEC fyzické vrstvy
- Standardizovaná konstrukce kódu pro interoperabilitu v 3GPP MBMS a PSS
- Snižuje šíření chyb v entropicky kódovaných multimediálních bitových tocích
- Zlepšuje uživatelský komfort u služeb mobilní TV a streamování

## Definující specifikace

- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia

---

📖 **Anglický originál a plná specifikace:** [RVLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rvlc/)
