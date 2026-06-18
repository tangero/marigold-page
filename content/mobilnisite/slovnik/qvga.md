---
slug: "qvga"
url: "/mobilnisite/slovnik/qvga/"
type: "slovnik"
title: "QVGA – Quarter Video Graphics Array"
date: 2025-01-01
abbr: "QVGA"
fullName: "Quarter Video Graphics Array"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qvga/"
summary: "QVGA je standardizované rozlišení videa 320x240 pixelů, definované v rámci 3GPP pro multimediální služby. Představuje běžný nízkorozlišovací formát používaný pro mobilní streamování videa, zasílání zp"
---

QVGA je standardizované rozlišení videa 3GPP o 320x240 pixelech používané pro mobilní multimediální služby, jako je streamování a konferenční hovory, které vyvažuje vizuální kvalitu s nižšími nároky na přenosovou kapacitu a zpracování.

## Popis

Quarter Video Graphics Array (QVGA) je standard rozlišení displeje určující 320 pixelů na šířku a 240 pixelů na výšku, což odpovídá poměru stran 4:3. Ve specifikacích 3GPP, zejména v TS 26.922 (Kodek pro vylepšené hlasové služby a další multimediální služby), je QVGA definováno jako podporovaný video formát pro multimediální telefonii a streamovací služby. Je základním stavebním kamenem pro profil a úroveň video kodeku, které určují maximální velikost snímku, kterou musí dekodér pro danou úroveň služby zvládnout zpracovat. Relativně nízký počet pixelů tohoto formátu snižuje výpočetní náročnost kódování a dekódování, což je klíčové pro mobilní zařízení napájená baterií.

V rámci multimediální relace 3GPP, jako je služba videotelefonie (VTS) nebo služba multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)), budou vyjednané schopnosti kodeku zahrnovat podporovaná rozlišení jako QVGA. Během navazování relace si koncové body vymění nabídku a odpověď protokolu [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol), která obsahuje seznam kodeků a jejich přidružených parametrů včetně rozlišení. Pokud oba koncové body podporují QVGA a síťové podmínky to dovolí, může být video stream navázán v tomto rozlišení. Video enkodér na vysílacím zařízení zachytí snímky, komprimuje je pomocí kodeku jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/) v rozlišení QVGA a zabalí datový tok do paketů pro přenos přes IP přenosovou vrstvu.

Úloha QVGA v síti spočívá v tom, že představuje jasně definovaný, interoperabilní bod pro kvalitu videa. Síťové prvky, jako je Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo aplikační servery, mohou překódovávat video streamy do QVGA kvůli kompatibilitě se staršími zařízeními nebo pro přizpůsobení se špatným síťovým podmínkám. V adaptivních streamovacích protokolech, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), je reprezentace v QVGA často nejnižší kvalitativní úrovní, která zajišťuje možnost základního přehrávání videa i při výrazném omezení přenosové kapacity. Jeho standardizace zajišťuje, že všechna kompatibilní zařízení mohou video v této základní kvalitě odesílat, přijímat a zobrazovat, čímž se garantuje minimální základní úroveň uživatelského zážitku v celém ekosystému.

## K čemu slouží

Rozlišení QVGA bylo v rámci 3GPP standardizováno za účelem vytvoření společného video formátu s nízkou složitostí pro rané mobilní multimediální služby. Když sítě 3G umožnily paketově přepínané datové služby, vznikla potřeba zavést video schopnosti pro telefonii, zasílání zpráv a streamování. Výpočetní výkon mobilních zařízení, dostupná výdrž baterie a omezená síťová přenosová kapacita (zejména v raných nasazeních 3G) však představovaly vážná omezení. Vysokorozlišovací formáty jako [VGA](/mobilnisite/slovnik/vga/) (640x480) nebo vyšší na tyto systémy kladly příliš vysoké nároky.

QVGA poskytlo pragmatické řešení, které nabízelo rozpoznatelnou kvalitu video obrazu při přibližně čtvrtinovém počtu pixelů oproti standardnímu VGA. To přímo vedlo k nižším datovým tokům pro přenos, což snížilo zahlcení sítě a náklady uživatelů na data, a také k menší výpočetní zátěži pro kódování a dekódování v reálném čase, čímž se šetřila výdrž baterie. Jeho poměr stran 4:3 byl v době zavedení standardem pro displeje. Standardizace tohoto rozlišení zajistila interoperabilitu mezi zařízeními a síťovým vybavením různých výrobců, zabránila fragmentaci a umožnila úspěšné zavedení služeb, jako je videohovor.

Přestože moderní chytré telefony podporují mnohem vyšší rozlišení, QVGA zůstává v rámci specifikací 3GPP relevantní z několika důvodů. Slouží jako povinná záložní úroveň pro univerzální kompatibilitu, která zajišťuje, že základní video relaci lze vždy navázat. Je také klíčové pro služby cílené na levná IoT zařízení s kamerami, pro scénáře s omezenou přenosovou kapacitou v přeplněných buňkách nebo jako nízkokvalitní vrstva ve škálovatelném kódování videa. Jeho pokračující zařazení podporuje dlouhověkost a zpětnou kompatibilitu multimediálních služeb 3GPP napříč širokým spektrem schopností zařízení.

## Klíčové vlastnosti

- Standardizované rozlišení 320x240 pixelů s poměrem stran 4:3
- Definováno jako omezení úrovně kodeku v rámci multimediálních specifikací 3GPP
- Nízké nároky na zpracování a přenosovou kapacitu vhodné pro zařízení s omezenými zdroji
- Slouží jako základní formát pro interoperabilitu video služeb
- Běžně používáno jako nejnižší kvalitativní úroveň v adaptivním streamování
- Podporováno staršími i moderními video kodeky jako H.264, H.265 a VP8

## Související pojmy

- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [QVGA na 3GPP Explorer](https://3gpp-explorer.com/glossary/qvga/)
