---
slug: "cprach"
url: "/mobilnisite/slovnik/cprach/"
type: "slovnik"
title: "CPRACH – Compact Packet Random Access Channel"
date: 2025-01-01
abbr: "CPRACH"
fullName: "Compact Packet Random Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cprach/"
summary: "CPRACH je specializovaný kanál pro náhodný přístup navržený pro GSM/EDGE Radio Access Network (GERAN) za účelem efektivního zpracování přenosů paketových dat. Umožňuje mobilním zařízením vyžádat si up"
---

CPRACH je specializovaný GERAN kanál pro náhodný přístup, který efektivně zpracovává paketová data tím, že umožňuje zařízením vyžádat si uplinkové zdroje s minimální signalizační režií.

## Popis

Compact Packet Random Access Channel (CPRACH) je klíčová komponenta architektury GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), která zajišťuje efektivní procedury náhodného přístupu specificky optimalizované pro služby paketových dat. Na rozdíl od tradičních kanálů pro náhodný přístup navržených primárně pro přepojování okruhů hlasových hovorů je CPRACH konstruován tak, aby zvládal trhavý charakter přenosů paketových dat při zachování zpětné kompatibility se stávající GSM infrastrukturou. Funguje v rámci GERAN packet control unit ([PCU](/mobilnisite/slovnik/pcu/)) a komunikuje s řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) za účelem řízení žádostí o uplinkové zdroje z mobilních stanic ([MS](/mobilnisite/slovnik/ms/)).

Architektonicky je CPRACH implementován jako logický kanál, který sdílí fyzické zdroje se stávajícími GSM kanály, ale využívá odlišné signalizační procedury optimalizované pro paketová data. Když mobilní zařízení potřebuje vyslat paketová data, odešle CPRACH burst obsahující specifické informační elementy identifikující typ žádosti o přístup a požadované zdroje. Tento burst je přenášen na určených časových slotů a frekvencích, které síť pro činnost CPRACH vyhradila. Kanál používá konkurující přístupový mechanismus, kdy více zařízení může o přístup usilovat současně, což vyžaduje protokoly pro detekci a řešení kolizí.

Procedura CPRACH zahrnuje několik klíčových komponent: packet control unit mobilní stanice, přijímací řetězec základnové stanice ([BTS](/mobilnisite/slovnik/bts/)) a funkce paketového řízení v BSC. Když má mobilní stanice paketová data k odeslání, nejprve naslouchá vysílaným systémovým informacím, aby určila parametry CPRACH včetně dostupných časových slotů, frekvencí a úrovní vytrvalosti přístupu. Zařízení pak vybere náhodnou příležitost pro přístup a vysílá CPRACH burst obsahující svou dočasnou logickou spojovací identitu ([TLLI](/mobilnisite/slovnik/tlli/)) a povahu požadovaného přístupu (přidělení na jeden blok nebo více bloků). BTS tento burst přijme, demoduluje jej a přepošle žádost o přístup k BSC prostřednictvím rozhraní PCU.

Provoz CPRACH je úzce integrován s GERAN paketovým datovým protokolovým zásobníkem, zejména s vrstvou řízení rádiového spoje a řízení přístupu k médiu ([RLC](/mobilnisite/slovnik/rlc/)/MAC). Po úspěšném přijetí CPRACH burst síť odpovídá zprávou okamžitého přidělení na přidruženém řídicím kanálu pro paketový přenos (PACCH), která přiděluje konkrétní uplinkové zdroje na kanálu pro přenos paketových dat (PDTCH). Tato dvoufázová přístupová procedura – náhodný přístup následovaný vyhrazeným přidělením zdrojů – optimalizuje využití zdrojů při zachování rychlého přístupu pro uživatele paketových dat. Kanál podporuje různé třídy přístupové služby, které umožňují operátorům upřednostňovat určité typy provozu nebo uživatelů.

Z pohledu sítě umožňuje CPRACH efektivní statistické multiplexování uživatelů paketových dat na sdílených rádiových zdrojích. Síťoví operátoři mohou nakonfigurovat více instancí CPRACH napříč různými kmitočty nosných a kombinacemi časových slotů, aby vyrovnali zatížení a minimalizovali kolize přístupu. Kanál obsahuje sofistikované mechanismy řízení výkonu, kde počáteční vysílací výkon pro CPRACH bursty je určen na základě naměřené síly signálu v downlinku, čímž se snižuje interference a zvyšuje celková kapacita systému. CPRACH navíc podporuje jednofázové i dvoufázové přístupové procedury v závislosti na množství dat k přenosu a konfiguraci sítě.

## K čemu slouží

CPRACH byl vyvinut za účelem řešení základního nesouladu mezi tradičními procedurami náhodného přístupu GSM – optimalizovanými pro okruhově orientované hlasové hovory – a požadavky vznikajících služeb paketových dat v sítích 2.5G. Před zavedením CPRACH používaly GSM sítě pro všechny pokusy o přístup kanál náhodného přístupu (RACH), který byl pro paketová data neefektivní kvůli nadměrné signalizační režii a nevhodnému přidělování zdrojů pro trhavý charakter provozu. Procedura RACH vyžadovala zřízení vyhrazeného signalizačního spojení i pro malé datové pakety, což vedlo ke špatné spektrální efektivitě a zvýšené latenci pro paketové služby jako GPRS a EDGE.

Primární motivací pro vytvoření CPRACH bylo umožnit efektivní statistické multiplexování uživatelů paketových dat při zachování zpětné kompatibility se stávající GSM infrastrukturou. Když začala počátkem roku 2000 narůstat spotřeba mobilních dat, potřebovali síťoví operátoři mechanismus, který by zvládal časté, krátké datové přenosy od více uživatelů bez spotřeby nadměrných signalizačních zdrojů. CPRACH to vyřešil zavedením zjednodušené přístupové procedury specificky navržené pro paketová data, která ve srovnání s tradičními procedurami založenými na RACH snižuje počet signalizačních zpráv potřebných k navázání přenosu dat.

CPRACH také řešil kapacitní omezení v raných nasazeních GPRS, kde uživatelé paketových dat soupeřili s hlasovými uživateli o příležitosti k náhodnému přístupu. Vytvořením odděleného, optimalizovaného kanálu pro paketový přístup mohli síťoví operátoři lépe řídit diferenciaci kvality služby mezi hlasovými a datovými službami. Kompaktní signalizační formát CPRACH burstů umožnil efektivnější využití rádiových zdrojů, podporující vyšší počty současných uživatelů paketových dat a současně snížení pravděpodobnosti kolizí při přístupu prostřednictvím optimalizovaných vytrvalostních algoritmů a omezení přístupových tříd.

## Klíčové vlastnosti

- Optimalizace pro trhavé přenosy paketových dat
- Snížení signalizační režie ve srovnání s tradičním RACH
- Konkurující přístup s řešením kolizí
- Podpora různých tříd přístupové služby
- Těsná integrace s GERAN vrstvou RLC/MAC
- Zpětná kompatibilita se stávající GSM infrastrukturou

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [CPRACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cprach/)
