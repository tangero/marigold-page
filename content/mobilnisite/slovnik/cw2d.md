---
slug: "cw2d"
url: "/mobilnisite/slovnik/cw2d/"
type: "slovnik"
title: "CW2D – Carrier-Wave to Device"
date: 2026-01-01
abbr: "CW2D"
fullName: "Carrier-Wave to Device"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cw2d/"
summary: "CW2D označuje architekturu přímé komunikace, kde uzel generující nosnou vlnu vysílá signály přímo do uživatelských zařízení bez mezilehlých základnových stanic. Tento přístup umožňuje zjednodušené nas"
---

CW2D je architektura přímé komunikace, ve které uzel generující nosnou vlnu vysílá signály přímo do uživatelských zařízení bez mezilehlých základnových stanic, což umožňuje zjednodušené nasazení a snížení latence.

## Popis

Carrier-Wave to Device (CW2D) představuje paradigma přímé komunikace v sítích 3GPP, ve kterém uzel generující nosnou vlnu navazuje přímé rádiové spojení s koncovými uživatelskými zařízeními (UE) a obejde tak tradiční infrastrukturu základnových stanic. Tato architektura je definována v několika technických specifikacích, včetně 38.191 (NR; rádiový přenos a příjem uživatelského zařízení), 38.194 (NR; sběr dat pro minimalizaci testů za jízdy) a 38.769 (Studie vylepšení lokalizace v NR). Koncept CW2D umožňuje zjednodušené topologie sítě odstraněním mezilehlých síťových prvků, které by signály typicky zpracovávaly a přeposílaly.

Z pohledu technické implementace CW2D funguje tak, že vyhrazený uzel nosné vlny generuje a vysílá referenční signály, synchronizační signály a případně datové kanály přímo do UE. Tento uzel může být implementován jako zjednodušený přenosový bod se sníženými schopnostmi zpracování ve srovnání s plnohodnotnými gNB, zaměřující se primárně na funkce generování a přenosu signálu. Architektura podporuje jak downlink přenos z uzlu nosné vlny do zařízení, tak potenciálně i uplink příjem v závislosti na konkrétní konfiguraci implementace.

Mezi klíčové architektonické komponenty patří samotný uzel nosné vlny, který obsahuje [RF](/mobilnisite/slovnik/rf/) přenosové schopnosti a základní funkce generování signálu; přijímače v UE schopné zpracovat CW2D signály; a síťové koordinační funkce, které spravují vztah mezi CW2D přenosy a konvenčními buněčnými signály. Uzel nosné vlny může fungovat jako samostatný přenosový bod nebo v koordinaci se stávajícími základnovými stanicemi, přičemž synchronizace časování a frekvence jsou kritickými aspekty implementace.

V ekosystému sítě CW2D plní více rolí, včetně poskytování rozšíření pokrytí v náročném prostředí, podpory vylepšení lokalizace prostřednictvím dodatečných referenčních signálů a umožnění zjednodušených scénářů nasazení pro konkrétní případy užití. Technologie se integruje se stávajícími NR protokoly a rozhraními, se zvláštním důrazem na synchronizační mechanismy, správu interference a procedury mobility při přechodu zařízení mezi pokrytím CW2D a konvenčním buněčným pokrytím.

## K čemu slouží

CW2D bylo zavedeno ve 3GPP Release 19, aby řešilo konkrétní výzvy nasazení a požadavky na výkon v sítích 5G-Advanced. Primární motivací bylo vytvořit zjednodušenou, nákladově efektivní přenosovou architekturu pro scénáře, kde je nasazení plnohodnotných základnových stanic nepraktické nebo zbytečné. To zahrnuje rozšíření pokrytí v odlehlých oblastech, dočasné nasazení sítě a specializované aplikace, kde přímý přenos signálu poskytuje technické nebo ekonomické výhody oproti tradičním buněčným architekturám.

Historicky se buněčné sítě spoléhaly na kompletní implementace základnových stanic s plnohodnotnými schopnostmi zpracování protokolového zásobníku, a to i pro jednoduché aplikace rozšíření pokrytí. CW2D řeší omezení tohoto přístupu oddělením funkce generování signálu od komplexity plné základnové stanice, což umožňuje flexibilnější a efektivnější nasazení sítě. To je zvláště relevantní pro scénáře nepozemských sítí, kde satelitní uzly nosné vlny mohou poskytovat širokoplošné pokrytí bez potřeby pozemní infrastruktury.

Technologie také řeší konkrétní požadavky na výkon, včetně snížené latence pro časově kritické aplikace, zlepšené přesnosti lokalizace prostřednictvím dodatečných referenčních signálů a zvýšené efektivity sítě optimalizací přenosových cest. Umožněním přímého přenosu nosné vlny do zařízení poskytuje CW2D alternativní architektonický přístup, který doplňuje, nikoli nahrazuje, stávající buněčnou infrastrukturu, a nabízí tak síťovým operátorům dodatečné možnosti nasazení pro splnění různorodých požadavků služeb.

## Klíčové vlastnosti

- Přímý přenos signálu z uzlu nosné vlny do UE bez zpracování v mezilehlé základnové stanici
- Podpora synchronizačních signálů a referenčních signálů pro akvizici a měření UE
- Integrace se stávajícími NR lokalizačními frameworky pro vylepšené služby určování polohy
- Flexibilní scénáře nasazení včetně pozemských a nepozemských implementací
- Snížená latence ve srovnání s tradičními vícekrokovými architekturami
- Zjednodušená implementace uzlu se zaměřenými přenosovými schopnostmi

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [IAB – Integrated Access and Backhaul](/mobilnisite/slovnik/iab/)

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [CW2D na 3GPP Explorer](https://3gpp-explorer.com/glossary/cw2d/)
