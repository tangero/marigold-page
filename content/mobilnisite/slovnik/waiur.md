---
slug: "waiur"
url: "/mobilnisite/slovnik/waiur/"
type: "slovnik"
title: "WAIUR – Wanted Air Interface User Rate"
date: 2025-01-01
abbr: "WAIUR"
fullName: "Wanted Air Interface User Rate"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/waiur/"
summary: "Wanted Air Interface User Rate (WAIUR) je parametr QoS, který specifikuje požadovanou datovou rychlost pro uživatelskou aplikaci přes rozhraní rádiového přenosu. Síť jej používá během zřizování nebo m"
---

WAIUR je parametr QoS (Quality of Service) definující požadovanou datovou rychlost pro uživatelskou aplikaci přes rozhraní rádiového přenosu (air interface). Síť jej používá k přidělení odpovídajících prostředků při zřizování nebo modifikaci přenosového kanálu (bearer).

## Popis

Wanted Air Interface User Rate (WAIUR) je parametr kvality služeb (QoS) definovaný ve specifikacích 3GPP pro konverzační a streamovací třídy paketově přepínaného provozu. Představuje datovou rychlost požadovanou uživatelskou aplikací pro přenos nebo příjem informací přes rozhraní rádiového přenosu (rozhraní Uu). Technicky je WAIUR signalizován během procedury aktivace [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) kontextu nebo zřizování/modifikace přenosového kanálu, typicky jako součást profilu QoS vyjednaného mezi uživatelským zařízením (UE) a sítí. Síťové elementy, včetně rádiové přístupové sítě (RAN) a jádra sítě, používají tento parametr jako vstup pro rozhodování o řízení přístupu (admission control) a přidělování prostředků.

Parametr funguje ve spojení s dalšími atributy QoS, jako je Třída provozu (Traffic Class), Maximální přenosová rychlost ([MBR](/mobilnisite/slovnik/mbr/)), Zaručená přenosová rychlost ([GBR](/mobilnisite/slovnik/gbr/)) a Přenosové zpoždění (Transfer Delay). Zatímco GBR a MBR definují závazek sítě a horní limity, WAIUR vyjadřuje preferenci nebo požadavek aplikace z pohledu uživatele. Například aplikace pro streamování videa může signalizovat WAIUR odpovídající datovému toku vybraného videostreamu. Řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo eNodeB v LTE tento parametr přijímá a používá jej spolu s aktuálním zatížením buňky a rádiovými podmínkami k rozhodnutí, zda lze zřídit rádiový přenosový kanál (radio bearer) s odpovídajícími charakteristikami. Ovlivňuje přidělování prostředků vyhrazeného kanálu, nastavení řízení výkonu a priority plánování.

WAIUR je zvláště relevantní pro služby reálného času, kde je konzistentní datová rychlost klíčová pro kvalitu. Síť nemusí být vždy schopna poskytnout přesně požadovaný WAIUR kvůli přetížení nebo politice, ale slouží jako klíčové vodítko. Zařazení parametru do signalizace QoS zajišťuje, že potřeby aplikace jsou sděleny rádiové vrstvě, což umožňuje inteligentnější a na službu zaměřené řízení prostředků. To přispívá k udržení vnímané kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) tím, že sladí poskytování síťových prostředků s požadavky aplikace.

## K čemu slouží

WAIUR byl zaveden, aby poskytl jemnější mechanismus pro předání požadavků aplikace na datovou rychlost rádiové přístupové síti, nad rámec jednoduchých minimálních/maximálních garancí. Rané paketové datové služby postrádaly standardizovaný způsob, jakým by uživatelská aplikace mohla vyjádřit svou požadovanou propustnost systémům pro správu prostředků sítě. To mohlo vést k neefektivnímu přidělování prostředků – buď k nadměrnému poskytování (plýtvání kapacitou), nebo k nedostatečnému poskytování (zhoršení uživatelského zážitku).

Parametr řeší problém asymetrických informací mezi aplikací a síťovým plánovačem (scheduler). Signalizací WAIUR aplikace informuje síť o svém ideálním provozním bodě. To umožňuje RAN činit informovanější rozhodnutí o řízení přístupu; například může odmítnout nový přenosový kanál, pokud není schopna podpořit požadovanou rychlost bez dopadu na existující relace, nebo může efektivněji plánovat prostředky, aby naplnila kolektivní WAIURy aktivních uživatelů. Jeho zavedení bylo motivováno potřebou podpory různorodých multimediálních služeb reálného času (jako videotelefonie a streamování) v sítích 3G, které mají striktní a proměnlivé požadavky na rychlost.

Jeho vytvoření řešilo omezení dřívějších, statičtějších modelů QoS. Přidalo vrstvu signalizace zaměřené na uživatele, která doplňuje parametry zaměřené na síť, jako je [GBR](/mobilnisite/slovnik/gbr/). To umožňuje lepší optimalizaci pro konverzační a streamovací služby, kde je uživatelsky vnímaná kvalita přímo svázána s udrženou datovou rychlostí. WAIUR pomáhá překlenout propast mezi požadavky aplikační vrstvy a přidělováním prostředků fyzické vrstvy, což je základní výzvou v řízení QoS v bezdrátových sítích.

## Klíčové vlastnosti

- Signalizován jako součást profilu QoS během zřizování přenosového kanálu (bearer)
- Vyjadřuje požadovanou datovou rychlost uživatelské aplikace přes rozhraní rádiového přenosu (air interface)
- Používán RAN pro řízení přístupu (admission control) a správu rádiových prostředků
- Platí primárně pro konverzační a streamovací třídy provozu
- Funguje společně se Zaručenou přenosovou rychlostí (GBR) a Maximální přenosovou rychlostí (MBR)
- Pomáhá optimalizovat uživatelský zážitek pro služby reálného času

## Definující specifikace

- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview

---

📖 **Anglický originál a plná specifikace:** [WAIUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/waiur/)
