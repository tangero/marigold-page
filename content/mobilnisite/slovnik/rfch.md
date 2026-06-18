---
slug: "rfch"
url: "/mobilnisite/slovnik/rfch/"
type: "slovnik"
title: "RFCH – Radio Frequency Channel"
date: 2025-01-01
abbr: "RFCH"
fullName: "Radio Frequency Channel"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rfch/"
summary: "Konkrétní, souvislá část rádiového spektra definovaná střední frekvencí a šířkou pásma, používaná pro komunikaci mezi vysílačem a přijímačem. Je to základní fyzický zdroj, přes který jsou v celulárníc"
---

RFCH je základní fyzický zdroj v celulárních sítích, definovaný jako souvislá část rádiového spektra s konkrétní střední frekvencí a šířkou pásma, přes kterou jsou přenášena všechna bezdrátová data a signalizace.

## Popis

Rádiový frekvenční kanál (Radio Frequency Channel – RFCH) je klíčový koncept v bezdrátových komunikacích, který představuje definovaný výřez elektromagnetického spektra používaný pro přenos a příjem informací. V systémech 3GPP je RFCH charakterizován svou střední frekvencí (měřenou v Hz, např. 2140 MHz) a svou šířkou pásma (rozsahem frekvencí, které zabírá, např. 5 MHz, 20 MHz nebo 100 MHz). Tento kanál je fyzickým médiem, na kterém fungují protokoly rádiového rozhraní. Celé dostupné spektrum pro mobilní síť je rozděleno na více RFCH, které mohou být přiděleny různým buňkám, nosným nebo technologiím (např. GSM, UMTS, LTE, NR).

Technicky slouží RFCH jako základ pro fyzickou vrstvu (Layer 1). Přenášená digitální data jsou modulována na rádiovou nosnou vlnu se středem uvnitř kanálu. Šířka pásma kanálu přímo určuje maximální potenciální datový tok podle Shannonovy věty. Specifikace 3GPP definují schémata číslování kanálů (např. [ARFCN](/mobilnisite/slovnik/arfcn/) pro GSM, [UARFCN](/mobilnisite/slovnik/uarfcn/) pro [UTRA](/mobilnisite/slovnik/utra/), [EARFCN](/mobilnisite/slovnik/earfcn/) pro [E-UTRA](/mobilnisite/slovnik/e-utra/), [NR-ARFCN](/mobilnisite/slovnik/nr-arfcn/) pro NR), která poskytují standardizovaný způsob odkazování na konkrétní RFCH bez uvádění absolutních frekvencí. Tato čísla se používají při plánování sítě, konfiguraci zařízení a v signalizačních zprávách (jako jsou hlášení měření).

Z pohledu provozu sítě je správa RFCH klíčová. Základnová stanice (např. Node B, eNodeB nebo gNB) používá jeden nebo více RFCH ke komunikaci s uživatelským zařízením (UE). V technologiích podporujících agregaci nosných může UE současně přijímat data na více RFCH, čímž se zvýší propustnost. Proces, při kterém UE vyhledává, synchronizuje se a měří kvalitu signálu RFCH, je zásadní pro výběr buňky, její převýběr a předávání spojení. Parametry RFCH, jako je vysílací výkon a povolené emisní masky, jsou přísně regulovány národními úřady, aby se zabránilo interferencím mezi sousedními kanály a různými operátory.

## K čemu slouží

Koncept rádiového frekvenčního kanálu existuje proto, aby umožnil uspořádané a efektivní využití vzácného zdroje, kterým je rádiové spektrum. Bez rozdělení na kanály by se přenosy chaoticky rušily. Rozdělením spektra na definované kanály může více komunikací probíhat současně v různých geografických oblastech nebo v různých časech (prostřednictvím plánování) bez vzájemného rušení. To je základ pro mnohonásobný přístup s dělením kmitočtu ([FDMA](/mobilnisite/slovnik/fdma/)). RFCH poskytuje standardizovaný 'přenosový kanál' pro komunikaci, což umožňuje inženýrům navrhovat vysílače, přijímače a protokoly se známými charakteristikami.

Ve vývoji celulárních standardů se definice a flexibilita RFCH výrazně posunuly. Rané systémy 1G používaly široké analogové kanály. GSM zavedlo digitální modulaci a přesnější definice kanálů (200 kHz). 3G UMTS standardizovalo šířku pásma kanálu 5 MHz pro své rozhraní [WCDMA](/mobilnisite/slovnik/wcdma/). 4G LTE zavedlo škálovatelné šířky pásma od 1,4 MHz do 20 MHz a 5G NR to dále rozšířilo, podporujíc flexibilní šířky kanálů až do 400 MHz v pásmu FR2 a ještě širší prostřednictvím agregace nosných. Každý pokrok umožnil vyšší datové toky a efektivnější využití spektra.

RFCH je také ústřední pro plánování a optimalizaci sítě. Operátoři nakupují licence pro konkrétní bloky RFCH. Poté musí naplánovat rozmístění své sítě (umístění buněk) a nakonfigurovat úrovně výkonu tak, aby zajistili pokrytí a zároveň minimalizovali interference mezi buňkami používajícími stejný kanál (interference na stejném kanálu). Jasná definice RFCH ve specifikacích 3GPP zajišťuje, že zařízení od různých výrobců mohou spolupracovat, protože sdílejí společnou představu o základním fyzickém zdroji, který používají ke komunikaci.

## Klíčové vlastnosti

- Definován konkrétní střední frekvencí a šířkou pásma
- Představuje základní fyzický zdroj pro rádiový přenos
- Odkazování prostřednictvím standardizovaných čísel kanálů (např. EARFCN, NR-ARFCN)
- Šířka pásma určuje maximální teoretickou datovou kapacitu
- Podléhá regulačním licenčním a emisním pravidlům
- Slouží jako základ pro procedury vyhledávání buňky, měření a předávání spojení

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RFCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfch/)
