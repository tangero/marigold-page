---
slug: "e-tch"
url: "/mobilnisite/slovnik/e-tch/"
type: "slovnik"
title: "E-TCH – Enhanced Traffic Channel"
date: 2025-01-01
abbr: "E-TCH"
fullName: "Enhanced Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-tch/"
summary: "Vylepšená verze GSM Traffic Channel (TCH), která poskytuje vyšší přenosové rychlosti pro služby přepojování okruhů v síti GERAN. Používá pokročilá modulační a kódovací schémata, jako je 8-PSK, pro zle"
---

E-TCH je vylepšená verze GSM Traffic Channel, která poskytuje vyšší přenosové rychlosti pro služby přepojování okruhů v síti GERAN díky použití pokročilých modulačních a kódovacích schémat, jako je 8-PSK.

## Popis

Enhanced Traffic Channel (E-TCH) je zásadním vylepšením fyzického kanálu v GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Vychází z klasického GSM Traffic Channel, který tradičně používal modulaci Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)). E-TCH zavádí modulační schémata vyššího řádu, zejména 8-Phase Shift Keying ([8-PSK](/mobilnisite/slovnik/8-psk/)), spolu s robustnějšími mechanismy kódování a adaptace spoje. V provozu síť a mobilní stanice vyjednávají a vybírají vhodný typ kanálu a modulaci na základě rádiových podmínek. Při příznivých podmínkách může systém přidělit E-TCH používající 8-PSK modulaci, která přenáší 3 bity na symbol oproti 1 bitu na symbol u GMSK, čímž efektivně ztrojnásobuje hrubou symbolovou rychlost. To je řízeno technologií Enhanced Data Rates for GSM Evolution (EDGE). E-TCH není jediný kanál, ale rodina konfigurací kanálů definovaných různými Modulation and Coding Schemes ([MCS](/mobilnisite/slovnik/mcs/)). Tyto třídy MCS (MCS-1 až MCS-9) nabízejí škálu přenosových rychlostí a úrovní robustnosti. Zpracování na fyzické vrstvě pro E-TCH zahrnuje segmentaci datových bloků, aplikaci konvolučního kódování (s různými kódovacími poměry), prokládání přes více rádiových výbuchů a mapování na 8-PSK symboly pro přenos přes rozhraní vzduchu. Přijímač provádí inverzní operace, včetně ekvalizace a demodulace. Klíčové síťové komponenty zahrnují Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)), která musí podporovat 8-PSK modulaci, a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)), který zajišťuje přidělování kanálů a adaptaci spoje. E-TCH funguje v rámci stávající 200 kHz GSM nosné šířky pásma a [TDMA](/mobilnisite/slovnik/tdma/) rámcové struktury, což z něj činí zpětně kompatibilní upgrade. Jeho úlohou je poskytovat transport fyzické vrstvy pro vylepšená data s přepojováním okruhů (HSCSD) a především pro službu s přepojováním paketů Enhanced GPRS (EGPRS), čímž tvoří jádro uživatelské roviny EDGE.

## K čemu slouží

E-TCH byl vyvinut pro řešení rostoucí poptávky po vyšších rychlostech mobilních dat v rámci omezení stávajícího GSM spektra a infrastruktury. Původní GSM TCH používající GMSK modulaci byl omezen na maximální teoretickou přenosovou rychlost přibližně 14,4 kbps na časový slot pro datové služby. To bylo nedostatečné pro nové internetové aplikace. Účelem E-TCH bylo výrazně zvýšit spektrální účinnost bez nutnosti nového spektra nebo kompletní přestavby rádiové sítě. Zavedením 8-PSK modulace efektivně ztrojnásobil datovou kapacitu na Hertz. Tato evoluce byla klíčovou součástí standardizace EDGE, která byla konkurenční odpovědí na rané možnosti 3G a nákladově efektivním způsobem pro operátory, jak vylepšit své sítě 2,5G. Vyřešila problém nízké datové propustnosti pro mobilní přístup k internetu a umožnila služby jako rychlejší prohlížení webu a e-mail v GSM sítích. Prodlužovala komerční životnost GSM infrastruktury tím, že poskytovala jasnou migrační cestu k vyšším přenosovým rychlostem před plným nasazením sítí 3G UMTS.

## Klíčové vlastnosti

- Používá modulaci 8-PSK pro vyšší spektrální účinnost (3 bity/symbol)
- Definuje sadu Modulation and Coding Schemes (MCS-1 až MCS-9) pro adaptaci spoje
- Funguje v rámci standardní 200 kHz GSM nosné šířky pásma
- Zpětně kompatibilní s dědictvím přiřazení TCH založených na GMSK
- Umožňuje špičkové přenosové rychlosti až 59,2 kbps na časový slot v EGPRS
- Podporuje jak režim s přepojováním okruhů (E-TCH/F), tak režim s přepojováním paketů (E-TCH/P)

## Související pojmy

- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [E-TCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-tch/)
