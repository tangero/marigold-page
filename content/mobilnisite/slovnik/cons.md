---
slug: "cons"
url: "/mobilnisite/slovnik/cons/"
type: "slovnik"
title: "CONS – Connection-Oriented Network Service"
date: 2025-01-01
abbr: "CONS"
fullName: "Connection-Oriented Network Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cons/"
summary: "CONS je okruhově přepínaná síťová služba definovaná v 3GPP pro vytváření vyhrazených, spolehlivých spojení mezi koncovými body. Poskytuje garantovanou šířku pásma, nízkou latenci a sekvenční doručován"
---

CONS je okruhově přepínaná síťová služba definovaná 3GPP, která vytváří vyhrazená spojení za účelem poskytnutí garantované šířky pásma, nízké latence a spolehlivého sekvenčního doručování dat.

## Popis

Connection-Oriented Network Service (CONS) je základní model síťové služby definovaný ve standardech 3GPP, který před zahájením přenosu dat vytváří vyhrazenou komunikační cestu mezi dvěma koncovými body. Tato služba funguje na architektuře s okruhovým přepínáním, kde jsou síťové prostředky po dobu trvání spojení rezervovány výhradně, což zajišťuje předvídatelné výkonnostní charakteristiky. Služba sleduje třífázový proces: navázání spojení, přenos dat a ukončení spojení, přičemž každá fáze zahrnuje specifické signalizační protokoly pro správu životního cyklu okruhu.

Z architektonického hlediska CONS funguje v rámci okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) domény mobilních sítí, rozhraní má jak s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro řízení hovorů, tak s Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)) pro správu rádiových prostředků. Služba využívá principy časového multiplexu (TDM) k přidělení pevných časových slotů pro každé spojení, čímž vytváří virtuální okruhy, které udržují konzistentní časové vztahy mezi přenášenými datovými jednotkami. Tento deterministický přístup se ostře liší od paketově přepínaných služeb, které sdílejí síťové prostředky statisticky mezi více uživateli.

Klíčové součásti implementace CONS zahrnují signalizační protokolový zásobník Signaling System No. 7 (SS7) pro signalizaci řízení hovorů, rozhraní A mezi BSS a MSC pro správu okruhů a rozhraní E mezi MSC pro mezisystémová spojení. Služba používá signalizaci asociovanou s kanálem, kde řídicí informace putují spolu s uživatelskými daty v rámci stejného fyzického okruhu, ačkoli existují i varianty s signalizací po společném kanálu. CONS poskytuje několik servisních primitiv, včetně žádosti o spojení, potvrzení spojení, přenosu dat a žádosti o odpojení, které aplikace využívají ke správě komunikačních relací.

Při provozu CONS navazuje spojení prostřednictvím procesu nazývaného sestavení hovoru, který zahrnuje překlad adres, přidělení prostředků a ověření cesty od konce ke konci, než může protékat jakákoli uživatelská data. Po navázání si spojení udržuje charakteristiky konstantní přenosové rychlosti s minimálním chvěním a garantovaným sekvenčním doručováním informačních jednotek. To činí CONS zvláště vhodnou pro izochronní aplikace, jako je hlasová telefonie, kde musí být zachovány časové vztahy mezi po sobě následujícími vzorky řeči. Služba zahrnuje mechanismy pro detekci a opravu chyb, ačkoli jsou tyto ve srovnání s paketově orientovanými službami obvykle omezené kvůli časovým omezením aplikací s okruhovým přepínáním.

## K čemu slouží

CONS byl vyvinut za účelem poskytování spolehlivých, předvídatelných komunikačních služeb pro rané systémy mobilní telefonie a řešil základní požadavek na přenos hlasu v reálném čase se zaručenou kvalitou. Před rozšířeným přijetím paketově přepínaných sítí představovaly služby s okruhovým přepínáním jedinou praktickou metodu pro poskytování hlasových komunikací s přijatelnou latencí a spolehlivostí. Tato technologie vyřešila problém, jak efektivně multiplexovat více současných konverzací v omezeném rádiovém spektru při zachování kontinuálních časových vztahů nezbytných pro srozumitelnou reprodukci řeči.

Historicky se CONS vyvinul z principů pevné telefonie přizpůsobených pro mobilní prostředí a navázal na desetiletí zkušeností s okruhovým přepínáním z veřejné telefonní sítě (PSTN). Rané mobilní systémy, jako je GSM, vyžadovaly model služby, který by mohl bezproblémově spolupracovat s existujícími telefonními sítěmi a zároveň akceptovat jedinečné výzvy bezdrátového přenosu, jako je předávání hovorů mezi buňkami a proměnlivá kvalita signálu. CONS poskytl tento most implementací kompatibilních signalizačních protokolů a charakteristik služeb, které umožnily mobilním účastníkům transparentně se připojovat k uživatelům pevných linek.

Vytvoření CONS řešilo několik konkrétních omezení dřívějších přístupů k mobilní komunikaci, včetně nedostatku standardizovaného propojení mezi různými síťovými operátory a neschopnosti garantovat kvalitu služby během událostí mobility. Stanovením formalizovaných postupů pro navázání, udržování a ukončení spojení CONS umožnil vývoj komerčně životaschopných celulárních sítí s předvídatelnými fakturačními modely založenými na délce trvání spojení spíše než na objemu dat. Tento model služby podpořil rychlé celosvětové přijetí mobilní telefonie v průběhu 90. let a počátku 21. století, než byl postupně nahrazen technologiemi Voice over IP (VoIP) v pozdějších vydáních 3GPP.

## Klíčové vlastnosti

- Garantované přidělení šířky pásma prostřednictvím vytvoření vyhrazeného okruhu
- Služba s konstantní přenosovou rychlostí a minimálním chvěním pro aplikace v reálném čase
- Sekvenční doručování všech datových jednotek v pořadí bez přerovnání paketů
- Třífázový životní cyklus spojení (sestavení, přenos, ukončení) s explicitní signalizací
- Interoperabilita se staršími PSTN sítěmi prostřednictvím standardizovaných rozhraní
- Podpora doplňkových služeb, jako je čekání na hovor, přesměrování a konferenční hovory

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [CONS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cons/)
