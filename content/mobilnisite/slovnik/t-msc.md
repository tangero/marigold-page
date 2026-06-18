---
slug: "t-msc"
url: "/mobilnisite/slovnik/t-msc/"
type: "slovnik"
title: "T-MSC – Terminating MSC"
date: 2025-01-01
abbr: "T-MSC"
fullName: "Terminating MSC"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-msc/"
summary: "Ústředna mobilního spojování (MSC), která zpracovává koncovou (příchozí) část okruhově přepínaného hlasového hovoru k mobilnímu účastníkovi. Zodpovídá za směrování hovoru od bránové MSC (GMSC), za pro"
---

T-MSC je ústředna mobilního spojování (Mobile Switching Center), která zpracovává koncovou část okruhově přepínaného hlasového hovoru k mobilnímu účastníkovi – směruje hovor od brány a navazuje spojení k účastníkově obsluhující síti.

## Popis

V okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně sítí 2G (GSM) a 3G (UMTS) je Terminating [MSC](/mobilnisite/slovnik/msc/) (T-MSC) specifická funkční role, kterou zaujímá ústředna mobilního spojování během sestavování příchozího hovoru k mobilnímu účastníkovi. Nejde nutně o samostatný fyzický uzel, ale o logickou funkci vykonávanou MSC na trase hovoru. Když je hovor určen mobilnímu účastníkovi, typicky nejprve dorazí k bránové MSC ([GMSC](/mobilnisite/slovnik/gmsc/)). GMSC se dotáže na registr domácí lokalizace ([HLR](/mobilnisite/slovnik/hlr/)), aby získala směrovací informace, které zahrnují adresu MSC aktuálně obsluhující účastníka – tato obsluhující MSC je pro daný konkrétní hovor T-MSC.

T-MSC přijímá signalizaci pro sestavení hovoru (např. zprávu [ISUP](/mobilnisite/slovnik/isup/) Initial Address Message) od GMSC. Jejím hlavním úkolem je dotaz na s ní asociovaný registr navštívené lokalizace ([VLR](/mobilnisite/slovnik/vlr/)) za účelem získání aktuálního stavu účastníka a informací o jeho poloze (např. lokalizační oblast). T-MSC poté iniciuje proces pagingu v příslušné rádiové přístupové síti ([BSS](/mobilnisite/slovnik/bss/) pro GSM, [RNS](/mobilnisite/slovnik/rns/) pro UMTS) k lokalizaci konkrétní mobilní stanice. Jakmile mobilní stanice odpoví, T-MSC v případě potřeby provede procedury autentizace a šifrování. Následně alokuje pozemní okruh (např. časový slot E1) pro hovor směrem k GMSC a naváže spojení k řídicí jednotce rádiové sítě (BSC nebo RNC) za účelem nastavení rádiového přenosového kanálu.

Během celého hovoru funguje T-MSC jako kotvící bod pro koncovou část hovoru. Zpracovává funkce řízení hovoru, jako je např. vyzvání volaného účastníka, připojení hlasové cesty po přijetí hovoru, správa služeb během hovoru (jako čekání na lince nebo podržení hovoru) a zpracování signalizace pro ukončení hovoru. Interaguje také s účtovacími systémy za účelem generování záznamů o hovoru (CDR) pro koncovou část hovoru. V sítích s pokročilými funkcemi, jako je CAMEL, může T-MSC také aktivovat servisní logiku pro koncovou stranu na základě informací o předplatném (T-CSI). Její role je klíčová pro úspěšné dokončení a správu jakéhokoli příchozího okruhově přepínaného hovoru k mobilnímu účastníkovi.

## K čemu slouží

Koncept Terminating MSC (T-MSC) vznikl ze zásadní potřeby směrování v mobilních sítích. Ve fixní telefonii je hovor směrován přímo na fyzickou linku. V mobilních sítích se může účastník nacházet kdekoliv, což vyžaduje dynamický směrovací mechanismus. Role T-MSC formalizuje síťový prvek zodpovědný za poslední krok směrování a řízení spojení k pohyblivému cíli – mobilnímu účastníkovi. Řeší tím základní problém 'najít a spojit' pro příchozí hovory.

Před standardizovanými buněčnými architekturami neexistoval efektivní způsob, jak směrovat hovory k putujícímu uživateli. Oddělení funkcí na bránovou MSC (pro příchozí směrovací dotaz) a koncovou MSC (pro lokální správu účastníka) vytvořilo škálovatelnou a efektivní architekturu. Účelem T-MSC je lokalizovat složité procedury dotazování na účastníka, pagingu, autentizace a alokace rádiových zdrojů do síťové oblasti, kde se účastník aktuálně nachází. Tento návrh minimalizuje signalizační provoz v síti a umožňuje efektivní využití zdrojů. Jeho zavedení bylo motivováno požadavkem, aby bylo mobilní zakončení hovoru stejně spolehlivé a funkčně bohaté jako zakončení ve fixních sítích, a zároveň aby řešilo jedinečné výzvy mobility účastníka, což vedlo ke vzniku robustního globálního systému mobilní komunikace, který máme dnes.

## Klíčové vlastnosti

- Přijímá příchozí sestavení hovoru od bránové MSC (GMSC)
- Dotazuje se na svůj asociovaný VLR o stavu a poloze účastníka
- Iniciuje a spravuje proceduru pagingu v rádiové přístupové síti
- Provádí autentizaci a šifrování pro koncovou část hovoru
- Kotví hlasovou cestu a spravuje služby během hovoru pro koncovou stranu
- Generuje účtovací záznamy (CDR) pro segment hovoru zakončeného u mobilního účastníka

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)

---

📖 **Anglický originál a plná specifikace:** [T-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-msc/)
