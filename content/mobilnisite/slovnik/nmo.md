---
slug: "nmo"
url: "/mobilnisite/slovnik/nmo/"
type: "slovnik"
title: "NMO – Network Mode of Operation"
date: 2025-01-01
abbr: "NMO"
fullName: "Network Mode of Operation"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nmo/"
summary: "Definuje operační konfiguraci jádra mobilní sítě, zejména s ohledem na koexistenci a vzájemnou spolupráci okruhově spínané (CS) a paketově spínané (PS) domény. Určuje způsob poskytování hlasových služ"
---

NMO je operační konfigurace jádra mobilní sítě, která definuje koexistenci okruhově spínané (CS) a paketově spínané (PS) domény a určuje způsob poskytování hlasových služeb.

## Popis

Network Mode of Operation (NMO) je základní konfigurační parametr mobilní sítě, který definuje vysokou úroveň operačního paradigmatu jádrové sítě (CN) s ohledem na poskytované služby a její interakci s uživatelským zařízením (UE). Konkrétně řídí vztah a dostupnost okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) domény (pro tradiční hlas a SMS) a paketově spínané (PS) domény (pro IP datové služby) v rámci síťové infrastruktury. Nastavení NMO instruuje zařízení UE, jak se připojit k síti a s kterými doménami se registrovat, což přímo ovlivňuje dostupnost služeb a procedury předávání spojení.

Technicky je NMO vysíláno sítí v systémových informacích (např. v SIB1 v LTE) a je kritickým parametrem během procedur připojení a aktualizace sledované oblasti zařízení UE. Zařízení UE tento parametr čte a podle něj se chová. Například v síti s NMO-I provede zařízení UE kombinované připojení EPS/[IMSI](/mobilnisite/slovnik/imsi/) (Combined EPS/IMSI Attach), čímž se současně zaregistruje jak k doméně EPS (PS), tak k CS doméně. To umožňuje, aby Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) fungovala jako proxy pro CS signalizaci, a umožňuje tak funkce jako SMS přes rozhraní SGs bez nutnosti plného CS rádiového spojení. NMO určuje strategii sítě pro poskytování hlasových služeb: zda se spoléhá na starší CS doménu (přes CS Fallback nebo Single Radio Voice Call Continuity), výhradně využívá PS doménu (IMS-based VoLTE/VoNR) nebo používá kombinaci.

NMO má zásadní architektonické důsledky. Určuje, zda síť potřebuje udržovat funkční CS jádro ([MSC](/mobilnisite/slovnik/msc/)) vedle PS jádra (EPC/5GC). V módech jako NMO-II nebo [III](/mobilnisite/slovnik/iii/) může být CS doména pro určité přístupové technologie nepřítomna nebo nepodporována, což přesouvá všechny služby do PS domény a do subsystému IP multimédií (IMS). To je klíčové pro evoluci směrem k plně IP sítím. Volba NMO ovlivňuje správu mobility, strategie vyhledávání a kontinuitu služeb během předávání spojení mezi různými technologiemi rádiového přístupu (např. LTE na 2G/3G). Je to klíčové rozhodnutí pro síťové operátory migrující své hlasové služby ze starších CS na moderní VoIP řešení.

## K čemu slouží

NMO bylo zavedeno pro řízení složitého přechodu ze sítí 2G/3G, které byly postaveny na robustním okruhově spínaném jádru pro hlas, na sítě 4G LTE a novější, které jsou ze své podstaty plně paketově spínané. LTE bylo z rádiového pohledu navrženo jako technologie pouze pro data, bez nativních [CS](/mobilnisite/slovnik/cs/) přenosů. To vytvořilo výzvu pro zajištění všudypřítomné hlasové služby, která je klíčovým zdrojem příjmů a očekáváním uživatelů. Koncept NMO poskytl standardizovaný rámec pro definování způsobu, jakým síť překlene tuto mezeru během přechodného období.

Vyřešil problém kontinuity služeb a interoperability zařízení. Bez definovaného NMO by zařízení UE nevěděla, jak se chovat v prostředí smíšené sítě. NMO poskytuje zařízení UE jasnou signalizaci o tom, které služby jsou dostupné a přes kterou doménu, což zajišťuje předvídatelný uživatelský zážitek. Vyřešilo to omezení předchozích modelů „vždy zapnuté CS“ tím, že umožnilo sítím postupně vyřazovat CS jádro, nejprve jeho používáním jako záložního řešení ([CSFB](/mobilnisite/slovnik/csfb/)), poté jako signalizační proxy pro SMS a nakonec jeho úplné odstavení ve prospěch plného řešení hlasu založeného na IMS (VoLTE/VoNR).

Historicky, když operátoři nasazovali LTE, potřebovali cestu k udržení hlasové služby při budování svých IMS kapacit. NMO poskytlo plán pro tuto migraci. Například začátek s NMO-I (CSFB pro hlas) umožnil okamžité nasazení dat LTE, zatímco přechod na NMO-II/[III](/mobilnisite/slovnik/iii/) s VoLTE představoval cílovou architekturu plně IP. Tento strukturovaný přístup zabránil fragmentaci a zajistil, že zařízení od různých výrobců budou konzistentně fungovat v sítích po celém světě, což bylo zásadní pro globální přijetí LTE.

## Klíčové vlastnosti

- Definuje dostupnost a vzájemnou spolupráci CS a PS domény
- Určuje proceduru připojení zařízení UE (kombinované připojení vs. připojení pouze k EPS)
- Řídí způsob poskytování hlasové služby (CSFB, VoLTE, VoNR)
- Ovlivňuje mechanismus doručování SMS (přes SGs, přes IMS)
- Ovlivňuje síťovou architekturu a požadavky na prvky jádra
- Řídí chování mobility a předávání spojení mezi LTE a 2G/3G

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems

---

📖 **Anglický originál a plná specifikace:** [NMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmo/)
