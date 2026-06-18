---
slug: "oacs"
url: "/mobilnisite/slovnik/oacs/"
type: "slovnik"
title: "OACS – Optimised Active Codec Set"
date: 2025-01-01
abbr: "OACS"
fullName: "Optimised Active Codec Set"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/oacs/"
summary: "Koncept správy v rámci samořídících sítí (SON), který definuje optimalizovanou podmnožinu audio kodeků aktivně využívaných v síťové oblasti. Cílem je snížit provozní složitost, zlepšit konzistenci hla"
---

OACS je koncept správy samořídících sítí (SON), který definuje optimalizovanou podmnožinu audio kodeků pro síťovou oblast za účelem snížení složitosti, zlepšení konzistence hlasové kvality a zefektivnění správy konfigurace.

## Popis

Optimised Active Codec Set (OACS) je princip v rámci architektury samořídících sítí ([SON](/mobilnisite/slovnik/son/)) konsorcia 3GPP, konkrétně v aspektech provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)). Řeší provozní výzvu spojenou se správou potenciálně rozsáhlé a různorodé sady řečových a audio kodeků podporovaných uživatelským zařízením (UE) a sítí. OACS představuje cíleně sestavený, minimalizovaný seznam kodeků, které síťový operátor aktivně povoluje a preferuje pro použití v konkrétní geografické oblasti nebo síťovém řezu. Cílem je přejít ze stavu, kdy jsou teoreticky dostupné všechny podporované kodeky, na řízený stav s menší, optimalizovanou sadou.

Implementace OACS vyžaduje koordinaci mezi systémem OAM, jádrem sítě (např. funkcí pravidel pro účtování a správu politik – [PCRF](/mobilnisite/slovnik/pcrf/), nebo uzly řízení hovorů) a rádiovou přístupovou sítí. Systém OAM využívá vstupy z dat správy výkonu ([PM](/mobilnisite/slovnik/pm/)) a správy poruch ([FM](/mobilnisite/slovnik/fm/)) k určení optimální sady kodeků na základě kritérií, jako jsou metriky hlasové kvality (např. střední známka kvality – [MOS](/mobilnisite/slovnik/mos/)), kapacita sítě, schopnosti UE a požadavky na interoperabilitu. Tato optimalizovaná sada je následně nakonfigurována do příslušných síťových uzlů. Během sestavování hovoru uzly jako [MSC](/mobilnisite/slovnik/msc/) Server (pro okruhově spínané hovory) nebo [P-CSCF](/mobilnisite/slovnik/p-cscf/)/Interrogating-CSCF (pro IMS hovory) používají OACS k usměrnění vyjednávání kodeků a upřednostňují kodeky z této sady.

Tento proces redukuje 'kodekovou džungli', kde mnohonásobné pokusy o vyjednání kodeku mohou vést k prodlevám při sestavování hovoru, k volbě suboptimální hlasové kvality nebo k problémům s interoperabilitou. Definováním OACS mohou operátoři zajistit konzistentnější a kvalitnější hlasový uživatelský zážitek, zjednodušit odstraňování problémů a snížit zátěž spojenou s testováním a validací rozsáhlého portfolia kodeků. Jde o klíčový prvek pro efektivní provoz sítě a je úzce spojen s dalšími případy užití SON, jako je optimalizace robustnosti mobility (MRO) a správa úspory energie (ESM), protože volba kodeku může ovlivnit úspěšnost předání hovoru a efektivitu využití rádiových prostředků.

## K čemu slouží

OACS byl zaveden k řešení provozních a kvalitativních problémů pramenících z množství hlasových kodeků v sítích 3GPP. Jak se sítě vyvíjely od GSM (s hlavně FR, EFR, AMR) přes UMTS a LTE (přidávající AMR-WB, EVS a další) až po nástup VoLTE a VoNR, počet možných kombinací kodeků explodoval. To vytvořilo 'bludiště vyjednávání kodeků', kde sestavení hovoru mohlo zahrnovat více kol nabídek a odpovědí, což zvyšovalo latenci. Navíc některé kodeky, byť efektivní, nemusely poskytovat nejlepší kvalitu za určitých rádiových podmínek, což vedlo k nekonzistentnímu uživatelskému zážitku.

Tradiční přístup podpory všech kodeků, které UE zvládá, byl provozně náročný, vyžadoval rozsáhlé testování a složitou správu konfigurace. OACS poskytuje rámec pro daty řízený, optimalizovaný přístup. Umožňuje operátorům analyzovat data o výkonu sítě a identifikovat, které kodeky skutečně poskytují nejlepší kvalitu a efektivitu v jejich konkrétním síťovém prostředí a pro jejich specifický mix UE. Aktivní správou a redukcí aktivní sady kodeků mohou operátoři zlepšit celkovou spolehlivost hlasových služeb, snížit dobu sestavování hovorů a soustředit optimalizační úsilí na menší sadu kodeků, což vede k předvídatelnějšímu chování sítě a zjednodušené správě poruch.

## Klíčové vlastnosti

- Definuje řízenou podmnožinu kodeků aktivně prosazovaných pro použití v síťové oblasti, na rozdíl od všech podporovaných kodeků.
- Je řízen analýzou systému OAM založenou na výkonnostních metrikách, jako je hlasová kvalita, míra úspěšnosti a hlášení schopností UE.
- Cílí na snížení složitosti a latence při sestavování hovoru zefektivněním procedury vyjednávání kodeků.
- Zlepšuje konzistenci uživatelského zážitku z hlasové kvality upřednostňováním prověřených, vysoce výkonných kodeků pro místní podmínky.
- Snižuje provozní náročnost testování, konfigurace a odstraňování problémů hlasových služeb.
- Integruje se s širšími architekturami SON pro automatizovanou nebo částečně automatizovanou optimalizaci síťových parametrů.

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [OACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/oacs/)
