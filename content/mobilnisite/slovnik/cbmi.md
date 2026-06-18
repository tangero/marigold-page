---
slug: "cbmi"
url: "/mobilnisite/slovnik/cbmi/"
type: "slovnik"
title: "CBMI – Cell Broadcast Message Identifier"
date: 2025-01-01
abbr: "CBMI"
fullName: "Cell Broadcast Message Identifier"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbmi/"
summary: "CBMI je jedinečný identifikátor používaný k rozlišení jednotlivých zpráv služby Cell Broadcast Service (CBS) v rámci sítě 3GPP. Umožňuje síti spravovat, plánovat a doručovat vysílací zprávy, jako jsou"
---

CBMI je jedinečný identifikátor používaný k rozlišení jednotlivých zpráv služby Cell Broadcast Service v rámci sítě 3GPP pro správu a doručování vysílacích zpráv všem zařízením v určité oblasti.

## Popis

Cell Broadcast Message Identifier (CBMI) je základní parametr v architektuře služby Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)) definované standardy 3GPP. Jedná se o číselný identifikátor, který jednoznačně označuje konkrétní entitu zprávy Cell Broadcast při jejím zpracování a doručování sítí. Architektura CBS zahrnuje Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), což je síťový uzel odpovědný za příjem vysílacích zpráv od poskytovatelů informací (např. vládních agentur pro veřejná varování). CBC používá CBMI spolu s dalšími parametry, jako je obsah zprávy a geografický rozsah, k naformátování zprávy Cell Broadcast pro doručení do rádiové přístupové sítě (RAN).

Operačně je CBMI součástí dat zprávy odesílané z CBC do Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) v GSM/UMTS nebo do [eNB](/mobilnisite/slovnik/enb/)/gNB v LTE/5G prostřednictvím rozhraní CBC-RAN (např. SBc-interface). RAN používá CBMI ke správě plánu vysílání, zejména pro opakované přenosy v definovaném časovém úseku. Pomáhá RAN a uživatelskému zařízení (UE) rozlišovat mezi různými souběžnými nebo následnými vysílacími zprávami. Například různá varování pro různé události (jako AMBER alert a varování před počasím) by měla odlišná CBMI.

Uvnitř UE hraje CBMI klíčovou roli při zpracování zpráv. UE si udržuje seznam přijatých CBMI, aby se uživateli nezobrazovaly duplicitní zprávy, což zlepšuje uživatelský zážitek. Identifikátor je vysílán přes rozhraní vzduch na specifických logických kanálech – Cell Broadcast Channel ([CBCH](/mobilnisite/slovnik/cbch/)) v GSM nebo System Information Block ([SIB](/mobilnisite/slovnik/sib/)) v UMTS/LTE/5G NR. Technické specifikace, jako je 3GPP TS 23.041, definují strukturu a použití CBMI, čímž zajišťují interoperabilitu mezi síťovými prvky a zařízeními od různých výrobců. Jeho konzistentní použití je zásadní pro spolehlivé a jednoznačné doručení kritických informací masovému publiku.

## K čemu slouží

CBMI byl vytvořen k řešení potřeby robustního, síťově řízeného mechanismu pro vysílání informací všem mobilním zařízením v definované buňce nebo skupině buněk. Před standardizovaným cell broadcastem bylo hromadné oznamování obtížné a často spoléhalo na neefektivní metody, jako je odesílání jednotlivých [SMS](/mobilnisite/slovnik/sms/) zpráv, které mohly zahlcovat síť a selhávat během mimořádných událostí. Služba Cell Broadcast Service a z ní vyplývající CBMI byly navrženy tak, aby poskytly systém hromadného doručování typu jeden-všem, založený na poloze a nezávislý na zatížení jednotlivých signalizačních kanálů.

Hlavním problémem, který CBMI řeší, je jednoznačná identifikace a správa vysílacích zpráv v síti a na zařízení. Bez jedinečného identifikátoru by síť nemohla efektivně plánovat opakované přenosy a UE by neměla způsob, jak určit, zda je příchozí zpráva duplikátem již přijaté a uložené zprávy. To je obzvláště kritické pro systémy veřejného varování, kde opakovaný přenos zajišťuje příjem, ale opakované zobrazování stejného varování by bylo nežádoucí. CBMI umožňuje tuto logiku deduplikace na straně UE.

Historicky zavedený v 3GPP Release 5 jako součást vylepšeného rámce [CBS](/mobilnisite/slovnik/cbs/), byl vznik CBMI motivován rostoucím uznáním mobilních sítí jako zásadní platformy pro služby veřejné bezpečnosti a komerčního informování. Poskytl nezbytný technický základ pro služby jako Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System (CMAS), které spoléhají na přesnou identifikaci a zpracování zpráv, aby mohly efektivně fungovat v globálních sítích.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní instanci zprávy Cell Broadcast v síti
- Umožňuje uživatelskému zařízení (UE) provádět deduplikaci zpráv a zabránit zobrazování opakování
- Používá se RAN pro plánování a správu cyklů vysílání
- Integrální součást struktury zprávy odesílané z Cell Broadcast Centre (CBC) do RAN
- Vysílán přes rozhraní vzduch k UE prostřednictvím specifických systémových informací nebo kanálů pro cell broadcast
- Definován ve specifikacích 3GPP pro zajištění interoperability mezi výrobci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CBMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbmi/)
