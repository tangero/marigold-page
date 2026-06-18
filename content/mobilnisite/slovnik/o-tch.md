---
slug: "o-tch"
url: "/mobilnisite/slovnik/o-tch/"
type: "slovnik"
title: "O-TCH – Octal Traffic Channel"
date: 2025-01-01
abbr: "O-TCH"
fullName: "Octal Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/o-tch/"
summary: "Plně rychlostní přenosový kanál (TCH) v systémech GSM/EDGE, který využívá modulaci s 8 fázovými posuvy (8-PSK) pro přenos uživatelských dat, primárně pro zvýšené přenosové rychlosti v rámci GSM Evolut"
---

O-TCH je plně rychlostní kanál pro přenos uživatelských dat v GSM/EDGE, který využívá modulaci 8-PSK, čímž poskytuje vyšší spektrální účinnost a umožňuje špičkové přenosové rychlosti až 59,2 kbps na časový slot.

## Popis

Osmový přenosový kanál (O-TCH) je specifický typ přenosového kanálu v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)), který využívá modulaci s 8 fázovými posuvy ([8-PSK](/mobilnisite/slovnik/8-psk/)). V GSM je základní jednotkou pro přenos hlasu a dat přenosový kanál ([TCH](/mobilnisite/slovnik/tch/)), který je mapován na fyzický rádiový časový slot. Tradiční GSM používá Gaussovské minimální fázové klíčování ([GMSK](/mobilnisite/slovnik/gmsk/)), což je forma binární modulace. O-TCH, zavedený s EDGE, používá 8-PSK, což je modulace vyššího řádu, která kóduje 3 bity na symbol namísto 1, čímž se za dobrých rádiových podmínek ztrojnásobí hrubá přenosová rychlost na symbol.

O-TCH je zřízen na vyhrazeném rádiovém zdroji (časovém slotu) mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)). Kanál se používá pro přenos uživatelských dat paketově přepínaných (přes [EGPRS](/mobilnisite/slovnik/egprs/)) nebo okruhově přepínaných datových služeb. Termín 'osmový' odkazuje na 8 možných fázových stavů konstelace 8-PSK, které odpovídají 3bitovým symbolům. Síť přiřazuje O-TCH na základě měření kvality rádiového spoje; 8-PSK je náchylnější k chybám než GMSK, takže se typicky používá pouze tehdy, když je poměr signálu k interferenci (C/I) dostatečně vysoký. BTS i MS musí podporovat funkci EDGE, aby mohly O-TCH používat.

Provoz O-TCH zahrnuje komplexní adaptaci spojení a techniky přírůstkové redundance. Řídicí jednotka paketů (PCU) sítě a MS neustále sledují kvalitu kanálu. Na základě toho může síť přepnout modulační a kódovací schéma (MCS) pro daný blok dat. O-TCH odpovídá vyšším třídám MCS (MCS-5 až MCS-9). Pokud se podmínky zhorší, systém může přejít zpět na kanál založený na GMSK (tzv. 'B-TCH' nebo binární TCH, používající MCS-1 až MCS-4). Toto dynamické přepínání probíhá po blocích (každých 20 ms), což činí EDGE robustním. Pro okruhově přepínaná data platí podobný koncept, kdy jsou kanály TCH/F a TCH/H rozšířeny na O-TCH/F a O-TCH/H pro vyšší přenosové rychlosti.

## K čemu slouží

O-TCH byl vytvořen za účelem významného zvýšení přenosových rychlostí uživatelských dat v rámci stávajícího spektra GSM a struktury časových slotů, což byl klíčový cíl standardu EDGE (Enhanced Data rates for GSM Evolution). Před EDGE byly datové služby GSM (GPRS) omezeny na modulaci GMSK, která nabízela teoretické maximum přibližně 21,4 kbps na časový slot. Explozivní růst poptávky po mobilních datech na počátku 21. století si vyžádal zpětně kompatibilní upgrade, který nevyžadoval nové spektrum. Modulace 8-PSK byla zvolena, protože poskytovala výrazné zvýšení spektrální účinnosti (bitů za sekundu na hertz) a zároveň byla realizovatelná s úpravami z velké části omezenými na základnové pásmo BTS a MS.

Zavedení O-TCH vyřešilo problém poskytnutí nákladově efektivní, evoluční cesty pro operátory GSM, aby mohli nabízet datové služby blízké 3G (často označované jako '2.75G') před nasazením sítí UMTS. Odstranilo to omezení nízkých přenosových rychlostí GPRS a umožnilo služby jako rychlejší prohlížení webu, e-mail s přílohami a ranou mobilní multimédii. Filozofií návrhu bylo znovu použít stávající kmitočtové rozestupy GSM, strukturu kanálů a protokoly, přičemž se na ně překládala nová modulace a vylepšené techniky spojové vrstvy. To umožnilo operátorům postupně upgradovat své sítě, často prostřednictvím softwarových aktualizací a aktualizací kanálových karet, čímž chránili svou stávající investici a zároveň uspokojovali rostoucí poptávku zákazníků po datech.

## Klíčové vlastnosti

- Používá modulaci 8-PSK k přenosu 3 bitů na symbol, čímž se za dobrých podmínek ztrojnásobí spektrální účinnost oproti GMSK
- Umožňuje špičkové přenosové rychlosti EGPRS až 59,2 kbps na rádiový časový slot
- Funguje v rámci stávající šířky pásma nosné GSM 200 kHz a struktury TDMA rámců
- Podléhá dynamické adaptaci spojení, při špatných rádiových podmínkách přechází na GMSK (B-TCH)
- Používá se pro zvýšená okruhově přepínaná data (ECSD) i pro paketově přepínané datové služby EGPRS
- Vyžaduje transceivery s podporou EDGE jak v síti, tak v mobilní stanici

## Související pojmy

- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [8-PSK – 8-state Phase Shift Keying](/mobilnisite/slovnik/8-psk/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [O-TCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-tch/)
