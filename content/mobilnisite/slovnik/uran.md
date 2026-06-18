---
slug: "uran"
url: "/mobilnisite/slovnik/uran/"
type: "slovnik"
title: "URAN – UMTS Radio Access Network"
date: 2025-01-01
abbr: "URAN"
fullName: "UMTS Radio Access Network"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uran/"
summary: "Kolektivní označení pro infrastrukturu rádiové přístupové sítě v systému UMTS (3G). Zahrnuje základnové stanice Node B a řadiče rádiové sítě (RNC), které spravují rádiové zdroje a zajišťují konektivit"
---

URAN je rádiová přístupová síť UMTS zahrnující základnové stanice Node B a řadiče rádiové sítě (RNC), které spravují rádiové zdroje a spojují uživatelské zařízení s jádrem sítě.

## Popis

UMTS Radio Access Network (URAN) je kompletní architektura rádiové přístupové sítě definovaná pro sítě Universal Mobile Telecommunications System (UMTS) konsorcia 3rd Generation Partnership Project (3GPP). Představuje vývoj z rádiové přístupové sítě GSM/[EDGE](/mobilnisite/slovnik/edge/) ([GERAN](/mobilnisite/slovnik/geran/)) systémů 2G. URAN je zodpovědná za všechny rádiové funkce mezi uživatelským zařízením (UE) a jádrem sítě (CN), včetně správy rádiových zdrojů, správy mobility a šifrování přes rozhraní vzduchu. Architektonicky je URAN hierarchická síť postavená na dvou hlavních typech uzlů: Node B (základnová stanice) a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)).

URAN funguje tak, že Node B zajišťuje zpracování fyzické vrstvy (modulace, kódování, rozprostření spektra) a vysílání/příjem rádiových signálů přes rozhraní Uu ([WCDMA](/mobilnisite/slovnik/wcdma/) rozhraní vzduchu). Více Node B je připojeno a řízeno jedním RNC přes rozhraní Iub, které v raných verzích používalo protokolový zásobník [ATM](/mobilnisite/slovnik/atm/) (Asynchronous Transfer Mode), s přenosem přes IP zavedeným později. RNC je inteligentní řadič URAN; provádí klíčové funkce jako řízení přijetí hovoru, rozhodování a provedení předání hovoru, řízení výkonu, plánování paketů a šifrování/dešifrování uživatelských dat. RNC se připojuje k jádru sítě s přepojováním okruhů ([MSC](/mobilnisite/slovnik/msc/)) přes rozhraní Iu-CS a k jádru sítě s přepojováním paketů ([SGSN](/mobilnisite/slovnik/sgsn/)) přes rozhraní Iu-PS.

Klíčové protokoly v rámci URAN zahrnují protokol Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), který spravuje spojení mezi UE a URAN, a Node B Application Part (NBAP) pro signalizaci na Iub. Pro uživatelská data vrstvy Packet Data Convergence Protocol (PDCP), Radio Link Control (RLC) a Medium Access Control (MAC) fungují jak v UE, tak v RNC. Charakteristickým rysem URAN je koncept subsystému rádiové sítě (RNS), který se skládá z jednoho RNC a všech Node B k němu připojených. Více RNS může být vzájemně propojeno přes rozhraní Iur, což umožňuje měkké předání hovoru – plynulé předání, kde je UE současně připojeno k více Node B – což je charakteristický znak UMTS založeného na WCDMA.

Role URAN v celkové síti je poskytovat robustní, efektivní a vysokokapacitní rádiový spoj pro hlasové a datové služby. Ve srovnání se sítěmi 2G zavedla podporu vyšších datových rychlostí (až 2 Mbps v raných verzích), umožněnou šířkou pásma nosné WCDMA 5 MHz a pokročilými kódovacími schématy. Centralizovaná architektura URAN s RNC umožnila sofistikovanou správu rádiových zdrojů, ale také přinesla složitost a potenciální úzká místa, což později ovlivnilo přechod k plošší architektuře v E-UTRAN sítě LTE.

## K čemu slouží

URAN byla vytvořena jako součást standardu UMTS, aby naplnila vizi Mezinárodní telekomunikační unie (ITU) pro 3G/IMT-2000, která ve srovnání se systémy 2G jako GSM vyžadovala vyšší datové rychlosti, lepší spektrální účinnost a podporu multimediálních služeb. Stávající GERAN byl limitován svým úzkopásmovým rozhraním vzduchu TDMA/FDMA a nemohl efektivně podporovat širokopásmové, paketově orientované služby plánované pro 3G. URAN s rozhraním vzduchu WCDMA byla navržena tak, aby poskytla potřebnou kapacitu a flexibilitu.

Hlavním problémem, který URAN řešila, bylo umožnění skutečného mobilního širokopásmového přístupu. Zavedla od základu optimalizovanou paketovou rádiovou přístupovou síť, vedle schopností s přepojováním okruhů pro hlas. Hierarchická architektura RNC-Node B byla zvolena pro centralizaci složitých řídicích funkcí, jako je měkké předání hovoru a makro-diverzitní kombinování, které jsou vlastní charakteristikám "dýchání" buněk WCDMA a jsou výpočetně náročné. Tato centralizovaná inteligence umožnila efektivní správu rušení a vynucování kvality služeb (QoS) napříč více buňkami.

Historicky URAN představovala významný posun v filozofii návrhu sítí a byl to velký krok směrem k plně IP síti. Položila základy mnoha konceptů, které se později staly ústředními pro 4G a 5G, jako je diferencovaná QoS a efektivní plánování paketů. Jejím účelem však také byla zpětná kompatibilita a hladká spolupráce se stávajícími sítěmi 2G GERAN, což zajišťovalo kontinuitu služeb pro operátory přecházející z GSM. Omezení centralizované architektury URAN, zejména v latenci a nákladech na datový provoz s vysokým objemem, později motivovaly vývoj plošší architektury E-UTRAN v LTE.

## Klíčové vlastnosti

- Hierarchická architektura s uzly Node B (základnová stanice) a Radio Network Controller (RNC)
- Používá širokopásmový přístup s kódovým dělením (WCDMA) s šířkou pásma nosné 5 MHz
- Podporuje měkké a měkčí předání hovoru přes rozhraní Iur pro plynulou mobilitu
- Centralizovaná správa rádiových zdrojů a mobility na RNC
- Poskytuje jak konektivitu s přepojováním okruhů (Iu-CS), tak s přepojováním paketů (Iu-PS) k jádru sítě
- Umožňuje evoluci vysokorychlostního paketového přístupu (HSPA) pro zvýšené datové rychlosti

## Související pojmy

- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS

---

📖 **Anglický originál a plná specifikace:** [URAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/uran/)
