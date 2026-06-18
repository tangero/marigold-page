---
slug: "monp"
url: "/mobilnisite/slovnik/monp/"
type: "slovnik"
title: "MONP – MC service Off-Network Protocol"
date: 2025-01-01
abbr: "MONP"
fullName: "MC service Off-Network Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/monp/"
summary: "Sada protokolů definovaná pro služby Kritických služeb (MC), jako je push-to-talk (MCPTT), umožňující přímou komunikaci mezi uživatelskými zařízeními (UE) při absenci pokrytí sítě nebo její nedostupno"
---

MONP je soubor protokolů, který umožňuje přímou komunikaci mezi zařízeními pro služby Kritické služby (Mission Critical), když je uživatelské zařízení mimo dosah pokrytí sítě.

## Popis

[MC](/mobilnisite/slovnik/mc/) service Off-Network Protocol (MONP) je komplexní soubor protokolů standardizovaný 3GPP pro umožnění služeb Kritických služeb (MC) v podmínkách mimo pokrytí sítě. Je specifikován napříč více technickými specifikacemi, včetně TS 24.281 ([MCPTT](/mobilnisite/slovnik/mcptt/) off-network), TS 24.282 (MCData off-network), TS 24.379 ([MCVideo](/mobilnisite/slovnik/mcvideo/) off-network) a souvisejících specifikací testů shody TS 36.579 a 37.579. MONP umožňuje uživatelským zařízením Kritických služeb (MC UEs) navazovat přímé komunikační spoje mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) využitím Služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)), když nejsou obsluhována 3GPP sítí (např. v odlehlých oblastech, při výpadcích sítě nebo uvnitř budov bez signálu). Protokolový zásobník funguje nad referenčním bodem PC5, což je přímé rozhraní mezi UEs definované pro ProSe. MONP zahrnuje několik vrstev a funkcí: definuje mechanismy objevování, aby se UEs vzájemně našla a vytvářela skupiny mimo síť, správu relací pro zřizování a ukončování skupinových hovorů (např. MCPTT hovorů), řízení práva mluvit (floor control) pro správu povolení k mluvení, bezpečnostní protokoly pro autentizaci a šifrování přímého spoje a protokoly mediální roviny pro přenos hlasu, dat nebo videa. Klíčovým architektonickým konceptem je Off-Network UE, které může autonomně fungovat jako klient, a v některých konfiguracích mohou určitá UEs přebírat omezené síťové role (např. pro přenos nebo správu objevování) za účelem rozšíření komunikačního dosahu nebo organizace skupiny. MONP je úzce integrován s architekturou služeb MC v síti; UE může plynule přecházet mezi režimy v síti a mimo síť na základě dostupnosti. Protokoly zajišťují, že i bez infrastruktury jsou zachovány kritické funkce jako správa skupin, tísňová volání a zabezpečení.

## K čemu slouží

MONP byl vytvořen pro splnění kritického požadavku uživatelů z oblasti veřejné bezpečnosti a profesionálů využívajících Kritické služby: spolehlivá komunikace musí být dostupná i když je mobilní síť poškozena, přetížena nebo jednoduše nepřítomna. Tradiční mobilní služby jsou zcela závislé na síťové infrastruktuře (bázové stanice, jádro sítě). V katastrofických scénářích, jako jsou zemětřesení, požáry nebo teroristické útoky, může tato infrastruktura selhat. MONP tento problém řeší standardizací přímého režimu provozu využívajícího [D2D](/mobilnisite/slovnik/d2d/) technologii. Odstraňuje omezení předchozích proprietárních řešení (jako jsou tradiční vysílačky) tím, že poskytuje standardizovaný, interoperabilní a funkčně bohatý protokol pro provoz mimo síť, který je bezproblémově integrován se širším ekosystémem služeb 3GPP Kritických služeb ([MCPTT](/mobilnisite/slovnik/mcptt/), MCData, [MCVideo](/mobilnisite/slovnik/mcvideo/)). To umožňuje přímou komunikaci mezi záchranáři z různých složek nebo používajícími zařízení od různých výrobců. Motivace vychází z poučení získaného při velkých incidentech, kdy došlo k výpadkům komunikace. Poskytnutím standardizovaného protokolu pro provoz mimo síť umožňuje 3GPP vývoj odolných UEs, které mohou pracovat jak v režimu založeném na infrastruktuře, tak v přímém režimu, čímž zajišťuje odolnost komunikace, což je nezbytný požadavek organizací veřejné bezpečnosti po celém světě.

## Klíčové vlastnosti

- Umožňuje přímou komunikaci mezi UEs přes rozhraní PC5 využitím ProSe
- Podporuje provoz mimo síť pro služby MCPTT, MCData a MCVideo
- Definuje protokoly pro objevování, vytváření skupin, správu relací a řízení práva mluvit (floor control)
- Zahrnuje bezpečnostní mechanismy pro autentizaci a šifrování v režimu mimo síť
- Umožňuje správu rolí, při které mohou UEs plnit funkce přenosu nebo omezených řídicích funkcí
- Navrženo pro plynulou kontinuitu služeb mezi scénáři v síti a mimo síť

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MONP na 3GPP Explorer](https://3gpp-explorer.com/glossary/monp/)
