---
slug: "hlrb"
url: "/mobilnisite/slovnik/hlrb/"
type: "slovnik"
title: "HLRB – Home Location Register of the B subscriber"
date: 2025-01-01
abbr: "HLRB"
fullName: "Home Location Register of the B subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hlrb/"
summary: "HLRB je Home Location Register (HLR), které ukládá předplatitelská data a informace o poloze pro 'B účastníka' ve volání. Jde o klíčovou síťovou entitu v GSM/UMTS sítích s přepojováním okruhů pro směr"
---

HLRB je Home Location Register, který ukládá předplatitelská data a informace o poloze pro 'B účastníka' ve volání, což umožňuje směrování, autentizaci a poskytování služeb v GSM/UMTS sítích s přepojováním okruhů.

## Popis

Home Location Register B účastníka (HLRB) je základní komponentou v doméně jádra s přepojováním okruhů systémů 2G (GSM) a 3G (UMTS) podle definice 3GPP. Nejde o samostatný fyzický uzel, ale o logické označení pro Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), které obsluhuje volanou stranu, neboli terminujícího účastníka, v telefonní relaci. HLR je centrální databáze obsahující trvalá data účastníka, včetně International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), Mobile Station International Subscriber Directory Number ([MSISDN](/mobilnisite/slovnik/msisdn/)), předplacených doplňkových služeb (jako přesměrování nebo zákaz hovorů) a autentizačních parametrů. Pro mobilní příchozí hovor se Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje HLRB, aby získal směrovací informace, konkrétně adresu MSC/VLR, která v daném okamžiku obsluhuje B účastníka. Tento proces, známý jako HLR interrogace, je klíčový pro vytvoření cesty hovoru.

Architektonicky HLRB komunikuje s několika dalšími uzly jádra sítě prostřednictvím standardizovaných signalizačních protokolů, především Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)). Klíčová rozhraní zahrnují rozhraní C a D. Rozhraní C spojuje GMSC s HLRB pro získání směrovacích informací. Rozhraní D spojuje HLRB s Visitor Location Register (VLR) asociovaným s obsluhujícím MSC; toto rozhraní se používá pro aktualizaci informací o poloze, správu dat účastníka ve VLR a řízení autentizačních procedur. Role HLRB je čistě v řídicí rovině; zpracovává signalizační zprávy pro správu mobility a logiky služeb, ale nezpracovává uživatelský hlasový ani datový provoz.

Při sestavování hovoru k mobilnímu účastníkovi odešle GMSC zdrojové sítě zprávu MAP_SEND_ROUTING_INFORMATION do HLRB. HLRB zkontroluje profil účastníka, včetně případných aktivních služeb přesměrování nebo zákazu hovorů. Pokud je hovor povolen, HLRB se dotáže aktuálního VLR (v případě potřeby přes rozhraní D), aby získal dočasné směrovací číslo zvané Mobile Station Roaming Number ([MSRN](/mobilnisite/slovnik/msrn/)). HLRB pak toto MSRN vrátí dotazujícímu se GMSC, který jej použije k směrování hovoru k obsluhujícímu MSC. Kromě směrování hovorů je HLRB zapojen do procedur, jako je aktualizace polohy (když se účastník pohybuje), správa dat účastníka a obnova dat účastníka ve VLR po výpadku. Jeho povaha centralizované databáze z něj činí kritický bod pro správu účastníků a potenciální jediný bod selhání, což vedlo k vývoji distribuovanějších architektur v pozdějších systémech.

## K čemu slouží

Koncept HLRB existuje, aby poskytl jasné logické a funkční rozlišení v rámci procedur směrování hovorů a řízení služeb v mobilních sítích s přepojováním okruhů. V jakékoli telefonní výměně existuje volající strana (A účastník) a volaná strana (B účastník). Síť potřebuje lokalizovat a směrovat hovor k B účastníkovi, jehož předplatitelská data jsou uložena v jeho určeném [HLR](/mobilnisite/slovnik/hlr/). Označení HLRB explicitně identifikuje, které HLR – to patřící B účastníkovi – musí být dotazováno, aby byly získány potřebné směrovací informace. Toto řeší základní problém lokalizace mobilního účastníka, který se může nacházet kdekoli v rámci pokrytí sítě nebo dokonce roamovat v cizí síti.

Historicky, před buněčnými sítěmi, používala pevná telefonie fyzické linky, což činilo směrování triviálním. Zavedení mobility vyžadovalo mechanismus dynamického vyhledávání. HLR jako centralizovaná databáze účastníků bylo řešením. Rozlišení mezi HLR A účastníka (které může být dotazováno pro služby odchozího volání) a HLR B účastníka (pro služby příchozího volání) poskytuje jasnost v signalizačních standardech a síťových implementacích. Řeší omezení neexistence pevného koncového bodu tím, že odděluje identitu účastníka od fyzické polohy. Procedury definované kolem HLRB zajišťují, že mobilní příchozí hovory mohou být efektivně dokončeny, což podporuje národní i mezinárodní roaming, který byl klíčovým komerčním hybatelem úspěchu GSM.

## Klíčové vlastnosti

- Ukládá trvalá data účastníka pro volanou stranu (B účastníka)
- Poskytuje směrovací informace (MSRN) GMSC pro sestavení mobilního příchozího hovoru
- Spravuje mobilitu prostřednictvím procedur aktualizace polohy s VLR
- Zpracovává autentizační a bezpečnostní informace pro účastníka
- Řídí a zřizuje doplňkové telefonní služby (např. přesměrování hovoru, zákaz)
- Komunikuje s GMSC (rozhraní C) a VLR (rozhraní D) pomocí MAP signalizace

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [HLRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/hlrb/)
