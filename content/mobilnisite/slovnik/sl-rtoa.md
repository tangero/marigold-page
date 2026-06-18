---
slug: "sl-rtoa"
url: "/mobilnisite/slovnik/sl-rtoa/"
type: "slovnik"
title: "SL-RTOA – Sidelink Relative Time of Arrival"
date: 2025-01-01
abbr: "SL-RTOA"
fullName: "Sidelink Relative Time of Arrival"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sl-rtoa/"
summary: "Metoda pozicování pro přímou komunikaci mezi zařízeními. Měří časový rozdíl příchodu mezi referenčním signálem z referenčního uživatelského terminálu (UE) a cílovým uživatelským terminálem. To umožňuj"
---

SL-RTOA je metoda pozicování v postranním spoji (sidelink), která měří časový rozdíl příchodu referenčních signálů mezi zařízeními, aby umožnila relativní pozicování mezi uživatelskými terminály (UE) bez síťové infrastruktury.

## Popis

Sidelink Relative Time of Arrival (SL-RTOA) je pozicovací technika definovaná v rámci standardů 3GPP pro New Radio (NR) a LTE komunikaci v postranním spoji (sidelink). Funguje v rámci rozhraní PC5, což je přímý komunikační spoj mezi uživatelskými terminály (UE). Metoda je v zásadě technikou časového rozdílu příchodu (TDOA) aplikovanou v doméně postranního spoje. Vyžaduje účast nejméně tří UE: referenčního UE, cílového UE, jehož poloha má být určena vůči referenčnímu, a jednoho nebo více pomocných UE. Referenční UE vysílá přes postranní spoj pozicovací referenční signál ([PRS](/mobilnisite/slovnik/prs/)). Tento signál přijímá jak cílové UE, tak pomocné UE a měří jeho čas příchodu. Cílové UE také vysílá vlastní PRS, který přijímají a měří pomocná UE. Základním měřením je rozdíl mezi časem, kdy pomocné UE přijme PRS od cílového UE, a časem, kdy přijme PRS od referenčního UE. Tento časový rozdíl, změřený více pomocnými UE na známých relativních pozicích, umožňuje výpočet polohy cílového UE vůči referenčnímu UE pomocí hyperbolické multilaterace. Architektura zahrnuje specifické signály fyzické vrstvy ([SL-PRS](/mobilnisite/slovnik/sl-prs/)) definované v příslušných specifikacích, měřicí postupy řízené protokolovým zásobníkem UE (vrstvami [RRC](/mobilnisite/slovnik/rrc/) a [MAC](/mobilnisite/slovnik/mac/)) a mechanismy hlášení buď funkci správy polohy v síti, nebo pro přímé použití v peer-to-peer aplikacích. Jejím úkolem je poskytnout základní, na infrastruktuře nezávislou schopnost relativního pozicování pro pokročilé služby [V2X](/mobilnisite/slovnik/v2x/), veřejné bezpečnosti a komerční komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)).

## K čemu slouží

SL-RTOA byl zaveden, aby řešil rostoucí potřebu přesného relativního pozicování ve scénářích, kde je absolutní globální pozicování (např. [GNSS](/mobilnisite/slovnik/gnss/)) nedostupné, nespolehlivé nebo nedostatečně přesné. Aplikace jako jízda v koloně (platooning), kooperativní prevence kolizí nebo hry s rozšířenou realitou vyžadují, aby zařízení znala svou vzájemnou polohu s přesností na úrovni centimetrů až decimetrů, často v prostředích bez GNSS signálu, jako jsou tunely, městské zástavby (urban canyons) nebo vnitřní prostory. Tradiční síťové metody pozicování, jako je [UTDOA](/mobilnisite/slovnik/utdoa/) nebo E-CID, spoléhají na buněčnou infrastrukturu, která nemusí být přítomna nebo může zavádět latenci nevhodnou pro bezpečnostně kritickou přímou komunikaci. SL-RTOA využívá samotný existující komunikační spoj postranního spoje k provádění pozicování, čímž vytváří samostatný systém relativního pozicování ve skupině zařízení. Tím řeší problém umožnění vysoce přesné lokalizace s nízkou latencí čistě prostřednictvím technologie komunikace mezi zařízeními, což je klíčový předpoklad pro autonomní koordinaci a zvýšené povědomí o situaci v rámci V2X a služeb blízkosti (ProSe) založených na 3GPP.

## Klíčové vlastnosti

- Umožňuje relativní pozicování mezi UE nezávislé na infrastruktuře
- Využívá pozicovací referenční signály postranního spoje (SL-PRS) pro přesná časová měření
- Založeno na principech časového rozdílu příchodu (TDOA) na rozhraní PC5
- Podporuje pozicování v prostředích bez GNSS signálu (např. tunelech, městských zástavbách)
- Navrženo pro provoz s nízkou latencí, který je klíčový pro bezpečnostní aplikace V2X
- Může fungovat s minimálně třemi UE: jedním referenčním, jedním cílovým a jedním pomocným UE

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [SL-RTT – Sidelink Round Trip Time](/mobilnisite/slovnik/sl-rtt/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [SL-RTOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-rtoa/)
